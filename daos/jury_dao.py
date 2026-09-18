# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.jury import Jury


@dataclass
class JuryDao(Dao[Jury]):
    """DAO permettant de gérer les jurys en base de données."""

    def create(self, jury: Jury) -> int:
        """Crée un jury et retourne son identifiant."""

        # Les seules valeurs autorisées par les règles métier sont MIN, MAX et EXACT.
        # Cette vérification évite d'envoyer une valeur invalide à MySQL.
        if jury.nb_entity_mode not in ("MIN", "MAX", "EXACT"):
            print(f"Erreur lors de la création du jury : mode invalide ({jury.nb_entity_mode}).")
            return 0

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO jury (
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
        """Recherche un jury à partir de son identifiant."""

        # Le DAO attend exactement un identifiant.
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
        """Modifie un jury existant."""

        # Le DAO protège également la base contre une valeur invalide.
        # Le Business applique déjà cette règle, mais le DAO doit rester robuste
        # car il peut être appelé directement par les tests ou par un autre code.
        if jury.nb_entity_mode not in ("MIN", "MAX", "EXACT"):
            print(f"Erreur lors de la modification du jury : mode invalide ({jury.nb_entity_mode}).")
            return False

        # Un jury doit posséder un identifiant pour pouvoir être modifié.
        if jury.id_jury is None or jury.id_jury <= 0:
            print("Erreur lors de la modification du jury : identifiant invalide.")
            return False

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

        # Un identifiant invalide ne doit pas provoquer de requête SQL.
        if id_jury is None or id_jury <= 0:
            return False

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
        """Compte les membres associés à un jury."""

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

    def find_by_president_name(self, name: str) -> list[Jury]:
        """Retourne les jurys correspondant au nom de leur président."""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT
                        j.id_jury,
                        j.date_begin,
                        j.date_end,
                        j.fk_id_identity_president,
                        j.nb_entity,
                        j.nb_entity_mode,
                        j.fk_id_jury_mother
                    FROM jury j
                    INNER JOIN identity i
                        ON i.id_identity = j.fk_id_identity_president
                    WHERE i.appelation LIKE %s
                    ORDER BY j.id_jury
                    """,
                    (f"%{name}%",)
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
            print(f"Erreur lors de la recherche des jurys par président : {error}")
            return []

    def count_elections(self, id_jury: int) -> int:
        """Compte les élections associées à un jury."""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT COUNT(*) AS total
                    FROM election
                    WHERE fk_id_jury = %s
                    """,
                    (id_jury,)
                )
                record = cursor.fetchone()

            return record["total"] if record else 0

        except Exception as error:
            print(f"Erreur lors du comptage des élections du jury : {error}")
            return -1