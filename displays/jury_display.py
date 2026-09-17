# -*- coding: utf-8 -*-

class DisplayJury:

    @staticmethod
    def display(jury, members=None):
        """Affiche un jury."""
        print("\n===== JURY =====")
        print(f"ID : {jury.id_jury}")
        print(f"Début : {jury.date_begin}")
        print(f"Fin : {jury.date_end}")
        print(f"Président : {jury.fk_id_identity_president}")
        print(f"Nombre : {jury.nb_entity}")
        print(f"Mode : {jury.nb_entity_mode}")
        print(f"Jury parent : {jury.fk_id_jury_mother}")

        if members is not None:
            print("Membres :")
            for member in members:
                print(
                    f"- {member['id_identity']} : "
                    f"{member['appelation']} "
                    f"{member['under_appelation'] or ''}"
                )

    @staticmethod
    def display_history(juries):
        """Affiche l'historique des jurys."""
        if not juries:
            print("Aucun jury trouvé.")
            return

        print("\n===== HISTORIQUE DES JURYS =====")

        for jury in juries:
            print(
                f"Jury {jury.id_jury} | "
                f"{jury.date_begin} -> {jury.date_end} | "
                f"Président : {jury.fk_id_identity_president} | "
                f"Membres : {jury.nb_entity} | "
                f"Mode : {jury.nb_entity_mode}"
            )

    @staticmethod
    def display_composition(jury, members):
        """Affiche la composition d'un jury."""
        print(f"\n===== COMPOSITION DU JURY {jury.id_jury} =====")
        print(f"Président : {jury.fk_id_identity_president}")

        if not members:
            print("Aucun membre.")
            return

        for member in members:
            print(
                f"- {member['id_identity']} : "
                f"{member['appelation']} "
                f"{member['under_appelation'] or ''}"
            )