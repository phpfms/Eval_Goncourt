# -*- coding: utf-8 -*-

"""
Classe Entity
"""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass
class Entity:
    """
    Représente une entité métier du projet Goncourt.

    Dans le chargement initial actuel, les Entity représentent
    principalement les livres.
    """

    ISBN: Optional[int]
    price: Optional[float]
    name: str
    first_name: Optional[str]
    type: str
    resume: Optional[str]
    creation_date: date
    nb: float
    unit_nb: str
    fk_id_entity_mother: Optional[int]

    id_entity: Optional[int] = field(default=None, init=False)

    def __str__(self) -> str:
        return self.name
