# fichier qui permet à l'utilisateur de faire des choix numériques,
# il joue un rôle de contrôleur, d'interaction avec l'utilisateur

from business.data_loader import DataLoader


class Application:

    def __init__(self):
        """Initialise l'application."""
        pass

    def run(self):
        """Lance l'application et charge les données dans la BDD."""
        DataLoader().load()


if __name__ == "__main__":
    app = Application()
    app.run()

