# -*- coding: utf-8 -*-

"""
Classe Business pour la gestion des identités.

Cette classe fait le lien entre :
- les displays (interface utilisateur)
- les DAO (accès à la base de données)

Le Business contient les règles de gestion
et délègue les opérations SQL au IdentityDao.
"""

from dataclasses import dataclass
from typing import Optional

from models.identity import Identity
from daos.identity_dao import IdentityDao

@dataclass
class IdentityBusiness:
    """
    Classe métier permettant de gérer les identités.
    """

    dao: IdentityDao

    def create(self, identity: Identity) -> int:
        """
        Vérifie les données puis crée une identité.

        Retourne l'identifiant créé ou 0 en cas d'erreur.
        """

        if not self._validate_identity(identity):
            return 0

        if self.dao.exists(
                identity.appelation,
                identity.under_appelation
        ):
            print("Erreur : cette identité existe déjà.")
            return 0

        id_identity = self.dao.create(identity)

        if id_identity == 0:
            print("Erreur : impossible de créer l'identité.")
            return 0

        print("Identité créée avec succès.")
        return id_identity

    def read(self, id_identity: int) -> Optional[Identity]:
        """
        Recherche une identité à partir de son identifiant.

        :param id_identity: identifiant de l'identité
        :return: Identity si trouvée, sinon None
        """

        if id_identity is None or id_identity <= 0:
            return None

        return self.dao.read(id_identity)

    def read_all(self) -> list[Identity]:
        """Retourne toutes les identités."""

        return self.dao.read_all()

    def update(self, identity: Identity) -> bool:
        """
        Modifie une identité existante.

        :param identity: identité contenant les nouvelles informations
        :return: True si la modification est effectuée, False sinon
        """

        if identity is None:
            print("Erreur : aucune identité n'a été fournie.")
            return False

        if identity.id_identity is None:
            print("Erreur : l'identifiant de l'identité est obligatoire.")
            return False

        if identity.id_identity <= 0:
            print("Erreur : l'identifiant de l'identité est invalide.")
            return False

        if not self._validate_identity(identity):
            return False

        if self.dao.read(identity.id_identity) is None:
            print("Erreur : cette identité n'existe pas.")
            return False

        # L'identifiant actuel est ignoré pour détecter un doublon.
        if self.dao.exists(
                identity.appelation,
                identity.under_appelation,
                identity.id_identity
        ):
            print(
                "Erreur : une autre identité possède déjà "
                "ces informations."
            )
            return False

        return self.dao.update(identity)

    def delete(self, id_identity: int) -> bool:
        """
        Supprime une identité.

        :param id_identity: identifiant de l'identité
        :return: True si la suppression est effectuée, False sinon
        """

        if id_identity is None or id_identity <= 0:
            print("Erreur : identifiant invalide.")
            return False

        if self.dao.read(id_identity) is None:
            print("Erreur : cette identité n'existe pas.")
            return False

        # Une identité utilisée dans identity_entity ne peut pas être supprimée.
        nb_usages = self.dao.count_usages_identity(id_identity)

        if nb_usages < 0:
            print(
                "Erreur : impossible de vérifier les utilisations "
                "de cette identité."
            )
            return False

        if nb_usages > 0:
            print(
                "Erreur : cette identité est encore utilisée par "
                f"{nb_usages} entité(s)."
            )
            return False

        return self.dao.delete(id_identity)

    def count_usages(self, id_identity: int) -> int:
        """
        Retourne le nombre d'entités utilisant une identité.

        :param id_identity: identifiant de l'identité
        :return: nombre d'utilisations, ou -1 en cas d'erreur
        """

        if id_identity is None or id_identity <= 0:
            return -1

        return self.dao.count_usages_identity(id_identity)

    def _validate_identity(self, identity: Identity) -> bool:
        """
        Nettoie et valide les données d'une identité.

        :param identity: identité à vérifier
        :return: True si les données sont valides, False sinon
        """

        if identity is None:
            print("Erreur : aucune identité n'a été fournie.")
            return False

        if identity.appelation is None:
            print("Erreur : l'appellation est obligatoire.")
            return False

        identity.appelation = identity.appelation.strip()

        if identity.appelation == "":
            print("Erreur : l'appellation ne peut pas être vide.")
            return False

        if len(identity.appelation) > 100:
            print(
                "Erreur : l'appellation ne peut pas dépasser "
                "100 caractères."
            )
            return False

        if identity.under_appelation is not None:
            identity.under_appelation = identity.under_appelation.strip()

            if identity.under_appelation == "":
                identity.under_appelation = None

        if (
                identity.under_appelation is not None
                and len(identity.under_appelation) > 80
        ):
            print(
                "Erreur : le sous-nom ne peut pas dépasser "
                "80 caractères."
            )
            return False

        if identity.address is not None:
            identity.address = identity.address.strip()

            if identity.address == "":
                identity.address = None

        if identity.address is not None and len(identity.address) > 100:
            print(
                "Erreur : l'adresse ne peut pas dépasser "
                "100 caractères."
            )
            return False

        return True

    def find_by_name(self, name: str) -> list[Identity]:
        """Recherche les identités par nom."""

        if name is None:
            return []

        name = name.strip()

        if name == "":
            return []

        return self.dao.find_by_name(name)
