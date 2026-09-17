# -*- coding: utf-8 -*-
from datetime import datetime
from models.jury import Jury


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

    def display_composition_input(self, jury_business):
        """Demande un jury et affiche sa composition."""
        try:
            id_jury = int(input("Identifiant du jury : "))
        except ValueError:
            print("L'identifiant doit être un nombre.")
            return

        jury, members = jury_business.get_composition(id_jury)

        if jury is None:
            print("Erreur : ce jury n'existe pas.")
            return

        self.display_composition(jury, members)

    def input_id_jury(self) -> int:
        """Demande l'identifiant d'un jury."""
        try:
            return int(input("Identifiant du jury : "))
        except ValueError:
            print("L'identifiant doit être un nombre.")
            return 0

    def input_president_name(self) -> str:
        """Demande le nom du président."""
        return input("Nom du président : ").strip()

    def input_create(self):
        """Saisit les informations nécessaires à la création d'un jury."""
        try:
            date_begin = datetime.strptime(
                input("Date de début (AAAA-MM-JJ) : "),
                "%Y-%m-%d"
            ).date()
            date_end = datetime.strptime(
                input("Date de fin (AAAA-MM-JJ) : "),
                "%Y-%m-%d"
            ).date()
            president = input(
                "Identifiant du président (vide si aucun) : "
            ).strip()
            nb_entity = int(input("Nombre de membres : "))
            nb_entity_mode = input(
                "Mode (MIN, MAX ou EXACT) : "
            ).strip().upper()

            id_members = []

            for index in range(nb_entity):
                id_identity = int(
                    input(f"Identifiant du membre {index + 1} : ")
                )
                id_members.append(id_identity)

            jury = Jury(
                date_begin=date_begin,
                date_end=date_end,
                fk_id_identity_president=int(president) if president else None,
                nb_entity=nb_entity,
                nb_entity_mode=nb_entity_mode,
                fk_id_jury_mother=None
            )

            return jury, id_members

        except ValueError:
            print("Erreur : les données saisies sont invalides.")
            return None, []

    def input_delete(self) -> int:
        """Demande l'identifiant du jury à supprimer."""
        try:
            return int(input("Identifiant du jury à supprimer : "))
        except ValueError:
            print("L'identifiant doit être un nombre.")
            return 0