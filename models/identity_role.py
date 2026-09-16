# -*- coding: utf-8 -*-

"""
Classe représentant une relation entre une Identity et un Role.
"""

from dataclasses import dataclass


@dataclass
class IdentityRole:
    fk_id_identity:int
    fk_id_role: int