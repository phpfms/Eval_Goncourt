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
        """Crée une relation Identity / Entity."""
        if identity_entity is None:
            print("Erreur : aucune relation n'a été fournie.")
            return False

        if identity_entity.fk_id_entity is None and identity_entity.fk_id_identity is None:
            print("Erreur : fk_id_entity et fk_id_identity ne peuvent pas être tous les deux NULL.")
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