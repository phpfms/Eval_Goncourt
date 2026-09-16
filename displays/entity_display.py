# -*- coding: utf-8 -*-

"""
Affichage des entités
"""


class DisplayEntity:

    def display_entity(self, entity) -> None:
        """Affiche les détails d'une entité."""

        print("\n===== DÉTAILS DE L'ENTITÉ =====")

        print(f"ID : {entity.id_entity}")
        print(f"ISBN : {entity.ISBN}")
        print(f"Prix : {entity.price}")
        print(f"Nom : {entity.name}")
        print(f"Prénom : {entity.first_name}")
        print(f"Type : {entity.type}")
        print(f"Résumé : {entity.resume}")
        print(f"Date de création : {entity.creation_date}")
        print(f"Quantité : {entity.nb} {entity.unit_nb}")
        print(f"Entité mère : {entity.fk_id_entity_mother}")

        print()

    def display_entities(self, entities) -> None:
        """Affiche la liste des entités."""

        print("\n===== LISTE DES ENTITÉS =====")

        for entity in entities:
            print(f"ID : {entity.id_entity} | {entity}")

        print()