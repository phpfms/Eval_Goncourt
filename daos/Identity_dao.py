# -*- coding: utf-8 -*-

"""
Classe Dao[Identity]
"""

from models.identity import Identity
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class IdentityDao(Dao[Identity]):

    def create(self, identity: Identity) -> int:
        """
        Crée une identité dans la BDD.
        Retourne l'identifiant de l'identité créée.
        Retourne 0 en cas d'erreur.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    INSERT INTO identity
                    (
                        appelation,
                        under_appelation,
                        description,
                        address,
                        fk_id_identity_mother
                    )
                    VALUES (%s, %s, %s, %s, %s)
                """

                cursor.execute(
                    sql,
                    (
                        identity.appelation,
                        identity.under_appelation,
                        identity.description,
                        identity.address,
                        identity.fk_id_identity_mother
                    )
                )

                id_identity = cursor.lastrowid

            Dao.connection.commit()

            identity.id_identity = id_identity

            return id_identity

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la création de l'identité : {error}")
            return 0

    def read(self, *id_entity: int) -> Optional[Identity]:
        """
        Renvoie l'identité correspondant à l'identifiant fourni.

        Retourne None si l'identité n'existe pas.
        """

        if len(id_entity) != 1:
            return None

        id_identity = id_entity[0]

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    SELECT
                        id_identity,
                        appelation,
                        under_appelation,
                        description,
                        address,
                        fk_id_identity_mother
                    FROM identity
                    WHERE id_identity = %s
                """

                cursor.execute(sql, (id_identity,))
                record = cursor.fetchone()

            if record is not None:
                identity = Identity(
                    record["appelation"],
                    record["under_appelation"],
                    record["description"],
                    record["address"],
                    record["fk_id_identity_mother"]
                )

                identity.id_identity = record["id_identity"]

                return identity

            return None

        except Exception as error:
            print(f"Erreur lors de la lecture de l'identité : {error}")
            return None

    def update(self, identity: Identity) -> None:
        """
        Modifie une identité existante dans la BDD.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    UPDATE identity
                    SET
                        appelation = %s,
                        under_appelation = %s,
                        description = %s,
                        address = %s,
                        fk_id_identity_mother = %s
                    WHERE id_identity = %s
                """

                cursor.execute(
                    sql,
                    (
                        identity.appelation,
                        identity.under_appelation,
                        identity.description,
                        identity.address,
                        identity.fk_id_identity_mother,
                        identity.id_identity
                    )
                )

            Dao.connection.commit()

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la modification de l'identité : {error}")

    def delete(self, id_identity: int) -> None:
        """
        Supprime une identité de la BDD.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    DELETE FROM identity
                    WHERE id_identity = %s
                """

                cursor.execute(sql, (id_identity,))

            Dao.connection.commit()

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la suppression de l'identité : {error}")

    def count_usages_identity(self, id_identity: int) -> int:
        """
        Compte le nombre d'Entity utilisant cette identité.
        """
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT COUNT(*) AS nb_utilisations
                    FROM identity_entity
                    WHERE fk_id_identity = %s
                    """,
                    (id_identity,)
                )

                return cursor.fetchone()["nb_utilisations"]

        except Exception as error:
            print(
                f"Erreur lors du comptage des utilisations de l'identité : {error}"
            )
            return -1