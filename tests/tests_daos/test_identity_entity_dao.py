# -*- coding: utf-8 -*-

"""
Tests du DAO IdentityEntityDao.
"""

from daos.identity_entity_dao import IdentityEntityDao
from models.identity_entity import IdentityEntity


def test_read_relation_existante():
    """Une relation Identity / Entity / Role existante doit être lue."""
    dao = IdentityEntityDao()

    result = dao.read(5, 22, 2)

    assert result is not None
    assert result.fk_id_entity == 5
    assert result.fk_id_identity == 22
    assert result.fk_id_role == 2


def test_read_relation_inexistante():
    """Une relation inexistante doit retourner None."""
    dao = IdentityEntityDao()

    result = dao.read(
        999999,
        999999,
        999999
    )

    assert result is None


def test_create_relation_invalide():
    """
    Une relation dont l'entité et l'identité sont toutes les deux
    NULL doit être refusée.
    """
    dao = IdentityEntityDao()

    relation = IdentityEntity(
        fk_id_entity=None,
        fk_id_identity=None,
        fk_id_role=9
    )

    result = dao.create(relation)

    assert result is False


def test_create_update_delete_relation():
    """
    Teste le cycle complet create -> read -> update -> delete.
    """
    dao = IdentityEntityDao()

    # Relation temporaire :
    # entité 1 + identité 3 + rôle 9.
    relation = IdentityEntity(
        fk_id_entity=1,
        fk_id_identity=3,
        fk_id_role=9
    )

    # On s'assure de ne pas avoir déjà cette relation.
    existing = dao.read(1, 3, 9)

    if existing is not None:
        dao.delete(relation)

    created = dao.create(relation)

    assert created is True

    try:
        result = dao.read(1, 3, 9)

        assert result is not None
        assert result.fk_id_entity == 1
        assert result.fk_id_identity == 3
        assert result.fk_id_role == 9

        # On modifie le rôle.
        relation.fk_id_role = 10

        updated = dao.update(relation)

        assert updated is True

        modified = dao.read(1, 3, 10)

        assert modified is not None
        assert modified.fk_id_role == 10

    finally:
        # Après l'update, le rôle est 10.
        relation.fk_id_role = 10

        deleted = dao.delete(relation)

        assert deleted is True

    assert dao.read(1, 3, 10) is None


def test_delete_relation_inexistante():
    """Une relation inexistante doit retourner False."""
    dao = IdentityEntityDao()

    relation = IdentityEntity(
        fk_id_entity=999999,
        fk_id_identity=999999,
        fk_id_role=999999
    )

    result = dao.delete(relation)

    assert result is False