# -*- coding: utf-8 -*-

"""
Tests du DAO JuryDao.
"""

from datetime import date

from daos.jury_dao import JuryDao
from models.jury import Jury


def test_create_jury():
    """Insère un jury de test et vérifie sa création."""
    dao = JuryDao()

    jury = Jury(
        date_begin=date(2026, 1, 1),
        date_end=date(2026, 12, 31),
        fk_id_identity_president=None,
        nb_entity=2,
        nb_entity_mode="EXACT",
        fk_id_jury_mother=None
    )

    created_id = dao.create(jury)

    assert created_id > 0
    assert jury.id_jury == created_id

    try:
        created = dao.read(created_id)

        assert created is not None
        assert created.id_jury == created_id
        assert created.nb_entity == 2
        assert created.nb_entity_mode == "EXACT"

    finally:
        deleted = dao.delete(created_id)
        assert deleted is True


def test_read_jury_existant():
    """Lit un jury qui vient d'être créé."""
    dao = JuryDao()

    jury = Jury(
        date_begin=date(2026, 1, 1),
        date_end=date(2026, 12, 31),
        fk_id_identity_president=None,
        nb_entity=2,
        nb_entity_mode="EXACT",
        fk_id_jury_mother=None
    )

    created_id = dao.create(jury)

    assert created_id > 0

    try:
        result = dao.read(created_id)

        assert result is not None
        assert result.id_jury == created_id
        assert result.nb_entity == 2
        assert result.nb_entity_mode == "EXACT"

    finally:
        assert dao.delete(created_id) is True


def test_read_jury_inexistant():
    """Un identifiant inexistant doit retourner None."""
    dao = JuryDao()

    jury = dao.read(-999999)

    assert jury is None


def test_read_all_juries():
    """read_all doit retourner une liste contenant le jury créé."""
    dao = JuryDao()

    jury = Jury(
        date_begin=date(2026, 1, 1),
        date_end=date(2026, 12, 31),
        fk_id_identity_president=None,
        nb_entity=2,
        nb_entity_mode="EXACT",
        fk_id_jury_mother=None
    )

    created_id = dao.create(jury)

    assert created_id > 0

    try:
        juries = dao.read_all()

        assert isinstance(juries, list)
        assert any(
            item.id_jury == created_id
            for item in juries
        )

    finally:
        assert dao.delete(created_id) is True


def test_count_members_jury():
    """Le comptage des membres retourne le nombre de membres du jury."""
    dao = JuryDao()

    jury = Jury(
        date_begin=date(2026, 1, 1),
        date_end=date(2026, 12, 31),
        fk_id_identity_president=None,
        nb_entity=2,
        nb_entity_mode="EXACT",
        fk_id_jury_mother=None
    )

    created_id = dao.create(jury)

    assert created_id > 0

    try:
        result = dao.count_members(created_id)

        assert result == 0

    finally:
        assert dao.delete(created_id) is True


def test_count_members_jury_inexistant():
    """Un jury inexistant doit avoir zéro membre."""
    dao = JuryDao()

    result = dao.count_members(-999999)

    assert result == 0


def test_find_by_president_name_inexistant():
    """Un président inexistant doit retourner une liste vide."""
    dao = JuryDao()

    juries = dao.find_by_president_name(
        "__PRESIDENT_INEXISTANT_TEST__"
    )

    assert juries == []


def test_count_elections_jury():
    """Le comptage des élections doit retourner un entier."""
    dao = JuryDao()

    jury = Jury(
        date_begin=date(2026, 1, 1),
        date_end=date(2026, 12, 31),
        fk_id_identity_president=None,
        nb_entity=2,
        nb_entity_mode="EXACT",
        fk_id_jury_mother=None
    )

    created_id = dao.create(jury)

    assert created_id > 0

    try:
        result = dao.count_elections(created_id)

        assert isinstance(result, int)
        assert result >= 0

    finally:
        assert dao.delete(created_id) is True


def test_count_elections_jury_inexistant():
    """Un jury inexistant doit avoir zéro élection."""
    dao = JuryDao()

    result = dao.count_elections(-999999)

    assert result == 0


def test_create_update_delete_jury():
    """
    Teste le cycle complet create -> read -> update -> delete.

    Le jury de test n'est lié à aucune identité.
    """
    dao = JuryDao()

    jury = Jury(
        date_begin=date(2026, 1, 1),
        date_end=date(2026, 12, 31),
        fk_id_identity_president=None,
        nb_entity=1,
        nb_entity_mode="EXACT",
        fk_id_jury_mother=None
    )

    created_id = dao.create(jury)

    assert created_id > 0
    assert jury.id_jury == created_id

    try:
        created = dao.read(created_id)

        assert created is not None
        assert created.id_jury == created_id
        assert created.nb_entity == 1
        assert created.nb_entity_mode == "EXACT"

        jury.nb_entity = 2
        jury.nb_entity_mode = "MIN"

        updated = dao.update(jury)

        assert updated is True

        modified = dao.read(created_id)

        assert modified is not None
        assert modified.nb_entity == 2
        assert modified.nb_entity_mode == "MIN"

    finally:
        deleted = dao.delete(created_id)

        assert deleted is True

    assert dao.read(created_id) is None


def test_delete_jury_inexistant():
    """Supprimer un jury inexistant doit retourner False."""
    dao = JuryDao()

    result = dao.delete(-999999)

    assert result is False