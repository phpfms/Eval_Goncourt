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
from business.identity_entity_business import IdentityEntityBusiness
from business.role_business import RoleBusiness
from business.entity_business import EntityBusiness


@dataclass
class IdentityBusiness:
    """Classe métier permettant de gérer les identités."""

    dao: IdentityDao
    identity_entity_business: IdentityEntityBusiness
    role_business: RoleBusiness
    entity_business: EntityBusiness


    def create(self, identity: Identity) -> int:
        """
        Vérifie les données puis crée une identité.

        Retourne l'identifiant créé ou 0 en cas d'erreur.
        """

        if not self.validate_identity(identity):
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

        if not self.validate_identity(identity):
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
        """Supprime une personne si elle n'est dans aucun jury
        et si elle n'a plus aucune entité liée.
        """

        if id_identity is None or id_identity <= 0:
            print("Erreur : identifiant invalide.")
            return False

        if self.dao.read(id_identity) is None:
            print("Erreur : cette personne n'existe pas.")
            return False

        # Vérification des jurys
        juries = self.dao.find_juries_by_identity(id_identity)

        if juries:
            print(
                "Erreur : cette personne est encore référencée "
                "dans un jury."
            )

            for jury in juries:
                print(
                    f"- Jury {jury.id_jury} : "
                    f"{jury.date_begin} -> {jury.date_end}"
                )

            return False

        # Vérification des entités encore liées
        nb_entities = self.dao.count_entity_usages_identity(id_identity)

        if nb_entities < 0:
            print(
                "Erreur : impossible de vérifier "
                "les entités liées à cette personne."
            )
            return False

        if nb_entities > 0:
            print(
                "Erreur : cette personne possède encore "
                f"{nb_entities} entité(s) liée(s)."
            )
            print(
                "Supprimez d'abord les entités concernées "
                "avant de supprimer cette personne."
            )
            return False

        # supprime ses rôles directs avant de supprimer l'identité
        self.identity_entity_business.delete_roles_by_identity(id_identity)
        # Suppression de la personne
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

    def validate_identity(self, identity: Identity) -> bool:
        """Nettoie et valide les données d'une identité."""

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
            print("Erreur : l'appellation ne peut pas dépasser 100 caractères.")
            return False

        if identity.under_appelation is not None:
            identity.under_appelation = identity.under_appelation.strip()

            if identity.under_appelation == "":
                identity.under_appelation = None

        if identity.under_appelation is not None and len(identity.under_appelation) > 80:
            print("Erreur : la sous-appellation ne peut pas dépasser 80 caractères.")
            return False

        if identity.description is not None:
            identity.description = identity.description.strip()

            if identity.description == "":
                identity.description = None

        if identity.address is not None:
            identity.address = identity.address.strip()

            if identity.address == "":
                identity.address = None

        if identity.address is not None and len(identity.address) > 100:
            print("Erreur : l'adresse ne peut pas dépasser 100 caractères.")
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

    def add_role(self, id_identity: int, id_role: int) -> bool:
        """Affecte un rôle à une identité après vérification des règles métier."""
        if id_identity is None or id_identity <= 0:
            print("Erreur : identifiant d'identité invalide.")
            return False
        if id_role is None or id_role <= 0:
            print("Erreur : identifiant de rôle invalide.")
            return False

        # Une identité doit obligatoirement exister avant de pouvoir recevoir un rôle.
        identity = self.dao.read(id_identity)
        if identity is None:
            print("Erreur : cette identité n'existe pas.")
            return False

        # Le rôle doit être validé par RoleBusiness et non directement par le DAO.
        role = self.role_business.read(id_role)
        if role is None:
            print("Erreur : ce rôle n'existe pas.")
            return False

        # On vérifie la règle métier : une même identité ne doit pas recevoir
        # deux fois le même rôle direct.
        if self.dao.has_role(id_identity, id_role):
            print("Erreur : ce rôle est déjà affecté à cette personne.")
            return False

        return self.dao.add_role(id_identity, id_role)


    def find_by_role(self, id_role: int) -> list[Identity]:
        """Retourne les identités possédant un rôle."""

        if id_role is None or id_role <= 0:
            return []

        return self.dao.find_by_role(id_role)

    def add_entity(
            self,
            id_identity: int,
            id_entity: int,
            id_role: int
    ) -> bool:

        if id_identity is None or id_identity <= 0:
            print("Erreur : identifiant d'identité invalide.")
            return False

        if id_entity is None or id_entity <= 0:
            print("Erreur : identifiant d'entité invalide.")
            return False

        if id_role is None or id_role <= 0:
            print("Erreur : identifiant de rôle invalide.")
            return False

        if self.dao.read(id_identity) is None:
            print("Erreur : l'identité n'existe pas.")
            return False

        if self.entity_business.read(id_entity) is None:
            print("Erreur : l'entité n'existe pas.")
            return False

        if self.role_business.read(id_role) is None:
            print("Erreur : le rôle n'existe pas.")
            return False

        if self.identity_entity_business.read(
                id_entity,
                id_identity,
                id_role
        ):
            print("Erreur : cette relation existe déjà.")
            return False

        return self.dao.add_entity(
            id_identity,
            id_entity,
            id_role
        )