# -*- coding: utf-8 -*-

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Jury:
    date_begin: date
    date_end: date
    fk_id_identity_president: Optional[int]
    nb_entity: int
    nb_entity_mode: str
    fk_id_jury_mother: Optional[int] = None
    id_jury: Optional[int] = None