# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.role import Role



@dataclass
class RoleDao(Dao[Role]):

    def create(self, role: Role) -> int:
        """Crée un rôle et retourne son identifiant (0 en cas d'erreur)."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO role (name_role) VALUES (%s)",
                    (role.name_role,)
                )
                role.id_role = cursor.lastrowid

            Dao.connection.commit()
            return role.id_role

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la création du rôle : {error}")
            return 0

    def read(self, id_role: int) -> Optional[Role]:
        """Retourne le rôle correspondant ou None."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id_role, name_role
                    FROM role
                    WHERE id_role = %s
                    """,
                    (id_role,)
                )
                record = cursor.fetchone()

            if not record:
                return None

            role = Role(name_role=record["name_role"])
            role.id_role = record["id_role"]

            return role

        except Exception as error:
            print(f"Erreur lors de la lecture du rôle : {error}")
            return None

    def update(self, role: Role) -> bool:
        """Met à jour un rôle."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE role
                    SET name_role = %s
                    WHERE id_role = %s
                    """,
                    (role.name_role, role.id_role)
                )

            Dao.connection.commit()
            return True

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la modification du rôle : {error}")
            return False

    def delete(self, role: Role) -> bool:
        """Supprime un rôle."""
        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM role WHERE id_role = %s",
                    (role.id_role,)
                )

            Dao.connection.commit()
            return True

        except Exception as error:
            Dao.connection.rollback()
            print(f"Erreur lors de la suppression du rôle : {error}")
            return False
