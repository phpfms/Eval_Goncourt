# -*- coding: utf-8 -*-

"""
Affichage des identités
"""


class DisplayIdentity:

    def display_identity(self, identity) -> None:
        """Affiche les détails d'une identité."""

        print("\n===== DÉTAILS DE L'IDENTITÉ =====")

        print(f"ID : {identity.id_identity}")
        print(f"Nom : {identity.appelation}")
        print(f"Sous-nom : {identity.under_appelation}")
        print(f"Description : {identity.description}")
        print(f"Adresse : {identity.address}")
        print(
            f"Identité mère : "
            f"{identity.fk_id_identity_mother}"
        )

        print()

    def display_identities(self, identities) -> None:
        """Affiche la liste des identités."""

        print("\n===== LISTE DES IDENTITÉS =====")

        for identity in identities:
            print(
                f"ID : {identity.id_identity} | "
                f"{identity}"
            )

        print()