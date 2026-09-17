-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : jeu. 17 sep. 2026 à 18:26
-- Version du serveur : 11.7.1-MariaDB
-- Version de PHP : 8.5.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `eval1_goncourt`
--

-- --------------------------------------------------------

--
-- Structure de la table `ballot`
--

CREATE TABLE `ballot` (
  `id_ballot` bigint(20) NOT NULL,
  `fk_id_election` smallint(5) UNSIGNED NOT NULL,
  `date_ballot` date NOT NULL,
  `fk_id_entity_who_choose` bigint(20) UNSIGNED NOT NULL,
  `fk_id_entity_chosen` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `election`
--

CREATE TABLE `election` (
  `id_election` smallint(5) UNSIGNED NOT NULL,
  `fk_id_jury` int(11) NOT NULL,
  `nb_candidates` smallint(6) NOT NULL,
  `name_election` varchar(80) NOT NULL,
  `date_election` date NOT NULL,
  `degree_election` varchar(50) NOT NULL,
  `done` tinyint(1) NOT NULL,
  `fk_id_winner` bigint(20) UNSIGNED DEFAULT NULL,
  `final` tinyint(1) NOT NULL,
  `modality` varchar(50) DEFAULT NULL,
  `fk_id_election_mother` smallint(5) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `entity`
--

CREATE TABLE `entity` (
  `id_entity` bigint(20) UNSIGNED NOT NULL,
  `ISBN` bigint(20) DEFAULT NULL,
  `price` decimal(15,2) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `type` varchar(50) NOT NULL,
  `resume` longtext DEFAULT NULL,
  `creation_date` date NOT NULL,
  `nb` decimal(15,2) NOT NULL,
  `unit_nb` varchar(10) NOT NULL,
  `fk_id_entity_mother` bigint(20) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Déchargement des données de la table `entity`
--

INSERT INTO `entity` (`id_entity`, `ISBN`, `price`, `name`, `first_name`, `type`, `resume`, `creation_date`, `nb`, `unit_nb`, `fk_id_entity_mother`) VALUES
(1, 9782226511874, 21.00, 'Minotaure', NULL, 'livre', 'A 23 ans, l\'auteur s\'apprête à surprendre son père, qu\'il n\'a jamais rencontré, dans son cabinet de psychiatre. Cette rencontre survient après une quête de ce père disparu depuis sa naissance. Un récit littéraire autobiographique en hommage à la mère.', '2026-08-19', 242.00, 'pages', NULL),
(2, 9782818063583, 21.00, 'Faire la peau', NULL, 'livre', 'Je dis que l\'une des plus tenaces fictions tient tout entière dans ce mot, mère. Que la haine qui circule entre les mères et leurs filles est sauvage, et qu\'il faut la regarder droit dans les yeux.', '2026-08-20', 286.00, 'pages', NULL),
(3, 9782246846949, 24.00, 'Chronique d\'un royaume perdu', NULL, 'livre', 'Au Bouchon, petit village isolé de l’île Maurice, quatre générations se succèdent depuis le temps de l’esclavage. La violence se mêle à l’amour, la tendresse à la haine, les plus nobles passions aux vices les plus vils, les sangs des unes aux sangs des autres… Les cinq fondateurs viennent d’une plantation lointaine  : trois sont nés dans la puissante et blanche famille Dumontais  ; deux d’une esclave noire. Mais les trois blancs sont en vérité le fruit d’une passion entre Madame et le Vieux Bouc, un esclave magnétique qui revendique aussi la paternité des deux derniers. Bannis pour s’être liés d’amour et d’amitié, les cinq enfants devenus grands trouvent refuge dans ce lieu perdu dont ils font leur royaume, autarcique et magique, qu’ils défendent d’un seul corps, puisqu’ici sont abolies les frontières entre passé, présent et avenir  ; vie et mort  ; réel et fantastique. Tel homme entend sans le vouloir tous les péchés humains  ; telle femme meurt et renait en déesse protectrice  ; un enfant vit parmi les oiseaux quand son cousin viole et tue sans frein  ; le moulin est hanté par les voix des fantômes, la nature donne les plus beaux fruits mais décapite la chapelle  ; les guerres du monde contemporain rencontrent les combats intérieurs de chaque individu et l’histoire de l’humanité se reproduit dans l’infiniment petit de leurs existences débridées. Parmi eux, un enfant timide sera le chroniqueur de ce royaume hors-norme dont il livre les jours de paix, de luttes, et les nuits de folie pour empêcher l’oubli. Épopée fabuleuse,  mythologie vibrante, fable majestueuse, cette Chronique d’un Royaume perdu est le chef d’œuvre d’Ananda Devi.', '2026-08-19', 454.00, 'pages', NULL),
(4, 9782378805975, 19.90, 'Joseph dans la nuit', NULL, 'livre', 'Voyageur épris d\'ailleurs, de stop et de liberté, Olivier est en route vers Lahore pour fêter la nouvelle année sur une plage indienne. En traversant l\'Iran, il est arrêté à Chiraz alors qu\'explose le mouvement Femme, Vie, Liberté. Accusé d\'espionnage, il reste deux ans et demi en prison. Olivier est un poète, habitué à vivre de peu, sans confort ni téléphone portable. En cellule, il mobilise tout ce qui peut lui apporter de la lumière, la poésie persane comme les chansons de Britney Spears. Derrière ses paupières, installé dans un cinéma dont il est le seul spectateur, il se projette des films. La nuit, il convoque dans ses rêves les êtres aimés. Un récit lumineux et bouleversant qui nous dit que, même dans la nuit, quelque chose en nous refusera toujours de céder. La découverte d\'un écrivain.', '2026-08-20', 256.00, 'pages', NULL),
(5, 9782226499523, 16.90, 'Une forêt', NULL, 'livre', 'Pendant les grands procès visant à éradiquer le nazisme dans la vie publique allemande, Jacob Michael Lenz, avocat et capitaine dans l\'US Army, est appelé par un tribunal pour une affaire hors du commun. Des mainates, des oiseaux parleurs, nichant dans une forêt de Brême, ont appris à chanter des hymnes nazis et les transmettent à leurs oisillons.', '2026-01-02', 112.00, 'pages', NULL),
(6, 9782080490896, 23.00, 'L\'inconnue du quai de Javel', NULL, 'livre', 'Le 6 septembre 1949, une jeune femme est retrouvée morte quai de Javel, à Paris, sans sac ni chaussures, manifestement rhabillée à la hâte puis déposée là par son assassin. Elle est identifiée le lendemain : c\'est Louise Cansot, le modèle le plus demandé par les peintres de Montparnasse. Rapidement, quatre suspects se détachent, évidents, presque des archétypes. On dirait le début d\'un roman de Simenon, mais l\'inspecteur-chef Ferrière n\'a pas le talent de Maigret, et doit se résoudre à classer l\'affaire au bout de six mois, sans avoir arrêté personne. Soixante-quinze ans plus tard, Philippe Jaenada reprend l\'enquête à partir du dossier retrouvé puis, comme à son habitude, sollicite ses contacts aux archives, exhume tous les documents, arpente tous les lieux - remonte le temps. Pour ce livre, il a lu les soixante-quinze enquêtes de Maigret, s\'inspirant humblement et fidèlement des méthodes du commissaire fictif. Et il va résoudre ce meurtre bien réel, laissant le lecteur subjugué par la dextérité de son investigation et fasciné par cette jeune femme à laquelle il redonne un visage et une histoire.', '2026-08-12', 528.00, 'pages', NULL),
(7, 9782073161925, 21.50, 'La solitude des professeurs est infinie', NULL, 'livre', 'Jean Deichel, jeune professeur de français, fait son stage dans un collège de la banlieue parisienne. La nuit, il loge dans un club de tennis à Deuil-la-Barre ; le jour, il découvre les difficultés du métier en même temps que ses joies profondes, la violence de l\'École en même temps que sa beauté. Jean est aussi un poète ivre d\'aventure, attentif à trouver la lumière de la « vraie vie » au coeur du quotidien le plus gris : dans des jardins réels ou rêvés, au bord d\'un lac, lors d\'évasions à Pompéi et à Tarquinia, mais surtout dans la grâce fragile d\'un cours réussi. Entre réalité politique et mystère existentiel, la vie des profs est un roman.', '2026-08-20', 320.00, 'pages', NULL),
(8, 9782378562953, 19.50, 'N\'efface pas mes cercles', NULL, 'livre', '1980, une femme se suicide dans un appartement cossu. Dans les années cinquante, elle s\'était unie avec un jeune homme à qui tout l\'opposait. Explorant son histoire familiale, la narratrice tente de démêler les raisons de ce drame et dresse ce faisant le portrait d\'une société aux prises avec ses démons : le patriarcat, la guerre, la colonisation, les injonctions à la réussite et au bonheur. N\'efface pas mes cercles remonte le temps à la recherche des destins brisés et restitue avec force l\'atmosphère des époques traversées. Cette saga bouleversante confirme le grand art d\'Emma Marsantes.', '2026-08-20', 160.00, 'pages', NULL),
(9, 9782707358233, 22.00, 'De l\'autre côté du lac', NULL, 'livre', 'Paola était comme ça. Elle était entière. Elle voulait toujours que tout soit vrai, les rapports humains, les discussions, les rencontres, les projets dans lesquels elle s’engageait. Elle ne supportait pas les faux-semblants, les demi-mesures. Elle était d’un bloc. Elle disait les mots ont de la valeur. Les actes ont de la valeur. Elle voulait qu’il y ait de l’enjeu. C’est dans l’inconfort qu’on se découvre, elle disait. C’est dans l’inconfort qu’on grandit. » Aux abords d’un lac de haute montagne, à la lisière d’une réserve interdite aux humains, un groupe de chercheurs s’affaire. Parmi eux, une photographe aperçoit sur un des versants quelque chose qui échappe au regard de tous les autres. Les signes étranges s’accumulent, un corps est retrouvé. La photographe décide de rester là-haut, seule.  Quelques mois plus tard, c’est elle qui, à son tour, disparaît. Avec ce roman tout en tension, Sylvain Prudhomme approfondit plusieurs thèmes qui lui sont chers : le désir d’intensité, l’appel du sauvage, le rêve d’une vie vraie', '2026-08-27', 288.00, 'pages', NULL),
(10, 9782246847069, 21.50, 'C\'était ça ou mourir', NULL, 'livre', 'Le premier roman de Thélyson Orélien est déjà le phénomène littéraire de l’année 2026. En cours de traduction dans plus d’une vingtaine de langues, C’était ça ou mourir a conquis le Québec et bientôt le monde entier, en racontant l’Odyssée de Jonas Dorléon. Après l’embrasement de son quartier de Port-au-Prince, Jonas n’emporte presque rien avec lui en quittant Haïti : un diplôme, un cahier de poèmes, la photo de sa mère. Toute une vie dans un sac plastique. Se réfugiant d’abord en République dominicaine, puis au Brésil et au Mexique, ce professeur d’histoire franchit les frontières tantôt à bord d’un autobus surchauffé, tantôt en affrontant les profondeurs de la jungle. À chaque étape des visages surgissent, des corps tombent, des solidarités se nouent puis se brisent. Dans l’espoir d’atteindre le Canada et le peu de famille qu’il lui reste, Jonas se retrouve aux portes des États-Unis, seul face aux agents de l’ICE et d’une administration prête à tout pour mener sa chasse aux migrants. Avec la trajectoire de Jonas, c’est une cartographie intime de la survie qui se dévoile. Aussi contemporain qu’universel, ce roman raconte les migrations au présent — non comme un concept, mais comme une expérience physique : marcher, avoir faim, se blesser, rire devant l’horreur pour ne pas abandonner. Thélyson Orélien y déploie une écriture foisonnante, traversée d’humour et de poésie, une langue d’exil qui s’apprend « sans grammaire, sans dictionnaire, juste avec les os et la peau ». Porté par un souffle narratif irrésistible, C’était ça ou mourir est un premier roman bouleversant qui révèle un écrivain majeur de notre temps.', '2026-08-19', 272.00, 'pages', NULL),
(11, 9782221286807, 21.00, 'Le fabuleux piano', NULL, 'livre', 'Après le succès littéraire et commercial de son récit Les Exportés , Sonia Devillers part à la recherche d\'un admirable piano à queue, volé par les nazis en 1943. Ce qu\'elle nous raconte est bouleversant, instructif, et magistralement mené. Le fabuleux piano est un instrument volé par les Allemands, en 1943, à des juifs qui le cherchent encore... Dans ce vide impossible à combler, Sonia Devillers entend une résonance intime, le souvenir d\'un instrument que sa propre grand-mère, forcée à l\'exil, a regretté toute sa vie. Elle part alors sur les traces des pianos fantômes pillés par milliers sous l\'Occupation et transportés jusqu\'aux confins du IIIe Reich. Avec cet instrument de concert ressurgit l\'incroyable destin d\'une famille d\'éditeurs de musique, les Enoch. Un siècle de partitions, des menuets de Ravel aux ritournelles de Prévert. Les nazis se sont acharnés sur les Enoch, mais ils ont échoué à les réduire au silence. Des douleurs de la guerre va naître une chanson portée par Yves Montand, Les Feuilles mortes : un triomphe mondial. Le piano disparu continue pourtant de hanter les survivants...', '2026-08-27', 288.00, 'pages', NULL),
(12, 9782073162854, 19.00, 'Choses que je croyais perdues', NULL, 'livre', ' Je voulais te dire : sans le faire exprès, j\'ai cassé le verre à moutarde Musclor que lu aimais bien. Le prince sous stéroïdes mal imprimé a perdu sa tête, mais il continue de flatter d\'une main distraite l\'encolure de son tigre vert de compagnie, Tu avais trouvé ce verre dans un vide-greniers où les gens vendaient pas cher de jolies choses. Après l\'avoir regardé longtemps, avec intensité, tu l\'avais négocié à deux euros. C\'était un souvenir d\'enfance et ta joie m\'avait attendrie. Ça allait encore entre nous à ce moment-là, enfin je crois. Seule dans son appartement, une jeune femme emballe ses affaires. Demain, des déménageurs emporteront ces traces fragiles de son existence. Elle pense à l\'homme dont elle vient de se séparer, et des histoires surgissent des objets qu\'elle manipule. Une assiette au filet d\'or, un ensemble H&M couleur poil de chameau, un rouleau de Sopalin : ces témoins d\'une vie ordinaire ont autant à raconter qu\'un trépidant roman d\'aventures... Que reste-t-il de ce que nous avons vécu ? De quelles légendes sommes-nous faits ? Les grandes amours comme les petits riens, les désillusions et les désirs sont au coeur de ce roman plein de surprises, à la fantaisie incomparable.', '2026-08-20', 176.00, 'pages', NULL),
(13, 9782862316857, 19.00, 'Bataille au procès', NULL, 'livre', 'En 1956, Georges Bataille est appelé à témoigner au procès de Jean-Jacques Pauvert, poursuivi pour avoir publié les œuvres de Sade. L’auteur d\'Histoire de l\'oeil comprend que la morale menace de mort la littérature. L’audience devient le miroir de sa propre vie. Les souvenirs affluent : enfance marquée par la folie d’un père aveugle et paralytique, l’indifférence d’une mère réfugiée dans la religion. Des événements qui ont émaillé son parcours surgissent : expériences limites dans ses amours placées sous l’égide de la transgression, visions de guerre et de sacrifice qui le hantent, traversée du mal, liens tourmentés avec le parti communiste, haine du fascisme… Réflexions et fulgurances se mêlent en un vertige où pensée et vie s’entrelacent, entre érotisme et sacré, extase et mort. Mais derrière ces éclats affleure aussi une énigme plus obscure. Refusera-t-elle de se dévoiler ?À travers cet épisode de la vie littéraire, Patrice Trigano accompagne Bataille au plus près de son vertige intérieur. Il explore ce point où l’écriture n’obéit plus à l’auteur, où l’œuvre surgit comme une puissance étrangère, excessive, qui le dépasse.Patrice Trigano a fait des études de droit et de philosophie avant de consacrer sa vie à l’art en tant que galeriste, écrivain et dramaturge. Ses livres sont publiés aux éditions de la Différence, Léo Scheer, Mercure de France et Maurice Nadeau. Il a publié en 2024, La Promesse de l’art, Mémoires d’un galeriste aux Éditions du Canoë.', '2026-08-21', 136.00, 'pages', NULL),
(14, 9782073121349, 20.00, 'La guerre éternelle : souvenirs de Troie', NULL, 'livre', '« Pour donner à ma longue rêverie la forme d\'un livre, j\'avais besoin de voir. De la terre, des pierres, des arbres, un rivage. J\'ai toujours besoin de voir. Je suis allé en Troade à la fin d\'un mois de juin, alors que les coquelicots jetaient de grandes flaques rouges au milieu des champs de blé et d\'oliviers où jadis s\'affrontaient les héros. » Il y a quelque trente-trois siècles, des guerriers grecs ravagent une cité d\'Asie Mineure qu\'ils appellent Troïa ou Ilios. Les hommes sont massacrés, les femmes traînées en esclavage. C\'était dans la nuit des temps, mais grâce à l\'Iliade cela vit toujours dans notre mémoire. C\'était, aussi bien, hier, aujourd\'hui, demain : la tragédie de la destruction d\'une ville n\'a cessé d\'être réécrite en lettres de feu et de sang, depuis Carthage un siècle et demi avant notre ère jusqu\'à Dresde et Hiroshima, Marioupol et Gaza de nos jours. La guerre de Troie est éternelle, et Troie est la Mère de toutes les villes martyrisées.', '2026-08-20', 219.00, 'pages', NULL),
(15, 9782073099945, 21.00, 'Je', NULL, 'livre', '« - Que savez-vous de la beauté, Antoinette ? Il se tourna vers moi, suspendu à ma réponse. - Pas grand-chose. Mais je sais la reconnaître quand elle est là. - Eh bien moi, chaque fois que je la vois, elle me blesse. Quand je vois votre visage, par exemple, quelque chose en moi se trouve comme ébranlé. » île de la Jamaïque, 1831. Antoinette Cosway, créole de bonne famille, s\'éprend d\'Edward Rochester, un Anglais aussi impénétrable que fascinant. Mais à la séduction enflammée succèdent rapidement des scènes vénéneuses, où les baisers sont des blessures, où toute une société livre la jeune femme à son bourreau. Des années plus tard, Antoinette tente de conquérir sa propre histoire. JE se situe à mi-chemin entre roman victorien et thriller intimiste contemporain. Lilia Hassaine s\'est inspirée du personnage de la première femme de Rochester dans Jane Eyre, le roman culte de Charlotte Brontë. Elle a choisi de lui donner une voix, un corps, une destinée.', '2026-08-20', 248.00, 'pages', NULL),
(16, 9782330225575, 20.00, 'Nous aussi', NULL, 'livre', 'On fait partie d\'une grande famille. On sait qu\'on est privilégiés. On vit ensemble, dans notre immeuble au centre de Paris, on se retrouve l\'été dans notre maison à la montagne. On trouve que c\'est normal. C\'est chez nous, c\'est à nous, c\'est pour nous. On se ressemble, on se compare, on se confronte, on ne se quitte pas, on se confond, on s\'appartient. On ne sait pas comment dire je, on n\'en a pas besoin, puisqu\'on est nous. Nous les enfants, les frères et soeurs, les cousins, les cousines, on partage tout, nos écoles, nos chambres, nos habits, nos repas, nos jeux, nos bains, nos lits. On est les membres indissociables du grand corps familial. On n\'a jamais vécu dehors. On ne sait pas ce que c\'est. On n\'en est pas capables. On n\'en a même pas envie. Et tout aurait dû continuer ainsi, dans un même immuable recommencement. Le jour où la façade s\'est fissurée, on n\'a pas compris. Ça n\'aurait pas dû se produire, pas dans notre famille. Ce n\'était pas possible que ça nous arrive, à nous aussi.', '2026-08-19', 237.00, 'pages', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `entity_election`
--

CREATE TABLE `entity_election` (
  `fk_id_entity` bigint(20) UNSIGNED NOT NULL,
  `fk_id_election` smallint(5) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `identity`
--

CREATE TABLE `identity` (
  `id_identity` bigint(20) UNSIGNED NOT NULL,
  `appelation` varchar(100) NOT NULL,
  `under_appelation` varchar(80) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `fk_id_identity_mother` bigint(20) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Déchargement des données de la table `identity`
--

INSERT INTO `identity` (`id_identity`, `appelation`, `under_appelation`, `description`, `address`, `fk_id_identity_mother`) VALUES
(1, 'Académie Goncourt', NULL, 'Académie littéraire française chargée notamment de décerner le prix Goncourt.', NULL, NULL),
(2, 'Prix Goncourt', NULL, 'Prix littéraire français créé en 1903 et décerné chaque année par l\'Académie Goncourt.', NULL, NULL),
(3, 'Decoin', 'Didier', 'Écrivain et scénariste. Entre à l’Académie Goncourt le 6 juin 1995, succédant à Jean Cayrol au 3ème couvert. Après en avoir été le Secrétaire général, il est Président de la Société littéraire du 20 janvier 2020 au 13 mai 2024.', NULL, NULL),
(4, 'Chandernagor', 'Françoise', 'Écrivaine. Ancien membre du Conseil d\'État. Entre à l’Académie Goncourt le 6 juin 1995, succédant à Emmanuel Roblès au 8ème couvert. Elle en est la Vice-Présidente.', NULL, NULL),
(5, 'Ben Jelloun', 'Tahar', 'Écrivain, poète et peintre. Entre à l’Académie Goncourt le 6 mai 2008, succédant à François Nourissier au 6ème couvert.', NULL, NULL),
(6, 'Constant', 'Paule', 'Écrivaine. Entre à l’Académie Goncourt le 8 janvier 2013, succédant à Robert Sabatier au 4ème couvert.', NULL, NULL),
(7, 'Claudel', 'Philippe', 'Écrivain, réalisateur et dramaturge. Entre à l’Académie Goncourt le 11 janvier 2012, succédant à Jorge Semprun au 9ème couvert. Après en avoir été le Trésorier, puis Secrétaire général, il est élu Président de la Société littéraire le 13 mai 2024.', NULL, NULL),
(8, 'Assouline', 'Pierre', 'Écrivain et journaliste. Entre à l’Académie Goncourt le 11 janvier 2012, succédant à Françoise Mallet-Joris au 10ème couvert.', NULL, NULL),
(9, 'Schmitt', 'Eric-Emmanuel', 'Dramaturge, philosophe et écrivain. Entre à l’Académie Goncourt le 5 janvier 2016, succédant à Edmonde Charles-Roux au 2ème couvert. Élu trésorier le 6 mai 2025.', NULL, NULL),
(10, 'Laurens', 'Camille', 'Écrivaine. Entre à l’Académie Goncourt le 11 février 2020, succédant à Virginie Despentes au 7ème couvert. Élue secrétaire générale le 13 mai 2024.', NULL, NULL),
(11, 'Bruckner', 'Pascal', 'Romancier, philosophe et essayiste. Entre à l’Académie Goncourt le 11 février 2020, succédant à Bernard Pivot au 1er couvert.', NULL, NULL),
(12, 'Angot', 'Christine', 'Écrivaine. Entre à l’Académie Goncourt le 28 février 2023, succédant à Patrick Rambaud au 5ème couvert.', NULL, NULL),
(13, 'Bergmann', 'Boris', 'Boris Bergmann est né à Paris en 1992. Il est l\'auteur de cinq romans dont Nage Libre (prix de la Vocation 2018) et Les Corps insurgés (Prix Fénéon 2020). Il a été pensionnaire de la Villa Medicis et de la Villa Kujoyama. Il a organisé des expositions en France et à l\'étranger (autour de l\'oeuvre de René Daumal, notamment) et collabore en tant qu\'éditeur associé à la revue d\'art et de littérature Magma. Minotaure est son premier roman autobiographique.', NULL, NULL),
(14, 'Chennevière', 'Louise', 'Autrice, chanteuse et musicienne française née en 1993.', NULL, NULL),
(15, 'Devi', 'Ananda', 'Née à l\'île Maurice, Ananda Devi est l\'autrice d\'une oeuvre récompensée par de nombreux prix et traduite en une douzaine de langues. Parmi ses livres les plus marquants, on peut citer Ève de ses décombres (Gallimard, 2006, prix des Cinq Continents, prix RFO, prix Télévision Suisse Romande), Le Sari vert (Gallimard 2009, prix Louis Guilloux), Le Rire des déesses (Grasset, 2021, prix Femina des lycéens) et Le Jour des caméléons (Grasset, 2023, prix de la Langue française). Elle a reçu le prestigieux prix américain Neustadt 2024 pour l\'ensemble de son oeuvre.', NULL, NULL),
(16, 'Devillers', 'Sonia', 'Sonia Devillers est journaliste dans la matinale de France Inter et présentatrice du « Dessous des images » sur Arte. Son premier livre, Les Exportés (Flammarion, 2022), raconte comment sa famille a fui la Roumanie communiste.', NULL, NULL),
(17, 'Godard', 'Anne', 'Anne Godard est née à Paris en 1971, elle enseigne la littérature et l\'écriture créative à l\'université Sorbonne-Nouvelle. Elle a publié aux Éditions de Minuit L\'Inconsolable en 2006 (prix RTL-Lire) et Une chance folle en 2017 (prix Alain Spiess du deuxième roman). Nous aussi est son troisième roman.', NULL, NULL),
(18, 'Grondeau', 'Olivier', 'Après des études littéraires et des emplois de libraire, Olivier Grondeau est parti huit ans sur les routes, avant d\'être arrêté en Iran. Libéré en mars 2025, il poursuit désormais des études d\'anthropologie. L\'écriture l\'a toujours accompagné. Joseph dans la nuit est son premier livre.', NULL, NULL),
(19, 'Haenel', 'Yannick', 'Yannick Haenel a notamment publié Cercle (prix Décembre 2007 et prix Roger Nimier 2008), Jan Karski (prix Interallié et prix du Roman Fnac 2009) et Tiens ferme ta couronne (prix Médicis 2017).', NULL, NULL),
(20, 'Hassaine', 'Lilia', 'Lilia Hassaine est notamment l\'autrice de Panorama (2023, prix Renaudot des lycéens). JEest son quatrième roman.', NULL, NULL),
(21, 'Jaenada', 'Philippe', 'Philippe Jaenada est l\'auteur d\'une douzaine de romans, dont Le Chameau sauvage (Julliard, 1997, prix de Flore), La Petite Femelle (2015) et La Serpe (2017, prix Femina) et plus récemment, chez Mialet-Barrault Éditeurs, Au printemps des monstres et La désinvolture est une bien belle chose (2021 et 2024). Il rejoint en cette rentrée littéraire les Éditions Flammarion.', NULL, NULL),
(22, 'Jouannais', 'Jean-Yves', 'Jean-Yves Jouannais, né en 1964, est professeur à l\'École nationale supérieure des beaux-arts de Paris. Il a publié, notamment, L\'Idiotie (Beaux-Arts livres), Artistes sans oeuvres (Verticales), Les Barrages de sable (Grasset). De 2008 à 2024, il est l\'auteur du cycle de conférences-performances, L\'Encyclopédie des guerres, au Centre Pompidou (Paris).', NULL, NULL),
(23, 'Marsantes', 'Emma', 'Écrivaine française.', NULL, NULL),
(24, 'Mélois', 'Clémentine', 'Clémentine Mélois est née en 1980. Elle est notamment l\'autrice, aux Editions Grasset, de Cent titres. Sinon j\'oublie, Dehors, la tempête, ainsi que du très remarqué Alors c\'est bien (« L\'Arbalète », Editions Gallimard, 2024).', NULL, NULL),
(25, 'Orélien', 'Thélyson', 'Né en 1988, Thélyson Orélien est un auteur québécois d\'origine haïtienne. Poète et critique, il construit une oeuvre habitée par la mémoire, l\'exil et la question de l\'appartenance. Depuis sa publication au Québec par les Éditions du Boréal, C\'était ça ou mourir rencontre un écho international exceptionnel et est en cours de traduction dans plus de vingt langues. Un premier roman phénomène qui révèle une grande voix de la littérature contemporaine.', NULL, NULL),
(26, 'Prudhomme', 'Sylvain', 'Sylvain Prudhomme est l\'auteur de romans, récits et reportages salués par la critique et traduits à l\'étranger. Il a reçu le prix Femina en 2019 pour Par les routes. L\'Enfant dans le taxi a paru en 2023 aux Éditions de Minuit. Coyote, récit d\'un voyage le long de la frontière américano-mexicaine, a reçu le prix Nicolas Bouvier 2025.', NULL, NULL),
(27, 'Rolin', 'Olivier', 'Écrivain français, auteur notamment de romans, récits et essais.', NULL, NULL),
(28, 'Trigano', 'Patrice', 'Écrivain et galeriste français.', NULL, NULL),
(29, 'Albin Michel', NULL, 'Maison d\'édition française.', '22 rue Huyghens 75014 Paris', NULL),
(30, 'P.O.L', NULL, 'Maison d\'édition française spécialisée notamment dans la littérature contemporaine.', '33 rue Saint-André-des-Arts 75006 Paris', NULL),
(31, 'Grasset', NULL, 'Maison d\'édition française publiant notamment de la littérature française et étrangère.', '61 rue des Saints-Pères 75006 Paris', NULL),
(32, 'Robert Laffont', NULL, 'Maison d\'édition française du groupe Editis.', '92 avenue de France 75013 Paris', NULL),
(33, 'Actes Sud', NULL, 'Maison d\'édition française indépendante publiant notamment de la littérature.', '47 rue du Docteur Fanton 13200 Arles Cedex', NULL),
(34, 'L\'Iconoclaste', NULL, 'Maison d\'édition française publiant notamment des romans, essais et documents.', '26 rue Jacob 75006 Paris', NULL),
(35, 'Gallimard', NULL, 'Maison d\'édition française historique spécialisée notamment dans la littérature.', '5 rue Gaston Gallimard 75007 Paris', NULL),
(36, 'Flammarion', NULL, 'Maison d\'édition française publiant notamment de la littérature, des essais et des documents.', '82 rue Saint-Lazare 75009 Paris', NULL),
(37, 'Verdier', NULL, 'Maison d\'édition française indépendante.', '11220 Lagrasse', NULL),
(38, 'Minuit', NULL, 'Maison d\'édition française connue notamment pour sa littérature contemporaine.', '7 rue Bernard-Palissy 75006 Paris', NULL),
(39, 'Maurice Nadeau', NULL, 'Maison d\'édition française indépendante fondée par Maurice Nadeau.', '5 rue Malebranche 75005 Paris', NULL),
(40, 'Georges Bataille', NULL, 'Personnage principal appelé à témoigner au procès de Jean-Jacques Pauvert', NULL, NULL),
(41, 'Jean-Jacques Pauvert', NULL, 'Personnage principal poursuivi pour avoir publié les œuvres de Sade', NULL, NULL),
(42, 'Paola', NULL, 'Personnage principal photographe et artiste disparue en montagne', NULL, NULL),
(43, 'Le narrateur', NULL, 'Personnage principal, il est le double de l\'auteur. il mène l\'enquête', NULL, NULL),
(44, 'Jonas Dorléon', NULL, 'Personnage principal, il quitte Haïti. il mène l\'enquête', NULL, NULL),
(45, 'Emilie', NULL, 'Personnage principal, narratrice, elle déménage.', NULL, NULL),
(46, 'Tristan', NULL, 'Personnage principal, ex d\'Emilie.', NULL, NULL),
(47, 'Sandra', NULL, 'Personnage principal, amie d\'Emilie.', NULL, NULL),
(48, 'Mia', NULL, 'Personnage principal, elle est le double de l\'auteur. elle se replonge dans la saga familiale', NULL, NULL),
(49, 'Jean Deichel', NULL, 'Personnage principal, protagoniste jeune agrégé de lettres et professeur de français stagiaire dans un collège de banlieue parisienne', NULL, NULL),
(50, 'Anya', NULL, 'Personnage principal, tutrice de Jean au sein de l\'établissement', NULL, NULL),
(51, 'Streger', NULL, 'Personnage principal, principal de l\'établissement', NULL, NULL),
(52, 'Laguille', NULL, 'Personnage principal, adjointe du principal de l\'établissement', NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `identity_entity`
--

CREATE TABLE `identity_entity` (
  `id_identity_entity` bigint(20) UNSIGNED NOT NULL,
  `fk_id_entity` bigint(20) UNSIGNED DEFAULT NULL,
  `fk_id_identity` bigint(20) UNSIGNED DEFAULT NULL,
  `fk_id_role` smallint(5) UNSIGNED NOT NULL
) ;

--
-- Déchargement des données de la table `identity_entity`
--

INSERT INTO `identity_entity` (`id_identity_entity`, `fk_id_entity`, `fk_id_identity`, `fk_id_role`) VALUES
(1, NULL, 3, 6),
(2, NULL, 3, 19),
(3, NULL, 3, 14),
(4, NULL, 3, 15),
(5, NULL, 4, 6),
(6, NULL, 4, 23),
(7, NULL, 4, 1),
(8, NULL, 5, 6),
(9, NULL, 5, 13),
(10, NULL, 5, 10),
(11, NULL, 5, 9),
(12, NULL, 6, 6),
(13, NULL, 6, 9),
(14, NULL, 7, 6),
(15, NULL, 7, 16),
(16, NULL, 7, 3),
(17, NULL, 7, 14),
(18, NULL, 7, 22),
(19, NULL, 7, 20),
(20, NULL, 7, 9),
(21, NULL, 8, 6),
(22, NULL, 8, 7),
(23, NULL, 8, 9),
(24, NULL, 9, 3),
(25, NULL, 9, 12),
(26, NULL, 9, 6),
(27, NULL, 9, 22),
(28, NULL, 9, 9),
(29, NULL, 10, 6),
(30, NULL, 10, 20),
(31, NULL, 10, 9),
(32, NULL, 11, 18),
(33, NULL, 11, 12),
(34, NULL, 11, 5),
(35, NULL, 11, 9),
(36, NULL, 12, 6),
(37, NULL, 12, 9),
(38, 1, 13, 2),
(39, 1, 29, 4),
(40, 2, 14, 2),
(41, 2, 30, 4),
(42, 3, 15, 2),
(43, 3, 31, 4),
(44, 4, 18, 2),
(45, 4, 34, 4),
(46, 5, 22, 2),
(47, 5, 29, 4),
(48, 6, 21, 2),
(49, 6, 36, 4),
(50, 7, 19, 2),
(51, 7, 35, 4),
(52, 7, 49, 11),
(53, 7, 50, 11),
(54, 7, 51, 11),
(55, 7, 52, 11),
(56, 8, 23, 2),
(57, 8, 37, 4),
(58, 8, 48, 11),
(59, 9, 26, 2),
(60, 9, 38, 4),
(61, 9, 42, 11),
(62, 9, 43, 11),
(63, 10, 25, 2),
(64, 10, 31, 4),
(65, 10, 44, 11),
(66, 11, 16, 2),
(67, 11, 32, 4),
(68, 12, 24, 2),
(69, 12, 35, 4),
(70, 12, 45, 11),
(71, 12, 46, 11),
(72, 12, 47, 11),
(73, 13, 28, 2),
(74, 13, 39, 4),
(75, 13, 40, 11),
(76, 13, 41, 11),
(77, 14, 27, 2),
(78, 14, 35, 4),
(79, 15, 20, 2),
(80, 15, 35, 4),
(81, 16, 17, 2),
(82, 16, 33, 4);

--
-- Déclencheurs `identity_entity`
--
DELIMITER $$
CREATE TRIGGER `before_identity_entity_insert` BEFORE INSERT ON `identity_entity` FOR EACH ROW BEGIN
    IF EXISTS (
        SELECT 1
        FROM identity_entity
        WHERE fk_id_entity <=> NEW.fk_id_entity
          AND fk_id_identity <=> NEW.fk_id_identity
          AND fk_id_role = NEW.fk_id_role
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cette relation identity/entity/role existe déjà.';
    END IF;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `before_identity_entity_update` BEFORE UPDATE ON `identity_entity` FOR EACH ROW BEGIN
    IF EXISTS (
        SELECT 1
        FROM identity_entity
        WHERE fk_id_entity <=> NEW.fk_id_entity
          AND fk_id_identity <=> NEW.fk_id_identity
          AND fk_id_role = NEW.fk_id_role
          AND id_identity_entity <> NEW.id_identity_entity
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cette relation identity/entity/role existe déjà.';
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Structure de la table `identity_jury`
--

CREATE TABLE `identity_jury` (
  `fk_id_jury` int(11) NOT NULL,
  `fk_id_identity` bigint(20) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Déchargement des données de la table `identity_jury`
--

INSERT INTO `identity_jury` (`fk_id_jury`, `fk_id_identity`) VALUES
(1, 9),
(3, 9),
(1, 10),
(3, 10),
(3, 11);

-- --------------------------------------------------------

--
-- Structure de la table `jury`
--

CREATE TABLE `jury` (
  `id_jury` int(11) NOT NULL,
  `date_begin` date NOT NULL,
  `date_end` date DEFAULT NULL,
  `fk_id_identity_president` bigint(20) UNSIGNED DEFAULT NULL,
  `nb_entity` smallint(6) NOT NULL,
  `fk_id_jury_mother` int(11) DEFAULT NULL,
  `nb_entity_mode` enum('MIN','MAX','EXACT') NOT NULL DEFAULT 'EXACT'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Déchargement des données de la table `jury`
--

INSERT INTO `jury` (`id_jury`, `date_begin`, `date_end`, `fk_id_identity_president`, `nb_entity`, `fk_id_jury_mother`, `nb_entity_mode`) VALUES
(1, '2026-09-17', '2026-09-18', NULL, 2, NULL, 'EXACT'),
(3, '1998-10-09', '1998-10-10', 11, 3, NULL, 'MAX');

-- --------------------------------------------------------

--
-- Structure de la table `role`
--

CREATE TABLE `role` (
  `id_role` smallint(5) UNSIGNED NOT NULL,
  `name_role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Déchargement des données de la table `role`
--

INSERT INTO `role` (`id_role`, `name_role`) VALUES
(1, 'ancien membre du conseil d\'etat'),
(2, 'auteur'),
(3, 'dramaturge'),
(6, 'écrivain'),
(4, 'éditeur'),
(5, 'essayiste'),
(7, 'journaliste'),
(8, 'livre'),
(9, 'membre du jury'),
(10, 'peintre'),
(11, 'personnage_principal'),
(12, 'philosophe'),
(13, 'poète'),
(14, 'président'),
(15, 'président du jury'),
(16, 'réalisateur'),
(17, 'relieur'),
(18, 'romancier'),
(19, 'scénariste'),
(20, 'secrétaire général'),
(21, 'traducteur'),
(22, 'trésorier'),
(23, 'vice-président du jury');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `ballot`
--
ALTER TABLE `ballot`
  ADD PRIMARY KEY (`id_ballot`),
  ADD UNIQUE KEY `uk_ballot_election_voter` (`fk_id_election`,`fk_id_entity_who_choose`),
  ADD KEY `fk_ballot_election` (`fk_id_election`),
  ADD KEY `fk_ballot_entity_who_choose` (`fk_id_entity_who_choose`),
  ADD KEY `fk_ballot_entity_chosen` (`fk_id_entity_chosen`);

--
-- Index pour la table `election`
--
ALTER TABLE `election`
  ADD PRIMARY KEY (`id_election`),
  ADD KEY `fk_election_mother` (`fk_id_election_mother`),
  ADD KEY `fk_election_jury` (`fk_id_jury`),
  ADD KEY `fk_election_winner` (`fk_id_winner`);

--
-- Index pour la table `entity`
--
ALTER TABLE `entity`
  ADD PRIMARY KEY (`id_entity`),
  ADD UNIQUE KEY `ISBN` (`ISBN`),
  ADD KEY `idx_entity_name` (`name`),
  ADD KEY `fk_entity_mother` (`fk_id_entity_mother`);

--
-- Index pour la table `entity_election`
--
ALTER TABLE `entity_election`
  ADD PRIMARY KEY (`fk_id_entity`,`fk_id_election`),
  ADD KEY `idx_entity_election_election` (`fk_id_election`);

--
-- Index pour la table `identity`
--
ALTER TABLE `identity`
  ADD PRIMARY KEY (`id_identity`),
  ADD UNIQUE KEY `uk_identity_name` (`appelation`,`under_appelation`),
  ADD KEY `fk_identity_mother` (`fk_id_identity_mother`);

--
-- Index pour la table `identity_entity`
--
ALTER TABLE `identity_entity`
  ADD PRIMARY KEY (`id_identity_entity`),
  ADD KEY `idx_identity_entity_entity` (`fk_id_entity`),
  ADD KEY `idx_identity_entity_identity` (`fk_id_identity`),
  ADD KEY `idx_identity_entity_role` (`fk_id_role`);

--
-- Index pour la table `identity_jury`
--
ALTER TABLE `identity_jury`
  ADD PRIMARY KEY (`fk_id_jury`,`fk_id_identity`),
  ADD KEY `idx_identity_jury_identity` (`fk_id_identity`);

--
-- Index pour la table `jury`
--
ALTER TABLE `jury`
  ADD PRIMARY KEY (`id_jury`),
  ADD KEY `fk_jury_mother` (`fk_id_jury_mother`),
  ADD KEY `fk_jury_president` (`fk_id_identity_president`);

--
-- Index pour la table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id_role`),
  ADD UNIQUE KEY `uk_role_name` (`name_role`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `ballot`
--
ALTER TABLE `ballot`
  MODIFY `id_ballot` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `election`
--
ALTER TABLE `election`
  MODIFY `id_election` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `entity`
--
ALTER TABLE `entity`
  MODIFY `id_entity` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pour la table `identity`
--
ALTER TABLE `identity`
  MODIFY `id_identity` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT pour la table `identity_entity`
--
ALTER TABLE `identity_entity`
  MODIFY `id_identity_entity` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `jury`
--
ALTER TABLE `jury`
  MODIFY `id_jury` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `role`
--
ALTER TABLE `role`
  MODIFY `id_role` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `ballot`
--
ALTER TABLE `ballot`
  ADD CONSTRAINT `fk_ballot_election` FOREIGN KEY (`fk_id_election`) REFERENCES `election` (`id_election`),
  ADD CONSTRAINT `fk_ballot_entity_chosen` FOREIGN KEY (`fk_id_entity_chosen`) REFERENCES `entity` (`id_entity`),
  ADD CONSTRAINT `fk_ballot_entity_who_choose` FOREIGN KEY (`fk_id_entity_who_choose`) REFERENCES `entity` (`id_entity`);

--
-- Contraintes pour la table `election`
--
ALTER TABLE `election`
  ADD CONSTRAINT `fk_election_jury` FOREIGN KEY (`fk_id_jury`) REFERENCES `jury` (`id_jury`),
  ADD CONSTRAINT `fk_election_mother` FOREIGN KEY (`fk_id_election_mother`) REFERENCES `election` (`id_election`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_election_winner` FOREIGN KEY (`fk_id_winner`) REFERENCES `entity` (`id_entity`) ON DELETE SET NULL;

--
-- Contraintes pour la table `entity`
--
ALTER TABLE `entity`
  ADD CONSTRAINT `fk_entity_mother` FOREIGN KEY (`fk_id_entity_mother`) REFERENCES `entity` (`id_entity`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Contraintes pour la table `entity_election`
--
ALTER TABLE `entity_election`
  ADD CONSTRAINT `fk_entity_election_election` FOREIGN KEY (`fk_id_election`) REFERENCES `election` (`id_election`),
  ADD CONSTRAINT `fk_entity_election_entity` FOREIGN KEY (`fk_id_entity`) REFERENCES `entity` (`id_entity`);

--
-- Contraintes pour la table `identity`
--
ALTER TABLE `identity`
  ADD CONSTRAINT `fk_identity_mother` FOREIGN KEY (`fk_id_identity_mother`) REFERENCES `identity` (`id_identity`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Contraintes pour la table `identity_entity`
--
ALTER TABLE `identity_entity`
  ADD CONSTRAINT `fk_ie_entity` FOREIGN KEY (`fk_id_entity`) REFERENCES `entity` (`id_entity`),
  ADD CONSTRAINT `fk_ie_identity` FOREIGN KEY (`fk_id_identity`) REFERENCES `identity` (`id_identity`),
  ADD CONSTRAINT `fk_ie_role` FOREIGN KEY (`fk_id_role`) REFERENCES `role` (`id_role`);

--
-- Contraintes pour la table `identity_jury`
--
ALTER TABLE `identity_jury`
  ADD CONSTRAINT `fk_entity_jury_jury` FOREIGN KEY (`fk_id_jury`) REFERENCES `jury` (`id_jury`),
  ADD CONSTRAINT `fk_identity_jury_identity` FOREIGN KEY (`fk_id_identity`) REFERENCES `identity` (`id_identity`);

--
-- Contraintes pour la table `jury`
--
ALTER TABLE `jury`
  ADD CONSTRAINT `fk_jury_identity_president` FOREIGN KEY (`fk_id_identity_president`) REFERENCES `identity` (`id_identity`),
  ADD CONSTRAINT `fk_jury_mother` FOREIGN KEY (`fk_id_jury_mother`) REFERENCES `jury` (`id_jury`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
