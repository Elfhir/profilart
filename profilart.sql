-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Client: localhost
<<<<<<< HEAD
-- Généré le: Mer 27 Novembre 2013 à 12:03
=======
-- Généré le: Ven 22 Novembre 2013 à 21:12
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345
-- Version du serveur: 5.6.12-log
-- Version de PHP: 5.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `profilart`
--
CREATE DATABASE IF NOT EXISTS `profilart` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `profilart`;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Contenu de la table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Artist'),
(2, 'Curator'),
(3, 'Subscriber');

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
<<<<<<< HEAD
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=43 ;
=======
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=40 ;
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contenu de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add site', 6, 'add_site'),
(17, 'Can change site', 6, 'change_site'),
(18, 'Can delete site', 6, 'delete_site'),
(19, 'Can add log entry', 7, 'add_logentry'),
(20, 'Can change log entry', 7, 'change_logentry'),
(21, 'Can delete log entry', 7, 'delete_logentry'),
(28, 'Can add text type', 10, 'add_texttype'),
(29, 'Can change text type', 10, 'change_texttype'),
(30, 'Can delete text type', 10, 'delete_texttype'),
(31, 'Can add image type', 11, 'add_imagetype'),
(32, 'Can change image type', 11, 'change_imagetype'),
(33, 'Can delete image type', 11, 'delete_imagetype'),
(34, 'Can add work', 12, 'add_work'),
(35, 'Can change work', 12, 'change_work'),
(36, 'Can delete work', 12, 'delete_work'),
(37, 'Can add work type', 13, 'add_worktype'),
(38, 'Can change work type', 13, 'change_worktype'),
<<<<<<< HEAD
(39, 'Can delete work type', 13, 'delete_worktype'),
(40, 'Can add pref website', 14, 'add_prefwebsite'),
(41, 'Can change pref website', 14, 'change_prefwebsite'),
(42, 'Can delete pref website', 14, 'delete_prefwebsite');
=======
(39, 'Can delete work type', 13, 'delete_worktype');
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
<<<<<<< HEAD
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;
=======
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contenu de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
<<<<<<< HEAD
(1, 'pbkdf2_sha256$10000$0AXPx985YcYK$r56e2vOMiThro8sJoPrYbrOg6gv4l8nIuqwm5rB+ePs=', '2013-11-26 20:57:27', 1, 'admin', '', '', 'admin@profilart.com', 1, 1, '2013-11-16 12:42:40'),
(10, 'pbkdf2_sha256$10000$g6f9toVnDJIj$kNscPstk9IYggk0u+xdaY0qZUpi+PhnSUMpmKCuC4To=', '2013-11-26 21:42:55', 0, 'user', 'user', 'user', 'usernew@user.com', 0, 1, '2013-11-26 21:06:19');
=======
(1, 'pbkdf2_sha256$10000$0AXPx985YcYK$r56e2vOMiThro8sJoPrYbrOg6gv4l8nIuqwm5rB+ePs=', '2013-11-22 16:15:37', 1, 'admin', '', '', 'admin@profilart.com', 1, 1, '2013-11-16 12:42:40'),
(2, 'pbkdf2_sha256$10000$RidMxE645B6C$8U4W4iRFJ/nnyduoornMVs39hsnuueWu4UwAq7MHpMk=', '2013-11-22 17:49:04', 0, 'user', '', '', 'user@user.com', 0, 1, '2013-11-16 15:04:25');
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
<<<<<<< HEAD
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Contenu de la table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(8, 10, 1);
=======
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `buildengine_imagetype`
--

CREATE TABLE IF NOT EXISTS `buildengine_imagetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `path` varchar(200) NOT NULL,
  `weight` smallint(5) unsigned NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `date_pub` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `buildengine_imagetype_6340c63c` (`user_id`),
  KEY `buildengine_imagetype_37ef4eb4` (`content_type_id`)
<<<<<<< HEAD
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=28 ;
=======
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=27 ;
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contenu de la table `buildengine_imagetype`
--

INSERT INTO `buildengine_imagetype` (`id`, `user_id`, `path`, `weight`, `content_type_id`, `date_pub`) VALUES
<<<<<<< HEAD
(27, 10, '/static/user_media/image/average/Chrysanthemum.jpg', 0, 11, '2013-11-26 21:13:39');

-- --------------------------------------------------------

--
-- Structure de la table `buildengine_prefwebsite`
--

CREATE TABLE IF NOT EXISTS `buildengine_prefwebsite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `id_template` int(10) unsigned NOT NULL,
  `color` varchar(10) NOT NULL,
  `font_family` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `buildengine_prefwebsite_6340c63c` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Contenu de la table `buildengine_prefwebsite`
--

INSERT INTO `buildengine_prefwebsite` (`id`, `user_id`, `id_template`, `color`, `font_family`) VALUES
(3, 10, 1, '#000000', 'Arial');
=======
(26, 2, '/static/user_media/image/average/Hydrangeas.jpg', 0, 11, '2013-11-22 21:10:43');
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

-- --------------------------------------------------------

--
-- Structure de la table `buildengine_texttype`
--

CREATE TABLE IF NOT EXISTS `buildengine_texttype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(3000) NOT NULL,
  `user_id` int(11) NOT NULL,
  `weight` smallint(5) unsigned NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `date_pub` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `buildengine_texttype_6340c63c` (`user_id`),
  KEY `buildengine_texttype_37ef4eb4` (`content_type_id`)
<<<<<<< HEAD
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;
=======
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contenu de la table `buildengine_texttype`
--

INSERT INTO `buildengine_texttype` (`id`, `text`, `user_id`, `weight`, `content_type_id`, `date_pub`) VALUES
<<<<<<< HEAD
(4, 'Bonjour !', 10, 0, 10, '2013-11-26 21:06:19');
=======
(2, 'Un œil sur la toile, un œil en tête, j’éclabousse, je salis la blancheur de la toile ; des taches, des lignes, des pâtés qui feront sens à mon imagination. C’est abstrait, sans contraintes, sans formes pour ne rien figer au départ.\r\n\r\n\r\nMa main se pose à l’envi dans la couleur, ici rose-quadrillage, tensions, début d’écrit : la ligne se barre. Pinceaux-stylos, traçant, dessinant, pinceaux-brosses liquides … ce qui est tracé se délite et s’éparpille, parfois se désagrège, coule une marque, brise la couleur résidente, manque, puis le trait se ressaisit, assemble, focalise l’attention en une densité colorée, concentre, intensifie.', 2, 0, 10, '2013-11-22 17:54:36');
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
<<<<<<< HEAD
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=17 ;
=======
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contenu de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
(1, '2013-11-16 17:31:28', 1, 2, '1', 'Artist', 1, ''),
(2, '2013-11-16 17:31:35', 1, 2, '2', 'Curator', 1, ''),
(3, '2013-11-16 17:31:42', 1, 2, '3', 'Subscriber', 1, ''),
(4, '2013-11-16 17:36:05', 1, 3, '14', 'user2', 3, ''),
(5, '2013-11-16 17:37:19', 1, 3, '15', 'user2', 3, ''),
(6, '2013-11-22 16:16:15', 1, 3, '5', 'user2', 3, ''),
<<<<<<< HEAD
(7, '2013-11-22 16:16:19', 1, 3, '6', 'user3', 3, ''),
(8, '2013-11-26 20:48:38', 1, 3, '2', 'user', 2, 'Modifié password.'),
(9, '2013-11-26 20:49:13', 1, 3, '2', 'user', 2, 'Modifié password et groups.'),
(10, '2013-11-26 20:49:29', 1, 3, '2', 'user', 3, ''),
(11, '2013-11-26 20:57:36', 1, 3, '3', 'user', 3, ''),
(12, '2013-11-26 20:59:25', 1, 3, '4', 'user', 3, ''),
(13, '2013-11-26 21:01:19', 1, 3, '6', 'user', 3, ''),
(14, '2013-11-26 21:03:13', 1, 3, '7', 'user', 3, ''),
(15, '2013-11-26 21:04:02', 1, 3, '8', 'user', 3, ''),
(16, '2013-11-26 21:04:35', 1, 3, '9', 'user', 3, '');
=======
(7, '2013-11-22 16:16:19', 1, 3, '6', 'user3', 3, '');
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
<<<<<<< HEAD
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;
=======
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contenu de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'content type', 'contenttypes', 'contenttype'),
(5, 'session', 'sessions', 'session'),
(6, 'site', 'sites', 'site'),
(7, 'log entry', 'admin', 'logentry'),
(10, 'text type', 'buildengine', 'texttype'),
(11, 'image type', 'buildengine', 'imagetype'),
(12, 'work', 'work', 'work'),
<<<<<<< HEAD
(13, 'work type', 'work', 'worktype'),
(14, 'pref website', 'buildengine', 'prefwebsite');
=======
(13, 'work type', 'work', 'worktype');
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
<<<<<<< HEAD
('2vsw8wgadrew0nfhhei2gcgkiq0vkz0n', 'OTJjNzMwNGFhNmEwYTg0YTllMTM1NzdkNjNlZWUzODNlNDAxMGRkMzp7Il9hdXRoX3VzZXJfaWQiOjIsImRqYW5nb19sYW5ndWFnZSI6ImZyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2013-12-10 14:42:57'),
('3v7wkl750kqyl1to76eji54d7mrtzy8q', 'NzNmNzE0NzhjNWJiMjY0NWNlMzgzOWNlYTE4YjJjNjQ0MDhkNDllMDp7fQ==', '2013-12-10 21:01:25'),
('549hmwxzw3m6cc7ph736o1tp0edl4n6t', 'NzNmNzE0NzhjNWJiMjY0NWNlMzgzOWNlYTE4YjJjNjQ0MDhkNDllMDp7fQ==', '2013-11-30 15:50:33'),
('htzgqln3wkd45xxhsdamry6wlock795g', 'NzNmNzE0NzhjNWJiMjY0NWNlMzgzOWNlYTE4YjJjNjQ0MDhkNDllMDp7fQ==', '2013-12-10 21:18:54'),
('lpgb91ljmc3m7flcim1xuc8xjmriu597', 'NzNmNzE0NzhjNWJiMjY0NWNlMzgzOWNlYTE4YjJjNjQ0MDhkNDllMDp7fQ==', '2013-11-30 18:58:31'),
('xydb6hbiqy2ehsdhsdqxepclsdd6zhja', 'NzNmNzE0NzhjNWJiMjY0NWNlMzgzOWNlYTE4YjJjNjQ0MDhkNDllMDp7fQ==', '2013-12-10 21:43:25'),
=======
('0dsxy7pwffmzcv0i6i03la7b85v98e2c', 'NjdhZmMyNWJiODNkYmE1ODBiNWZkMWY4ZGY2ZThmYmNmYjY4MGUxYjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2013-12-06 17:49:04'),
('549hmwxzw3m6cc7ph736o1tp0edl4n6t', 'NzNmNzE0NzhjNWJiMjY0NWNlMzgzOWNlYTE4YjJjNjQ0MDhkNDllMDp7fQ==', '2013-11-30 15:50:33'),
('lpgb91ljmc3m7flcim1xuc8xjmriu597', 'NzNmNzE0NzhjNWJiMjY0NWNlMzgzOWNlYTE4YjJjNjQ0MDhkNDllMDp7fQ==', '2013-11-30 18:58:31'),
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345
('yntsoevyjabynx61b5ivrgbtuvf65zyd', 'NjdhZmMyNWJiODNkYmE1ODBiNWZkMWY4ZGY2ZThmYmNmYjY4MGUxYjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=', '2013-12-03 23:02:57');

-- --------------------------------------------------------

--
-- Structure de la table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Contenu de la table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Structure de la table `work_work`
--

CREATE TABLE IF NOT EXISTS `work_work` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `text` varchar(2000) NOT NULL,
  `user_id` int(11) NOT NULL,
  `imagepath` varchar(200) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `date_pub` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `work_work_6340c63c` (`user_id`),
  KEY `work_work_37ef4eb4` (`content_type_id`)
<<<<<<< HEAD
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;
=======
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contenu de la table `work_work`
--

INSERT INTO `work_work` (`id`, `name`, `text`, `user_id`, `imagepath`, `content_type_id`, `date_pub`) VALUES
<<<<<<< HEAD
(12, 'essai', 'fleur', 10, '/static/user_media/image/average/Hydrangeas.jpg', 12, '2013-11-26 21:14:04');
=======
(11, 'Jolie méduse', 'Ma Méduse très jolie et étrange dans la mer.', 2, '/static/user_media/image/average/Jellyfish.jpg', 12, '2013-11-22 16:17:20');
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

-- --------------------------------------------------------

--
-- Structure de la table `work_worktype`
--

CREATE TABLE IF NOT EXISTS `work_worktype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idType` smallint(5) unsigned NOT NULL,
  `idWork_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `work_worktype_b6d70940` (`idWork_id`)
<<<<<<< HEAD
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;
=======
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contenu de la table `work_worktype`
--

INSERT INTO `work_worktype` (`id`, `idType`, `idWork_id`) VALUES
<<<<<<< HEAD
(9, 1, 12),
(10, 3, 12);
=======
(8, 1, 11);
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `buildengine_imagetype`
--
ALTER TABLE `buildengine_imagetype`
<<<<<<< HEAD
  ADD CONSTRAINT `content_type_id_refs_id_62e719be` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_a7650a7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `buildengine_prefwebsite`
--
ALTER TABLE `buildengine_prefwebsite`
  ADD CONSTRAINT `user_id_refs_id_68376e43` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
=======
  ADD CONSTRAINT `user_id_refs_id_a7650a7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `content_type_id_refs_id_62e719be` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contraintes pour la table `buildengine_texttype`
--
ALTER TABLE `buildengine_texttype`
<<<<<<< HEAD
  ADD CONSTRAINT `content_type_id_refs_id_866b7f87` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_4848f933` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
=======
  ADD CONSTRAINT `user_id_refs_id_4848f933` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `content_type_id_refs_id_866b7f87` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `work_work`
--
ALTER TABLE `work_work`
<<<<<<< HEAD
  ADD CONSTRAINT `content_type_id_refs_id_c5a6b53f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_8d0f6783` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
=======
  ADD CONSTRAINT `user_id_refs_id_8d0f6783` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `content_type_id_refs_id_c5a6b53f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
>>>>>>> 3f6fefa60771d0f050fbc0a4d44bfdf8d978f345

--
-- Contraintes pour la table `work_worktype`
--
ALTER TABLE `work_worktype`
  ADD CONSTRAINT `idWork_id_refs_id_d6ae5db4` FOREIGN KEY (`idWork_id`) REFERENCES `work_work` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
