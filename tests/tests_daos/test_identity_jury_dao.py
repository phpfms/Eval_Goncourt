# -*- coding: utf-8 -*-

"""
Tests du DAO IdentityJuryDao.

Ces tests utilisent les données présentes dans
la dernière version de la base eval1_goncourt.
"""

from daos.identity_jury_dao import IdentityJuryDao


def test_read_membre_jury_existant():
    """L'identité 9 est membre du jury 1."""
    dao = IdentityJuryDao()
    result = dao.read(1, 9)
    assert result is True


def test_read_membre_jury_inexistant():
    """Une relation inexistante doit retourner False."""
    dao = IdentityJuryDao()
    result = dao.read(999999, 999999)
    assert result is False


def test_count_membres_jury_1():
    """Le jury 1 possède actuellement 2 membres."""
    dao = IdentityJuryDao()
    result = dao.count_by_jury(1)
    assert result == 2


def test_count_membres_jury_3():
    """Le jury 3 possède actuellement 3 membres."""
    dao = IdentityJuryDao()
    result = dao.count_by_jury(3)
    assert result == 3


def test_find_identities_by_jury():
    """Le jury 3 possède les identités 9, 10 et 11."""
    dao = IdentityJuryDao()
    identities = dao.find_identities_by_jury(3)
    assert identities == [9, 10, 11]


def test_find_juries_by_identity():
    """L'identité 9 appartient actuellement aux jurys 1 et 3."""
    dao = IdentityJuryDao()
    juries = dao.find_juries_by_identity(9)
    assert juries == [1, 3]


def test_find_members_details():
    """Les détails des membres du jury 3 doivent contenir 3 personnes."""
    dao = IdentityJuryDao()
    members = dao.find_members_details(3)
    assert isinstance(members, list)
    assert len(members) == 3
    assert [member["id_identity"] for member in members] == [9, 10, 11]