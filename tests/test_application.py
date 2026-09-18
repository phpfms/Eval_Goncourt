import pytest
from application import Application

# Fixture technique : on instancie réellement Application pour utiliser application.py,
# Menu, les Business, les DAO et la connexion à la base de test du projet.
@pytest.fixture
def app():
    return Application()

# Règle métier : le menu principal doit permettre de quitter avec le choix 0.
# Choix technique : on ne remplace aucun objet métier ; seul input() est piloté
# pour rendre le test automatique dans PyCharm/pytest.
def test_run_quitte_avec_0(app, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    app.run()
    assert "Au revoir." in capsys.readouterr().out

# Règle métier : un choix absent du menu principal doit être signalé comme invalide.
def test_run_affiche_choix_invalide(app, monkeypatch, capsys):
    choix = iter(["99", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.run()
    assert "Choix invalide." in capsys.readouterr().out

# Règle métier : le sous-menu jury doit revenir au menu principal avec 0.
# Ici le Menu réel affiche le sous-menu et application.py traite réellement le choix.
def test_jury_menu_quitte_avec_0(app, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    app.jury_menu()
    assert "Retour au menu principal." in capsys.readouterr().out

# Règle métier : un choix invalide dans le sous-menu jury doit être signalé.
def test_jury_menu_choix_invalide(app, monkeypatch, capsys):
    choix = iter(["99", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.jury_menu()
    assert "Choix invalide." in capsys.readouterr().out

# Règle métier : le sous-menu vote doit accepter les choix prévus par le cahier des charges.
# Le code actuel affiche l'action demandée ; il n'exécute pas encore de Business de vote.
def test_vote_menu_affiche_action(app, monkeypatch, capsys):
    choix = iter(["1", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.vote_menu()
    sortie = capsys.readouterr().out
    assert "Afficher l'historique des votes" in sortie
    assert "Retour au menu principal." in sortie

# Règle métier : le sous-menu élection doit reconnaître ses actions déclarées.
# Choix technique : aucune donnée n'est créée ou modifiée dans ce menu actuellement.
def test_election_menu_affiche_action(app, monkeypatch, capsys):
    choix = iter(["1", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.election_menu()
    sortie = capsys.readouterr().out
    assert "Afficher l'historique des élections" in sortie
    assert "Retour au menu principal." in sortie

# Règle métier : le sous-menu rôle doit reconnaître les actions déclarées.
def test_role_menu_affiche_action(app, monkeypatch, capsys):
    choix = iter(["1", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.role_menu()
    sortie = capsys.readouterr().out
    assert "Afficher les différents rôles en base" in sortie
    assert "Retour au menu principal." in sortie

# Règle métier : le choix 1 du menu jury doit consulter les jurys puis afficher leur historique.
# Choix technique : la base de test est utilisée ; on ne suppose pas un nombre précis de jurys.
def test_jury_menu_affiche_historique(app, monkeypatch, capsys):
    choix = iter(["1", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.jury_menu()
    sortie = capsys.readouterr().out
    assert "Retour au menu principal." in sortie

# Règle métier : une recherche de jury par identifiant non numérique doit être refusée proprement.
def test_jury_menu_id_non_numerique(app, monkeypatch, capsys):
    choix = iter(["3", "abc", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.jury_menu()
    assert "L'identifiant doit être un nombre." in capsys.readouterr().out

# Règle métier : une recherche de personne par identifiant non numérique doit être refusée.
def test_jury_menu_membre_id_non_numerique(app, monkeypatch, capsys):
    choix = iter(["5", "abc", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.jury_menu()
    assert "L'identifiant doit être un nombre." in capsys.readouterr().out

# Règle métier : le menu livre doit pouvoir revenir au menu principal sans accéder à la BDD.
def test_book_menu_quitte_avec_0(app, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    app.book_menu()
    assert "Retour au menu principal." in capsys.readouterr().out

# Règle métier : un identifiant de livre doit être numérique pour les recherches.
def test_book_menu_id_non_numerique(app, monkeypatch, capsys):
    choix = iter(["2", "abc", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.book_menu()
    assert "L'identifiant doit être un nombre." in capsys.readouterr().out

# Règle métier : la recherche d'un livre par identifiant inexistant doit produire
# un message utilisateur plutôt qu'une exception non gérée.
def test_book_menu_livre_introuvable(app, monkeypatch, capsys):
    choix = iter(["2", "999999999", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.book_menu()
    assert "Livre introuvable." in capsys.readouterr().out

# Règle métier : le menu personne doit pouvoir revenir au menu principal.
def test_person_menu_quitte_avec_0(app, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    app.person_menu()
    assert "Retour au menu principal." in capsys.readouterr().out

# Règle métier : un identifiant de personne non numérique doit être refusé.
def test_person_menu_id_non_numerique(app, monkeypatch, capsys):
    choix = iter(["2", "abc", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.person_menu()
    assert "L'identifiant doit être un nombre." in capsys.readouterr().out

# Règle métier : une personne inexistante doit être signalée sans arrêter le programme.
def test_person_menu_personne_introuvable(app, monkeypatch, capsys):
    choix = iter(["2", "999999999", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.person_menu()
    assert "Identité introuvable." in capsys.readouterr().out

# Règle métier : le menu rôle doit pouvoir revenir au menu principal.
def test_role_menu_quitte_avec_0(app, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    app.role_menu()
    assert "Retour au menu principal." in capsys.readouterr().out

# Règle métier : les menus vote, élection et rôle doivent rejeter un choix inconnu.
def test_vote_menu_choix_invalide(app, monkeypatch, capsys):
    choix = iter(["99", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.vote_menu()
    assert "Choix invalide." in capsys.readouterr().out

def test_election_menu_choix_invalide(app, monkeypatch, capsys):
    choix = iter(["99", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.election_menu()
    assert "Choix invalide." in capsys.readouterr().out

def test_role_menu_choix_invalide(app, monkeypatch, capsys):
    choix = iter(["99", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choix))
    app.role_menu()
    assert "Choix invalide." in capsys.readouterr().out
