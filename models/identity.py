# -*- coding: utf-8 -*-

"""
Classe Identity
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Identity:
    """
    Représente une identité : personne ou organisation.
    """
    appelation: str
    under_appelation: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    fk_id_identity_mother: Optional[int] = None

    id_identity: Optional[int] = field(default=None, init=False)

    def __str__(self) -> str:
        if self.under_appelation:
            return f"{self.under_appelation} {self.appelation}"

        return self.appelation

