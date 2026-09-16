# -*- coding: utf-8 -*-

"""
Classe Business pour la gestion des rôles.
"""

from dataclasses import dataclass

from daos.role_dao import RoleDao
from models.role import Role


@dataclass
class RoleBusiness:
    """Classe métier permettant de gérer les rôles."""

    dao: RoleDao

    def read_all(self) -> list[Role]:
        """Retourne tous les rôles."""

        return self.dao.read_all()