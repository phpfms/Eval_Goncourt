# -*- coding: utf-8 -*-

"""
Tests du DAO RoleDao.

Ces tests utilisent les données présentes dans la dernière version
de la base eval1_goncourt.
"""

from daos.role_dao import RoleDao


def test_read_role_existant():
    """Le rôle 9 existe dans la base et correspond à membre du jury."""
    dao = RoleDao()
    role = dao.read(9)
    assert role is not None
    assert role.id_role == 9
    assert role.name_role == "membre du jury"


def test_read_role_inexistant():
    """Un identifiant négatif ne correspond à aucun rôle."""
    dao = RoleDao()
    role = dao.read(-999999)
    assert role is None


def test_read_all_roles():
    """La base contient actuellement 23 rôles."""
    dao = RoleDao()
    roles = dao.read_all()
    assert isinstance(roles, list)
    assert len(roles) == 23


def test_find_role_existant():
    """Le rôle membre du jury doit être trouvé par son nom."""
    dao = RoleDao()
    role = dao.find_by_name("membre du jury")
    assert role is not None
    assert role.id_role == 9
    assert role.name_role == "membre du jury"


def test_find_role_inexistant():
    """Un nom qui n'existe pas doit retourner None."""
    dao = RoleDao()
    role = dao.find_by_name("__ROLE_INEXISTANT_TEST__")
    assert role is None