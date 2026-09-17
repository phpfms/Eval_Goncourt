# -*- coding: utf-8 -*-

"""
Classe métier pour la gestion des rôles.
"""

from dataclasses import dataclass
from typing import Optional
from models.role import Role
from daos.role_dao import RoleDao


@dataclass
class RoleBusiness:
    """Classe métier permettant de gérer les rôles."""
    dao: RoleDao

    def read(self, id_role: int) -> Optional[Role]:
        """Recherche un rôle à partir de son identifiant."""
        if id_role is None or id_role <= 0:
            return None
        return self.dao.read(id_role)

    def read_all(self) -> list[Role]:
        """Retourne tous les rôles."""
        return self.dao.read_all()

    def find_by_name(self, name_role: str) -> Optional[Role]:
        """Recherche un rôle à partir de son nom."""
        # Le Business valide la donnée avant de transmettre la recherche au DAO.
        if name_role is None:
            return None
        name_role = name_role.strip()
        if name_role == "":
            return None
        return self.dao.find_by_name(name_role)