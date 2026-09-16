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

    def create(self, identity_entity: IdentityEntity) -> int:
        """
        Crée une relation entre une Identity et une Entity.

        Retourne 1 si la création a réussi.
        Retourne 0 en cas d'erreur.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    INSERT INTO identity_entity
                    (
                        fk_id_entity,
                        fk_id_identity,
                        fk_id_role
                    )
                    VALUES (%s, %s, %s)
                """

                cursor.execute(
                    sql,
                    (
                        identity_entity.fk_id_entity,
                        identity_entity.fk_id_identity,
                        identity_entity.fk_id_role
                    )
                )

            Dao.connection.commit()

            return 1

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors de la création de la relation "
                f"Identity / Entity : {error}"
            )
            return 0

    def read(self, id_entity: int, id_identity: int,
             fk_id_role: str) -> Optional[IdentityEntity]:
        """
        Renvoie une relation Identity / Entity.

        Une relation est identifiée par :
        - l'id de l'Entity
        - l'id de l'Identity
        - le rôle
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    SELECT
                        fk_id_entity,
                        fk_id_identity,
                        fk_id_role
                    FROM identity_entity
                    WHERE fk_id_entity = %s
                      AND fk_id_identity = %s
                      AND fk_id_role = %s
                """

                cursor.execute(
                    sql,
                    (
                        id_entity,
                        id_identity,
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
        """
        Modifie le rôle d'une relation Identity / Entity.

        Les deux clés étrangères constituent l'identification
        de la relation.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    UPDATE identity_entity
                    SET fk_id_role = %s
                    WHERE fk_id_entity = %s
                      AND fk_id_identity = %s
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

            return True

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors de la modification de la relation "
                f"Identity / Entity : {error}"
            )
            return False

    def delete(self, identity_entity: IdentityEntity) -> bool:
        """
        Supprime une relation Identity / Entity.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    DELETE FROM identity_entity
                    WHERE fk_id_entity = %s
                      AND fk_id_identity = %s
                      AND fk_id_role = %s
                """

                cursor.execute(
                    sql,
                    (
                        identity_entity.fk_id_entity,
                        identity_entity.fk_id_identity,
                        identity_entity.fk_id_role
                    )
                )

            Dao.connection.commit()

            return True

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors de la suppression de la relation "
                f"Identity / Entity : {error}"
            )
            return False
