# -*- coding: utf-8 -*-

from application import Application
from models.entity import Entity


def saisir(monkeypatch, valeurs):
    """Fournit les réponses utilisateur au sous-menu sans remplacer le menu lui-même."""
    reponses = iter(valeurs)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(reponses))


def creer_livre_test(app, suffix):
    """Crée un livre directement par le Business pour préparer un test du sous-menu."""
    livre = Entity(
        ISBN="9791234567890",
        price=19.90,
        name=f"Livre Test {suffix}",
        first_name=None,
        type="livre",
        resume="Livre créé pour un test pytest.",
        creation_date="2026-09-18",
        nb=100,
        unit_nb="pages",
        fk_id_entity_mother=None
    )
    id_livre = app.entity_business.create(livre)
    assert id_livre != 0
    return id_livre


def test_sous_menu_livres_1_afficher_tous_les_livres(monkeypatch, capsys):
    # Règle métier : l'option 1 lit les livres réellement présents en base.
    # Le test récupère un livre existant au lieu de dépendre d'un nom précis dans la BDD.
    # Choix "0" après l'action : indispensable pour sortir proprement de la boucle du sous-menu.
    app = Application()
    livres = app.entity_business.read_all()
    assert livres
    nom_livre = livres[0].name
    saisir(monkeypatch, ["1", "0"])

    app.book_menu()

    sortie = capsys.readouterr().out
    assert "LIVRE" in sortie
    assert nom_livre in sortie


def test_sous_menu_livres_2_afficher_details(monkeypatch, capsys):
    # L'identifiant utilisé est récupéré dans la BDD : le test ne dépend donc pas d'un id inventé.
    app = Application()
    livres = app.entity_business.read_all()
    assert livres
    id_livre = livres[0].id_entity
    nom_livre = livres[0].name
    saisir(monkeypatch, ["2", str(id_livre), "0"])

    app.book_menu()

    sortie = capsys.readouterr().out
    assert nom_livre in sortie


def test_sous_menu_livres_3_trouver_par_id(monkeypatch, capsys):
    # L'option 3 utilise EntityBusiness.read(), qui vérifie réellement l'existence de l'entité.
    app = Application()
    livres = app.entity_business.read_all()
    assert livres
    id_livre = livres[0].id_entity
    nom_livre = livres[0].name
    saisir(monkeypatch, ["3", str(id_livre), "0"])

    app.book_menu()

    sortie = capsys.readouterr().out
    assert nom_livre in sortie


def test_sous_menu_livres_4_trouver_par_nom(monkeypatch, capsys):
    # La recherche est effectuée par EntityBusiness.find_by_name() sur la vraie BDD.
    app = Application()
    livres = app.entity_business.read_all()
    assert livres
    nom_livre = livres[0].name
    saisir(monkeypatch, ["4", nom_livre, "0"])

    app.book_menu()

    sortie = capsys.readouterr().out
    assert nom_livre in sortie


def test_sous_menu_livres_5_creer_un_livre(monkeypatch, capsys):
    # Le test passe par Application.book_menu(), puis EntityBusiness.create() et EntityDao.create().
    # Le livre est donc réellement inséré dans la BDD de test.
    app = Application()
    roles = app.role_business.read_all()
    role_livre = next((role for role in roles if role.name_role == "livre"), None)
    assert role_livre is not None

    nom_test = "Livre Test Sous Menu Creation"
    saisir(monkeypatch, [
        "5",
        "9791234567890",
        "19.90",
        nom_test,
        "",
        str(role_livre.id_role),
        "Livre créé par pytest.",
        "2026-09-18",
        "100",
        "pages",
        "0"
    ])

    app.book_menu()

    livre = next((entity for entity in app.entity_business.read_all() if entity.name == nom_test), None)
    sortie = capsys.readouterr().out
    assert livre is not None
    assert livre.type == "livre"
    assert "Livre créé avec l'identifiant" in sortie

    # Nettoyage : le livre de test est retiré de la BDD après vérification.
    assert app.entity_business.delete(livre.id_entity) is True


def test_sous_menu_livres_6_modifier_un_livre(monkeypatch, capsys):
    # Le livre de départ est créé par le vrai Business afin de ne pas modifier une donnée métier existante.
    app = Application()
    id_livre = creer_livre_test(app, "Modification")
    nom_modifie = "Livre Test Sous Menu Modification"

    # Règle métier : une saisie vide conserve la valeur actuelle ; seul le nom est modifié ici.
    saisir(monkeypatch, [
        "6",
        str(id_livre),
        "",
        "",
        nom_modifie,
        "",
        "",
        "",
        "",
        "",
        "",
        "0"
    ])

    app.book_menu()

    livre = app.entity_business.read(id_livre)
    sortie = capsys.readouterr().out
    assert livre is not None
    assert livre.name == nom_modifie
    assert "Livre modifié avec succès." in sortie

    assert app.entity_business.delete(id_livre) is True


def test_sous_menu_livres_7_supprimer_un_livre(monkeypatch, capsys):
    # Le livre est créé uniquement pour ce test puis supprimé via l'option 7 du sous-menu.
    app = Application()
    id_livre = creer_livre_test(app, "Suppression")
    saisir(monkeypatch, ["7", str(id_livre), "o", "0"])

    app.book_menu()

    sortie = capsys.readouterr().out
    assert "Livre supprimé avec succès." in sortie
    assert app.entity_business.read(id_livre) is None


def test_sous_menu_livres_8_ajouter_un_intervenant(monkeypatch, capsys):
    # On choisit réellement un rôle possédé par une personne existante en BDD.
    # Cela permet de tester la règle métier IdentityBusiness.add_entity().
    app = Application()
    id_livre = creer_livre_test(app, "Intervenant")
    roles = app.role_business.read_all()

    choix = next(
        (
            (role, app.identity_business.find_by_role(role.id_role)[0])
            for role in roles
            if app.identity_business.find_by_role(role.id_role)
        ),
        None
    )
    assert choix is not None

    role, identity = choix
    saisir(monkeypatch, [
        "8",
        str(id_livre),
        str(role.id_role),
        str(identity.id_identity),
        "0"
    ])

    app.book_menu()

    relation = app.identity_entity_business.read(
        id_livre,
        identity.id_identity,
        role.id_role
    )
    sortie = capsys.readouterr().out
    assert relation is not None
    assert "Intervenant ajouté au livre avec succès." in sortie

    # EntityBusiness.delete() ne supprime pas une entité encore utilisée par une élection,
    # mais la relation Identity/Entity créée par ce test doit être retirée avant le nettoyage.
    assert app.identity_entity_business.delete_by_entity(id_livre) is True
    assert app.entity_business.delete(id_livre) is True


def test_sous_menu_livres_id_invalide(monkeypatch, capsys):
    # Règle technique : les identifiants saisis par l'utilisateur sont convertis avec int().
    # Une valeur non numérique doit être interceptée par le try/except du sous-menu.
    app = Application()
    saisir(monkeypatch, ["2", "abc", "0"])

    app.book_menu()

    sortie = capsys.readouterr().out
    assert "L'identifiant doit être un nombre." in sortie


def test_sous_menu_livres_type_inexistant(monkeypatch, capsys):
    # Règle métier : un livre ne peut pas être créé si le type sélectionné n'existe pas.
    app = Application()
    nom_test = "Livre Test Type Inexistant"
    saisir(monkeypatch, [
        "5",
        "9791234567891",
        "19.90",
        nom_test,
        "",
        "999999",
        "Test",
        "2026-09-18",
        "100",
        "pages",
        "0"
    ])

    app.book_menu()

    sortie = capsys.readouterr().out
    livre = next((entity for entity in app.entity_business.read_all() if entity.name == nom_test), None)
    assert livre is None
    assert "Erreur : le type choisi n'existe pas." in sortie


def test_sous_menu_livres_supprimer_annulation(monkeypatch, capsys):
    # La confirmation "n" doit empêcher toute suppression.
    app = Application()
    id_livre = creer_livre_test(app, "Annulation")
    saisir(monkeypatch, ["7", str(id_livre), "n", "0"])

    app.book_menu()

    sortie = capsys.readouterr().out
    assert "Suppression annulée." in sortie
    assert app.entity_business.read(id_livre) is not None

    assert app.entity_business.delete(id_livre) is True
