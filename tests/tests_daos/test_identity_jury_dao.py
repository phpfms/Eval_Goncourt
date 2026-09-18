# -*- coding: utf-8 -*-

"""
Tests du DAO IdentityJuryDao.
"""

from datetime import date

from daos.identity_jury_dao import IdentityJuryDao
from daos.jury_dao import JuryDao
from models.jury import Jury


def create_test_jury():
    """
    Crée un jury temporaire pour les tests.

    Cette fonction évite de dépendre des identifiants de jurys
    présents au départ dans la base de données.
    """
    dao = JuryDao()

    jury = Jury(
        date_begin=date(2026, 1, 1),
        date_end=date(2026, 12, 31),
        fk_id_identity_president=None,
        nb_entity=3,
        nb_entity_mode="MIN",
        fk_id_jury_mother=None
    )

    id_jury = dao.create(jury)

    assert id_jury > 0

    return id_jury


def delete_test_jury(id_jury):
    """Supprime le jury temporaire utilisé par un test."""
    dao = JuryDao()

    assert dao.delete(id_jury) is True


def test_read_membre_jury_existant():
    """
    Vérifie qu'une relation existante est correctement trouvée.

    Le jury et la relation sont créés pour le test afin de ne pas
    dépendre des données déjà présentes dans la base.
    """
    jury_dao = JuryDao()
    dao = IdentityJuryDao()

    id_jury = create_test_jury()

    try:
        assert dao.create(id_jury, 9) is True

        result = dao.read(id_jury, 9)

        assert result is True

    finally:
        assert dao.delete(id_jury, 9) is True
        assert jury_dao.delete(id_jury) is True


def test_read_membre_jury_inexistant():
    """Une relation inexistante doit retourner False."""
    dao = IdentityJuryDao()

    result = dao.read(999999, 999999)

    assert result is False


def test_count_membres_jury_1():
    """
    Vérifie qu'un jury possédant deux membres retourne bien 2.

    Le jury est créé pour le test et deux relations sont ajoutées.
    """
    jury_dao = JuryDao()
    dao = IdentityJuryDao()

    id_jury = create_test_jury()

    try:
        assert dao.create(id_jury, 9) is True
        assert dao.create(id_jury, 10) is True

        result = dao.count_by_jury(id_jury)

        assert result == 2

    finally:
        assert dao.delete(id_jury, 9) is True
        assert dao.delete(id_jury, 10) is True
        assert jury_dao.delete(id_jury) is True


def test_count_membres_jury_3():
    """
    Vérifie qu'un jury possédant trois membres retourne bien 3.

    Le jury est créé pour le test et trois relations sont ajoutées.
    """
    jury_dao = JuryDao()
    dao = IdentityJuryDao()

    id_jury = create_test_jury()

    try:
        assert dao.create(id_jury, 9) is True
        assert dao.create(id_jury, 10) is True
        assert dao.create(id_jury, 11) is True

        result = dao.count_by_jury(id_jury)

        assert result == 3

    finally:
        assert dao.delete(id_jury, 9) is True
        assert dao.delete(id_jury, 10) is True
        assert dao.delete(id_jury, 11) is True
        assert jury_dao.delete(id_jury) is True


def test_count_membres_jury_inexistant():
    """Un jury inexistant doit avoir zéro membre."""
    dao = IdentityJuryDao()

    result = dao.count_by_jury(-999999)

    assert result == 0


def test_find_identities_by_jury():
    """
    Vérifie que les identités associées à un jury sont correctement
    retournées.
    """
    jury_dao = JuryDao()
    dao = IdentityJuryDao()

    id_jury = create_test_jury()

    try:
        assert dao.create(id_jury, 9) is True
        assert dao.create(id_jury, 10) is True
        assert dao.create(id_jury, 11) is True

        identities = dao.find_identities_by_jury(id_jury)

        assert isinstance(identities, list)
        assert identities == [9, 10, 11]

    finally:
        assert dao.delete(id_jury, 9) is True
        assert dao.delete(id_jury, 10) is True
        assert dao.delete(id_jury, 11) is True
        assert jury_dao.delete(id_jury) is True


def test_find_identities_by_jury_inexistant():
    """Un jury inexistant doit retourner une liste vide."""
    dao = IdentityJuryDao()

    identities = dao.find_identities_by_jury(-999999)

    assert identities == []


def test_find_juries_by_identity():
    """
    Vérifie qu'une identité peut être retrouvée dans les jurys
    auxquels elle est associée.

    La relation est créée temporairement afin de ne pas dépendre
    des données existantes en base.
    """
    jury_dao = JuryDao()
    dao = IdentityJuryDao()

    id_jury = create_test_jury()

    try:
        assert dao.create(id_jury, 9) is True

        juries = dao.find_juries_by_identity(9)

        assert isinstance(juries, list)
        assert id_jury in juries

    finally:
        assert dao.delete(id_jury, 9) is True
        assert jury_dao.delete(id_jury) is True


def test_find_juries_by_identity_inexistante():
    """Une identité inexistante doit retourner une liste vide."""
    dao = IdentityJuryDao()

    juries = dao.find_juries_by_identity(-999999)

    assert juries == []


def test_find_members_details():
    """
    Vérifie que les détails des membres du jury contiennent
    les trois identités ajoutées pour le test.
    """
    jury_dao = JuryDao()
    dao = IdentityJuryDao()

    id_jury = create_test_jury()

    try:
        assert dao.create(id_jury, 9) is True
        assert dao.create(id_jury, 10) is True
        assert dao.create(id_jury, 11) is True

        members = dao.find_members_details(id_jury)

        assert isinstance(members, list)
        assert len(members) == 3
        assert [member["id_identity"] for member in members] == [
            9, 10, 11
        ]

    finally:
        assert dao.delete(id_jury, 9) is True
        assert dao.delete(id_jury, 10) is True
        assert dao.delete(id_jury, 11) is True
        assert jury_dao.delete(id_jury) is True


def test_find_members_details_jury_inexistant():
    """Un jury inexistant doit retourner une liste vide."""
    dao = IdentityJuryDao()

    members = dao.find_members_details(-999999)

    assert members == []


def test_create_delete_relation():
    """
    Teste create -> read -> delete sur une relation temporaire.

    Le jury est créé spécialement pour le test.
    """
    jury_dao = JuryDao()
    dao = IdentityJuryDao()

    id_jury = create_test_jury()

    try:
        assert dao.read(id_jury, 3) is False

        created = dao.create(id_jury, 3)

        assert created is True
        assert dao.read(id_jury, 3) is True

        juries = dao.find_juries_by_identity(3)

        assert id_jury in juries

        identities = dao.find_identities_by_jury(id_jury)

        assert 3 in identities

    finally:
        assert dao.delete(id_jury, 3) is True
        assert jury_dao.delete(id_jury) is True

    assert dao.read(id_jury, 3) is False


def test_delete_relation_inexistante():
    """
    Supprimer une relation inexistante ne doit pas provoquer
    d'exception.
    """
    dao = IdentityJuryDao()

    result = dao.delete(
        999999,
        999999
    )

    assert result is True


def test_delete_by_jury():
    """
    Vérifie delete_by_jury sur plusieurs relations temporaires.

    Un jury temporaire est créé, trois membres lui sont associés,
    puis toutes les relations sont supprimées avec delete_by_jury.
    """
    jury_dao = JuryDao()
    dao = IdentityJuryDao()

    id_jury = create_test_jury()

    try:
        assert dao.create(id_jury, 9) is True
        assert dao.create(id_jury, 10) is True
        assert dao.create(id_jury, 11) is True

        assert dao.read(id_jury, 9) is True
        assert dao.read(id_jury, 10) is True
        assert dao.read(id_jury, 11) is True

        result = dao.delete_by_jury(id_jury)

        assert result is True

        assert dao.read(id_jury, 9) is False
        assert dao.read(id_jury, 10) is False
        assert dao.read(id_jury, 11) is False

    finally:
        assert jury_dao.delete(id_jury) is True