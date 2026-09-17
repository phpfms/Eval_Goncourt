# -*- coding: utf-8 -*-

"""
Classe Business pour la gestion des entités.

Cette classe fait le lien entre :
- les displays (interface utilisateur)
- les DAO (accès à la base de données)

Le Business contient les règles de gestion
et délègue les opérations SQL au EntityDao.
"""

from dataclasses import dataclass
from typing import Optional
from business.identity_entity_business import IdentityEntityBusiness
from business.identity_entity_business import IdentityEntityBusiness

from models.entity import Entity
from daos.entity_dao import EntityDao

from datetime import datetime


@dataclass
class EntityBusiness:
    """Classe métier permettant de gérer les entités."""

    dao: EntityDao
    identity_entity_business: IdentityEntityBusiness

    def create(self, entity: Entity) -> int:
        """Crée une entité."""

        if not self.convert_entity(entity):
            return 0

        if not self.validate_entity(entity):
            return 0

        if self.dao.exists(
                entity.name,
                entity.first_name
        ):
            print("Erreur : cette entité existe déjà.")
            return 0

        id_entity = self.dao.create(entity)

        if id_entity == 0:
            print("Erreur : impossible de créer l'entité.")
            return 0

        print("Entité créée avec succès.")
        return id_entity

    def read(self, id_entity: int) -> Optional[Entity]:
        """Recherche une entité à partir de son identifiant."""

        if id_entity is None or id_entity <= 0:
            return None

        return self.dao.read(id_entity)

    def read_all(self) -> list[Entity]:
        """Retourne toutes les entités."""

        return self.dao.read_all()

    def update(self, entity: Entity) -> bool:
        """Modifie une entité existante."""

        if entity is None:
            print("Erreur : aucune entité n'a été fournie.")
            return False

        if entity.id_entity is None:
            print("Erreur : l'identifiant de l'entité est obligatoire.")
            return False

        if entity.id_entity <= 0:
            print("Erreur : l'identifiant de l'entité est invalide.")
            return False

        if not self.convert_entity(entity):
            return False

        if not self.validate_entity(entity):
            return False

        if self.dao.read(entity.id_entity) is None:
            print("Erreur : cette entité n'existe pas.")
            return False

        if self.dao.exists(entity.name, entity.first_name, entity.id_entity):
            print("Erreur : une autre entité possède déjà ces informations.")
            return False

        return self.dao.update(entity)

    def delete(self, id_entity: int) -> bool:
        """Supprime une entité et ses relations Identity / Entity."""

        if id_entity is None or id_entity <= 0:
            print("Erreur : identifiant invalide.")
            return False

        if self.dao.read(id_entity) is None:
            print("Erreur : cette entité n'existe pas.")
            return False

        nb_usages = self.dao.count_usages_entity(id_entity)

        if nb_usages < 0:
            print(
                "Erreur : impossible de vérifier "
                "les utilisations de cette entité."
            )
            return False

        if nb_usages > 0:
            print(
                f"Erreur : cette entité est encore utilisée "
                f"par {nb_usages} élément(s)."
            )
            return False

        # Supprime les relations avec les identités
        if not self.identity_entity_business.delete_by_entity(id_entity):
            print(
                "Erreur : impossible de supprimer les relations "
                "Identity / Entity."
            )
            return False

        # Supprime ensuite l'entité
        return self.dao.delete(id_entity)

    def count_usages(self, id_entity: int) -> int:
        """Retourne le nombre d'utilisations d'une entité."""

        if id_entity is None or id_entity <= 0:
            return -1

        return self.dao.count_usages_entity(id_entity)

    def validate_entity(self, entity: Entity) -> bool:
        """Nettoie et valide les données d'une entité."""

        if entity is None:
            print("Erreur : aucune entité n'a été fournie.")
            return False

        if entity.name is None:
            print("Erreur : le nom est obligatoire.")
            return False

        entity.name = entity.name.strip()

        if entity.name == "":
            print("Erreur : le nom ne peut pas être vide.")
            return False

        if len(entity.name) > 50:
            print("Erreur : le nom ne peut pas dépasser 50 caractères.")
            return False

        if entity.first_name is not None:
            entity.first_name = entity.first_name.strip()

            if entity.first_name == "":
                entity.first_name = None

        if entity.first_name is not None and len(entity.first_name) > 50:
            print("Erreur : le prénom ne peut pas dépasser 50 caractères.")
            return False

        if entity.type is None:
            print("Erreur : le type est obligatoire.")
            return False

        entity.type = entity.type.strip()

        if entity.type == "":
            print("Erreur : le type ne peut pas être vide.")
            return False

        if len(entity.type) > 50:
            print("Erreur : le type ne peut pas dépasser 50 caractères.")
            return False

        if entity.resume is not None:
            entity.resume = entity.resume.strip()

            if entity.resume == "":
                entity.resume = None

        if entity.creation_date is None:
            print("Erreur : la date de création est obligatoire.")
            return False

        if entity.nb is None:
            print("Erreur : la quantité est obligatoire.")
            return False

        if entity.unit_nb is None:
            print("Erreur : l'unité de quantité est obligatoire.")
            return False

        entity.unit_nb = entity.unit_nb.strip()

        if entity.unit_nb == "":
            print("Erreur : l'unité de quantité ne peut pas être vide.")
            return False

        if len(entity.unit_nb) > 10:
            print("Erreur : l'unité de quantité ne peut pas dépasser 10 caractères.")
            return False

        return True

    def find_by_name(self, name: str) -> list[Entity]:
        """Recherche les entités par nom."""

        if name is None:
            return []

        name = name.strip()

        if name == "":
            return []

        return self.dao.find_by_name(name)

    def convert_entity(self, entity: Entity) -> bool:
        """Convertit et vérifie les données d'une entité."""

        erreurs = []

        # Champs obligatoires
        if entity.name is None or entity.name.strip() == "":
            erreurs.append("Le nom est obligatoire.")

        if entity.type is None or entity.type.strip() == "":
            erreurs.append("Le type est obligatoire.")

        if entity.creation_date is None or str(entity.creation_date).strip() == "":
            erreurs.append("La date de création est obligatoire.")

        if entity.nb is None or str(entity.nb).strip() == "":
            erreurs.append("La quantité est obligatoire.")

        if entity.unit_nb is None or entity.unit_nb.strip() == "":
            erreurs.append("L'unité est obligatoire.")

        # ISBN
        if entity.ISBN is not None and str(entity.ISBN).strip() != "":
            isbn = str(entity.ISBN).strip()

            if not isbn.isdigit():
                erreurs.append(
                    "L'ISBN doit contenir exactement 13 chiffres."
                )
            elif len(isbn) != 13:
                erreurs.append(
                    "L'ISBN doit contenir exactement 13 chiffres."
                )
            else:
                entity.ISBN = int(isbn)

        # Prix
        if entity.price is not None and str(entity.price).strip() != "":
            try:
                entity.price = float(entity.price)
            except ValueError:
                erreurs.append("Le prix doit être un nombre.")

        # Quantité
        if entity.nb is not None and str(entity.nb).strip() != "":
            try:
                entity.nb = float(entity.nb)
            except ValueError:
                erreurs.append("La quantité doit être un nombre.")

        # Date
        if entity.creation_date is not None:
            try:
                entity.creation_date = datetime.strptime(
                    str(entity.creation_date).strip(),
                    "%Y-%m-%d"
                ).date()
            except ValueError:
                erreurs.append(
                    "La date de création doit être au format YYYY-MM-DD."
                )

        # Nettoyage des champs texte
        if entity.name is not None:
            entity.name = entity.name.strip()

        if entity.type is not None:
            entity.type = entity.type.strip()

        if entity.unit_nb is not None:
            entity.unit_nb = entity.unit_nb.strip()

        if entity.first_name is not None:
            entity.first_name = entity.first_name.strip()

            if entity.first_name == "":
                entity.first_name = None

        if entity.resume is not None:
            entity.resume = entity.resume.strip()

            if entity.resume == "":
                entity.resume = None

        # Affichage de toutes les erreurs
        if erreurs:
            print("\n===== ERREURS =====")

            for erreur in erreurs:
                print(f"- {erreur}")

            return False

        return True
