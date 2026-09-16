from datetime import date

from models.identity import Identity
from models.entity import Entity
from models.identity_entity import IdentityEntity
from models.role import Role


from daos.role_dao import RoleDao
from daos.identity_dao import IdentityDao
from daos.entity_dao import EntityDao
from daos.identity_entity_dao import IdentityEntityDao



class DataLoader:
    """
    créer toutes les Identity
    chaque Identity récupère son id_identity
    créer toutes les Entity
    chaque Entity récupère son id_entity
    parcourir identity_entities
    retrouver l'objet Identity correspondant
    retrouver l'objet Entity correspondant
    construire IdentityEntity(id_entity, id_identity, role)
    insérer dans identity_entity
    """

    def __init__(self):
        """
        Initialise les DAO nécessaires au chargement des données.
        """
        self.identity_dao = IdentityDao()
        self.entity_dao = EntityDao()
        self.identity_entity_dao = IdentityEntityDao()
        self.role_dao = RoleDao()

    def load(self):
        """
        Charge les données initiales dans la BDD.
        """

        # ==========================================================
        # 0. RÔLES
        # ==========================================================

        roles = [
            Role(name_role="ancien membre du conseil d'etat"),
            Role(name_role="auteur"),
            Role(name_role="dramaturge"),
            Role(name_role="éditeur"),
            Role(name_role="essayiste"),
            Role(name_role="écrivain"),
            Role(name_role="journaliste"),
            Role(name_role="livre"),
            Role(name_role="membre du jury"),
            Role(name_role="peintre"),
            Role(name_role="personnage_principal"),
            Role(name_role="philosophe"),
            Role(name_role="poète"),
            Role(name_role="président"),
            Role(name_role="président du jury"),
            Role(name_role="réalisateur"),
            Role(name_role="relieur"),
            Role(name_role="romancier"),
            Role(name_role="scénariste"),
            Role(name_role="secrétaire général"),
            Role(name_role="traducteur"),
            Role(name_role="trésorier"),
            Role(name_role="vice-président du jury")
        ]

        # Création des rôles en BDD
        for role in roles:
            self.role_dao.create(role)

        # Faire correspondre le nom du rôle avec son id
        role_ids = {}

        for role in roles:
            role_ids[role.name_role] = role.id_role


        # ==========================================================
        # 1. IDENTITIES
        # ==========================================================

        identities = [

            # ==========================================================
            # ORGANISATIONS
            # ==========================================================

            Identity(
                appelation="Académie Goncourt",
                under_appelation=None,
                description="Académie littéraire française chargée notamment de décerner le prix Goncourt.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Prix Goncourt",
                under_appelation=None,
                description="Prix littéraire français créé en 1903 et décerné chaque année par l'Académie Goncourt.",
                address=None,
                fk_id_identity_mother=None
            ),

            # ==========================================================
            # ACADÉMIE GONCOURT
            # ==========================================================

            Identity(
                appelation="Decoin",
                under_appelation="Didier",
                description="Écrivain et scénariste. Entre à l’Académie Goncourt le 6 juin 1995, succédant à Jean Cayrol au 3ème couvert. Après en avoir été le Secrétaire général, il est Président de la Société littéraire du 20 janvier 2020 au 13 mai 2024.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Chandernagor",
                under_appelation="Françoise",
                description="Écrivaine. Ancien membre du Conseil d'État. Entre à l’Académie Goncourt le 6 juin 1995, succédant à Emmanuel Roblès au 8ème couvert. Elle en est la Vice-Présidente.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Ben Jelloun",
                under_appelation="Tahar",
                description="Écrivain, poète et peintre. Entre à l’Académie Goncourt le 6 mai 2008, succédant à François Nourissier au 6ème couvert.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Constant",
                under_appelation="Paule",
                description="Écrivaine. Entre à l’Académie Goncourt le 8 janvier 2013, succédant à Robert Sabatier au 4ème couvert.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Claudel",
                under_appelation="Philippe",
                description="Écrivain, réalisateur et dramaturge. Entre à l’Académie Goncourt le 11 janvier 2012, succédant à Jorge Semprun au 9ème couvert. Après en avoir été le Trésorier, puis Secrétaire général, il est élu Président de la Société littéraire le 13 mai 2024.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Assouline",
                under_appelation="Pierre",
                description="Écrivain et journaliste. Entre à l’Académie Goncourt le 11 janvier 2012, succédant à Françoise Mallet-Joris au 10ème couvert.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Schmitt",
                under_appelation="Eric-Emmanuel",
                description="Dramaturge, philosophe et écrivain. Entre à l’Académie Goncourt le 5 janvier 2016, succédant à Edmonde Charles-Roux au 2ème couvert. Élu trésorier le 6 mai 2025.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Laurens",
                under_appelation="Camille",
                description="Écrivaine. Entre à l’Académie Goncourt le 11 février 2020, succédant à Virginie Despentes au 7ème couvert. Élue secrétaire générale le 13 mai 2024.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Bruckner",
                under_appelation="Pascal",
                description="Romancier, philosophe et essayiste. Entre à l’Académie Goncourt le 11 février 2020, succédant à Bernard Pivot au 1er couvert.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Angot",
                under_appelation="Christine",
                description="Écrivaine. Entre à l’Académie Goncourt le 28 février 2023, succédant à Patrick Rambaud au 5ème couvert.",
                address=None,
                fk_id_identity_mother=None
            ),

            # ==========================================================
            # AUTEURS
            # ==========================================================

            Identity(
                appelation="Bergmann",
                under_appelation="Boris",
                description="Boris Bergmann est né à Paris en 1992. Il est l'auteur de cinq romans dont Nage Libre (prix de la Vocation 2018) et Les Corps insurgés (Prix Fénéon 2020). Il a été pensionnaire de la Villa Medicis et de la Villa Kujoyama. Il a organisé des expositions en France et à l'étranger (autour de l'oeuvre de René Daumal, notamment) et collabore en tant qu'éditeur associé à la revue d'art et de littérature Magma. Minotaure est son premier roman autobiographique.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Chennevière",
                under_appelation="Louise",
                description="Autrice, chanteuse et musicienne française née en 1993.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Devi",
                under_appelation="Ananda",
                description="Née à l'île Maurice, Ananda Devi est l'autrice d'une oeuvre récompensée par de nombreux prix et traduite en une douzaine de langues. Parmi ses livres les plus marquants, on peut citer Ève de ses décombres (Gallimard, 2006, prix des Cinq Continents, prix RFO, prix Télévision Suisse Romande), Le Sari vert (Gallimard 2009, prix Louis Guilloux), Le Rire des déesses (Grasset, 2021, prix Femina des lycéens) et Le Jour des caméléons (Grasset, 2023, prix de la Langue française). Elle a reçu le prestigieux prix américain Neustadt 2024 pour l'ensemble de son oeuvre.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Devillers",
                under_appelation="Sonia",
                description="Sonia Devillers est journaliste dans la matinale de France Inter et présentatrice du « Dessous des images » sur Arte. Son premier livre, Les Exportés (Flammarion, 2022), raconte comment sa famille a fui la Roumanie communiste.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Godard",
                under_appelation="Anne",
                description="Anne Godard est née à Paris en 1971, elle enseigne la littérature et l'écriture créative à l'université Sorbonne-Nouvelle. Elle a publié aux Éditions de Minuit L'Inconsolable en 2006 (prix RTL-Lire) et Une chance folle en 2017 (prix Alain Spiess du deuxième roman). Nous aussi est son troisième roman.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Grondeau",
                under_appelation="Olivier",
                description="Après des études littéraires et des emplois de libraire, Olivier Grondeau est parti huit ans sur les routes, avant d'être arrêté en Iran. Libéré en mars 2025, il poursuit désormais des études d'anthropologie. L'écriture l'a toujours accompagné. Joseph dans la nuit est son premier livre.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Haenel",
                under_appelation="Yannick",
                description="Yannick Haenel a notamment publié Cercle (prix Décembre 2007 et prix Roger Nimier 2008), Jan Karski (prix Interallié et prix du Roman Fnac 2009) et Tiens ferme ta couronne (prix Médicis 2017).",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Hassaine",
                under_appelation="Lilia",
                description="Lilia Hassaine est notamment l'autrice de Panorama (2023, prix Renaudot des lycéens). JEest son quatrième roman.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Jaenada",
                under_appelation="Philippe",
                description="Philippe Jaenada est l'auteur d'une douzaine de romans, dont Le Chameau sauvage (Julliard, 1997, prix de Flore), La Petite Femelle (2015) et La Serpe (2017, prix Femina) et plus récemment, chez Mialet-Barrault Éditeurs, Au printemps des monstres et La désinvolture est une bien belle chose (2021 et 2024). Il rejoint en cette rentrée littéraire les Éditions Flammarion.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Jouannais",
                under_appelation="Jean-Yves",
                description="Jean-Yves Jouannais, né en 1964, est professeur à l'École nationale supérieure des beaux-arts de Paris. Il a publié, notamment, L'Idiotie (Beaux-Arts livres), Artistes sans oeuvres (Verticales), Les Barrages de sable (Grasset). De 2008 à 2024, il est l'auteur du cycle de conférences-performances, L'Encyclopédie des guerres, au Centre Pompidou (Paris).",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Marsantes",
                under_appelation="Emma",
                description="Écrivaine française.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Mélois",
                under_appelation="Clémentine",
                description="Clémentine Mélois est née en 1980. Elle est notamment l'autrice, aux Editions Grasset, de Cent titres. Sinon j'oublie, Dehors, la tempête, ainsi que du très remarqué Alors c'est bien (« L'Arbalète », Editions Gallimard, 2024).",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Orélien",
                under_appelation="Thélyson",
                description="Né en 1988, Thélyson Orélien est un auteur québécois d'origine haïtienne. Poète et critique, il construit une oeuvre habitée par la mémoire, l'exil et la question de l'appartenance. Depuis sa publication au Québec par les Éditions du Boréal, C'était ça ou mourir rencontre un écho international exceptionnel et est en cours de traduction dans plus de vingt langues. Un premier roman phénomène qui révèle une grande voix de la littérature contemporaine.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Prudhomme",
                under_appelation="Sylvain",
                description="Sylvain Prudhomme est l'auteur de romans, récits et reportages salués par la critique et traduits à l'étranger. Il a reçu le prix Femina en 2019 pour Par les routes. L'Enfant dans le taxi a paru en 2023 aux Éditions de Minuit. Coyote, récit d'un voyage le long de la frontière américano-mexicaine, a reçu le prix Nicolas Bouvier 2025.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Rolin",
                under_appelation="Olivier",
                description="Écrivain français, auteur notamment de romans, récits et essais.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Trigano",
                under_appelation="Patrice",
                description="Écrivain et galeriste français.",
                address=None,
                fk_id_identity_mother=None
            ),

            # ==========================================================
            # ÉDITEURS
            # ==========================================================

            Identity(
                appelation="Albin Michel",
                under_appelation=None,
                description="Maison d'édition française.",
                address="22 rue Huyghens 75014 Paris",
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="P.O.L",
                under_appelation=None,
                description="Maison d'édition française spécialisée notamment dans la littérature contemporaine.",
                address="33 rue Saint-André-des-Arts 75006 Paris",
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Grasset",
                under_appelation=None,
                description="Maison d'édition française publiant notamment de la littérature française et étrangère.",
                address="61 rue des Saints-Pères 75006 Paris",
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Robert Laffont",
                under_appelation=None,
                description="Maison d'édition française du groupe Editis.",
                address="92 avenue de France 75013 Paris",
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Actes Sud",
                under_appelation=None,
                description="Maison d'édition française indépendante publiant notamment de la littérature.",
                address="47 rue du Docteur Fanton 13200 Arles Cedex",
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="L'Iconoclaste",
                under_appelation=None,
                description="Maison d'édition française publiant notamment des romans, essais et documents.",
                address="26 rue Jacob 75006 Paris",
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Gallimard",
                under_appelation=None,
                description="Maison d'édition française historique spécialisée notamment dans la littérature.",
                address="5 rue Gaston Gallimard 75007 Paris",
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Flammarion",
                under_appelation=None,
                description="Maison d'édition française publiant notamment de la littérature, des essais et des documents.",
                address="82 rue Saint-Lazare 75009 Paris",
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Verdier",
                under_appelation=None,
                description="Maison d'édition française indépendante.",
                address="11220 Lagrasse",
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Minuit",
                under_appelation=None,
                description="Maison d'édition française connue notamment pour sa littérature contemporaine.",
                address="7 rue Bernard-Palissy 75006 Paris",
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Maurice Nadeau",
                under_appelation=None,
                description="Maison d'édition française indépendante fondée par Maurice Nadeau.",
                address="5 rue Malebranche 75005 Paris",
                fk_id_identity_mother=None
            ),

            # ==========================================================
            # PERSONNAGES PRINCIPAUX
            # ==========================================================

            # BATAILLE AU PROCÈS

            Identity(
                appelation="Georges Bataille",
                under_appelation=None,
                description="Personnage principal appelé à témoigner au procès de Jean-Jacques Pauvert",
                address=None,
                fk_id_identity_mother=None
            ),
            Identity(
                appelation="Jean-Jacques Pauvert",
                under_appelation=None,
                description="Personnage principal poursuivi pour avoir publié les œuvres de Sade",
                address=None,
                fk_id_identity_mother=None
            ),

            # DE L'AUTRE CÔTÉ DU LAC

            Identity(
                appelation="Paola",
                under_appelation=None,
                description="Personnage principal photographe et artiste disparue en montagne",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Le narrateur",
                under_appelation=None,
                description="Personnage principal, il est le double de l'auteur. il mène l'enquête",
                address=None,
                fk_id_identity_mother=None
            ),

            # C'ÉTAIT ÇA OU MOURIR

            Identity(
                appelation="Jonas Dorléon",
                under_appelation=None,
                description="Personnage principal, il quitte Haïti. il mène l'enquête",
                address=None,
                fk_id_identity_mother=None
            ),

            # CHOSES QUE JE CROYAIS PERDUES

            Identity(
                appelation="Emilie",
                under_appelation=None,
                description="Personnage principal, narratrice, elle déménage.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Tristan",
                under_appelation=None,
                description="Personnage principal, ex d'Emilie.",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Sandra",
                under_appelation=None,
                description="Personnage principal, amie d'Emilie.",
                address=None,
                fk_id_identity_mother=None
            ),

            # N'EFFACE PAS MES CERCLES

            Identity(
                appelation="Mia",
                under_appelation=None,
                description="Personnage principal, elle est le double de l'auteur. elle se replonge dans la saga familiale",
                address=None,
                fk_id_identity_mother=None
            ),

            # LA SOLITUDE DES PROFESSEURS EST INFINIE

            Identity(
                appelation="Jean Deichel",
                under_appelation=None,
                description="Personnage principal, protagoniste jeune agrégé de lettres et professeur de français stagiaire dans un collège de banlieue parisienne",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Anya",
                under_appelation=None,
                description="Personnage principal, tutrice de Jean au sein de l'établissement",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Streger",
                under_appelation=None,
                description="Personnage principal, principal de l'établissement",
                address=None,
                fk_id_identity_mother=None
            ),

            Identity(
                appelation="Laguille",
                under_appelation=None,
                description="Personnage principal, adjointe du principal de l'établissement",
                address=None,
                fk_id_identity_mother=None
            )

        ]

        # ==========================================================
        # 2. ENTITIES
        # ==========================================================

        entities = [

            Entity(
                ISBN=9782226511874,
                price=21.0,
                name="Minotaure",
                first_name=None,
                type="livre",
                resume="A 23 ans, l'auteur s'apprête à surprendre son père, qu'il n'a jamais rencontré, dans son cabinet de psychiatre. Cette rencontre survient après une quête de ce père disparu depuis sa naissance. Un récit littéraire autobiographique en hommage à la mère.",
                creation_date=date(2026, 8, 19),
                nb=242,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782818063583,
                price=21.0,
                name="Faire la peau",
                first_name=None,
                type="livre",
                resume="Je dis que l'une des plus tenaces fictions tient tout entière dans ce mot, mère. Que la haine qui circule entre les mères et leurs filles est sauvage, et qu'il faut la regarder droit dans les yeux.",
                creation_date=date(2026, 8, 20),
                nb=286,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782246846949,
                price=24.0,
                name="Chronique d'un royaume perdu",
                first_name=None,
                type="livre",
                resume="Au Bouchon, petit village isolé de l’île Maurice, quatre générations se succèdent depuis le temps de l’esclavage. La violence se mêle à l’amour, la tendresse à la haine, les plus nobles passions aux vices les plus vils, les sangs des unes aux sangs des autres… Les cinq fondateurs viennent d’une plantation lointaine  : trois sont nés dans la puissante et blanche famille Dumontais  ; deux d’une esclave noire. Mais les trois blancs sont en vérité le fruit d’une passion entre Madame et le Vieux Bouc, un esclave magnétique qui revendique aussi la paternité des deux derniers. Bannis pour s’être liés d’amour et d’amitié, les cinq enfants devenus grands trouvent refuge dans ce lieu perdu dont ils font leur royaume, autarcique et magique, qu’ils défendent d’un seul corps, puisqu’ici sont abolies les frontières entre passé, présent et avenir  ; vie et mort  ; réel et fantastique. Tel homme entend sans le vouloir tous les péchés humains  ; telle femme meurt et renait en déesse protectrice  ; un enfant vit parmi les oiseaux quand son cousin viole et tue sans frein  ; le moulin est hanté par les voix des fantômes, la nature donne les plus beaux fruits mais décapite la chapelle  ; les guerres du monde contemporain rencontrent les combats intérieurs de chaque individu et l’histoire de l’humanité se reproduit dans l’infiniment petit de leurs existences débridées. Parmi eux, un enfant timide sera le chroniqueur de ce royaume hors-norme dont il livre les jours de paix, de luttes, et les nuits de folie pour empêcher l’oubli. Épopée fabuleuse,  mythologie vibrante, fable majestueuse, cette Chronique d’un Royaume perdu est le chef d’œuvre d’Ananda Devi.",
                creation_date=date(2026, 8, 19),
                nb=454,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782378805975,
                price=19.90,
                name="Joseph dans la nuit",
                first_name=None,
                type="livre",
                resume="Voyageur épris d'ailleurs, de stop et de liberté, Olivier est en route vers Lahore pour fêter la nouvelle année sur une plage indienne. En traversant l'Iran, il est arrêté à Chiraz alors qu'explose le mouvement Femme, Vie, Liberté. Accusé d'espionnage, il reste deux ans et demi en prison. Olivier est un poète, habitué à vivre de peu, sans confort ni téléphone portable. En cellule, il mobilise tout ce qui peut lui apporter de la lumière, la poésie persane comme les chansons de Britney Spears. Derrière ses paupières, installé dans un cinéma dont il est le seul spectateur, il se projette des films. La nuit, il convoque dans ses rêves les êtres aimés. Un récit lumineux et bouleversant qui nous dit que, même dans la nuit, quelque chose en nous refusera toujours de céder. La découverte d'un écrivain.",
                creation_date=date(2026, 8, 20),
                nb=256,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782226499523,
                price=16.90,
                name="Une forêt",
                first_name=None,
                type="livre",
                resume="Pendant les grands procès visant à éradiquer le nazisme dans la vie publique allemande, Jacob Michael Lenz, avocat et capitaine dans l'US Army, est appelé par un tribunal pour une affaire hors du commun. Des mainates, des oiseaux parleurs, nichant dans une forêt de Brême, ont appris à chanter des hymnes nazis et les transmettent à leurs oisillons.",
                creation_date=date(2026, 1, 2),
                nb=112,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782080490896,
                price=23.0,
                name="L'inconnue du quai de Javel",
                first_name=None,
                type="livre",
                resume="Le 6 septembre 1949, une jeune femme est retrouvée morte quai de Javel, à Paris, sans sac ni chaussures, manifestement rhabillée à la hâte puis déposée là par son assassin. Elle est identifiée le lendemain : c'est Louise Cansot, le modèle le plus demandé par les peintres de Montparnasse. Rapidement, quatre suspects se détachent, évidents, presque des archétypes. On dirait le début d'un roman de Simenon, mais l'inspecteur-chef Ferrière n'a pas le talent de Maigret, et doit se résoudre à classer l'affaire au bout de six mois, sans avoir arrêté personne. Soixante-quinze ans plus tard, Philippe Jaenada reprend l'enquête à partir du dossier retrouvé puis, comme à son habitude, sollicite ses contacts aux archives, exhume tous les documents, arpente tous les lieux - remonte le temps. Pour ce livre, il a lu les soixante-quinze enquêtes de Maigret, s'inspirant humblement et fidèlement des méthodes du commissaire fictif. Et il va résoudre ce meurtre bien réel, laissant le lecteur subjugué par la dextérité de son investigation et fasciné par cette jeune femme à laquelle il redonne un visage et une histoire.",
                creation_date=date(2026, 8, 12),
                nb=528,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782073161925,
                price=21.50,
                name="La solitude des professeurs est infinie",
                first_name=None,
                type="livre",
                resume="Jean Deichel, jeune professeur de français, fait son stage dans un collège de la banlieue parisienne. La nuit, il loge dans un club de tennis à Deuil-la-Barre ; le jour, il découvre les difficultés du métier en même temps que ses joies profondes, la violence de l'École en même temps que sa beauté. Jean est aussi un poète ivre d'aventure, attentif à trouver la lumière de la « vraie vie » au coeur du quotidien le plus gris : dans des jardins réels ou rêvés, au bord d'un lac, lors d'évasions à Pompéi et à Tarquinia, mais surtout dans la grâce fragile d'un cours réussi. Entre réalité politique et mystère existentiel, la vie des profs est un roman.",
                creation_date=date(2026, 8, 20),
                nb=320,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782378562953,
                price=19.50,
                name="N'efface pas mes cercles",
                first_name=None,
                type="livre",
                resume="1980, une femme se suicide dans un appartement cossu. Dans les années cinquante, elle s'était unie avec un jeune homme à qui tout l'opposait. Explorant son histoire familiale, la narratrice tente de démêler les raisons de ce drame et dresse ce faisant le portrait d'une société aux prises avec ses démons : le patriarcat, la guerre, la colonisation, les injonctions à la réussite et au bonheur. N'efface pas mes cercles remonte le temps à la recherche des destins brisés et restitue avec force l'atmosphère des époques traversées. Cette saga bouleversante confirme le grand art d'Emma Marsantes.",
                creation_date=date(2026, 8, 20),
                nb=160,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782707358233,
                price=22.0,
                name="De l'autre côté du lac",
                first_name=None,
                type="livre",
                resume="Paola était comme ça. Elle était entière. Elle voulait toujours que tout soit vrai, les rapports humains, les discussions, les rencontres, les projets dans lesquels elle s’engageait. Elle ne supportait pas les faux-semblants, les demi-mesures. Elle était d’un bloc. Elle disait les mots ont de la valeur. Les actes ont de la valeur. Elle voulait qu’il y ait de l’enjeu. C’est dans l’inconfort qu’on se découvre, elle disait. C’est dans l’inconfort qu’on grandit. » Aux abords d’un lac de haute montagne, à la lisière d’une réserve interdite aux humains, un groupe de chercheurs s’affaire. Parmi eux, une photographe aperçoit sur un des versants quelque chose qui échappe au regard de tous les autres. Les signes étranges s’accumulent, un corps est retrouvé. La photographe décide de rester là-haut, seule.  Quelques mois plus tard, c’est elle qui, à son tour, disparaît. Avec ce roman tout en tension, Sylvain Prudhomme approfondit plusieurs thèmes qui lui sont chers : le désir d’intensité, l’appel du sauvage, le rêve d’une vie vraie",
                creation_date=date(2026, 8, 27),
                nb=288,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782246847069,
                price=21.50,
                name="C'était ça ou mourir",
                first_name=None,
                type="livre",
                resume="Le premier roman de Thélyson Orélien est déjà le phénomène littéraire de l’année 2026. En cours de traduction dans plus d’une vingtaine de langues, C’était ça ou mourir a conquis le Québec et bientôt le monde entier, en racontant l’Odyssée de Jonas Dorléon. Après l’embrasement de son quartier de Port-au-Prince, Jonas n’emporte presque rien avec lui en quittant Haïti : un diplôme, un cahier de poèmes, la photo de sa mère. Toute une vie dans un sac plastique. Se réfugiant d’abord en République dominicaine, puis au Brésil et au Mexique, ce professeur d’histoire franchit les frontières tantôt à bord d’un autobus surchauffé, tantôt en affrontant les profondeurs de la jungle. À chaque étape des visages surgissent, des corps tombent, des solidarités se nouent puis se brisent. Dans l’espoir d’atteindre le Canada et le peu de famille qu’il lui reste, Jonas se retrouve aux portes des États-Unis, seul face aux agents de l’ICE et d’une administration prête à tout pour mener sa chasse aux migrants. Avec la trajectoire de Jonas, c’est une cartographie intime de la survie qui se dévoile. Aussi contemporain qu’universel, ce roman raconte les migrations au présent — non comme un concept, mais comme une expérience physique : marcher, avoir faim, se blesser, rire devant l’horreur pour ne pas abandonner. Thélyson Orélien y déploie une écriture foisonnante, traversée d’humour et de poésie, une langue d’exil qui s’apprend « sans grammaire, sans dictionnaire, juste avec les os et la peau ». Porté par un souffle narratif irrésistible, C’était ça ou mourir est un premier roman bouleversant qui révèle un écrivain majeur de notre temps.",
                creation_date=date(2026, 8, 19),
                nb=272,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782221286807,
                price=21.0,
                name="Le fabuleux piano",
                first_name=None,
                type="livre",
                resume="Après le succès littéraire et commercial de son récit Les Exportés , Sonia Devillers part à la recherche d'un admirable piano à queue, volé par les nazis en 1943. Ce qu'elle nous raconte est bouleversant, instructif, et magistralement mené. Le fabuleux piano est un instrument volé par les Allemands, en 1943, à des juifs qui le cherchent encore... Dans ce vide impossible à combler, Sonia Devillers entend une résonance intime, le souvenir d'un instrument que sa propre grand-mère, forcée à l'exil, a regretté toute sa vie. Elle part alors sur les traces des pianos fantômes pillés par milliers sous l'Occupation et transportés jusqu'aux confins du IIIe Reich. Avec cet instrument de concert ressurgit l'incroyable destin d'une famille d'éditeurs de musique, les Enoch. Un siècle de partitions, des menuets de Ravel aux ritournelles de Prévert. Les nazis se sont acharnés sur les Enoch, mais ils ont échoué à les réduire au silence. Des douleurs de la guerre va naître une chanson portée par Yves Montand, Les Feuilles mortes : un triomphe mondial. Le piano disparu continue pourtant de hanter les survivants...",
                creation_date=date(2026, 8, 27),
                nb=288,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782073162854,
                price=19.0,
                name="Choses que je croyais perdues",
                first_name=None,
                type="livre",
                resume=" Je voulais te dire : sans le faire exprès, j'ai cassé le verre à moutarde Musclor que lu aimais bien. Le prince sous stéroïdes mal imprimé a perdu sa tête, mais il continue de flatter d'une main distraite l'encolure de son tigre vert de compagnie, Tu avais trouvé ce verre dans un vide-greniers où les gens vendaient pas cher de jolies choses. Après l'avoir regardé longtemps, avec intensité, tu l'avais négocié à deux euros. C'était un souvenir d'enfance et ta joie m'avait attendrie. Ça allait encore entre nous à ce moment-là, enfin je crois. Seule dans son appartement, une jeune femme emballe ses affaires. Demain, des déménageurs emporteront ces traces fragiles de son existence. Elle pense à l'homme dont elle vient de se séparer, et des histoires surgissent des objets qu'elle manipule. Une assiette au filet d'or, un ensemble H&M couleur poil de chameau, un rouleau de Sopalin : ces témoins d'une vie ordinaire ont autant à raconter qu'un trépidant roman d'aventures... Que reste-t-il de ce que nous avons vécu ? De quelles légendes sommes-nous faits ? Les grandes amours comme les petits riens, les désillusions et les désirs sont au coeur de ce roman plein de surprises, à la fantaisie incomparable.",
                creation_date=date(2026, 8, 20),
                nb=176,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782862316857,
                price=19.0,
                name="Bataille au procès",
                first_name=None,
                type="livre",
                resume="En 1956, Georges Bataille est appelé à témoigner au procès de Jean-Jacques Pauvert, poursuivi pour avoir publié les œuvres de Sade. L’auteur d'Histoire de l'oeil comprend que la morale menace de mort la littérature. L’audience devient le miroir de sa propre vie. Les souvenirs affluent : enfance marquée par la folie d’un père aveugle et paralytique, l’indifférence d’une mère réfugiée dans la religion. Des événements qui ont émaillé son parcours surgissent : expériences limites dans ses amours placées sous l’égide de la transgression, visions de guerre et de sacrifice qui le hantent, traversée du mal, liens tourmentés avec le parti communiste, haine du fascisme… Réflexions et fulgurances se mêlent en un vertige où pensée et vie s’entrelacent, entre érotisme et sacré, extase et mort. Mais derrière ces éclats affleure aussi une énigme plus obscure. Refusera-t-elle de se dévoiler ?À travers cet épisode de la vie littéraire, Patrice Trigano accompagne Bataille au plus près de son vertige intérieur. Il explore ce point où l’écriture n’obéit plus à l’auteur, où l’œuvre surgit comme une puissance étrangère, excessive, qui le dépasse.Patrice Trigano a fait des études de droit et de philosophie avant de consacrer sa vie à l’art en tant que galeriste, écrivain et dramaturge. Ses livres sont publiés aux éditions de la Différence, Léo Scheer, Mercure de France et Maurice Nadeau. Il a publié en 2024, La Promesse de l’art, Mémoires d’un galeriste aux Éditions du Canoë.",
                creation_date=date(2026, 8, 21),
                nb=136,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782073121349,
                price=20.0,
                name="La guerre éternelle : souvenirs de Troie",
                first_name=None,
                type="livre",
                resume="« Pour donner à ma longue rêverie la forme d'un livre, j'avais besoin de voir. De la terre, des pierres, des arbres, un rivage. J'ai toujours besoin de voir. Je suis allé en Troade à la fin d'un mois de juin, alors que les coquelicots jetaient de grandes flaques rouges au milieu des champs de blé et d'oliviers où jadis s'affrontaient les héros. » Il y a quelque trente-trois siècles, des guerriers grecs ravagent une cité d'Asie Mineure qu'ils appellent Troïa ou Ilios. Les hommes sont massacrés, les femmes traînées en esclavage. C'était dans la nuit des temps, mais grâce à l'Iliade cela vit toujours dans notre mémoire. C'était, aussi bien, hier, aujourd'hui, demain : la tragédie de la destruction d'une ville n'a cessé d'être réécrite en lettres de feu et de sang, depuis Carthage un siècle et demi avant notre ère jusqu'à Dresde et Hiroshima, Marioupol et Gaza de nos jours. La guerre de Troie est éternelle, et Troie est la Mère de toutes les villes martyrisées.",
                creation_date=date(2026, 8, 20),
                nb=219,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782073099945,
                price=21.0,
                name="Je",
                first_name=None,
                type="livre",
                resume="« - Que savez-vous de la beauté, Antoinette ? Il se tourna vers moi, suspendu à ma réponse. - Pas grand-chose. Mais je sais la reconnaître quand elle est là. - Eh bien moi, chaque fois que je la vois, elle me blesse. Quand je vois votre visage, par exemple, quelque chose en moi se trouve comme ébranlé. » île de la Jamaïque, 1831. Antoinette Cosway, créole de bonne famille, s'éprend d'Edward Rochester, un Anglais aussi impénétrable que fascinant. Mais à la séduction enflammée succèdent rapidement des scènes vénéneuses, où les baisers sont des blessures, où toute une société livre la jeune femme à son bourreau. Des années plus tard, Antoinette tente de conquérir sa propre histoire. JE se situe à mi-chemin entre roman victorien et thriller intimiste contemporain. Lilia Hassaine s'est inspirée du personnage de la première femme de Rochester dans Jane Eyre, le roman culte de Charlotte Brontë. Elle a choisi de lui donner une voix, un corps, une destinée.",
                creation_date=date(2026, 8, 20),
                nb=248,
                unit_nb="pages",
                fk_id_entity_mother=None
            ),

            Entity(
                ISBN=9782330225575,
                price=20.0,
                name="Nous aussi",
                first_name=None,
                type="livre",
                resume="On fait partie d'une grande famille. On sait qu'on est privilégiés. On vit ensemble, dans notre immeuble au centre de Paris, on se retrouve l'été dans notre maison à la montagne. On trouve que c'est normal. C'est chez nous, c'est à nous, c'est pour nous. On se ressemble, on se compare, on se confronte, on ne se quitte pas, on se confond, on s'appartient. On ne sait pas comment dire je, on n'en a pas besoin, puisqu'on est nous. Nous les enfants, les frères et soeurs, les cousins, les cousines, on partage tout, nos écoles, nos chambres, nos habits, nos repas, nos jeux, nos bains, nos lits. On est les membres indissociables du grand corps familial. On n'a jamais vécu dehors. On ne sait pas ce que c'est. On n'en est pas capables. On n'en a même pas envie. Et tout aurait dû continuer ainsi, dans un même immuable recommencement. Le jour où la façade s'est fissurée, on n'a pas compris. Ça n'aurait pas dû se produire, pas dans notre famille. Ce n'était pas possible que ça nous arrive, à nous aussi.",
                creation_date=date(2026, 8, 19),
                nb=237,
                unit_nb="pages",
                fk_id_entity_mother=None
            )
        ]

        # ==========================================================
        # 3. IDENTITY_ENTITY
        # ==========================================================

        # on cré une liste de de dictionnaire avec 3 clés chacun
        # le but est ensuite de faire correspondre les valeur à des id dans mes tables identity et entity
        identity_entities = [

            # ==========================================================
            # MINOTAURE
            # ==========================================================

            {
                "entity_name": "Minotaure",
                "identity_name": "Boris Bergmann",
                "role": "auteur"
            },
            {
                "entity_name": "Minotaure",
                "identity_name": "Albin Michel",
                "role": "éditeur"
            },

            # ==========================================================
            # FAIRE LA PEAU
            # ==========================================================

            {
                "entity_name": "Faire la peau",
                "identity_name": "Louise Chennevière",
                "role": "auteur"
            },
            {
                "entity_name": "Faire la peau",
                "identity_name": "P.O.L",
                "role": "éditeur"
            },

            # ==========================================================
            # CHRONIQUE D'UN ROYAUME PERDU
            # ==========================================================

            {
                "entity_name": "Chronique d'un royaume perdu",
                "identity_name": "Ananda Devi",
                "role": "auteur"
            },
            {
                "entity_name": "Chronique d'un royaume perdu",
                "identity_name": "Grasset",
                "role": "éditeur"
            },

            # ==========================================================
            # JOSEPH DANS LA NUIT
            # ==========================================================

            {
                "entity_name": "Joseph dans la nuit",
                "identity_name": "Olivier Grondeau",
                "role": "auteur"
            },
            {
                "entity_name": "Joseph dans la nuit",
                "identity_name": "L'Iconoclaste",
                "role": "éditeur"
            },

            # ==========================================================
            # UNE FORÊT
            # ==========================================================

            {
                "entity_name": "Une forêt",
                "identity_name": "Jean-Yves Jouannais",
                "role": "auteur"
            },
            {
                "entity_name": "Une forêt",
                "identity_name": "Albin Michel",
                "role": "éditeur"
            },

            # ==========================================================
            # L'INCONNUE DU QUAI DE JAVEL
            # ==========================================================

            {
                "entity_name": "L'inconnue du quai de Javel",
                "identity_name": "Philippe Jaenada",
                "role": "auteur"
            },
            {
                "entity_name": "L'inconnue du quai de Javel",
                "identity_name": "Flammarion",
                "role": "éditeur"
            },

            # ==========================================================
            # LA SOLITUDE DES PROFESSEURS EST INFINIE
            # ==========================================================

            {
                "entity_name": "La solitude des professeurs est infinie",
                "identity_name": "Yannick Haenel",
                "role": "auteur"
            },
            {
                "entity_name": "La solitude des professeurs est infinie",
                "identity_name": "Gallimard",
                "role": "éditeur"
            },
            {
                "entity_name": "La solitude des professeurs est infinie",
                "identity_name": "Jean Deichel",
                "role": "personnage_principal"
            },
            {
                "entity_name": "La solitude des professeurs est infinie",
                "identity_name": "Anya",
                "role": "personnage_principal"
            },
            {
                "entity_name": "La solitude des professeurs est infinie",
                "identity_name": "Streger",
                "role": "personnage_principal"
            },
            {
                "entity_name": "La solitude des professeurs est infinie",
                "identity_name": "Laguille",
                "role": "personnage_principal"
            },


            # ==========================================================
            # N'EFFACE PAS MES CERCLES
            # ==========================================================

            {
                "entity_name": "N'efface pas mes cercles",
                "identity_name": "Emma Marsantes",
                "role": "auteur"
            },
            {
                "entity_name": "N'efface pas mes cercles",
                "identity_name": "Verdier",
                "role": "éditeur"
            },
            {
                "entity_name": "N'efface pas mes cercles",
                "identity_name": "Mia",
                "role": "personnage_principal"
            },

            # ==========================================================
            # DE L'AUTRE CÔTÉ DU LAC
            # ==========================================================

            {
                "entity_name": "De l'autre côté du lac",
                "identity_name": "Sylvain Prudhomme",
                "role": "auteur"
            },
            {
                "entity_name": "De l'autre côté du lac",
                "identity_name": "Minuit",
                "role": "éditeur"
            },
            {
                "entity_name": "De l'autre côté du lac",
                "identity_name": "Paola",
                "role": "personnage_principal"
            },
            {
                "entity_name": "De l'autre côté du lac",
                "identity_name": "Le narrateur",
                "role": "personnage_principal"
            },

            # ==========================================================
            # C'ÉTAIT ÇA OU MOURIR
            # ==========================================================

            {
                "entity_name": "C'était ça ou mourir",
                "identity_name": "Thélyson Orélien",
                "role": "auteur"
            },
            {
                "entity_name": "C'était ça ou mourir",
                "identity_name": "Grasset",
                "role": "éditeur"
            },
            {
                "entity_name": "C'était ça ou mourir",
                "identity_name": "Jonas Dorléon",
                "role": "personnage_principal"
            },

            # ==========================================================
            # LE FABULEUX PIANO
            # ==========================================================

            {
                "entity_name": "Le fabuleux piano",
                "identity_name": "Sonia Devillers",
                "role": "auteur"
            },
            {
                "entity_name": "Le fabuleux piano",
                "identity_name": "Robert Laffont",
                "role": "éditeur"
            },

            # ==========================================================
            # CHOSES QUE JE CROYAIS PERDUES
            # ==========================================================

            {
                "entity_name": "Choses que je croyais perdues",
                "identity_name": "Clémentine Mélois",
                "role": "auteur"
            },
            {
                "entity_name": "Choses que je croyais perdues",
                "identity_name": "Gallimard",
                "role": "éditeur"
            },
            {
                "entity_name": "Choses que je croyais perdues",
                "identity_name": "Emilie",
                "role": "personnage_principal"
            },
            {
                "entity_name": "Choses que je croyais perdues",
                "identity_name": "Tristan",
                "role": "personnage_principal"
            },
            {
                "entity_name": "Choses que je croyais perdues",
                "identity_name": "Sandra",
                "role": "personnage_principal"
            },

            # ==========================================================
            # BATAILLE AU PROCÈS
            # ==========================================================

            {
                "entity_name": "Bataille au procès",
                "identity_name": "Patrice Trigano",
                "role": "auteur"
            },
            {
                "entity_name": "Bataille au procès",
                "identity_name": "Maurice Nadeau",
                "role": "éditeur"
            },
            {
                "entity_name": "Bataille au procès",
                "identity_name": "Georges Bataille",
                "role": "personnage_principal"
            },
            {
                "entity_name": "Bataille au procès",
                "identity_name": "Jean-Jacques Pauvert",
                "role": "personnage_principal"
            },

            # ==========================================================
            # LA GUERRE ÉTERNELLE
            # ==========================================================

            {
                "entity_name": "La guerre éternelle : souvenirs de Troie",
                "identity_name": "Olivier Rolin",
                "role": "auteur"
            },
            {
                "entity_name": "La guerre éternelle : souvenirs de Troie",
                "identity_name": "Gallimard",
                "role": "éditeur"
            },

            # ==========================================================
            # JE
            # ==========================================================

            {
                "entity_name": "Je",
                "identity_name": "Lilia Hassaine",
                "role": "auteur"
            },
            {
                "entity_name": "Je",
                "identity_name": "Gallimard",
                "role": "éditeur"
            },

            # ==========================================================
            # NOUS AUSSI
            # ==========================================================

            {
                "entity_name": "Nous aussi",
                "identity_name": "Anne Godard",
                "role": "auteur"
            },
            {
                "entity_name": "Nous aussi",
                "identity_name": "Actes Sud",
                "role": "éditeur"
            }
        ]

        # ==========================================================
        # 3.1. IDENTITY_ROLE
        # ==========================================================

        identity_roles = [

            # ==========================================================
            # DIDIER DECOIN
            # ==========================================================

            {
                "identity_name": "Didier Decoin",
                "role": "écrivain"
            },
            {
                "identity_name": "Didier Decoin",
                "role": "scénariste"
            },
            {
                "identity_name": "Didier Decoin",
                "role": "président"
            },
            {
                "identity_name": "Didier Decoin",
                "role": "président du jury"
            },

            # ==========================================================
            # FRANÇOISE CHANDERNAGOR
            # ==========================================================

            {
                "identity_name": "Françoise Chandernagor",
                "role": "écrivain"
            },
            {
                "identity_name": "Françoise Chandernagor",
                "role": "vice-président du jury"
            },
            {
                "identity_name": "Françoise Chandernagor",
                "role": "ancien membre du conseil d'etat"
            },

            # ==========================================================
            # TAHAR BEN JELLOUN
            # ==========================================================

            {
                "identity_name": "Tahar Ben Jelloun",
                "role": "écrivain"
            },
            {
                "identity_name": "Tahar Ben Jelloun",
                "role": "poète"
            },
            {
                "identity_name": "Tahar Ben Jelloun",
                "role": "peintre"
            },
            {
                "identity_name": "Tahar Ben Jelloun",
                "role": "membre du jury"
            },

            # ==========================================================
            # PAULE CONSTANT
            # ==========================================================

            {
                "identity_name": "Paule Constant",
                "role": "écrivain"
            },
            {
                "identity_name": "Paule Constant",
                "role": "membre du jury"
            },

            # ==========================================================
            # PHILIPPE CLAUDEL
            # ==========================================================

            {
                "identity_name": "Philippe Claudel",
                "role": "écrivain"
            },
            {
                "identity_name": "Philippe Claudel",
                "role": "réalisateur"
            },
            {
                "identity_name": "Philippe Claudel",
                "role": "dramaturge"
            },
            {
                "identity_name": "Philippe Claudel",
                "role": "président"
            },
            {
                "identity_name": "Philippe Claudel",
                "role": "trésorier"
            },
            {
                "identity_name": "Philippe Claudel",
                "role": "secrétaire général"
            },
            {
                "identity_name": "Philippe Claudel",
                "role": "membre du jury"
            },

            # ==========================================================
            # PIERRE ASSOULINE
            # ==========================================================

            {
                "identity_name": "Pierre Assouline",
                "role": "écrivain"
            },
            {
                "identity_name": "Pierre Assouline",
                "role": "journaliste"
            },
            {
                "identity_name": "Pierre Assouline",
                "role": "membre du jury"
            },


            # ==========================================================
            # ERIC-EMMANUEL SCHMITT
            # ==========================================================

            {
                "identity_name": "Eric-Emmanuel Schmitt",
                "role": "dramaturge"
            },
            {
                "identity_name": "Eric-Emmanuel Schmitt",
                "role": "philosophe"
            },
            {
                "identity_name": "Eric-Emmanuel Schmitt",
                "role": "écrivain"
            },
            {
                "identity_name": "Eric-Emmanuel Schmitt",
                "role": "trésorier"
            },
            {
                "identity_name": "Eric-Emmanuel Schmitt",
                "role": "membre du jury"
            },

            # ==========================================================
            # CAMILLE LAURENS
            # ==========================================================

            {
                "identity_name": "Camille Laurens",
                "role": "écrivain"
            },
            {
                "identity_name": "Camille Laurens",
                "role": "secrétaire général"
            },
            {
                "identity_name": "Camille Laurens",
                "role": "membre du jury"
            },

            # ==========================================================
            # PASCAL BRUCKNER
            # ==========================================================

            {
                "identity_name": "Pascal Bruckner",
                "role": "romancier"
            },
            {
                "identity_name": "Pascal Bruckner",
                "role": "philosophe"
            },
            {
                "identity_name": "Pascal Bruckner",
                "role": "essayiste"
            },
            {
                "identity_name": "Pascal Bruckner",
                "role": "membre du jury"
            },

            # ==========================================================
            # CHRISTINE ANGOT
            # ==========================================================

            {
                "identity_name": "Christine Angot",
                "role": "écrivain"
            },
            {
                "identity_name": "Christine Angot",
                "role": "membre du jury"
            }
        ]


        # ==========================================================
        # 4. CRÉATION DES IDENTITY
        # ==========================================================

        for identity in identities:
            self.identity_dao.create(identity)

        # ==========================================================
        # 5. CRÉATION DES ENTITY
        # ==========================================================

        for entity in entities:
            self.entity_dao.create(entity)

        # ==========================================================
        # 6. CRÉATION DES IDENTITY_ENTITY
        # 6.1. Relations Identity + Role sans Entity
        # ----------------------------------------------------------

        for relation in identity_roles:

            identity = None

            for current_identity in identities:

                if current_identity.under_appelation:
                    identity_name = (
                        f"{current_identity.under_appelation} "
                        f"{current_identity.appelation}"
                    )
                else:
                    identity_name = current_identity.appelation

                if identity_name == relation["identity_name"]:
                    identity = current_identity

            if identity is not None:

                role_id = role_ids.get(relation["role"])

                if role_id is not None:

                    identity_entity = IdentityEntity(
                        fk_id_entity=None,
                        fk_id_identity=identity.id_identity,
                        fk_id_role=role_id
                    )

                    self.identity_entity_dao.create(identity_entity)

                else:
                    print(
                        f"Rôle introuvable : {relation['role']}"
                    )

            else:
                print(
                    f"Identité introuvable : "
                    f"{relation['identity_name']}"
                )

        # ----------------------------------------------------------
        # 6.2. Relations Entity + Identity + Role
        # ----------------------------------------------------------

        for relation in identity_entities:

            identity = None
            entity = None

            for current_identity in identities:

                if current_identity.under_appelation:
                    identity_name = (
                        f"{current_identity.under_appelation} "
                        f"{current_identity.appelation}"
                    )
                else:
                    identity_name = current_identity.appelation

                if identity_name == relation["identity_name"]:
                    identity = current_identity

            for current_entity in entities:

                if current_entity.name == relation["entity_name"]:
                    entity = current_entity

            if identity is not None and entity is not None:

                role_id = role_ids.get(relation["role"])

                if role_id is not None:

                    identity_entity = IdentityEntity(
                        fk_id_entity=entity.id_entity,
                        fk_id_identity=identity.id_identity,
                        fk_id_role=role_id
                    )

                    self.identity_entity_dao.create(identity_entity)

                else:
                    print(
                        f"Rôle introuvable : {relation['role']}"
                    )

            else:

                if identity is None:
                    print(
                        f"Identité introuvable : "
                        f"{relation['identity_name']}"
                    )

                if entity is None:
                    print(
                        f"Entité introuvable : "
                        f"{relation['entity_name']}"
                    )

        print("Données initiales chargées avec succès.")

        return {
            "identities": identities,
            "entities": entities,
            "identity_entities": identity_entities,
            "identity_roles": identity_roles
        }
