class DisplayEntity:
    def display_entity(self, entity, identities=None) -> None:
        # Règle métier : le détail d'un livre présente ses informations
        # ainsi que les personnes associées et le rôle qu'elles occupent.
        print("\n===== DÉTAILS DU LIVRE =====")
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
        print("===== PERSONNES CONCERNÉES =====")
        if identities:
            for identity, role in identities:
                print(f"ID : {identity.id_identity} | Nom : {identity.appelation} | Rôle : {role.name_role}")
        else:
            print("Aucune personne associée à ce livre.")
        print()

    def display_entities(self, entities) -> None:
        # Le choix 1 affiche la liste des livres sans charger leurs relations.
        # Les personnes sont chargées uniquement lors de l'affichage du détail.
        print("\n===== LISTE DES LIVRES =====")
        for entity in entities:
            print(f"ID : {entity.id_entity} | {entity}")
        print()