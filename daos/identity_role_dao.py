# -*- coding: utf-8 -*-

"""
Classe Dao[IdentityRole]
"""

from models.identity_role import IdentityRole
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class IdentityRoleDao(Dao[IdentityRole]):

    def create(self, identity_role: IdentityRole) -> int:
        """
        Crée une relation entre une Identity et un Role.

        Retourne 1 si la création a réussi.
        Retourne 0 en cas d'erreur.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    INSERT INTO identity_role
                    (
                        fk_id_identity,
                        fk_id_role
                    )
                    VALUES (%s, %s)
                """

                cursor.execute(
                    sql,
                    (
                        identity_role.fk_id_identity,
                        identity_role.fk_id_role
                    )
                )

            Dao.connection.commit()

            return 1

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors de la création de la relation "
                f"Identity / Role : {error}"
            )
            return 0

    def read(self, *id_entity: int) -> Optional[IdentityRole]:
        """
        Renvoie une relation Identity / Role.

        Une relation est identifiée par :
        - l'id de l'Identity
        - l'id du Role
        """

        if len(id_entity) != 2:
            return None

        id_identity = id_entity[0]
        id_role = id_entity[1]

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    SELECT
                        fk_id_identity,
                        fk_id_role
                    FROM identity_role
                    WHERE fk_id_identity = %s
                      AND fk_id_role = %s
                """

                cursor.execute(
                    sql,
                    (
                        id_identity,
                        id_role
                    )
                )

                record = cursor.fetchone()

            if record is not None:
                return IdentityRole(
                    fk_id_identity=record["fk_id_identity"],
                    fk_id_role=record["fk_id_role"]
                )

            return None

        except Exception as error:
            print(
                f"Erreur lors de la lecture de la relation "
                f"Identity / Role : {error}"
            )
            return None

    def update(self, identity_role: IdentityRole) -> bool:
        """
        Modifie une relation Identity / Role.

        Comme les deux colonnes constituent la clé primaire,
        on identifie la relation avec les anciennes valeurs.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    UPDATE identity_role
                    SET fk_id_role = %s
                    WHERE fk_id_identity = %s
                      AND fk_id_role = %s
                """

                cursor.execute(
                    sql,
                    (
                        identity_role.fk_id_role,
                        identity_role.fk_id_identity,
                        identity_role.fk_id_role
                    )
                )

            Dao.connection.commit()

            return True

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors de la modification de la relation "
                f"Identity / Role : {error}"
            )
            return False

    def delete(self, identity_role: IdentityRole) -> bool:
        """
        Supprime une relation Identity / Role.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    DELETE FROM identity_role
                    WHERE fk_id_identity = %s
                      AND fk_id_role = %s
                """

                cursor.execute(
                    sql,
                    (
                        identity_role.fk_id_identity,
                        identity_role.fk_id_role
                    )
                )

            Dao.connection.commit()

            return True

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors de la suppression de la relation "
                f"Identity / Role : {error}"
            )
            return False