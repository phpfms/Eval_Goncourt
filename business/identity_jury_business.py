# -*- coding: utf-8 -*-

from dataclasses import dataclass
from daos.identity_jury_dao import IdentityJuryDao


@dataclass
class IdentityJuryBusiness:
    """Classe métier pour les relations Identity / Jury."""

    dao: IdentityJuryDao

    def create(
            self,
            id_jury: int,
            id_identity: int
    ) -> bool:
        """Ajoute une personne à un jury."""
        if id_jury is None or id_jury <= 0:
            print("Erreur : identifiant de jury invalide.")
            return False
        if id_identity is None or id_identity <= 0:
            print("Erreur : identifiant d'identité invalide.")
            return False
        if self.dao.read(id_jury, id_identity):
            print("Erreur : cette personne est déjà membre du jury.")
            return False
        return self.dao.create(id_jury, id_identity)

    def exists(
            self,
            id_jury: int,
            id_identity: int
    ) -> bool:
        """Vérifie si une personne appartient à un jury."""
        if id_jury is None or id_jury <= 0:
            return False
        if id_identity is None or id_identity <= 0:
            return False
        return self.dao.read(id_jury, id_identity)

    def delete(
            self,
            id_jury: int,
            id_identity: int
    ) -> bool:
        """Retire une personne d'un jury."""
        if id_jury is None or id_jury <= 0:
            print("Erreur : identifiant de jury invalide.")
            return False
        if id_identity is None or id_identity <= 0:
            print("Erreur : identifiant d'identité invalide.")
            return False
        if not self.dao.read(id_jury, id_identity):
            print("Erreur : cette personne n'est pas membre du jury.")
            return False
        return self.dao.delete(id_jury, id_identity)

    def delete_by_jury(self, id_jury: int) -> bool:
        """Supprime tous les membres d'un jury."""
        if id_jury is None or id_jury <= 0:
            return False
        return self.dao.delete_by_jury(id_jury)

    def count_by_jury(self, id_jury: int) -> int:
        """Retourne le nombre de membres d'un jury."""
        if id_jury is None or id_jury <= 0:
            return -1
        return self.dao.count_by_jury(id_jury)

    def find_identities_by_jury(
            self,
            id_jury: int
    ) -> list[int]:
        """Retourne les identifiants des membres."""
        if id_jury is None or id_jury <= 0:
            return []
        return self.dao.find_identities_by_jury(id_jury)

    def find_juries_by_identity(
            self,
            id_identity: int
    ) -> list[int]:
        """Retourne les jurys d'une identité."""
        if id_identity is None or id_identity <= 0:
            return []
        return self.dao.find_juries_by_identity(id_identity)

    def find_members_details(
            self,
            id_jury: int
    ) -> list[dict]:
        """Retourne les informations détaillées des membres."""
        if id_jury is None or id_jury <= 0:
            return []
        return self.dao.find_members_details(id_jury)