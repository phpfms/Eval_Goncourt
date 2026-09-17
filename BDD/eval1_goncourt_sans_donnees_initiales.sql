-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : jeu. 17 sep. 2026 à 18:28
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

-- --------------------------------------------------------

--
-- Structure de la table `role`
--

CREATE TABLE `role` (
  `id_role` smallint(5) UNSIGNED NOT NULL,
  `name_role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

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
  MODIFY `id_entity` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `identity`
--
ALTER TABLE `identity`
  MODIFY `id_identity` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `identity_entity`
--
ALTER TABLE `identity_entity`
  MODIFY `id_identity_entity` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `jury`
--
ALTER TABLE `jury`
  MODIFY `id_jury` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `role`
--
ALTER TABLE `role`
  MODIFY `id_role` smallint(5) UNSIGNED NOT NULL AUTO_INCREMENT;

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
