# fichier qui permet à l'utilisateur de faire des choix numériques,
# il joue un rôle de contrôleur, d'interaction avec l'utilisateur

from business.data_loader import DataLoader
from menu import Menu

from business.identity_business import IdentityBusiness
from business.entity_business import EntityBusiness
from daos.entity_dao import EntityDao
from daos.identity_dao import IdentityDao
from models.identity import Identity
from models.entity import Entity
from displays.entity_display import DisplayEntity
from displays.identity_display import DisplayIdentity
from business.role_business import RoleBusiness
from daos.role_dao import RoleDao






class Application:

    def __init__(self):
        """Initialise l'application."""
        self.menu = Menu()
        self.identity_business = IdentityBusiness( IdentityDao() )
        self.identity_display = DisplayIdentity()
        self.entity_business = EntityBusiness(EntityDao())
        self.entity_display = DisplayEntity()
        self.role_business = RoleBusiness(RoleDao())

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
                entities = self.entity_business.read_all()
                self.entity_display.display_entities(entities)

            elif choix == "2":
                try:
                    id_entity = int(input("Identifiant du livre : "))
                    entity = self.entity_business.read(id_entity)

                    if entity is not None:
                        self.entity_display.display_entity(entity)
                    else:
                        print("Livre introuvable.")
                except ValueError:
                    print("L'identifiant doit être un nombre.")

            elif choix == "3":
                try:
                    id_entity = int(input("Identifiant du livre : "))
                    entity = self.entity_business.read(id_entity)

                    if entity is not None:
                        self.entity_display.display_entity(entity)
                    else:
                        print("Livre introuvable.")
                except ValueError:
                    print("L'identifiant doit être un nombre.")

            elif choix == "4":
                name = input("Nom du livre : ")
                entities = self.entity_business.find_by_name(name)

                if entities:
                    for entity in entities:
                        self.entity_display.display_entity(entity)
                else:
                    print("Aucun livre trouvé.")

            # la création de l'entité n'est pas terrible, surtout les verifs utilisateurs, pas le temps de faire mieux
            elif choix == "5":
                print("\n===== CRÉER UN LIVRE =====")

                ISBN = input("ISBN (13 chiffres): ")
                price = input("Prix : ")
                name = input("Nom (obligatoire): ")
                first_name = input("Prénom : ")
                # pour l'instant j'ai melangé volontairement tous les types d'entités à la table identité faute de temps de dév suffisant
                roles = self.role_business.read_all()

                print("\n===== TYPE DU LIVRE =====")

                for role in roles:
                    print(f"{role.id_role} - {role.name_role}")

                type_entity = input("Identifiant du type : ")

                type_selected = None

                for role in roles:
                    if str(role.id_role) == type_entity:
                        type_selected = role.name_role

                resume = input("Résumé : ")
                creation_date = input("Date de création (YYYY-MM-DD) : ")
                nb = input("Quantité : ")
                unit_nb = input("Unité : ")

                if type_selected is None:
                    print("Erreur : le type choisi n'existe pas.")
                else:
                    entity = Entity(
                        ISBN,
                        price,
                        name,
                        first_name if first_name else None,
                        type_selected,
                        resume if resume else None,
                        creation_date,
                        nb,
                        unit_nb,
                        None
                    )

                    id_entity = self.entity_business.create(entity)

                    if id_entity != 0:
                        print(f"Livre créé avec l'identifiant {id_entity}.")

            elif choix == "6":
                try:
                    id_entity = int(input("Identifiant du livre à modifier : "))
                    entity = self.entity_business.read(id_entity)

                    if entity is None:
                        print("Livre introuvable.")
                    else:
                        print("\n===== MODIFIER UN LIVRE =====")
                        print("Laissez vide pour conserver la valeur actuelle.")

                        ISBN = input(f"ISBN [{entity.ISBN}] : ")
                        price = input(f"Prix [{entity.price}] : ")
                        name = input(f"Nom [{entity.name}] : ")
                        first_name = input(f"Prénom [{entity.first_name}] : ")
                        type_entity = input(f"Type [{entity.type}] : ")
                        resume = input(f"Résumé [{entity.resume}] : ")
                        creation_date = input(
                            f"Date de création [{entity.creation_date}] : "
                        )
                        nb = input(f"Quantité [{entity.nb}] : ")
                        unit_nb = input(f"Unité [{entity.unit_nb}] : ")

                        if ISBN != "":
                            entity.ISBN = ISBN

                        if price != "":
                            entity.price = price

                        if name != "":
                            entity.name = name

                        if first_name != "":
                            entity.first_name = first_name

                        if type_entity != "":
                            entity.type = type_entity

                        if resume != "":
                            entity.resume = resume

                        if creation_date != "":
                            entity.creation_date = creation_date

                        if nb != "":
                            entity.nb = nb

                        if unit_nb != "":
                            entity.unit_nb = unit_nb

                        if self.entity_business.update(entity):
                            print("Livre modifié avec succès.")
                        else:
                            print("La modification a échoué.")

                except ValueError:
                    print("Une valeur saisie n'est pas valide.")

            elif choix == "7":
                try:
                    id_entity = int(
                        input("Identifiant du livre à supprimer : ")
                    )

                    entity = self.entity_business.read(id_entity)

                    if entity is None:
                        print("Livre introuvable.")
                    else:
                        self.entity_display.display_entity(entity)
                        confirmation = input(
                            "Voulez-vous vraiment supprimer ce livre ? (o/n) : "
                        )

                        if confirmation.lower() == "o":
                            if self.entity_business.delete(id_entity):
                                print("Livre supprimé avec succès.")
                            else:
                                print("La suppression a échoué.")
                        else:
                            print("Suppression annulée.")

                except ValueError:
                    print("L'identifiant doit être un nombre.")


            elif choix == "8":

                try:

                    id_entity = int(input("Identifiant du livre : "))

                    entity = self.entity_business.read(id_entity)

                    if entity is None:

                        print("Livre introuvable.")

                    else:

                        roles = self.role_business.read_all()

                        if not roles:

                            print("Aucun rôle disponible.")

                        else:

                            print("\n===== CHOISIR LE RÔLE =====")

                            for role in roles:
                                print(

                                    f"{role.id_role} - "

                                    f"{role.name_role}"

                                )

                            id_role = int(

                                input("Identifiant du rôle : ")

                            )

                            role_selected = None

                            for role in roles:

                                if role.id_role == id_role:
                                    role_selected = role

                                    break

                            if role_selected is None:

                                print("Rôle introuvable.")

                            else:

                                identities = (

                                    self.identity_business

                                    .find_by_role(id_role)

                                )

                                if not identities:

                                    print(

                                        "Aucune personne ne possède "

                                        f"le rôle « {role_selected.name_role} »."

                                    )

                                else:

                                    print(

                                        f"\n===== PERSONNES AVEC LE RÔLE "

                                        f"{role_selected.name_role.upper()} ====="

                                    )

                                    for identity in identities:
                                        print(

                                            f"{identity.id_identity} - "

                                            f"{identity.appelation}"

                                        )

                                    id_identity = int(

                                        input(

                                            "Identifiant de la personne : "

                                        )

                                    )

                                    identity_selected = None

                                    for identity in identities:

                                        if identity.id_identity == id_identity:
                                            identity_selected = identity

                                            break

                                    if identity_selected is None:

                                        print(

                                            "Cette personne n'existe pas "

                                            "ou ne possède pas ce rôle."

                                        )

                                    else:

                                        if self.identity_business.add_entity(

                                                id_identity,

                                                id_entity,

                                                id_role

                                        ):

                                            print(

                                                "Intervenant ajouté au livre "

                                                "avec succès."

                                            )

                                        else:

                                            print(

                                                "Impossible d'ajouter "

                                                "l'intervenant."

                                            )


                except ValueError:

                    print("L'identifiant doit être un nombre.")

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
                    under_appelation if under_appelation else None,
                    description if description else None,
                    address if address else None,
                    None
                )
                id_identity = self.identity_business.create(identity)
                if id_identity != 0:
                    print(f"Identité créée avec l'identifiant {id_identity}.")

                    roles = self.role_business.read_all()

                    if roles:
                        print("\n===== FONCTION DE LA PERSONNE =====")

                        for role in roles:
                            print(f"{role.id_role} - {role.name_role}")

                        role_ids = []

                        try:
                            id_role = int(input("Quelle est la fonction de cette personne ? "))
                            role = self.role_business.read(id_role)

                            if role is not None:
                                if self.identity_business.add_role(id_identity, id_role):
                                    role_ids.append(id_role)
                                    print(f"Fonction '{role.name_role}' affectée.")

                                while True:
                                    answer = input("Affecter une fonction supplémentaire ? (o/n) : ")

                                    if answer.lower() != "o":
                                        break

                                    for role in roles:
                                        print(f"{role.id_role} - {role.name_role}")

                                    try:
                                        id_role = int(input("Identifiant du rôle : "))

                                        if id_role in role_ids:
                                            print("Cette fonction est déjà affectée à cette personne.")
                                        else:
                                            role = self.role_business.read(id_role)

                                            if role is not None:
                                                if self.identity_business.add_role(id_identity, id_role):
                                                    role_ids.append(id_role)
                                                    print(f"Fonction '{role.name_role}' affectée.")
                                            else:
                                                print("Rôle introuvable.")

                                    except ValueError:
                                        print("L'identifiant du rôle doit être un nombre.")

                            else:
                                print("Rôle introuvable.")

                        except ValueError:
                            print("L'identifiant du rôle doit être un nombre.")
                    else:
                        print("Aucun rôle disponible.")

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
                    id_identity = int( input("Identifiant de l'identité à supprimer : ") )
                    identity = self.identity_business.read(id_identity)
                    if identity is None:
                        print("Identité introuvable.")
                    else:
                        self.identity_display.display_identity(identity)
                        confirmation = input( "Voulez-vous vraiment supprimer cette identité ? (o/n) : " )
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

