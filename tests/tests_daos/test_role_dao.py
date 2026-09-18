# -*- coding: utf-8 -*-

"""
Tests du DAO RoleDao.
"""

from daos.role_dao import RoleDao
from models.role import Role


def test_read_role_existant():
    """Le rôle 9 correspond à membre du jury."""
    dao = RoleDao()

    role = dao.read(9)

    assert role is not None
    assert role.id_role == 9
    assert role.name_role == "membre du jury"


def test_read_role_inexistant():
    """Un identifiant inexistant doit retourner None."""
    dao = RoleDao()

    role = dao.read(-999999)

    assert role is None


def test_read_all_roles():
    """read_all doit retourner une liste de rôles."""
    dao = RoleDao()

    roles = dao.read_all()

    assert isinstance(roles, list)
    assert len(roles) > 0
    assert all(
        role.id_role is not None
        for role in roles
    )


def test_find_role_existant():
    """Le rôle membre du jury doit être trouvé."""
    dao = RoleDao()

    role = dao.find_by_name("membre du jury")

    assert role is not None
    assert role.id_role == 9
    assert role.name_role == "membre du jury"


def test_find_role_inexistant():
    """Un rôle inexistant doit retourner None."""
    dao = RoleDao()

    role = dao.find_by_name(
        "__ROLE_INEXISTANT_TEST__"
    )

    assert role is None


def test_find_role_none():
    """Une recherche avec None doit retourner None."""
    dao = RoleDao()

    assert dao.find_by_name(None) is None


def test_find_role_vide():
    """Une recherche vide doit retourner None."""
    dao = RoleDao()

    assert dao.find_by_name("") is None


def test_find_role_espaces():
    """Les espaces autour du nom doivent être ignorés."""
    dao = RoleDao()

    role = dao.find_by_name("  membre du jury  ")

    assert role is not None
    assert role.id_role == 9


def test_create_update_delete_role():
    """
    Teste le cycle complet create -> read -> update -> delete.
    """
    dao = RoleDao()

    role = Role("__TEST_ROLE_DAO__")

    created_id = dao.create(role)

    assert created_id > 0
    assert role.id_role == created_id

    try:
        created = dao.read(created_id)

        assert created is not None
        assert created.id_role == created_id
        assert created.name_role == "__TEST_ROLE_DAO__"

        role.name_role = "__TEST_ROLE_DAO_UPDATED__"

        updated = dao.update(role)

        assert updated is True

        modified = dao.read(created_id)

        assert modified is not None
        assert modified.name_role == "__TEST_ROLE_DAO_UPDATED__"

    finally:
        deleted = dao.delete(role)

        assert deleted is True

    assert dao.read(created_id) is None