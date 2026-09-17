# -*- coding: utf-8 -*-

"""
Tests du DAO JuryDao.

Ces tests utilisent les données présentes dans
la dernière version de la base eval1_goncourt.
"""

from daos.jury_dao import JuryDao


def test_read_jury_existant():
    """Le jury 1 existe dans la base."""
    dao = JuryDao()
    jury = dao.read(1)
    assert jury is not None
    assert jury.id_jury == 1
    assert jury.nb_entity == 2
    assert jury.nb_entity_mode == "EXACT"


def test_read_jury_inexistant():
    """Un identifiant qui n'existe pas doit retourner None."""
    dao = JuryDao()
    jury = dao.read(-999999)
    assert jury is None


def test_read_all_juries():
    """La dernière base contient actuellement 2 jurys."""
    dao = JuryDao()
    juries = dao.read_all()
    assert isinstance(juries, list)
    assert len(juries) == 2
    assert [jury.id_jury for jury in juries] == [1, 3]


def test_count_members_jury_1():
    """Le jury 1 possède actuellement 2 membres."""
    dao = JuryDao()
    result = dao.count_members(1)
    assert result == 2


def test_count_members_jury_3():
    """Le jury 3 possède actuellement 3 membres."""
    dao = JuryDao()
    result = dao.count_members(3)
    assert result == 3


def test_find_by_president_name():
    """Le jury 3 possède Bruckner comme président."""
    dao = JuryDao()
    juries = dao.find_by_president_name("Bruckner")
    assert isinstance(juries, list)
    assert len(juries) >= 1
    assert any(jury.id_jury == 3 for jury in juries)


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
    result = dao.count_elections(1)
    assert isinstance(result, int)
    assert result >= 0