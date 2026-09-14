-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : lun. 14 sep. 2026 à 15:36
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
-- Structure de la table `election`
--

CREATE TABLE `election` (
  `id_election` smallint(6) NOT NULL,
  `fk_id_jury` int(11) NOT NULL,
  `nb_candidates` smallint(6) NOT NULL,
  `name_election` varchar(80) NOT NULL,
  `date_election` date NOT NULL,
  `degree_election` varchar(50) NOT NULL,
  `done` tinyint(1) NOT NULL,
  `fk_id_winner` bigint(20) DEFAULT NULL,
  `final` tinyint(1) NOT NULL,
  `modality` varchar(50) DEFAULT NULL,
  `fk_id_election_mother` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `entity`
--

CREATE TABLE `entity` (
  `id_entity` bigint(20) NOT NULL,
  `ISBN` bigint(20) DEFAULT NULL,
  `price` decimal(15,2) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `type` varchar(50) NOT NULL,
  `resume` longtext DEFAULT NULL,
  `creation_date` date NOT NULL,
  `nb` decimal(15,2) NOT NULL,
  `unit_nb` varchar(10) NOT NULL,
  `fk_id_entity_mother` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `jury`
--

CREATE TABLE `jury` (
  `id_jury` int(11) NOT NULL,
  `date_begin` date NOT NULL,
  `date_end` date DEFAULT NULL,
  `fk_id_entity_president` bigint(20) DEFAULT NULL,
  `nb_entity` smallint(6) NOT NULL,
  `fk_id_jury_mother` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `election`
--
ALTER TABLE `election`
  ADD PRIMARY KEY (`id_election`);

--
-- Index pour la table `entity`
--
ALTER TABLE `entity`
  ADD PRIMARY KEY (`id_entity`),
  ADD UNIQUE KEY `type` (`type`),
  ADD UNIQUE KEY `unit_nb` (`unit_nb`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `ISBN` (`ISBN`);

--
-- Index pour la table `jury`
--
ALTER TABLE `jury`
  ADD PRIMARY KEY (`id_jury`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
