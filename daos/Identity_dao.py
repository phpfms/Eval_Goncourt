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
        """Supprime une identité."""

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    DELETE FROM identity
                    WHERE id_identity = %s
                """

                cursor.execute(sql, (id_identity,))

                deleted = cursor.rowcount > 0

            Dao.connection.commit()
            return deleted

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors de la suppression de l'identité : {error}"
            )
            return False

    def count_usages_identity(self, id_identity: int) -> int:
        """
        Compte le nombre d'utilisations de l'identité.
        """
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        (
                            SELECT COUNT(*)
                            FROM identity_entity
                            WHERE fk_id_identity = %s
                        )
                        +
                        (
                            SELECT COUNT(*)
                            FROM identity_jury
                            WHERE fk_id_identity = %s
                        )
                        AS nb_utilisations
                    """,
                    (id_identity, id_identity)
                )
                return cursor.fetchone()["nb_utilisations"]
        except Exception as error:
            print(f"Erreur lors du comptage des utilisations de l'identité : {error}")
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

    def add_role(self, id_identity: int, id_role: int) -> bool:
        """Affecte un rôle direct à une identité s'il n'existe pas."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT 1
                    FROM identity_entity
                    WHERE fk_id_identity = %s
                    AND fk_id_role = %s
                    AND fk_id_entity IS NULL
                    """,
                    (id_identity, id_role)
                )

                if cursor.fetchone() is not None:
                    return True

                cursor.execute(
                    """
                    INSERT INTO identity_entity
                    (
                        fk_id_entity,
                        fk_id_identity,
                        fk_id_role
                    )
                    VALUES (%s, %s, %s)
                    """,
                    (None, id_identity, id_role)
                )

            Dao.connection.commit()
            return True

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de l'affectation du rôle : {error}")
            return False

    def find_by_role(self, id_role: int) -> list[Identity]:
        """Retourne les identités possédant un rôle."""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT DISTINCT
                           i.id_identity,
                           i.appelation,
                           i.under_appelation,
                           i.description,
                           i.address,
                           i.fk_id_identity_mother
                    FROM identity i
                    INNER JOIN identity_entity ie
                        ON ie.fk_id_identity = i.id_identity
                    WHERE ie.fk_id_role = %s
                    ORDER BY i.appelation
                    """,
                    (id_role,)
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
                f"Erreur lors de la recherche des identités par rôle : "
                f"{error}"
            )
            return []

    def add_entity(
            self,
            id_identity: int,
            id_entity: int,
            id_role: int
    ) -> bool:
        """Associe une identité à une entité avec un rôle."""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO identity_entity
                    (
                        fk_id_entity,
                        fk_id_identity,
                        fk_id_role
                    )
                    VALUES (%s, %s, %s)
                    """,
                    (
                        id_entity,
                        id_identity,
                        id_role
                    )
                )

            Dao.connection.commit()
            return True

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors de l'ajout de l'intervenant : "
                f"{error}"
            )
            return False

    def find_entities_by_identity(self, id_identity: int) -> list:
        """Retourne les entités utilisant cette identité."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT e.*
                    FROM entity e
                    INNER JOIN identity_entity ie
                        ON ie.fk_id_entity = e.id_entity
                    WHERE ie.fk_id_identity = %s
                    """,
                    (id_identity,)
                )
                return cursor.fetchall()
        except Exception as error:
            print(f"Erreur lors de la recherche des entités liées à l'identité : {error}")
            return []

    def find_juries_by_identity(self, id_identity: int) -> list:
        """Retourne les jurys utilisant cette identité."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT j.*
                    FROM jury j
                    INNER JOIN identity_jury ij
                        ON ij.fk_id_jury = j.id_jury
                    WHERE ij.fk_id_identity = %s
                    """,
                    (id_identity,)
                )
                return cursor.fetchall()
        except Exception as error:
            print(f"Erreur lors de la recherche des jurys liés à l'identité : {error}")
            return []

    def find_elections_by_identity(self, id_identity: int) -> list:
        """Retourne les entités liées à une identité et présentes dans une élection."""

        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    SELECT DISTINCT
                        e.id_entity,
                        e.name,
                        e.first_name,
                        ee.fk_id_election
                    FROM identity_entity ie
                    INNER JOIN entity e
                        ON e.id_entity = ie.fk_id_entity
                    INNER JOIN entity_election ee
                        ON ee.fk_id_entity = e.id_entity
                    WHERE ie.fk_id_identity = %s
                    ORDER BY e.id_entity, ee.fk_id_election
                """

                cursor.execute(sql, (id_identity,))
                return cursor.fetchall()

        except Exception as error:
            print(
                "Erreur lors de la recherche des élections "
                f"de l'identité : {error}"
            )
            return []

    def count_entity_usages_identity(self, id_identity: int) -> int:
        """Compte les entités encore liées à une identité."""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT COUNT(*) AS nb_utilisations
                    FROM identity_entity
                    WHERE fk_id_identity = %s
                    AND fk_id_entity IS NOT NULL
                    """,
                    (id_identity,)
                )

                return cursor.fetchone()["nb_utilisations"]

        except Exception as error:
            print(
                "Erreur lors du comptage des entités liées à l'identité : "
                f"{error}"
            )
            return -1