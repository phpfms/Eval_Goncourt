# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.jury import Jury


@dataclass
class JuryDao(Dao[Jury]):

    def create(self, jury: Jury) -> int:
        """Crée un jury."""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO jury
                    (
                        date_begin,
                        date_end,
                        fk_id_identity_president,
                        nb_entity,
                        nb_entity_mode,
                        fk_id_jury_mother
                    )
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (
                        jury.date_begin,
                        jury.date_end,
                        jury.fk_id_identity_president,
                        jury.nb_entity,
                        jury.nb_entity_mode,
                        jury.fk_id_jury_mother
                    )
                )

                id_jury = cursor.lastrowid

            Dao.connection.commit()
            jury.id_jury = id_jury
            return id_jury

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la création du jury : {error}")
            return 0

    def read(self, *id_jury: int) -> Optional[Jury]:
        """Recherche un jury."""

        if len(id_jury) != 1:
            return None

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        id_jury,
                        date_begin,
                        date_end,
                        fk_id_identity_president,
                        nb_entity,
                        nb_entity_mode,
                        fk_id_jury_mother
                    FROM jury
                    WHERE id_jury = %s
                    """,
                    (id_jury[0],)
                )

                record = cursor.fetchone()

            if record is None:
                return None

            jury = Jury(
                record["date_begin"],
                record["date_end"],
                record["fk_id_identity_president"],
                record["nb_entity"],
                record["nb_entity_mode"],
                record["fk_id_jury_mother"]
            )
            jury.id_jury = record["id_jury"]
            return jury

        except Exception as error:
            print(f"Erreur lors de la lecture du jury : {error}")
            return None

    def read_all(self) -> list[Jury]:
        """Retourne tous les jurys."""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        id_jury,
                        date_begin,
                        date_end,
                        fk_id_identity_president,
                        nb_entity,
                        nb_entity_mode,
                        fk_id_jury_mother
                    FROM jury
                    ORDER BY id_jury
                    """
                )

                records = cursor.fetchall()

            juries = []

            for record in records:
                jury = Jury(
                    record["date_begin"],
                    record["date_end"],
                    record["fk_id_identity_president"],
                    record["nb_entity"],
                    record["nb_entity_mode"],
                    record["fk_id_jury_mother"]
                )
                jury.id_jury = record["id_jury"]
                juries.append(jury)

            return juries

        except Exception as error:
            print(f"Erreur lors de la lecture des jurys : {error}")
            return []

    def update(self, jury: Jury) -> bool:
        """Modifie un jury."""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE jury
                    SET
                        date_begin = %s,
                        date_end = %s,
                        fk_id_identity_president = %s,
                        nb_entity = %s,
                        nb_entity_mode = %s,
                        fk_id_jury_mother = %s
                    WHERE id_jury = %s
                    """,
                    (
                        jury.date_begin,
                        jury.date_end,
                        jury.fk_id_identity_president,
                        jury.nb_entity,
                        jury.nb_entity_mode,
                        jury.fk_id_jury_mother,
                        jury.id_jury
                    )
                )

                updated = cursor.rowcount > 0

            Dao.connection.commit()
            return updated

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la modification du jury : {error}")
            return False

    def delete(self, id_jury: int) -> bool:
        """Supprime un jury."""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM jury
                    WHERE id_jury = %s
                    """,
                    (id_jury,)
                )

                deleted = cursor.rowcount > 0

            Dao.connection.commit()
            return deleted

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la suppression du jury : {error}")
            return False

    def count_members(self, id_jury: int) -> int:
        """Compte les membres d'un jury."""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT COUNT(*) AS nb
                    FROM identity_jury
                    WHERE fk_id_jury = %s
                    """,
                    (id_jury,)
                )

                record = cursor.fetchone()

            return record["nb"] if record else 0

        except Exception as error:
            print(f"Erreur lors du comptage des membres : {error}")
            return -1