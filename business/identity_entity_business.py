# -*- coding: utf-8 -*-

"""
Classe Business pour la gestion des relations Identity / Entity.
"""

from dataclasses import dataclass

from models.identity_entity import IdentityEntity
from daos.identity_entity_dao import IdentityEntityDao


@dataclass
class IdentityEntityBusiness:
    """Classe métier permettant de gérer les relations Identity / Entity."""

    dao: IdentityEntityDao

    def create(self, identity_entity: IdentityEntity) -> bool:

        if identity_entity is None:
            print("Erreur : aucune relation n'a été fournie.")
            return False

        if (
                identity_entity.fk_id_entity is None
                and identity_entity.fk_id_identity is None
        ):
            print(
                "Erreur : une identité ou une entité doit être renseignée."
            )
            return False

        if identity_entity.fk_id_identity is None:
            print("Erreur : l'identité est obligatoire.")
            return False

        if identity_entity.fk_id_identity <= 0:
            print("Erreur : identifiant d'identité invalide.")
            return False

        if identity_entity.fk_id_role is None:
            print("Erreur : le rôle est obligatoire.")
            return False

        if identity_entity.fk_id_role <= 0:
            print("Erreur : identifiant de rôle invalide.")
            return False

        if self.identity_business.read(
                identity_entity.fk_id_identity
        ) is None:
            print("Erreur : l'identité n'existe pas.")
            return False

        if identity_entity.fk_id_entity is not None:
            if self.entity_business.read(
                    identity_entity.fk_id_entity
            ) is None:
                print("Erreur : l'entité n'existe pas.")
                return False

        if self.role_business.read(
                identity_entity.fk_id_role
        ) is None:
            print("Erreur : le rôle n'existe pas.")
            return False

        if self.dao.read(
                identity_entity.fk_id_entity,
                identity_entity.fk_id_identity,
                identity_entity.fk_id_role
        ):
            print("Erreur : cette relation existe déjà.")
            return False

        return self.dao.create(identity_entity)

    def read(self, fk_id_entity: int, fk_id_identity: int, fk_id_role: int):
        """Recherche une relation Identity / Entity."""
        return self.dao.read(fk_id_entity, fk_id_identity, fk_id_role)

    def delete(self, identity_entity: IdentityEntity) -> bool:
        """Supprime une relation Identity / Entity."""
        if identity_entity is None:
            print("Erreur : aucune relation n'a été fournie.")
            return False

        return self.dao.delete(identity_entity)

    def delete_by_entity(self, id_entity: int) -> bool:
        """Supprime toutes les relations liées à une entité."""
        if id_entity is None or id_entity <= 0:
            print("Erreur : identifiant d'entité invalide.")
            return False

        return self.dao.delete_by_entity(id_entity)

    def delete_roles_by_identity(self, id_identity: int) -> bool:
        """Supprime les rôles directs d'une identité."""
        if id_identity is None or id_identity <= 0:
            print("Erreur : identifiant d'identité invalide.")
            return False
        return self.dao.delete_roles_by_identity(id_identity)