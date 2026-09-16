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
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    INSERT INTO identity (
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

                Dao.connection.commit()

                identity.id_identity = cursor.lastrowid

                return identity.id_identity

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

    def read_all(self) -> list[Identity]:
        """Retourne toutes les identités."""

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
                    ORDER BY id_identity
                """

                cursor.execute(sql)
                records = cursor.fetchall()

            identities = []

            for record in records:
                identity = Identity(
                    record["appelation"],
                    record["under_appelation"],
                    record["description"],
                    record["address"],
                    record["fk_id_identity_mother"]
                )

                identity.id_identity = record["id_identity"]

                identities.append(identity)

            return identities

        except Exception as error:
            print(
                f"Erreur lors de la lecture des identités : {error}"
            )
            return []

    def update(self, identity: Identity) -> bool:
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

            return cursor.rowcount > 0

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la modification de l'identité : {error}")
            return False

    def delete(self, id_identity: int) -> bool:
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

            return cursor.rowcount > 0

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la suppression de l'identité : {error}")
            return False

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

    def exists(
            self,
            appelation: str,
            under_appelation: str,
            id_identity: Optional[int] = None
    ) -> bool:
        """
        Vérifie si une identité existe déjà avec la même
        appellation et la même sous-appellation.

        Si id_identity est fourni, cette identité est ignorée
        dans la recherche. Cela permet d'utiliser cette méthode
        lors d'une modification.

        Retourne True si une autre identité correspond.
        Retourne False sinon.
        """

        try:
            with Dao.connection.cursor() as cursor:

                if id_identity is None:
                    sql = """
                        SELECT COUNT(*) AS nb
                        FROM identity
                        WHERE appelation = %s
                        AND under_appelation = %s
                    """

                    cursor.execute(
                        sql,
                        (
                            appelation,
                            under_appelation
                        )
                    )

                else:
                    sql = """
                        SELECT COUNT(*) AS nb
                        FROM identity
                        WHERE appelation = %s
                        AND under_appelation = %s
                        AND id_identity != %s
                    """

                    cursor.execute(
                        sql,
                        (
                            appelation,
                            under_appelation,
                            id_identity
                        )
                    )

                result = cursor.fetchone()

                return result["nb"] > 0

        except Exception as error:
            print(
                f"Erreur lors de la vérification du doublon : {error}"
            )
            return False

    def find_by_name(self, name: str) -> list[Identity]:
        """Recherche les identités par appellation ou sous-appellation."""

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
                    WHERE appelation LIKE %s
                       OR under_appelation LIKE %s
                    ORDER BY id_identity
                """

                search = f"%{name}%"

                cursor.execute(
                    sql,
                    (search, search)
                )

                records = cursor.fetchall()

            identities = []

            for record in records:
                identity = Identity(
                    record["appelation"],
                    record["under_appelation"],
                    record["description"],
                    record["address"],
                    record["fk_id_identity_mother"]
                )

                identity.id_identity = record["id_identity"]

                identities.append(identity)

            return identities

        except Exception as error:
            print(
                f"Erreur lors de la recherche de l'identité : {error}"
            )
            return []