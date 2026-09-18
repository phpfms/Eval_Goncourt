# -*- coding: utf-8 -*-

from application import Application
from models.identity import Identity


def saisir(monkeypatch, valeurs):
    """Fournit les réponses utilisateur au sous-menu sans remplacer le menu lui-même."""
    reponses = iter(valeurs)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(reponses))


def creer_personne_test(app, suffix):
    """Crée une personne directement par le Business pour préparer un test du sous-menu."""
    personne = Identity(
        appelation=f"Personne Test {suffix}",
        under_appelation="Pytest",
        description="Personne créée pour un test pytest.",
        address="Adresse Test",
        fk_id_identity_mother=None
    )
    id_personne = app.identity_business.create(personne)
    assert id_personne != 0
    return id_personne


def recuperer_role(app):
    """Récupère un rôle réellement présent dans la BDD de test."""
    roles = app.role_business.read_all()
    assert roles
    return roles[0]


def test_sous_menu_personnes_1_afficher_toutes_les_personnes(monkeypatch, capsys):
    # Règle métier : l'option 1 récupère toutes les personnes réellement présentes en base.
    # Le test utilise une personne existante afin de ne pas dépendre d'un nom précis.
    app = Application()
    personnes = app.identity_business.read_all()
    assert personnes
    nom_personne = personnes[0].appelation
    saisir(monkeypatch, ["1", "0"])

    app.person_menu()

    sortie = capsys.readouterr().out
    assert "PERSONNE" in sortie
    assert nom_personne in sortie


def test_sous_menu_personnes_2_afficher_tous_les_details(monkeypatch, capsys):
    # L'identifiant est récupéré dans la BDD : le test vérifie les détails d'une personne existante.
    app = Application()
    personnes = app.identity_business.read_all()
    assert personnes
    id_personne = personnes[0].id_identity
    nom_personne = personnes[0].appelation
    saisir(monkeypatch, ["2", str(id_personne), "0"])

    app.person_menu()

    sortie = capsys.readouterr().out
    assert nom_personne in sortie


def test_sous_menu_personnes_3_trouver_par_id(monkeypatch, capsys):
    # L'option 3 utilise IdentityBusiness.read() pour rechercher une personne par son identifiant.
    app = Application()
    personnes = app.identity_business.read_all()
    assert personnes
    id_personne = personnes[0].id_identity
    nom_personne = personnes[0].appelation
    saisir(monkeypatch, ["3", str(id_personne), "0"])

    app.person_menu()

    sortie = capsys.readouterr().out
    assert nom_personne in sortie


def test_sous_menu_personnes_4_trouver_par_nom(monkeypatch, capsys):
    # La recherche par nom utilise IdentityBusiness.find_by_name() sur la vraie BDD.
    app = Application()
    personnes = app.identity_business.read_all()
    assert personnes
    nom_personne = personnes[0].appelation
    saisir(monkeypatch, ["4", nom_personne, "0"])

    app.person_menu()

    sortie = capsys.readouterr().out
    assert nom_personne in sortie


def test_sous_menu_personnes_5_creer_une_personne(monkeypatch, capsys):
    # Le test passe par Application.person_menu(), puis IdentityBusiness.create().
    # La personne est donc réellement insérée dans la BDD de test.
    app = Application()
    role = recuperer_role(app)
    nom_test = "Personne Test Sous Menu Creation"

    saisir(monkeypatch, [
        "5",
        nom_test,
        "Pytest",
        "Personne créée par le sous-menu.",
        "Adresse Test",
        str(role.id_role),
        "n",
        "0"
    ])

    app.person_menu()

    personne = next((identity for identity in app.identity_business.read_all() if identity.appelation == nom_test), None)
    sortie = capsys.readouterr().out
    assert personne is not None
    assert personne.under_appelation == "Pytest"
    assert "Identité créée avec l'identifiant" in sortie
    assert f"Fonction '{role.name_role}' affectée." in sortie

    # Nettoyage : la personne de test et son rôle direct sont supprimés de la BDD.
    assert app.identity_business.delete(personne.id_identity) is True


def test_sous_menu_personnes_6_modifier_une_personne(monkeypatch, capsys):
    # La personne de départ est créée par le vrai Business afin de ne pas modifier une donnée existante.
    app = Application()
    id_personne = creer_personne_test(app, "Modification")
    nom_modifie = "Personne Test Sous Menu Modification"

    # Règle métier : une saisie vide conserve la valeur actuelle ; seul le nom est modifié ici.
    saisir(monkeypatch, [
        "6",
        str(id_personne),
        nom_modifie,
        "",
        "",
        "",
        "0"
    ])

    app.person_menu()

    personne = app.identity_business.read(id_personne)
    sortie = capsys.readouterr().out
    assert personne is not None
    assert personne.appelation == nom_modifie
    assert "Identité modifiée avec succès." in sortie

    assert app.identity_business.delete(id_personne) is True


def test_sous_menu_personnes_7_supprimer_une_personne(monkeypatch, capsys):
    # La personne est créée uniquement pour ce test puis supprimée via l'option 7.
    app = Application()
    id_personne = creer_personne_test(app, "Suppression")
    saisir(monkeypatch, ["7", str(id_personne), "o", "0"])

    app.person_menu()

    sortie = capsys.readouterr().out
    assert "Identité supprimée avec succès." in sortie
    assert app.identity_business.read(id_personne) is None


def test_sous_menu_personnes_id_invalide(monkeypatch, capsys):
    # Règle technique : les identifiants saisis sont convertis avec int().
    # Une valeur non numérique doit être interceptée par le try/except du sous-menu.
    app = Application()
    saisir(monkeypatch, ["2", "abc", "0"])

    app.person_menu()

    sortie = capsys.readouterr().out
    assert "L'identifiant doit être un nombre." in sortie


def test_sous_menu_personnes_identite_introuvable(monkeypatch, capsys):
    # Un identifiant numérique mais inexistant doit produire le message métier prévu.
    app = Application()
    personnes = app.identity_business.read_all()
    assert personnes
    id_inexistant = max(identity.id_identity for identity in personnes) + 10000
    saisir(monkeypatch, ["3", str(id_inexistant), "0"])

    app.person_menu()

    sortie = capsys.readouterr().out
    assert "Identité introuvable." in sortie


def test_sous_menu_personnes_nom_introuvable(monkeypatch, capsys):
    # Une recherche avec un nom inexistant doit retourner une liste vide.
    app = Application()
    nom_inexistant = "Nom_Personne_Pytest_Inexistant_999999"
    saisir(monkeypatch, ["4", nom_inexistant, "0"])

    app.person_menu()

    sortie = capsys.readouterr().out
    assert "Aucune identité trouvée." in sortie


def test_sous_menu_personnes_supprimer_annulation(monkeypatch, capsys):
    # La confirmation "n" doit empêcher toute suppression.
    app = Application()
    id_personne = creer_personne_test(app, "Annulation")
    saisir(monkeypatch, ["7", str(id_personne), "n", "0"])

    app.person_menu()

    sortie = capsys.readouterr().out
    assert "Suppression annulée." in sortie
    assert app.identity_business.read(id_personne) is not None

    assert app.identity_business.delete(id_personne) is True
