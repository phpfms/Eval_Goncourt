# -*- coding: utf-8 -*-

"""
Classe Dao[IdentityEntity]
"""

from models.identity_entity import IdentityEntity
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class IdentityEntityDao(Dao[IdentityEntity]):

    def create(self, identity_entity: IdentityEntity) -> bool:
        """Crée une relation Identity / Entity."""
        if identity_entity.fk_id_entity is None and identity_entity.fk_id_identity is None:
            print("Erreur : fk_id_entity et fk_id_identity ne peuvent pas être tous les deux NULL.")
            return False

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    INSERT INTO identity_entity (fk_id_entity, fk_id_identity, fk_id_role)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(sql, (
                    identity_entity.fk_id_entity,
                    identity_entity.fk_id_identity,
                    identity_entity.fk_id_role
                ))
            Dao.connection.commit()
            return True
        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la création de la relation Identity / Entity : {error}")
            return False

    def read(self, *id_entity: int) -> Optional[IdentityEntity]:
        """
        Renvoie une relation Identity / Entity / Role.
        """

        if len(id_entity) != 3:
            return None

        fk_id_entity = id_entity[0]
        fk_id_identity = id_entity[1]
        fk_id_role = id_entity[2]

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    SELECT
                        fk_id_entity,
                        fk_id_identity,
                        fk_id_role
                    FROM identity_entity
                    WHERE fk_id_entity <=> %s
                      AND fk_id_identity <=> %s
                      AND fk_id_role = %s
                """

                cursor.execute(
                    sql,
                    (
                        fk_id_entity,
                        fk_id_identity,
                        fk_id_role
                    )
                )

                record = cursor.fetchone()

            if record is not None:
                return IdentityEntity(
                    fk_id_entity=record["fk_id_entity"],
                    fk_id_identity=record["fk_id_identity"],
                    fk_id_role=record["fk_id_role"]
                )

            return None

        except Exception as error:
            print(
                f"Erreur lors de la lecture de la relation "
                f"Identity / Entity : {error}"
            )
            return None

    def update(self, identity_entity: IdentityEntity) -> bool:
        """Modifie le rôle d'une relation Identity / Entity."""

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    UPDATE identity_entity
                    SET fk_id_role = %s
                    WHERE fk_id_entity <=> %s
                      AND fk_id_identity <=> %s
                """

                cursor.execute(
                    sql,
                    (
                        identity_entity.fk_id_role,
                        identity_entity.fk_id_entity,
                        identity_entity.fk_id_identity
                    )
                )

            Dao.connection.commit()

            return cursor.rowcount > 0

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors de la modification de la relation "
                f"Identity / Entity : {error}"
            )
            return False

    def delete(self, identity_entity: IdentityEntity) -> bool:
        """Supprime une relation Identity / Entity."""
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    DELETE FROM identity_entity
                    WHERE fk_id_entity <=> %s
                      AND fk_id_identity <=> %s
                      AND fk_id_role = %s
                """
                cursor.execute(sql, (identity_entity.fk_id_entity, identity_entity.fk_id_identity,
                                     identity_entity.fk_id_role))
            Dao.connection.commit()
            return cursor.rowcount > 0
        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la suppression de la relation Identity / Entity : {error}")
            return False

    def delete_by_entity(self, id_entity: int) -> bool:
        """Supprime les relations Identity / Entity liées à une entité."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM identity_entity
                    WHERE fk_id_entity = %s
                    """,
                    (id_entity,)
                )
            Dao.connection.commit()
            return True
        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la suppression des relations de l'entité : {error}")
            return False