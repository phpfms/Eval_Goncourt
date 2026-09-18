# -*- coding: utf-8 -*-

"""
Tests du DAO IdentityDao.
"""

from daos.identity_dao import IdentityDao
from models.identity import Identity


def test_read_identity_existante():
    """L'identité 3 correspond à Didier Decoin."""
    dao = IdentityDao()

    identity = dao.read(3)

    assert identity is not None
    assert identity.id_identity == 3
    assert identity.appelation == "Decoin"
    assert identity.under_appelation == "Didier"


def test_read_identity_inexistante():
    """Un identifiant inexistant doit retourner None."""
    dao = IdentityDao()

    identity = dao.read(-999999)

    assert identity is None


def test_read_all_identities():
    """read_all doit retourner une liste d'identités."""
    dao = IdentityDao()

    identities = dao.read_all()

    assert isinstance(identities, list)
    assert len(identities) > 0
    assert all(
        identity.id_identity is not None
        for identity in identities
    )


def test_find_identity_par_nom():
    """La recherche doit trouver Decoin."""
    dao = IdentityDao()

    identities = dao.find_by_name("Decoin")

    assert isinstance(identities, list)
    assert len(identities) >= 1
    assert any(
        identity.id_identity == 3
        for identity in identities
    )


def test_find_identity_inexistante():
    """Une recherche inexistante doit retourner une liste vide."""
    dao = IdentityDao()

    identities = dao.find_by_name(
        "__IDENTITE_INEXISTANTE_TEST__"
    )

    assert identities == []


def test_create_update_delete_identity():
    """
    Teste le cycle complet create -> read -> update -> delete.
    """
    dao = IdentityDao()

    identity = Identity(
        appelation="__TEST_IDENTITY_DAO__",
        under_appelation="Test",
        description="Identité créée uniquement pour les tests.",
        address="Adresse de test",
        fk_id_identity_mother=None
    )

    created_id = dao.create(identity)

    assert created_id > 0
    assert identity.id_identity == created_id

    try:
        created = dao.read(created_id)

        assert created is not None
        assert created.id_identity == created_id
        assert created.appelation == "__TEST_IDENTITY_DAO__"
        assert created.under_appelation == "Test"

        identity.appelation = "__TEST_IDENTITY_DAO_UPDATED__"
        identity.address = "Nouvelle adresse"

        updated = dao.update(identity)

        assert updated is True

        modified = dao.read(created_id)

        assert modified is not None
        assert modified.appelation == "__TEST_IDENTITY_DAO_UPDATED__"
        assert modified.address == "Nouvelle adresse"

    finally:
        deleted = dao.delete(created_id)

        assert deleted is True

    assert dao.read(created_id) is None


def test_delete_identity_inexistante():
    """Supprimer une identité inexistante doit échouer."""
    dao = IdentityDao()

    result = dao.delete(-999999)

    assert result is False