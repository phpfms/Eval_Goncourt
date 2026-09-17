class Menu:
    """Gère l'affichage du menu principal et des sous-menus."""

    def display_main_menu(self):
        """Affiche le menu principal."""
        print("\n===== MENU PRINCIPAL =====")
        print("1. Jury")
        print("2. Vote")
        print("3. Election")
        print("4. Livre")
        print("5. Personne")
        print("6. Rôle")
        print("0. Quitter")

        return input("Votre choix : ")

    def display_jury_menu(self):
        """Affiche le sous-menu des jurys."""
        print("\n===== JURY =====")
        print("1. Afficher l'historique des jurys")
        print("2. Afficher la composition d'un jury")
        print("3. Trouver un jury par id")
        print("4. Trouver un jury par nom de son president")
        print("5. Afficher les détails d'un membre du jury")
        print("6. Créer un jury")
        print("7. Modifier un jury")
        print("8. Supprimer un jury")
        print("0. Retour")

        return input("Votre choix : ")

    def display_vote_menu(self):
        """Affiche le sous-menu des votes."""
        print("\n===== VOTE =====")
        print("1. Afficher l'historique des votes")
        print("2. Afficher les détails d'un vote")
        print("3. Trouver un vote par id")
        print("4. Trouver un vote par nom")
        print("5. Voter")
        print("6. Modifier un vote")
        print("7. Supprimer un vote")
        print("8. Indiquer le résultat d'un vote en nombre de voix par livre")
        print("9. Indiquer le résultat d'un vote en auteur par livre")
        print("10. Annoncer le résultat du vote")
        print("0. Retour")

        return input("Votre choix : ")

    def display_election_menu(self):
        """Affiche le sous-menu des élections."""
        print("\n===== ELECTION =====")
        print("1. Afficher l'historique des élections")
        print("2. Afficher les détails d'une élection")
        print("3. Trouver une élection par id")
        print("4. Trouver une élection par nom")
        print("5. Générer la composition des candidats du tour suivant")
        print("6. Annoncer le nouveau panel de candidats")
        print("7. Créer une élection")
        print("8. Modifier une élection")
        print("9. Supprimer une élection")
        print("0. Retour")

        return input("Votre choix : ")

    def display_book_menu(self):
        """Affiche le sous-menu des livres."""
        print("\n===== LIVRE =====")
        print("1. Afficher la liste des livres")
        print("2. Afficher les détails d'un livre")
        print("3. Trouver un livre par id")
        print("4. Trouver un livre par nom")
        print("5. Créer un livre")
        print("6. Modifier un livre")
        print("7. Supprimer un livre")
        print("8 - Ajouter un intervenant à un livre")
        print("0. Retour")

        return input("Votre choix : ")

    def display_person_menu(self):
        """Affiche le sous-menu des personnes."""
        print("\n===== PERSONNE =====")
        print("1. Afficher la liste des personnes")
        print("2. Afficher tous les détails d'une personne")
        print("3. Trouver une personne par id")
        print("4. Trouver une personne par nom")
        print("5. Créer une personne")
        print("6. Modifier une personne")
        print("7. Supprimer une personne")
        print("0. Retour")

        return input("Votre choix : ")

    def display_role_menu(self):
        """Affiche le sous-menu des rôles."""
        print("\n===== RÔLE =====")
        print("1. Afficher les différents rôles en base")
        print("2. Afficher tous les éléments appartenant à un rôle")
        print("3. Créer un rôle")
        print("4. Modifier un rôle")
        print("5. Supprimer un rôle")
        print("0. Retour")

        return input("Votre choix : ")