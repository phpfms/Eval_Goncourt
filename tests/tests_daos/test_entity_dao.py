# -*- coding: utf-8 -*-

"""
Tests du DAO EntityDao.

Ces tests utilisent les données présentes dans
la dernière version de la base eval1_goncourt.
"""

from daos.entity_dao import EntityDao


def test_read_entity_existante():
    """L'entité 1 correspond au livre Minotaure."""
    dao = EntityDao()
    entity = dao.read(1)
    assert entity is not None
    assert entity.id_entity == 1
    assert entity.name == "Minotaure"
    assert entity.type == "livre"


def test_read_entity_inexistante():
    """Un identifiant qui n'existe pas doit retourner None."""
    dao = EntityDao()
    entity = dao.read(-999999)
    assert entity is None


def test_read_all_entities():
    """La dernière base contient actuellement 52 entités."""
    dao = EntityDao()
    entities = dao.read_all()
    assert isinstance(entities, list)
    assert len(entities) == 52


def test_find_entity_par_nom():
    """La recherche doit trouver l'entité Minotaure."""
    dao = EntityDao()
    entities = dao.find_by_name("Minotaure")
    assert isinstance(entities, list)
    assert len(entities) >= 1
    assert any(entity.id_entity == 1 for entity in entities)


def test_find_entity_inexistante():
    """Une recherche avec un nom inexistant doit retourner une liste vide."""
    dao = EntityDao()
    entities = dao.find_by_name("__ENTITE_INEXISTANTE_TEST__")
    assert entities == []


def test_count_usages_entity():
    """Le comptage des utilisations d'une entité doit retourner un entier."""
    dao = EntityDao()
    result = dao.count_usages_entity(1)
    assert isinstance(result, int)
    assert result >= 0