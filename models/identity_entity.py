# -*- coding: utf-8 -*-

"""
Classe représentant une relation entre une Identity et une Entity.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class IdentityEntity:
    fk_id_entity: Optional[int] = None
    fk_id_identity: Optional[int] = None
    role_id_identity: str = ""
