# -*- coding: utf-8 -*-

from dataclasses import dataclass

from models.jury import Jury
from daos.jury_dao import JuryDao
from daos.role_dao import RoleDao
from business.identity_business import IdentityBusiness
from business.identity_jury_business import IdentityJuryBusiness


@dataclass
class JuryBusiness:
    """Classe métier pour la gestion des jurys."""

    dao: JuryDao
    identity_business: IdentityBusiness
    identity_jury_business: IdentityJuryBusiness
    role_dao: RoleDao

    def create(
            self,
            jury: Jury,
            id_members: list[int]
    ) -> int:
        """Crée un jury et lui associe ses membres."""

        if not self.validate_jury(jury):
            return 0

        if not self.validate_members(id_members, jury):
            return 0

        # Le président doit exister.
        if jury.fk_id_identity_president is not None:
            president = self.identity_business.read(
                jury.fk_id_identity_president
            )

            if president is None:
                print("Erreur : le président n'existe pas.")
                return 0

        # Vérifie que toutes les personnes existent avant la création.
        for id_identity in id_members:
            identity = self.identity_business.read(id_identity)

            if identity is None:
                print(
                    f"Erreur : la personne {id_identity} n'existe pas."
                )
                return 0

        # Le rôle est nécessaire pour les membres du jury.
        role = self.role_dao.find_by_name("membre du jury")

        if role is None:
            print(
                "Erreur : le rôle 'membre du jury' n'existe pas en base."
            )
            return 0

        id_jury = self.dao.create(jury)

        if id_jury == 0:
            return 0

        for id_identity in id_members:
            if not self.identity_jury_business.create(
                    id_jury,
                    id_identity
            ):
                print(
                    "Erreur lors de l'ajout d'un membre au jury."
                )
                return 0

            self.identity_business.add_role(
                id_identity,
                role.id_role
            )

        print("Jury créé avec succès.")
        return id_jury


    def read(self, id_jury: int) -> Jury | None:
        """Recherche un jury."""

        if id_jury is None or id_jury <= 0:
            print("Erreur : identifiant de jury invalide.")
            return None

        return self.dao.read(id_jury)

    def read_all(self) -> list[Jury]:
        """Retourne tous les jurys."""
        return self.dao.read_all()


    def update(self, jury: Jury) -> bool:
        """Modifie un jury."""

        if jury is None:
            print("Erreur : aucun jury fourni.")
            return False

        if jury.id_jury is None or jury.id_jury <= 0:
            print("Erreur : identifiant de jury invalide.")
            return False

        if self.dao.read(jury.id_jury) is None:
            print("Erreur : ce jury n'existe pas.")
            return False

        if not self.validate_jury(jury):
            return False

        if jury.fk_id_identity_president is not None:
            president = self.identity_business.read(
                jury.fk_id_identity_president
            )

            if president is None:
                print("Erreur : le président n'existe pas.")
                return False

        nb_members = self.dao.count_members(jury.id_jury)

        if nb_members < 0:
            print("Erreur : impossible de compter les membres.")
            return False

        if jury.nb_entity_mode == "MIN":
            if nb_members < jury.nb_entity:
                print(
                    "Erreur : le nombre actuel de membres est inférieur "
                    "au minimum demandé."
                )
                return False

        elif jury.nb_entity_mode == "MAX":
            if nb_members > jury.nb_entity:
                print(
                    "Erreur : le nombre actuel de membres dépasse "
                    "le maximum demandé."
                )
                return False

        elif jury.nb_entity_mode == "EXACT":
            if nb_members != jury.nb_entity:
                print(
                    "Erreur : le nombre de membres doit être exactement "
                    f"{jury.nb_entity}."
                )
                return False

        return self.dao.update(jury)

    def delete(self, id_jury: int) -> bool:
        """Supprime un jury s'il n'est lié à aucune élection."""
        if id_jury is None or id_jury <= 0:
            print("Erreur : identifiant de jury invalide.")
            return False

        if self.dao.read(id_jury) is None:
            print("Erreur : ce jury n'existe pas.")
            return False

        nb_elections = self.dao.count_elections(id_jury)

        if nb_elections < 0:
            print("Erreur : impossible de vérifier les élections.")
            return False

        if nb_elections > 0:
            print("Erreur : ce jury est lié à une élection.")
            print("Une nouvelle élection doit être créée avec un autre jury.")
            return False

        if not self.identity_jury_business.delete_by_jury(id_jury):
            print("Erreur lors de la suppression des membres du jury.")
            return False

        return self.dao.delete(id_jury)

    def add_member(
            self,
            id_jury: int,
            id_identity: int
    ) -> bool:
        """Ajoute une personne à un jury."""

        jury = self.read(id_jury)

        if jury is None:
            print("Erreur : ce jury n'existe pas.")
            return False

        identity = self.identity_business.read(id_identity)

        if identity is None:
            print("Erreur : cette personne n'existe pas.")
            return False

        nb_members = self.dao.count_members(id_jury)

        if nb_members < 0:
            print("Erreur : impossible de compter les membres.")
            return False

        if jury.nb_entity_mode == "MAX":
            if nb_members >= jury.nb_entity:
                print(
                    "Erreur : le nombre maximum de membres est atteint."
                )
                return False

        if jury.nb_entity_mode == "EXACT":
            if nb_members >= jury.nb_entity:
                print(
                    "Erreur : le nombre exact de membres est déjà atteint."
                )
                return False

        role = self.role_dao.find_by_name("membre du jury")

        if role is None:
            print(
                "Erreur : le rôle 'membre du jury' n'existe pas."
            )
            return False

        if not self.identity_jury_business.create(
                id_jury,
                id_identity
        ):
            return False

        # Le rôle est ajouté à la personne lorsqu'elle devient membre.
        if not self.identity_business.add_role(
                id_identity,
                role.id_role
        ):
            print(
                "Attention : la personne a été ajoutée au jury "
                "mais le rôle n'a pas pu être ajouté."
            )
            return False

        return True

    def remove_member(
            self,
            id_jury: int,
            id_identity: int
    ) -> bool:
        """Retire une personne d'un jury."""

        jury = self.read(id_jury)

        if jury is None:
            print("Erreur : ce jury n'existe pas.")
            return False

        if not self.identity_jury_business.exists(
                id_jury,
                id_identity
        ):
            print("Erreur : cette personne n'est pas membre du jury.")
            return False

        nb_members = self.dao.count_members(id_jury)

        if nb_members < 0:
            print("Erreur : impossible de compter les membres.")
            return False

        if jury.nb_entity_mode == "MIN":
            if nb_members <= jury.nb_entity:
                print(
                    "Erreur : le nombre minimum de membres serait dépassé."
                )
                return False

        if jury.nb_entity_mode == "EXACT":
            if nb_members <= jury.nb_entity:
                print(
                    "Erreur : un jury EXACT doit conserver exactement "
                    f"{jury.nb_entity} membre(s)."
                )
                return False

        return self.identity_jury_business.delete(
            id_jury,
            id_identity
        )

    def count_members(self, id_jury: int) -> int:
        """Retourne le nombre de membres d'un jury."""

        if id_jury is None or id_jury <= 0:
            return -1

        return self.dao.count_members(id_jury)

    def find_members(self, id_jury: int) -> list[int]:
        """Retourne les identifiants des membres d'un jury."""

        if id_jury is None or id_jury <= 0:
            return []

        return self.identity_jury_business.find_identities_by_jury(
            id_jury
        )

    def validate_members(
            self,
            id_members: list[int],
            jury: Jury
    ) -> bool:
        """Vérifie la composition initiale du jury."""

        if id_members is None:
            print("Erreur : aucun membre n'a été fourni.")
            return False

        if len(id_members) == 0:
            print("Erreur : le jury doit avoir au moins un membre.")
            return False

        if len(set(id_members)) != len(id_members):
            print(
                "Erreur : une personne ne peut pas être ajoutée "
                "plusieurs fois au même jury."
            )
            return False

        if jury.nb_entity_mode == "MIN":
            if len(id_members) < jury.nb_entity:
                print(
                    "Erreur : le nombre de membres est inférieur "
                    "au minimum demandé."
                )
                return False

        elif jury.nb_entity_mode == "MAX":
            if len(id_members) > jury.nb_entity:
                print(
                    "Erreur : le nombre de membres dépasse "
                    "le maximum autorisé."
                )
                return False

        elif jury.nb_entity_mode == "EXACT":
            if len(id_members) != jury.nb_entity:
                print(
                    "Erreur : le nombre de membres doit être exactement "
                    f"{jury.nb_entity}."
                )
                return False

        else:
            print("Erreur : mode de nombre de membres invalide.")
            return False

        return True

    def validate_jury(self, jury: Jury) -> bool:
        """Vérifie les données du jury."""

        if jury is None:
            print("Erreur : aucun jury fourni.")
            return False

        if jury.date_begin is None:
            print("Erreur : la date de début est obligatoire.")
            return False

        if jury.date_end is None:
            print("Erreur : la date de fin est obligatoire.")
            return False

        if jury.date_begin >= jury.date_end:
            print(
                "Erreur : la date de début doit être antérieure "
                "à la date de fin."
            )
            return False

        if jury.nb_entity <= 0:
            print(
                "Erreur : le nombre de membres doit être supérieur à 0."
            )
            return False

        if jury.nb_entity_mode not in (
                "MIN",
                "MAX",
                "EXACT"
        ):
            print(
                "Erreur : le mode doit être MIN, MAX ou EXACT."
            )
            return False

        if jury.fk_id_identity_president is not None:
            if jury.fk_id_identity_president <= 0:
                print("Erreur : identifiant du président invalide.")
                return False

        if jury.fk_id_jury_mother is not None:
            if jury.fk_id_jury_mother <= 0:
                print("Erreur : identifiant du jury parent invalide.")
                return False

        return True

    def get_composition(self, id_jury: int):
        """Retourne un jury et les informations de ses membres."""
        jury = self.read(id_jury)

        if jury is None:
            return None, []

        members = self.identity_jury_business.find_members_details(id_jury)

        return jury, members


    def find_by_president_name(self, name: str) -> list[Jury]:
        """Recherche les jurys par nom de président."""
        if name is None or name.strip() == "":
            print("Erreur : le nom du président est obligatoire.")
            return []
        return self.dao.find_by_president_name(name.strip())