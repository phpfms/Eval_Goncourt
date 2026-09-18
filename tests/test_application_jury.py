# -*- coding: utf-8 -*-

from application import Application
from models.jury import Jury
from datetime import date


def saisir(monkeypatch, valeurs):
    """Fournit les réponses utilisateur au sous-menu sans remplacer le menu lui-même."""
    reponses = iter(valeurs)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(reponses))


def preparer_jury_test(app, suffix, nb_entity=1, nb_entity_mode="EXACT"):
    """Crée un jury de test avec une personne réellement présente en BDD."""
    personnes = app.identity_business.read_all()
    assert personnes

    membre = personnes[0]

    # Règle métier : un jury doit avoir au moins un membre et le nombre
    # de membres doit respecter le mode EXACT utilisé ici.
    jury = Jury(
        date_begin=date(2026, 1, 1),
        date_end=date(2026, 12, 31),
        fk_id_identity_president=membre.id_identity,
        nb_entity=nb_entity,
        nb_entity_mode=nb_entity_mode,
        fk_id_jury_mother=None
    )

    # Choix technique : la création passe par JuryBusiness afin de tester
    # la vraie chaîne métier et les contraintes de la BDD de test.
    id_jury = app.jury_business.create(jury, [membre.id_identity])

    assert id_jury != 0
    return id_jury, membre


def test_sous_menu_jury_1_afficher_historique(monkeypatch, capsys):
    # Règle métier : l'option 1 doit afficher les jurys présents en base.
    # Le test récupère un jury réel afin de ne pas dépendre d'un identifiant fixe.
    app = Application()
    juries = app.jury_business.read_all()
    assert juries

    id_jury = juries[0].id_jury

    saisir(monkeypatch, ["1", "0"])
    app.jury_menu()

    sortie = capsys.readouterr().out

    assert "HISTORIQUE DES JURYS" in sortie
    assert f"Jury {id_jury}" in sortie


def test_sous_menu_jury_2_afficher_composition(monkeypatch, capsys):
    # Règle métier : la composition doit être demandée uniquement pour un jury existant.
    app = Application()
    id_jury, membre = preparer_jury_test(app, "composition")

    saisir(monkeypatch, ["2", str(id_jury), "0"])
    app.jury_menu()

    sortie = capsys.readouterr().out

    assert f"COMPOSITION DU JURY {id_jury}" in sortie
    assert str(membre.id_identity) in sortie

    # Nettoyage : le jury créé uniquement pour ce test est supprimé après vérification.
    assert app.jury_business.delete(id_jury) is True


def test_sous_menu_jury_3_trouver_par_id(monkeypatch, capsys):
    # Règle métier : un jury existant doit être retrouvable avec son identifiant.
    app = Application()
    id_jury, membre = preparer_jury_test(app, "recherche_id")

    saisir(monkeypatch, ["3", str(id_jury), "0"])
    app.jury_menu()

    sortie = capsys.readouterr().out

    # Choix technique : DisplayJury.display() affiche "ID : X", et non "Jury X".
    assert f"ID : {id_jury}" in sortie
    assert str(membre.id_identity) in sortie or "Président :" in sortie

    assert app.jury_business.delete(id_jury) is True


def test_sous_menu_jury_4_trouver_par_nom_president(monkeypatch, capsys):
    # Règle métier : la recherche doit utiliser le nom d'un président
    # réellement associé à un jury existant.
    app = Application()
    juries = app.jury_business.read_all()
    assert juries

    # Certains jurys peuvent ne pas avoir de président.
    # On sélectionne donc explicitement un jury dont la clé étrangère est renseignée.
    jury_avec_president = next(
        (
            jury
            for jury in juries
            if jury.fk_id_identity_president is not None
        ),
        None
    )

    assert jury_avec_president is not None

    id_jury = jury_avec_president.id_jury
    id_president = jury_avec_president.fk_id_identity_president
    president = app.identity_business.read(id_president)

    assert president is not None

    # Vérification métier directe : le Business doit retrouver le jury
    # à partir du nom du président réellement enregistré en BDD.
    juries_trouves = app.jury_business.find_by_president_name(
        president.appelation
    )

    assert juries_trouves
    assert any(
        jury.id_jury == id_jury
        for jury in juries_trouves
    )

    # On remplace uniquement la saisie du nom du président.
    # Le menu lui-même reste celui de l'application réelle.
    monkeypatch.setattr(
        app.jury_display,
        "input_president_name",
        lambda: president.appelation
    )

    saisir(monkeypatch, ["4", "0"])
    app.jury_menu()

    sortie = capsys.readouterr().out

    # Correction principale :
    # DisplayJury.display() affiche "ID : X".
    # "Jury X" est utilisé uniquement par display_history().
    assert f"ID : {id_jury}" in sortie
    assert f"Président : {id_president}" in sortie


def test_sous_menu_jury_5_trouver_un_membre(monkeypatch, capsys):
    # Règle métier : une personne existante doit pouvoir être retrouvée
    # à partir de son identifiant.
    app = Application()
    personnes = app.identity_business.read_all()
    assert personnes

    membre = personnes[0]

    saisir(monkeypatch, ["5", str(membre.id_identity), "0"])
    app.jury_menu()

    sortie = capsys.readouterr().out

    assert membre.appelation in sortie


def test_sous_menu_jury_6_creer_un_jury(monkeypatch, capsys):
    # Règle métier : le jury doit avoir un président existant,
    # au moins un membre et un nombre de membres cohérent avec le mode EXACT.
    app = Application()
    personnes = app.identity_business.read_all()
    assert personnes

    membre = personnes[0]

    saisir(
        monkeypatch,
        [
            "6",
            "2026-01-01",
            "2026-12-31",
            str(membre.id_identity),
            "1",
            "EXACT",
            str(membre.id_identity),
            "0"
        ]
    )

    app.jury_menu()

    sortie = capsys.readouterr().out

    assert "Jury créé avec l'identifiant" in sortie

    # Choix technique : on récupère le jury créé à partir de son président
    # afin de pouvoir le supprimer proprement après le test.
    juries = app.jury_business.find_by_president_name(membre.appelation)
    jury_test = next(
        (
            jury
            for jury in juries
            if jury.fk_id_identity_president == membre.id_identity
            and jury.date_begin == date(2026, 1, 1)
            and jury.date_end == date(2026, 12, 31)
        ),
        None
    )

    assert jury_test is not None
    assert app.jury_business.delete(jury_test.id_jury) is True


def test_sous_menu_jury_7_modifier_un_jury(monkeypatch, capsys):
    # Règle métier : la modification ne concerne qu'un jury existant
    # et les nouvelles dates doivent rester cohérentes.
    app = Application()
    id_jury, membre = preparer_jury_test(app, "modification")

    saisir(
        monkeypatch,
        [
            "7",
            str(id_jury),
            "2026-02-01",
            "2026-11-30",
            str(membre.id_identity),
            "1",
            "EXACT",
            "0"
        ]
    )

    app.jury_menu()

    jury = app.jury_business.read(id_jury)
    sortie = capsys.readouterr().out

    assert jury is not None
    assert jury.date_begin == date(2026, 2, 1)
    assert jury.date_end == date(2026, 11, 30)
    assert "Jury modifié avec succès." in sortie

    assert app.jury_business.delete(id_jury) is True


def test_sous_menu_jury_8_supprimer_un_jury(monkeypatch, capsys):
    # Règle métier : un jury non lié à une élection peut être supprimé.
    app = Application()
    id_jury, membre = preparer_jury_test(app, "suppression")

    monkeypatch.setattr(
        app.jury_display,
        "input_delete",
        lambda: id_jury
    )

    saisir(monkeypatch, ["8", "0"])
    app.jury_menu()

    sortie = capsys.readouterr().out

    assert "Jury supprimé avec succès." in sortie
    assert app.jury_business.read(id_jury) is None


def test_sous_menu_jury_id_invalide(monkeypatch, capsys):
    # Règle technique : un identifiant saisi au clavier doit être numérique.
    # La conversion invalide doit être interceptée sans provoquer d'exception.
    app = Application()

    saisir(monkeypatch, ["3", "abc", "0"])
    app.jury_menu()

    sortie = capsys.readouterr().out

    assert "L'identifiant doit être un nombre." in sortie


def test_sous_menu_jury_introuvable(monkeypatch, capsys):
    # Règle métier : un identifiant valide mais absent de la BDD doit
    # produire le message "Jury introuvable.".
    app = Application()

    saisir(monkeypatch, ["3", "999999", "0"])
    app.jury_menu()

    sortie = capsys.readouterr().out

    assert "Jury introuvable." in sortie


def test_sous_menu_jury_president_introuvable(monkeypatch, capsys):
    # Règle métier : une recherche par nom qui ne correspond à aucun
    # président doit retourner une liste vide et afficher le message prévu.
    app = Application()

    monkeypatch.setattr(
        app.jury_display,
        "input_president_name",
        lambda: "Président totalement inexistant pytest"
    )

    saisir(monkeypatch, ["4", "0"])
    app.jury_menu()

    sortie = capsys.readouterr().out

    assert "Aucun jury trouvé pour ce président." in sortie


def test_sous_menu_jury_membre_introuvable(monkeypatch, capsys):
    # Règle métier : l'identifiant d'une personne doit correspondre
    # à une identité réellement présente en base.
    app = Application()

    saisir(monkeypatch, ["5", "999999", "0"])
    app.jury_menu()

    sortie = capsys.readouterr().out

    assert "Personne introuvable." in sortie