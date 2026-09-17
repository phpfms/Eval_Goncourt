# -*- coding: utf-8 -*-

from daos.dao import Dao


class IdentityJuryDao(Dao):
    """DAO pour la gestion des relations Identity / Jury."""

    def create(self, id_jury: int, id_identity: int) -> bool:
        """Associe une identité à un jury."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO identity_jury (
                        fk_id_jury,
                        fk_id_identity
                    )
                    VALUES (%s, %s)
                    """,
                    (id_jury, id_identity)
                )

            Dao.connection.commit()
            return True

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors de l'ajout de la personne au jury : {error}"
            )
            return False

    def read(
            self,
            id_jury: int,
            id_identity: int
    ) -> bool:
        """Vérifie si une identité appartient à un jury."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT 1
                    FROM identity_jury
                    WHERE fk_id_jury = %s
                    AND fk_id_identity = %s
                    """,
                    (id_jury, id_identity)
                )

                return cursor.fetchone() is not None

        except Exception as error:
            print(
                f"Erreur lors de la recherche de la relation : {error}"
            )
            return False

    def update(self, id_jury: int, id_identity: int) -> bool:
        """Modifie une relation Identity / Jury."""
        return False

    def delete(
            self,
            id_jury: int,
            id_identity: int
    ) -> bool:
        """Retire une identité d'un jury."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM identity_jury
                    WHERE fk_id_jury = %s
                    AND fk_id_identity = %s
                    """,
                    (id_jury, id_identity)
                )

            Dao.connection.commit()
            return True

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors du retrait de la personne du jury : {error}"
            )
            return False

    def delete_by_jury(self, id_jury: int) -> bool:
        """Supprime toutes les relations d'un jury."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM identity_jury
                    WHERE fk_id_jury = %s
                    """,
                    (id_jury,)
                )

            Dao.connection.commit()
            return True

        except Exception as error:
            Dao.connection.rollback()
            print(
                f"Erreur lors de la suppression des membres : {error}"
            )
            return False

    def count_by_jury(self, id_jury: int) -> int:
        """Compte le nombre de membres d'un jury."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT COUNT(*) AS total
                    FROM identity_jury
                    WHERE fk_id_jury = %s
                    """,
                    (id_jury,)
                )

                record = cursor.fetchone()

            return record["total"] if record else 0

        except Exception as error:
            print(
                f"Erreur lors du comptage des membres : {error}"
            )
            return -1

    def find_identities_by_jury(self, id_jury: int) -> list[int]:
        """Retourne les identifiants des membres d'un jury."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT fk_id_identity
                    FROM identity_jury
                    WHERE fk_id_jury = %s
                    ORDER BY fk_id_identity
                    """,
                    (id_jury,)
                )

                records = cursor.fetchall()

            return [
                record["fk_id_identity"]
                for record in records
            ]

        except Exception as error:
            print(
                f"Erreur lors de la recherche des membres : {error}"
            )
            return []

    def find_juries_by_identity(
            self,
            id_identity: int
    ) -> list[int]:
        """Retourne les identifiants des jurys d'une identité."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT fk_id_jury
                    FROM identity_jury
                    WHERE fk_id_identity = %s
                    ORDER BY fk_id_jury
                    """,
                    (id_identity,)
                )

                records = cursor.fetchall()

            return [
                record["fk_id_jury"]
                for record in records
            ]

        except Exception as error:
            print(
                f"Erreur lors de la recherche des jurys : {error}"
            )
            return []

    def find_members_details(self, id_jury: int) -> list[dict]:
        """Retourne les informations des membres d'un jury."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        i.id_identity,
                        i.appelation,
                        i.under_appelation
                    FROM identity_jury ij
                    INNER JOIN identity i
                        ON i.id_identity = ij.fk_id_identity
                    WHERE ij.fk_id_jury = %s
                    ORDER BY i.id_identity
                    """,
                    (id_jury,)
                )
                return cursor.fetchall()
        except Exception as error:
            print(
                f"Erreur lors de la recherche des membres : {error}"
            )
            return []