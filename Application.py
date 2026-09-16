# fichier qui permet à l'utilisateur de faire des choix numériques,
# il joue un rôle de contrôleur, d'interaction avec l'utilisateur

from business.data_loader import DataLoader
from menu import Menu

from business.identity_business import IdentityBusiness
from daos.identity_dao import IdentityDao
from models.identity import Identity

from displays.identity_display import DisplayIdentity


class Application:

    def __init__(self):
        """Initialise l'application."""
        self.menu = Menu()
        self.identity_business = IdentityBusiness( IdentityDao() )
        self.identity_display = DisplayIdentity()

    def run(self):
        """Lance l'application et charge les données dans la BDD si la ligne est décommentée."""
        #DataLoader().load()

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
                identities = self.identity_business.read_all()
                self.identity_display.display_identities(identities)


            elif choix == "2":
                try:
                    id_identity = int(  input("Identifiant de l'identité : ") )
                    identity = self.identity_business.read(id_identity)
                    if identity is not None:
                        self.identity_display.display_identity(identity)
                    else:
                        print("Identité introuvable.")
                except ValueError:
                    print("L'identifiant doit être un nombre.")



            elif choix == "3":
                try:
                    id_identity = int( input("Identifiant de l'identité : ") )
                    identity = self.identity_business.read(id_identity)
                    if identity is not None:
                        self.identity_display.display_identity(identity)
                    else:
                        print("Identité introuvable.")
                except ValueError:
                    print("L'identifiant doit être un nombre.")



            elif choix == "4":
                name = input("Nom de la personne : ")
                identities = self.identity_business.find_by_name(name)
                if identities:
                    for identity in identities:
                        self.identity_display.display_identity(identity)
                else:
                    print("Aucune identité trouvée.")


            elif choix == "5":
                print("\n===== CRÉER UNE IDENTITÉ =====")
                appelation = input("Appellation : ")
                under_appelation = input("Sous-appellation : ")
                description = input("Description : ")
                address = input("Adresse : ")

                identity = Identity(
                    appelation,
                    under_appelation,
                    description,
                    address,
                    None
                )
                id_identity = self.identity_business.create(identity)
                if id_identity != 0:
                    print( f"Identité créée avec l'identifiant {id_identity}." )


            elif choix == "6":
                try:
                    id_identity = int( input("Identifiant de l'identité à modifier : ") )
                    identity = self.identity_business.read(id_identity)
                    if identity is None:
                        print("Identité introuvable.")

                    print("\n===== MODIFIER UNE IDENTITÉ =====")
                    print("Laissez vide pour conserver la valeur actuelle.")

                    appelation = input( f"Appellation [{identity.appelation}] : " )
                    under_appelation = input( f"Sous-appellation [{identity.under_appelation}] : ")

                    description = input( f"Description [{identity.description}] : " )
                    address = input( f"Adresse [{identity.address}] : " )

                    if appelation != "":
                        identity.appelation = appelation
                    if under_appelation != "":
                        identity.under_appelation = under_appelation
                    if description != "":
                        identity.description = description
                    if address != "":
                        identity.address = address

                    if self.identity_business.update(identity):
                        print("Identité modifiée avec succès.")
                    else:
                        print("La modification a échoué.")
                except ValueError:
                    print("L'identifiant doit être un nombre.")



            elif choix == "7":
                try:
                    id_identity = int(
                        input("Identifiant de l'identité à supprimer : ")
                    )
                    identity = self.identity_business.read(id_identity)
                    if identity is None:
                        print("Identité introuvable.")
                    else:
                        self.identity_display.display_identity(identity)
                        confirmation = input(
                            "Voulez-vous vraiment supprimer cette identité ? (o/n) : "
                        )

                        if confirmation.lower() == "o":
                            if self.identity_business.delete(id_identity):
                                print("Identité supprimée avec succès.")
                            else:
                                print("La suppression a échoué.")
                        else:
                            print("Suppression annulée.")
                except ValueError:

                    print("L'identifiant doit être un nombre.")

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

