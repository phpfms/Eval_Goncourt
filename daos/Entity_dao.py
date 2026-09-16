# -*- coding: utf-8 -*-

"""
Classe Dao[Entity]
"""

from models.entity import Entity
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class EntityDao(Dao[Entity]):

    def create(self, entity: Entity) -> int:
        """Crée une entité dans la BDD."""

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    INSERT INTO entity
                    (
                        ISBN, price, name, first_name, type,
                        resume, creation_date, nb, unit_nb,
                        fk_id_entity_mother
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                cursor.execute(
                    sql,
                    (
                        entity.ISBN,
                        entity.price,
                        entity.name,
                        entity.first_name,
                        entity.type,
                        entity.resume,
                        entity.creation_date,
                        entity.nb,
                        entity.unit_nb,
                        entity.fk_id_entity_mother
                    )
                )

                id_entity = cursor.lastrowid

            Dao.connection.commit()
            entity.id_entity = id_entity
            return id_entity

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la création de l'entité : {error}")
            return 0

    def read(self, *id_entity: int) -> Optional[Entity]:
        """Renvoie l'entité correspondant à l'identifiant fourni."""

        if len(id_entity) != 1:
            return None

        id_entity = id_entity[0]

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    SELECT
                        id_entity, ISBN, price, name, first_name,
                        type, resume, creation_date, nb, unit_nb,
                        fk_id_entity_mother
                    FROM entity
                    WHERE id_entity = %s
                """

                cursor.execute(sql, (id_entity,))
                record = cursor.fetchone()

            if record is not None:
                entity = Entity(
                    record["ISBN"],
                    record["price"],
                    record["name"],
                    record["first_name"],
                    record["type"],
                    record["resume"],
                    record["creation_date"],
                    record["nb"],
                    record["unit_nb"],
                    record["fk_id_entity_mother"]
                )
                entity.id_entity = record["id_entity"]
                return entity

            return None

        except Exception as error:
            print(f"Erreur lors de la lecture de l'entité : {error}")
            return None

    def read_all(self) -> list[Entity]:
        """Retourne toutes les entités."""

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    SELECT
                        id_entity, ISBN, price, name, first_name,
                        type, resume, creation_date, nb, unit_nb,
                        fk_id_entity_mother
                    FROM entity
                    ORDER BY id_entity
                """

                cursor.execute(sql)
                records = cursor.fetchall()

            entities = []

            for record in records:
                entity = Entity(
                    record["ISBN"],
                    record["price"],
                    record["name"],
                    record["first_name"],
                    record["type"],
                    record["resume"],
                    record["creation_date"],
                    record["nb"],
                    record["unit_nb"],
                    record["fk_id_entity_mother"]
                )
                entity.id_entity = record["id_entity"]
                entities.append(entity)

            return entities

        except Exception as error:
            print(f"Erreur lors de la lecture des entités : {error}")
            return []

    def update(self, entity: Entity) -> bool:
        """Modifie une entité existante dans la BDD."""

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    UPDATE entity
                    SET
                        ISBN = %s,
                        price = %s,
                        name = %s,
                        first_name = %s,
                        type = %s,
                        resume = %s,
                        creation_date = %s,
                        nb = %s,
                        unit_nb = %s,
                        fk_id_entity_mother = %s
                    WHERE id_entity = %s
                """

                cursor.execute(
                    sql,
                    (
                        entity.ISBN,
                        entity.price,
                        entity.name,
                        entity.first_name,
                        entity.type,
                        entity.resume,
                        entity.creation_date,
                        entity.nb,
                        entity.unit_nb,
                        entity.fk_id_entity_mother,
                        entity.id_entity
                    )
                )

            Dao.connection.commit()
            return cursor.rowcount > 0

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la modification de l'entité : {error}")
            return False

    def delete(self, id_entity: int) -> bool:
        """Supprime une entité de la BDD."""

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    DELETE FROM entity
                    WHERE id_entity = %s
                """

                cursor.execute(sql, (id_entity,))

            Dao.connection.commit()
            return cursor.rowcount > 0

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la suppression de l'entité : {error}")
            return False

    def count_usages_entity(self, id_entity: int) -> int:
        """Compte les utilisations de l'entité dans les tables de liaison."""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        (
                            SELECT COUNT(*)
                            FROM identity_entity
                            WHERE fk_id_entity = %s
                        )
                        +
                        (
                            SELECT COUNT(*)
                            FROM entity_election
                            WHERE fk_id_entity = %s
                        )
                        +
                        (
                            SELECT COUNT(*)
                            FROM entity_jury
                            WHERE fk_id_entity = %s
                        ) AS nb_utilisations
                    """,
                    (id_entity, id_entity, id_entity)
                )

                return cursor.fetchone()["nb_utilisations"]

        except Exception as error:
            print(f"Erreur lors du comptage des utilisations de l'entité : {error}")
            return -1

    def exists(
            self,
            name: str,
            first_name: Optional[str],
            id_entity: Optional[int] = None
    ) -> bool:
        """Vérifie si une autre entité possède le même nom et prénom."""

        try:
            with Dao.connection.cursor() as cursor:
                if id_entity is None:
                    sql = """
                        SELECT COUNT(*) AS nb
                        FROM entity
                        WHERE name = %s
                        AND first_name = %s
                    """
                    cursor.execute(sql, (name, first_name))
                else:
                    sql = """
                        SELECT COUNT(*) AS nb
                        FROM entity
                        WHERE name = %s
                        AND first_name = %s
                        AND id_entity != %s
                    """
                    cursor.execute(sql, (name, first_name, id_entity))

                result = cursor.fetchone()
                return result["nb"] > 0

        except Exception as error:
            print(f"Erreur lors de la vérification du doublon : {error}")
            return False

    def find_by_name(self, name: str) -> list[Entity]:
        """Recherche les entités par nom ou prénom."""

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    SELECT
                        id_entity, ISBN, price, name, first_name,
                        type, resume, creation_date, nb, unit_nb,
                        fk_id_entity_mother
                    FROM entity
                    WHERE name LIKE %s
                       OR first_name LIKE %s
                    ORDER BY id_entity
                """

                search = f"%{name}%"
                cursor.execute(sql, (search, search))
                records = cursor.fetchall()

            entities = []

            for record in records:
                entity = Entity(
                    record["ISBN"],
                    record["price"],
                    record["name"],
                    record["first_name"],
                    record["type"],
                    record["resume"],
                    record["creation_date"],
                    record["nb"],
                    record["unit_nb"],
                    record["fk_id_entity_mother"]
                )
                entity.id_entity = record["id_entity"]
                entities.append(entity)

            return entities

        except Exception as error:
            print(f"Erreur lors de la recherche de l'entité : {error}")
            return []