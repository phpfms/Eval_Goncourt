# -*- coding: utf-8 -*-

"""
Tests du DAO IdentityDao.

Ces tests utilisent les données présentes dans
la dernière version de la base eval1_goncourt.
"""

from daos.identity_dao import IdentityDao


def test_read_identity_existante():
    """L'identité 3 correspond à Didier Decoin."""
    dao = IdentityDao()
    identity = dao.read(3)
    assert identity is not None
    assert identity.id_identity == 3
    assert identity.appelation == "Decoin"
    assert identity.under_appelation == "Didier"


def test_read_identity_inexistante():
    """Un identifiant qui n'existe pas doit retourner None."""
    dao = IdentityDao()
    identity = dao.read(-999999)
    assert identity is None


def test_read_all_identities():
    """La dernière base contient actuellement 52 identités."""
    dao = IdentityDao()
    identities = dao.read_all()
    assert isinstance(identities, list)
    assert len(identities) == 52


def test_find_identity_par_nom():
    """La recherche doit trouver Decoin à partir de son appellation."""
    dao = IdentityDao()
    identities = dao.find_by_name("Decoin")
    assert isinstance(identities, list)
    assert len(identities) >= 1
    assert any(identity.id_identity == 3 for identity in identities)


def test_find_identity_inexistante():
    """Une recherche avec un nom inexistant doit retourner une liste vide."""
    dao = IdentityDao()
    identities = dao.find_by_name("__IDENTITE_INEXISTANTE_TEST__")
    assert identities == []