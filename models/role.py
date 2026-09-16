# -*- coding: utf-8 -*-

"""
Classe Role
"""

from dataclasses import dataclass, field


@dataclass
class Role:
    """
    Représente un rôle associé à une identité.
    """

    name_role: str
    id_role: int = field(default=None, init=False)

    def __str__(self) -> str:
        return self.name_role
