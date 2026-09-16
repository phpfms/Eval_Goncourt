# fichier qui permet à l'utilisateur de faire des choix numériques,
# il joue un rôle de contrôleur, d'interaction avec l'utilisateur

from business.data_loader import DataLoader
from menu import Menu


class Application:

    def __init__(self):
        """Initialise l'application."""
        self.menu = Menu()

    def run(self):
        """Lance l'application et charge les données dans la BDD si la ligne est décommentée."""
        DataLoader().load()

        conti = True

        while conti:
            choix = self.menu.display_main_menu()

            if choix == "1":
                self.jury_menu()

            elif choix == "2":
                self.vote_menu()

            elif choix == "3":
                self.election_menu()

            elif choix == "4":
                self.book_menu()

            elif choix == "5":
                self.person_menu()

            elif choix == "6":
                self.role_menu()

            elif choix == "0":
                print("Au revoir.")
                conti = False

            else:
                print("Choix invalide.")

    def jury_menu(self):
        """Gère le sous-menu des jurys."""

        conti = True

        while conti:
            choix = self.menu.display_jury_menu()

            if choix == "1":
                print("Afficher l'historique des jurys")

            elif choix == "2":
                print("Afficher la composition du jury et le nom de son président")

            elif choix == "3":
                print("Trouver un livre par id")

            elif choix == "4":
                print("Trouver un livre par nom")

            elif choix == "5":
                print("Afficher les détails d'un membre du jury")

            elif choix == "6":
                print("Créer un jury")

            elif choix == "7":
                print("Modifier un jury")

            elif choix == "8":
                print("Supprimer un jury")

            elif choix == "0":
                print("Retour au menu principal.")
                conti = False

            else:
                print("Choix invalide.")

    def vote_menu(self):
        """Gère le sous-menu des votes."""

        conti = True

        while conti:
            choix = self.menu.display_vote_menu()

            if choix == "1":
                print("Afficher l'historique des votes")

            elif choix == "2":
                print("Afficher les détails d'un vote")

            elif choix == "3":
                print("Trouver un vote par id")

            elif choix == "4":
                print("Trouver un vote par nom")

            elif choix == "5":
                print("Voter")

            elif choix == "6":
                print("Modifier un vote")

            elif choix == "7":
                print("Supprimer un vote")

            elif choix == "8":
                print("Indiquer le résultat d'un vote en nombre de voix par livre")

            elif choix == "9":
                print("Indiquer le résultat d'un vote en auteur par livre")

            elif choix == "10":
                print("Annoncer le résultat du vote")

            elif choix == "0":
                print("Retour au menu principal.")
                conti = False

            else:
                print("Choix invalide.")

    def election_menu(self):
        """Gère le sous-menu des élections."""

        conti = True

        while conti:
            choix = self.menu.display_election_menu()

            if choix == "1":
                print("Afficher l'historique des élections")

            elif choix == "2":
                print("Afficher les détails d'une élection")

            elif choix == "3":
                print("Trouver une élection par id")

            elif choix == "4":
                print("Trouver une élection par nom")

            elif choix == "5":
                print("Générer la composition des candidats du tour suivant")

            elif choix == "6":
                print("Annoncer le nouveau panel de candidats")

            elif choix == "7":
                print("Créer une élection")

            elif choix == "8":
                print("Modifier une élection")

            elif choix == "9":
                print("Supprimer une élection")

            elif choix == "0":
                print("Retour au menu principal.")
                conti = False

            else:
                print("Choix invalide.")

    def book_menu(self):
        """Gère le sous-menu des livres."""

        conti = True

        while conti:
            choix = self.menu.display_book_menu()

            if choix == "1":
                print("Afficher la liste des livres, avec id et titre")

            elif choix == "2":
                print("Afficher les détails d'un livre")

            elif choix == "3":
                print("Trouver un livre par id")

            elif choix == "4":
                print("Trouver un livre par nom")

            elif choix == "5":
                print("Créer un livre")

            elif choix == "6":
                print("Modifier un livre")

            elif choix == "7":
                print("Supprimer un livre")

            elif choix == "0":
                print("Retour au menu principal.")
                conti = False

            else:
                print("Choix invalide.")

    def person_menu(self):
        """Gère le sous-menu des personnes."""

        conti = True

        while conti:
            choix = self.menu.display_person_menu()

            if choix == "1":
                print("Afficher la liste des personnes, avec id, nom et rôle")

            elif choix == "2":
                print("Afficher tous les détails d'une personne")

            elif choix == "3":
                print("Trouver une personne par id")

            elif choix == "4":
                print("Trouver une personne par nom")

            elif choix == "5":
                print("Créer une personne")

            elif choix == "6":
                print("Modifier une personne")

            elif choix == "7":
                print("Supprimer une personne")

            elif choix == "0":
                print("Retour au menu principal.")
                conti = False

            else:
                print("Choix invalide.")

    def role_menu(self):
        """Gère le sous-menu des rôles."""

        conti = True

        while conti:
            choix = self.menu.display_role_menu()

            if choix == "1":
                print("Afficher les différents rôles en base")

            elif choix == "2":
                print(
                    "Afficher tous les éléments appartenant à un rôle, "
                    "avec leur id et leur nom"
                )

            elif choix == "3":
                print("Créer un rôle")

            elif choix == "4":
                print("Modifier un rôle")

            elif choix == "5":
                print("Supprimer un rôle")

            elif choix == "0":
                print("Retour au menu principal.")
                conti = False

            else:
                print("Choix invalide.")


if __name__ == "__main__":
    app = Application()
    app.run()

