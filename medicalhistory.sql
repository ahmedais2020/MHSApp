-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 30, 2020 at 02:22 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medicalhistory`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add analyst', 7, 'add_analyst'),
(26, 'Can change analyst', 7, 'change_analyst'),
(27, 'Can delete analyst', 7, 'delete_analyst'),
(28, 'Can view analyst', 7, 'view_analyst'),
(29, 'Can add citizen', 8, 'add_citizen'),
(30, 'Can change citizen', 8, 'change_citizen'),
(31, 'Can delete citizen', 8, 'delete_citizen'),
(32, 'Can view citizen', 8, 'view_citizen'),
(33, 'Can add doctor', 9, 'add_doctor'),
(34, 'Can change doctor', 9, 'change_doctor'),
(35, 'Can delete doctor', 9, 'delete_doctor'),
(36, 'Can view doctor', 9, 'view_doctor'),
(37, 'Can add health ministry license center', 10, 'add_healthministrylicensecenter'),
(38, 'Can change health ministry license center', 10, 'change_healthministrylicensecenter'),
(39, 'Can delete health ministry license center', 10, 'delete_healthministrylicensecenter'),
(40, 'Can view health ministry license center', 10, 'view_healthministrylicensecenter'),
(41, 'Can add health ministry license lab', 11, 'add_healthministrylicenselab'),
(42, 'Can change health ministry license lab', 11, 'change_healthministrylicenselab'),
(43, 'Can delete health ministry license lab', 11, 'delete_healthministrylicenselab'),
(44, 'Can view health ministry license lab', 11, 'view_healthministrylicenselab'),
(45, 'Can add laboratory', 12, 'add_laboratory'),
(46, 'Can change laboratory', 12, 'change_laboratory'),
(47, 'Can delete laboratory', 12, 'delete_laboratory'),
(48, 'Can view laboratory', 12, 'view_laboratory'),
(49, 'Can add medical analyst license', 13, 'add_medicalanalystlicense'),
(50, 'Can change medical analyst license', 13, 'change_medicalanalystlicense'),
(51, 'Can delete medical analyst license', 13, 'delete_medicalanalystlicense'),
(52, 'Can view medical analyst license', 13, 'view_medicalanalystlicense'),
(53, 'Can add medical center', 14, 'add_medicalcenter'),
(54, 'Can change medical center', 14, 'change_medicalcenter'),
(55, 'Can delete medical center', 14, 'delete_medicalcenter'),
(56, 'Can view medical center', 14, 'view_medicalcenter'),
(57, 'Can add medical syndicate license', 15, 'add_medicalsyndicatelicense'),
(58, 'Can change medical syndicate license', 15, 'change_medicalsyndicatelicense'),
(59, 'Can delete medical syndicate license', 15, 'delete_medicalsyndicatelicense'),
(60, 'Can view medical syndicate license', 15, 'view_medicalsyndicatelicense'),
(61, 'Can add test', 16, 'add_test'),
(62, 'Can change test', 16, 'change_test'),
(63, 'Can delete test', 16, 'delete_test'),
(64, 'Can view test', 16, 'view_test'),
(65, 'Can add person medical center', 17, 'add_personmedicalcenter'),
(66, 'Can change person medical center', 17, 'change_personmedicalcenter'),
(67, 'Can delete person medical center', 17, 'delete_personmedicalcenter'),
(68, 'Can view person medical center', 17, 'view_personmedicalcenter'),
(69, 'Can add person lab', 18, 'add_personlab'),
(70, 'Can change person lab', 18, 'change_personlab'),
(71, 'Can delete person lab', 18, 'delete_personlab'),
(72, 'Can view person lab', 18, 'view_personlab'),
(73, 'Can add personal data', 19, 'add_personaldata'),
(74, 'Can change personal data', 19, 'change_personaldata'),
(75, 'Can delete personal data', 19, 'delete_personaldata'),
(76, 'Can view personal data', 19, 'view_personaldata'),
(77, 'Can add medical history', 20, 'add_medicalhistory'),
(78, 'Can change medical history', 20, 'change_medicalhistory'),
(79, 'Can delete medical history', 20, 'delete_medicalhistory'),
(80, 'Can view medical history', 20, 'view_medicalhistory'),
(81, 'Can add doc work on center history', 21, 'add_docworkoncenterhistory'),
(82, 'Can change doc work on center history', 21, 'change_docworkoncenterhistory'),
(83, 'Can delete doc work on center history', 21, 'delete_docworkoncenterhistory'),
(84, 'Can view doc work on center history', 21, 'view_docworkoncenterhistory'),
(85, 'Can add doc work on center', 22, 'add_docworkoncenter'),
(86, 'Can change doc work on center', 22, 'change_docworkoncenter'),
(87, 'Can delete doc work on center', 22, 'delete_docworkoncenter'),
(88, 'Can view doc work on center', 22, 'view_docworkoncenter'),
(89, 'Can add doctor person', 23, 'add_doctorperson'),
(90, 'Can change doctor person', 23, 'change_doctorperson'),
(91, 'Can delete doctor person', 23, 'delete_doctorperson'),
(92, 'Can view doctor person', 23, 'view_doctorperson'),
(93, 'Can add analyst work on lab', 24, 'add_analystworkonlab'),
(94, 'Can change analyst work on lab', 24, 'change_analystworkonlab'),
(95, 'Can delete analyst work on lab', 24, 'delete_analystworkonlab'),
(96, 'Can view analyst work on lab', 24, 'view_analystworkonlab'),
(97, 'Can add analyst lab history', 25, 'add_analystlabhistory'),
(98, 'Can change analyst lab history', 25, 'change_analystlabhistory'),
(99, 'Can delete analyst lab history', 25, 'delete_analystlabhistory'),
(100, 'Can view analyst lab history', 25, 'view_analystlabhistory');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$180000$GUPgau6IawEn$lF0IqsnJUZqYmVn6pNIc/Hy3dWsHMVCt24ZUErAiw5Y=', '2020-08-30 00:39:29.139750', 1, 'ahmedais', 'Ahmed', 'Ibrahim', 'engahmedibrahim780@gmail.com', 1, 1, '2020-08-08 00:38:58.000000'),
(2, 'pbkdf2_sha256$180000$eObhMVg9culD$tMmjfrmzyQtOA5yvB7s91X5I89PT2Hi9DZF8jdnq0rA=', NULL, 1, 'osama', '', '', 'osama@gmail.com', 1, 1, '2020-08-08 01:52:41.887170'),
(3, 'pbkdf2_sha256$180000$zw2zPZKm9Uob$04n43UZTKuuezzh2BRqHOrgSnE3kdjpnD2+2qFpVp9Y=', '2020-08-30 01:52:37.827395', 1, 'Dr.Tarek', 'Tarek Ali', 'Ali', '', 1, 1, '2020-08-20 23:35:21.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-08-08 01:33:22.029721', '254', 'Doctor object (254)', 2, '[{\"changed\": {\"fields\": [\"DoctorNationalId\"]}}]', 9, 1),
(2, '2020-08-08 01:35:20.055774', '1', 'PersonMedicalCenter object (1)', 1, '[{\"added\": {}}]', 17, 1),
(3, '2020-08-08 01:35:44.016402', '1', 'PersonLab object (1)', 1, '[{\"added\": {}}]', 18, 1),
(4, '2020-08-08 01:35:47.651251', '1', 'PersonLab object (1)', 2, '[]', 18, 1),
(5, '2020-08-14 00:13:17.516883', '16', 'AnalystLabHistory object (16)', 3, '', 25, 1),
(6, '2020-08-20 23:35:22.461993', '3', 'Dr.Tarek', 1, '[{\"added\": {}}]', 4, 1),
(7, '2020-08-20 23:35:47.548592', '3', 'Dr.Tarek', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\"]}}]', 4, 1),
(8, '2020-08-20 23:39:19.148428', '3', 'Dr.Tarek', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]', 4, 1),
(9, '2020-08-20 23:40:20.222591', '1', 'ahmedais', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'website', 'analyst'),
(25, 'website', 'analystlabhistory'),
(24, 'website', 'analystworkonlab'),
(8, 'website', 'citizen'),
(9, 'website', 'doctor'),
(23, 'website', 'doctorperson'),
(22, 'website', 'docworkoncenter'),
(21, 'website', 'docworkoncenterhistory'),
(10, 'website', 'healthministrylicensecenter'),
(11, 'website', 'healthministrylicenselab'),
(12, 'website', 'laboratory'),
(13, 'website', 'medicalanalystlicense'),
(14, 'website', 'medicalcenter'),
(20, 'website', 'medicalhistory'),
(15, 'website', 'medicalsyndicatelicense'),
(19, 'website', 'personaldata'),
(18, 'website', 'personlab'),
(17, 'website', 'personmedicalcenter'),
(16, 'website', 'test');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-07-18 02:56:32.677859'),
(2, 'auth', '0001_initial', '2020-07-18 02:56:33.153110'),
(3, 'admin', '0001_initial', '2020-07-18 02:56:34.250853'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-07-18 02:56:34.536503'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-07-18 02:56:34.550465'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-07-18 02:56:34.682704'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-07-18 02:56:34.822189'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-07-18 02:56:34.866708'),
(9, 'auth', '0004_alter_user_username_opts', '2020-07-18 02:56:34.881399'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-07-18 02:56:34.972720'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-07-18 02:56:34.979231'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-07-18 02:56:34.992083'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-07-18 02:56:35.022209'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-07-18 02:56:35.055162'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-07-18 02:56:35.087668'),
(16, 'auth', '0011_update_proxy_permissions', '2020-07-18 02:56:35.103439'),
(17, 'sessions', '0001_initial', '2020-07-18 02:56:35.180570'),
(18, 'website', '0001_initial', '2020-07-18 02:56:36.281757'),
(19, 'website', '0002_auto_20200723_2001', '2020-07-23 20:01:53.516883'),
(20, 'website', '0003_auto_20200724_0150', '2020-07-24 01:50:31.987088'),
(21, 'website', '0004_auto_20200724_0207', '2020-07-24 02:07:22.229926'),
(22, 'website', '0005_auto_20200725_1240', '2020-07-25 12:40:54.059460'),
(23, 'website', '0006_auto_20200725_1242', '2020-07-25 12:42:45.212496'),
(24, 'website', '0007_auto_20200726_2231', '2020-07-26 22:31:49.733549'),
(25, 'website', '0008_medicalhistory_doctorname', '2020-07-26 23:07:50.340779'),
(26, 'website', '0009_auto_20200727_2141', '2020-07-27 21:41:54.259760'),
(27, 'website', '0010_auto_20200727_2141', '2020-07-27 21:41:54.398289'),
(28, 'website', '0011_auto_20200728_0247', '2020-07-28 02:47:23.957560'),
(29, 'website', '0012_auto_20200728_0505', '2020-07-28 05:06:06.111820'),
(30, 'website', '0013_auto_20200728_0626', '2020-07-28 06:26:15.102932'),
(31, 'website', '0014_auto_20200728_2330', '2020-07-28 23:30:56.564989'),
(32, 'website', '0015_doctor_doctornationalid', '2020-07-28 23:39:56.861648'),
(33, 'website', '0016_auto_20200728_2346', '2020-07-28 23:46:51.506429'),
(34, 'website', '0017_auto_20200728_2348', '2020-07-28 23:48:40.993622'),
(35, 'website', '0018_auto_20200729_0105', '2020-07-29 01:05:44.399022'),
(36, 'website', '0019_auto_20200729_0156', '2020-07-29 01:56:51.499479'),
(37, 'website', '0020_auto_20200729_0218', '2020-07-29 02:18:07.195311'),
(38, 'website', '0021_auto_20200730_0216', '2020-07-30 02:16:46.325039'),
(39, 'website', '0022_medicalhistory_passportno', '2020-07-30 16:54:23.365271'),
(40, 'website', '0023_auto_20200802_2000', '2020-08-02 20:00:47.785679'),
(41, 'website', '0024_auto_20200803_0423', '2020-08-03 04:23:17.038673'),
(42, 'website', '0025_auto_20200803_0425', '2020-08-03 04:25:13.035564'),
(43, 'website', '0026_auto_20200803_1844', '2020-08-03 18:45:00.923177'),
(44, 'website', '0027_auto_20200803_1849', '2020-08-03 18:49:16.960309'),
(45, 'website', '0028_auto_20200803_2016', '2020-08-03 20:16:35.276787'),
(46, 'website', '0029_auto_20200804_0503', '2020-08-04 05:03:51.916403'),
(47, 'website', '0030_remove_medicalhistory_passportno', '2020-08-04 06:35:32.860452'),
(48, 'website', '0031_remove_doctor_username', '2020-08-04 07:02:28.685122'),
(49, 'website', '0032_delete_test', '2020-08-08 01:29:55.443841');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('72k0azs7ifv14f8g4kzilb50xwbwni9l', 'MGU1MjYxNDRmMTRhZmI0MmNkNGU1NTJhMTJlNzZkYjhiZGRmMDFhZjp7IkdldERvY1N5bkNvZGVfc2UiOiIyNTIiLCJHZXREb2N0b3JOYW1lX3NlIjoiU2FmYWEgQWxpIE1vaGFtZWQiLCJHZXRTeW5kaWNhdGVDb2RlX3NlIjoyNTIsIkdldERvY3RvcklkX3NlIjoiMzAyIiwiR2V0UGF0aWVudE5hdGlvbmFsSWRfc2UiOiIzMDMifQ==', '2020-08-10 02:24:32.125614'),
('b4h8psa4cwpp2jsjlorcfm2y5hc6pnd6', 'MzRlYzc1M2NiNWE3ZjYzNmYyYjI4ZGI4NjUzNjVjODlhZTk5Y2EyMDp7IkdldENlbnRlckNvZGVfc2UiOiI1MiIsIkdldENlbnRlclBhc3NlX3NlIjoiMjIyIiwiR2V0TGFib3JhdG9yeUNvZGVfX19TRSI6IjE1MSIsIkdldExhYm9yYXRvcnlQYXNzX19fU0UiOiIxNTEiLCJHZXRBbmFseXN0X0NvZGVfc2UiOiI3MDYiLCJQYXRpZW50X05hdGlvbmFsX0lEX19zZSI6IjMxMSIsIkdldERvY1N5bkNvZGVfc2UiOiIyNTQiLCJHZXRTeW5kaWNhdGVDb2RlX1BhdGllbnRJZExvZ2luX3NlIjoiMjU0IiwiR2V0RG9jdG9yTmFtZV9zZSI6Ik5vciBFbC1EZW4gQWhtZWQiLCJHZXRTeW5kaWNhdGVDb2RlX3NlIjoyNTQsIkdldERvY3RvcklkX3NlIjoiMzA0IiwiR2V0UGF0aWVudE5hdGlvbmFsSWRfc2UiOiIzMTEiLCJQYXRpZW50RGF0YV9TU0VFIjoiMzA2IiwiR2V0TGFiQ29kZV9fX19TZSI6IjIwMyIsIkdldFBhc3Nwb3J0TnVtYmVyZV9zZSI6IjUxMSIsIkdldENpdGl6ZW5Db2RlX3NlIjoiTWFobW91ZEFobWVkIiwiR2V0UGFzc3dvcmRMb2dpbl9zZSI6IjEyMyIsIkdldEFuYWx5c3RDb2RlX3NlIjoiNzA5IiwiR2V0QW5hbHlzdENvZGVfX3NlIjoiNzA5IiwiR2V0QW5hbHlzdENvZGVfQW5hbHlzdEVkaXRfc2UiOiI3MDkiLCJHZXRTeW5kaWNhdGVDb2RlX0FkZERvY3Rvcl9zZSI6IjI1NCIsIkdldFN5bmRpY2F0ZUNvZGVfRG9jdG9yRWRpdF9zZSI6IjI1NCIsIkdldENlbnRlcl9Db2RlX3NlIjoiNTIiLCJHZXRNQ2VudGVyQ29kZV9zZSI6IjUyIiwiR2V0U3luZGljYXRlX0NvZGVfc2UiOiIyNTEiLCJHZXRMYWJvcmF0b3J5Q29kZV9zZSI6IjIwMyIsIkdldExhYm9yYXRvcnlQYXNzX3NlIjoiNTU1IiwiR2V0TGFiQ29kZV9zZSI6IjIwMyJ9', '2020-08-18 08:26:14.913843'),
('m182m2j9qshvpaik4yrqr056sehz8mit', 'NmYyYmE1ZDQ2Y2I0YjJlMTQwYjUzZjI4YzU4M2Q3MmJiOWJlZjg4NDp7IkdldENlbnRlckNvZGVfc2UiOiI1MSIsIkdldENpdGl6ZW5Db2RlX3NlIjoiQXphYW1ZYXNzZXIiLCJHZXRBbmFseXN0Q29kZV9zZSI6IjcwOSIsIkdldFN5bmRpY2F0ZUNvZGVfQWRkRG9jdG9yX3NlIjoiMjUxIiwiR2V0U3luZGljYXRlQ29kZV9Eb2N0b3JFZGl0X3NlIjoiMjUzIiwiR2V0U3luZGljYXRlQ29kZV9QYXRpZW50SWRMb2dpbl9zZSI6IjI1MiIsIkdldExhYm9yYXRvcnlDb2RlX3NlIjoiMTUzIiwiR2V0TGFib3JhdG9yeV9Db2RlX3NlIjoiMTAxMCIsIkdldEFuYWx5c3RfQ29kZV9zZSI6IjcwNyIsIkdldE1DZW50ZXJDb2RlX3NlIjoiMSIsIkdldFN5bmRpY2F0ZV9Db2RlX3NlIjoiMjUxIiwiR2V0Q2VudGVyX0NvZGVfc2UiOiI1MSIsIkdldFBhc3Nwb3J0TnVtYmVyZV9zZSI6IjQxIiwiR2V0UGFzc3dvcmRMb2dpbl9zZSI6IjEyMyIsIkdldERvY3RvcklkX1BhdGllbnRJZExvZ2luX3NlIjoiMzAyIiwiRG9jdG9yUGVyc29uYWxEYXRhX1BhdGllbnRJZExvZ2luX3NlIjoiU2FmYWEgQWxpIE1vaGFtZWQiLCJHZXRTeW5kaWNhdGVDb2RlX3NlIjoyNTIsIkdldERvY3RvcklkX3NlIjoiMzAyIiwiR2V0U3luZGljYXRlQ29kZV9BZGREb2N0b3IiOiIzMDMiLCJHZXREb2N0b3JOYW1lX3NlIjoiU2FmYWEgQWxpIE1vaGFtZWQiLCJHZXRQYXRpZW50TmF0aW9uYWxJZF9zZSI6IjMwNiIsIkdldERvY1N5bkNvZGVfc2UiOiIyNTIiLCJHZXRDZW50ZXJQYXNzZV9zZSI6IjIyMiIsIkdldExhYm9yYXRvcnlQYXNzX3NlIjoiNTU1IiwiR2V0TGFiQ29kZV9zZSI6IjIwMiIsIkdldFBhdGllbnRfTmF0aW9uYWxfSURfc2UiOiIzMTEiLCJQYXRpZW50X05hdGlvbmFsX0lEX19zZSI6IjMxMSIsIkdldEFuYWx5c3RDb2RlX0FuYWx5c3RFZGl0X3NlIjoiNzA2In0=', '2020-08-17 21:40:35.554250'),
('m86sf9fv3pjdk2k4gy34nooidswgnhjo', 'ZjA4OWFlM2NmZWEwOGM4ZDY4OTBkMWYxM2E5NmI5NmRmMTVhNGNhZjp7IkdldEFuYWx5c3RDb2RlX3NlIjoiNzA5IiwiR2V0QW5hbHlzdENvZGVfX3NlIjoiNzA5IiwiR2V0QW5hbHlzdENvZGVfQW5hbHlzdEVkaXRfc2UiOiI3MDkiLCJHZXRDaXRpemVuQ29kZV9zZSI6IlNhZmFhQWxpQWhtZWQiLCJHZXRQYXNzd29yZExvZ2luX3NlIjoiMTIzIiwiR2V0U3luZGljYXRlQ29kZV9BZGREb2N0b3Jfc2UiOiIyNTEiLCJHZXRTeW5kaWNhdGVDb2RlX0RvY3RvckVkaXRfc2UiOiIyNTEiLCJHZXREb2NTeW5Db2RlX3NlIjoiMjUyIiwiR2V0RG9jdG9yTmFtZV9zZSI6IlNhZmFhIEFsaSBNb2hhbWVkIiwiR2V0U3luZGljYXRlQ29kZV9zZSI6MjUyLCJHZXREb2N0b3JJZF9zZSI6IjMwMiIsIkdldFN5bmRpY2F0ZUNvZGVfUGF0aWVudElkTG9naW5fc2UiOiIyNTIiLCJHZXRDZW50ZXJDb2RlX3NlIjoiMSIsIkdldENlbnRlclBhc3NlX3NlIjoiMTExIn0=', '2020-08-18 01:28:35.230319'),
('q610rdkz3j85pdyvh658tz4u72igr57o', 'MGEzYWRhMWRiYjZhNjVjNzFlY2Y5OTNiMDhhNGZjOGJjZWE3Mzk2OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1MTgyNjQ5ODE2NzlhYjk4NjM2YjFjMTc5NDA1ZDg2ODNmNWFlZjE0In0=', '2020-09-13 00:39:29.261680'),
('td7imtfqpik3oy8z4vvom1se3zfktbnt', 'N2Y2YWI3MzgxNDgwYzlhZTE0MjJkN2UzNmQzNzQ1NjFjNWQzNjBlNTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhODUwNTUzMTAzNjI2OGJkOTdiYTljODEwMTU1NmVlNGYyMTk1YTZmIiwiR2V0TUNlbnRlckNvZGVfc2UiOiIyIiwiR2V0U3luZGljYXRlX0NvZGVfc2UiOiIyNTIifQ==', '2020-09-13 02:14:40.053608');

-- --------------------------------------------------------

--
-- Table structure for table `website_analyst`
--

CREATE TABLE `website_analyst` (
  `AnalystCode` bigint(20) NOT NULL,
  `UserName` varchar(50) DEFAULT NULL,
  `Password` varchar(60) NOT NULL,
  `RegisterDate` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_analyst`
--

INSERT INTO `website_analyst` (`AnalystCode`, `UserName`, `Password`, `RegisterDate`) VALUES
(706, 'Mostafa', '777', '2020-07-13 02:50:45.000000'),
(707, 'MuuhameedAlaa', '777', '2020-07-31 02:50:45.000000'),
(708, 'Mostafa Ali', '777', '2020-07-13 02:50:45.000000'),
(709, 'Safaa Ali  Ahmed', '777', '2020-08-04 06:49:25.347220');

-- --------------------------------------------------------

--
-- Table structure for table `website_analystlabhistory`
--

CREATE TABLE `website_analystlabhistory` (
  `id` int(11) NOT NULL,
  `AnalystCode` varchar(30) NOT NULL,
  `AnalystAddDate` datetime(6) NOT NULL,
  `RemoveAnalystDate` datetime(6) DEFAULT NULL,
  `LabCode_id` bigint(20) NOT NULL,
  `AnalystName` varchar(60) DEFAULT NULL,
  `AnalystNationalId` varchar(30) DEFAULT NULL,
  `Specialization1` varchar(50) DEFAULT NULL,
  `Specialization2` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_analystlabhistory`
--

INSERT INTO `website_analystlabhistory` (`id`, `AnalystCode`, `AnalystAddDate`, `RemoveAnalystDate`, `LabCode_id`, `AnalystName`, `AnalystNationalId`, `Specialization1`, `Specialization2`) VALUES
(2, '707', '2020-07-30 15:34:23.254652', NULL, 202, 'Muuhameed ussama', 'Citizen object (307)', 'Anf w Ozon', 'Bacteria'),
(3, '706', '2020-07-30 15:36:04.783089', NULL, 202, 'OmarAhmed', '306', 'Batna', 'Gra7a 3eon'),
(4, '706', '2020-07-30 20:58:02.857623', NULL, 151, 'OmarAhmed', '306', 'Batna', 'Gra7a 3eon'),
(5, '707', '2020-07-30 20:58:25.692086', NULL, 151, 'Muuhameed ussama', '307', 'Anf w Ozon', 'Bacteria'),
(6, '706', '2020-07-30 21:04:30.267034', NULL, 151, 'OmarAhmed', '306', 'دم', 'اشعة اكس'),
(7, '707', '2020-07-30 21:04:47.953419', NULL, 151, 'Muuhameed ussama', '307', 'اشعة مقطعيه', 'دوبلر'),
(8, '708', '2020-08-02 20:10:36.788982', NULL, 201, 'Mostafa Ali', '308', 'رسم قلب', 'مكروبات'),
(9, '707', '2020-08-02 20:10:51.086357', NULL, 201, 'Muuhameed ussama', '307', 'اشعة مقطعيه', 'دوبلر'),
(10, '706', '2020-08-02 20:11:05.530775', NULL, 201, 'OmarAhmed', '306', 'دم', 'اشعة اكس'),
(11, '707', '2020-08-02 20:34:27.769115', NULL, 202, 'Muuhameed ussama', '307', 'اشعة مقطعيه', 'دوبلر'),
(12, '708', '2020-08-02 20:34:44.267628', NULL, 202, 'Mostafa Ali', '308', 'رسم قلب', 'مكروبات'),
(13, '707', '2020-08-04 07:56:13.977255', NULL, 203, 'Muuhameed ussama', '307', 'اشعة مقطعيه', 'دوبلر'),
(14, '707', '2020-08-04 08:23:51.678917', NULL, 203, 'Muuhameed ussama', '307', 'اشعة مقطعيه', 'دوبلر'),
(15, '707', '2020-08-04 08:26:38.709891', NULL, 203, 'Muuhameed ussama', '307', 'اشعة مقطعيه', 'دوبلر');

-- --------------------------------------------------------

--
-- Table structure for table `website_analystworkonlab`
--

CREATE TABLE `website_analystworkonlab` (
  `id` int(11) NOT NULL,
  `WorkOnDate` datetime(6) NOT NULL,
  `AnalystCode_id` bigint(20) NOT NULL,
  `LabCode_id` bigint(20) NOT NULL,
  `AnalystName` varchar(60) DEFAULT NULL,
  `AnalystNationalId` varchar(30) DEFAULT NULL,
  `Specialization1` varchar(50) DEFAULT NULL,
  `Specialization2` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_analystworkonlab`
--

INSERT INTO `website_analystworkonlab` (`id`, `WorkOnDate`, `AnalystCode_id`, `LabCode_id`, `AnalystName`, `AnalystNationalId`, `Specialization1`, `Specialization2`) VALUES
(9, '2020-07-30 21:04:30.262047', 706, 151, 'OmarAhmed', '306', 'دم', 'اشعة اكس'),
(10, '2020-07-30 21:04:47.949431', 707, 151, 'Muuhameed ussama', '307', 'اشعة مقطعيه', 'دوبلر'),
(11, '2020-08-02 20:10:36.783007', 708, 201, 'Mostafa Ali', '308', 'رسم قلب', 'مكروبات'),
(13, '2020-08-02 20:11:05.524161', 706, 201, 'OmarAhmed', '306', 'دم', 'اشعة اكس'),
(14, '2020-08-02 20:34:27.763938', 707, 202, 'Muuhameed ussama', '307', 'اشعة مقطعيه', 'دوبلر'),
(15, '2020-08-02 20:34:44.262641', 708, 202, 'Mostafa Ali', '308', 'رسم قلب', 'مكروبات'),
(18, '2020-08-04 08:26:38.704905', 707, 203, 'Muuhameed ussama', '307', 'اشعة مقطعيه', 'دوبلر');

-- --------------------------------------------------------

--
-- Table structure for table `website_citizen`
--

CREATE TABLE `website_citizen` (
  `PerNationalId` bigint(20) NOT NULL,
  `UserName` varchar(50) DEFAULT NULL,
  `Password` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_citizen`
--

INSERT INTO `website_citizen` (`PerNationalId`, `UserName`, `Password`) VALUES
(301, 'Mostafa', 'ci2020'),
(302, 'SafaaAliMohamed', '123'),
(303, 'anasazam', '123'),
(304, 'NorEldenAhmed', '123'),
(305, 'diaaNor', '123'),
(306, 'omarahmed', '123'),
(307, 'MuuhameedUssama', '123'),
(308, 'MostafaAli', '123'),
(309, 'SafaaAliAhmed', '123'),
(310, 'AzaamYasser', '123'),
(311, 'MahmoudAhmed', '123'),
(312, 'AmalSaad', '123'),
(313, 'George', '123'),
(314, 'Noura', '123'),
(315, 'Naglaa', '123'),
(316, 'SamahAnwar ', '123'),
(317, 'AhmedMohamedAli', '123'),
(318, 'Diaa_Ahhmed', '123'),
(319, 'NehalAhmed', '123'),
(320, 'Fares', '123'),
(321, 'Gana', '123'),
(12345678912345, 'ahmedais', '123456'),
(1234567891232020, 'ahmedibrahim', 'ahmedais');

-- --------------------------------------------------------

--
-- Table structure for table `website_doctor`
--

CREATE TABLE `website_doctor` (
  `SynCode` bigint(20) NOT NULL,
  `DoctorNationalId` varchar(30) DEFAULT NULL,
  `Password` varchar(60) DEFAULT NULL,
  `Date` datetime(6) DEFAULT current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_doctor`
--

INSERT INTO `website_doctor` (`SynCode`, `DoctorNationalId`, `Password`, `Date`) VALUES
(251, '12345678912345', '666', '2020-07-09 12:41:35.359659'),
(252, '302', '666', '2020-07-09 12:53:33.881896'),
(253, '303', '666', '2020-07-09 12:58:38.494173'),
(254, '12345678912345', '666', '2020-08-04 06:56:51.700070');

-- --------------------------------------------------------

--
-- Table structure for table `website_doctorperson`
--

CREATE TABLE `website_doctorperson` (
  `id` int(11) NOT NULL,
  `CurrentTime` datetime(6) NOT NULL,
  `PerNationalId_id` bigint(20) DEFAULT NULL,
  `SynCode_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `website_docworkoncenter`
--

CREATE TABLE `website_docworkoncenter` (
  `id` bigint(20) NOT NULL,
  `WorkOnDate` datetime(6) NOT NULL,
  `CenterCode_id` bigint(20) DEFAULT NULL,
  `SynCode_id` bigint(20) DEFAULT NULL,
  `DoctorName` varchar(60) DEFAULT NULL,
  `Specialization1` varchar(50) DEFAULT NULL,
  `Specialization2` varchar(50) DEFAULT NULL,
  `DoctorNationalId` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_docworkoncenter`
--

INSERT INTO `website_docworkoncenter` (`id`, `WorkOnDate`, `CenterCode_id`, `SynCode_id`, `DoctorName`, `Specialization1`, `Specialization2`, `DoctorNationalId`) VALUES
(20, '2020-07-29 02:58:17.110225', 2, 252, 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', '302'),
(21, '2020-07-30 01:00:58.647870', 2, 253, 'anas azam', 'Geldia', 'Hasasia', '303'),
(24, '2020-07-30 20:54:42.863263', 2, 251, 'Ali Mohamed Abdelrahman', 'Batna', 'Bacteria', '301');

-- --------------------------------------------------------

--
-- Table structure for table `website_docworkoncenterhistory`
--

CREATE TABLE `website_docworkoncenterhistory` (
  `SynCode` varchar(30) NOT NULL,
  `WorkOnDate` datetime(6) NOT NULL,
  `RemoveDate` datetime(6) DEFAULT NULL,
  `CenterCode` varchar(30) DEFAULT NULL,
  `DoctorName` varchar(60) DEFAULT NULL,
  `Specialization1` varchar(50) DEFAULT NULL,
  `Specialization2` varchar(50) DEFAULT NULL,
  `DoctorNationalId` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_docworkoncenterhistory`
--

INSERT INTO `website_docworkoncenterhistory` (`SynCode`, `WorkOnDate`, `RemoveDate`, `CenterCode`, `DoctorName`, `Specialization1`, `Specialization2`, `DoctorNationalId`) VALUES
('253', '2020-07-29 01:19:18.196304', NULL, '1', NULL, NULL, NULL, NULL),
('251', '2020-07-29 01:20:10.638478', NULL, '1', NULL, NULL, NULL, NULL),
('252', '2020-07-29 01:20:22.613357', NULL, '1', NULL, NULL, NULL, NULL),
('251', '2020-07-29 02:05:13.482999', NULL, '1', 'Ali Mohamed Abdelrahman', 'Batna', 'Bacteria', NULL),
('252', '2020-07-29 02:07:30.626607', NULL, '1', 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', NULL),
('251', '2020-07-29 02:08:23.823214', NULL, '2', 'Ali Mohamed Abdelrahman', 'Batna', 'Bacteria', NULL),
('253', '2020-07-29 02:08:35.130234', NULL, '2', 'anas azam', 'Geldia', 'Hasasia', NULL),
('252', '2020-07-29 02:09:11.818502', NULL, '3', 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', NULL),
('253', '2020-07-29 02:09:17.523049', NULL, '3', 'anas azam', 'Geldia', 'Hasasia', NULL),
('251', '2020-07-29 02:20:10.519275', NULL, '1', 'Ali Mohamed Abdelrahman', 'Batna', 'Bacteria', 'Citizen object (301)'),
('251', '2020-07-29 02:20:28.557502', NULL, '1', 'Ali Mohamed Abdelrahman', 'Batna', 'Bacteria', 'Citizen object (301)'),
('251', '2020-07-29 02:21:04.856198', NULL, '1', 'Ali Mohamed Abdelrahman', 'Batna', 'Bacteria', '301'),
('251', '2020-07-29 02:22:35.816926', NULL, '2', 'Ali Mohamed Abdelrahman', 'Batna', 'Bacteria', '301'),
('253', '2020-07-29 02:22:50.012365', NULL, '2', 'anas azam', 'Geldia', 'Hasasia', '303'),
('252', '2020-07-29 02:53:35.562586', NULL, '1', 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', '302'),
('251', '2020-07-29 02:53:49.096307', NULL, '1', 'Ali Mohamed Abdelrahman', 'Batna', 'Bacteria', '301'),
('252', '2020-07-29 02:58:17.118202', NULL, '2', 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', '302'),
('253', '2020-07-30 01:00:58.652855', NULL, '2', 'anas azam', 'Geldia', 'Hasasia', '303'),
('252', '2020-07-30 20:52:42.881391', NULL, '1', 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', '302'),
('253', '2020-07-30 20:52:58.308652', NULL, '1', 'anas azam', 'Geldia', 'Hasasia', '303'),
('251', '2020-07-30 20:54:42.867253', NULL, '2', 'Ali Mohamed Abdelrahman', 'Batna', 'Bacteria', '301'),
('251', '2020-07-30 20:55:33.919194', NULL, '3', 'Ali Mohamed Abdelrahman', 'Batna', 'Bacteria', '301'),
('252', '2020-07-30 20:55:50.566865', NULL, '3', 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', '302'),
('253', '2020-07-30 20:56:13.160682', NULL, '3', 'anas azam', 'Geldia', 'Hasasia', '303'),
('251', '2020-08-02 20:44:58.759662', NULL, '51', 'Ali Mohamed Abdelrahman', 'Batna', 'Bacteria', '301'),
('252', '2020-08-04 01:10:25.276969', NULL, '1', 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', '302'),
('253', '2020-08-04 01:10:38.223969', NULL, '1', 'anas azam', 'Geldia', 'Hasasia', '303'),
('252', '2020-08-04 01:19:55.559653', NULL, '1', 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', '302'),
('252', '2020-08-04 03:05:04.102696', NULL, '1', 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', '302'),
('251', '2020-08-04 03:42:57.003783', NULL, '1', 'Mostafa Mohamed Abdelrahman', 'Batna', 'Bacteria', '301'),
('252', '2020-08-04 03:43:09.914682', NULL, '1', 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', '302'),
('252', '2020-08-04 04:14:12.278531', NULL, '1', 'Safaa Ali Mohamed', 'Anf w Ozon', 'Bacteria', '302'),
('253', '2020-08-04 04:14:24.092587', NULL, '1', 'anas azam', 'Geldia', 'Hasasia', '303'),
('251', '2020-08-04 07:30:35.678519', NULL, '52', 'Mostafa Mohamed Abdelrahman', 'Batna', 'Bacteria', '301'),
('251', '2020-08-04 07:32:10.369176', NULL, '52', 'Mostafa Mohamed Abdelrahman', 'Batna', 'Bacteria', '301');

-- --------------------------------------------------------

--
-- Table structure for table `website_healthministrylicensecenter`
--

CREATE TABLE `website_healthministrylicensecenter` (
  `CenterCode` bigint(20) NOT NULL,
  `CenterName` varchar(60) NOT NULL,
  `CenterType` varchar(20) NOT NULL,
  `CenterGov` varchar(40) NOT NULL,
  `Password` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_healthministrylicensecenter`
--

INSERT INTO `website_healthministrylicensecenter` (`CenterCode`, `CenterName`, `CenterType`, `CenterGov`, `Password`) VALUES
(1, 'Demerdash', 'General', 'Cairo', '111'),
(2, 'El-Asr-El-Eenyy', 'Genaral', 'Cairo', '111'),
(3, 'El-Saed_Galal', 'Genaral', 'Cairo', '111'),
(51, 'El-Shrouq', 'Special', 'Giza', '222'),
(52, 'El-Nile', 'Special', 'Cairo', '222'),
(53, 'Badrawy', 'Special', 'Cairo', '222');

-- --------------------------------------------------------

--
-- Table structure for table `website_healthministrylicenselab`
--

CREATE TABLE `website_healthministrylicenselab` (
  `MinLabCode` bigint(20) NOT NULL,
  `LabName` varchar(60) DEFAULT NULL,
  `LabType` varchar(20) DEFAULT NULL,
  `LabGov` varchar(40) DEFAULT NULL,
  `Password` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_healthministrylicenselab`
--

INSERT INTO `website_healthministrylicenselab` (`MinLabCode`, `LabName`, `LabType`, `LabGov`, `Password`) VALUES
(151, 'Alfa', 'General', 'Giza', '444'),
(152, 'El Se7a', 'General', 'Cairo', '444'),
(153, 'El 3eyon', 'General', 'Giza', '444'),
(201, 'Kasr el Eny', 'Special', 'Giza', '555'),
(202, 'El-Nor', 'Special', 'Cairo', '555'),
(203, 'Helath', 'Special', 'Cairo', '555');

-- --------------------------------------------------------

--
-- Table structure for table `website_laboratory`
--

CREATE TABLE `website_laboratory` (
  `LabCode` bigint(20) NOT NULL,
  `LabName` varchar(60) NOT NULL,
  `LabType` varchar(50) DEFAULT NULL,
  `LabPassword` varchar(60) NOT NULL,
  `LabGov` varchar(40) NOT NULL,
  `CurrentAddress` varchar(120) NOT NULL,
  `FirstPhone` bigint(20) NOT NULL,
  `SecoundPhone` bigint(20) NOT NULL,
  `Date` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_laboratory`
--

INSERT INTO `website_laboratory` (`LabCode`, `LabName`, `LabType`, `LabPassword`, `LabGov`, `CurrentAddress`, `FirstPhone`, `SecoundPhone`, `Date`) VALUES
(151, 'ALFA', 'General', 'ahmedais', 'Giza', '11 st Mohamed Ahmed  - Giza', 1008748162, 228171232, '2020-07-21 04:54:28.000000'),
(152, 'El Se7a', 'General', '444', 'Cairo', 'Madent Nasr', 1235644654, 45245623456, '2020-07-09 12:53:33.881896'),
(153, 'El 3eyon', 'General', '444', 'Giza', '3434344', 3434343, 343434, '2020-07-09 12:41:35.359659'),
(201, 'Kasr el Eny', 'Special', '555', 'Giza', 'Nazlet El Seman', 2134564, 324156345, '2020-07-21 04:54:28.000000'),
(202, 'El-Nor', 'Special', '555', 'Giza', 'Nazlet El Seman', 24352435, 245245423, '2020-07-09 15:31:02.632336'),
(203, 'Helath', 'Special', '555', 'Cairo', '5555', 5555, 5555, '2020-07-20 05:10:18.000000');

-- --------------------------------------------------------

--
-- Table structure for table `website_medicalanalystlicense`
--

CREATE TABLE `website_medicalanalystlicense` (
  `AnalystCode` bigint(20) NOT NULL,
  `NationalId` varchar(30) NOT NULL,
  `Specialization1` varchar(50) NOT NULL,
  `Specialization2` varchar(50) DEFAULT NULL,
  `Password` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_medicalanalystlicense`
--

INSERT INTO `website_medicalanalystlicense` (`AnalystCode`, `NationalId`, `Specialization1`, `Specialization2`, `Password`) VALUES
(706, '306', 'دم', 'اشعة اكس', '777'),
(707, '307', 'اشعة مقطعيه', 'دوبلر', '777'),
(708, '308', 'رسم قلب', 'مكروبات', '777'),
(709, '309', 'رسم قلب', 'اشعة اكس', '777');

-- --------------------------------------------------------

--
-- Table structure for table `website_medicalcenter`
--

CREATE TABLE `website_medicalcenter` (
  `CenterCode` bigint(20) NOT NULL,
  `CenterType` varchar(20) DEFAULT NULL,
  `Password` varchar(60) NOT NULL,
  `CenterName` varchar(60) NOT NULL,
  `CenterGov` varchar(40) NOT NULL,
  `CurrentAddress` varchar(120) NOT NULL,
  `FirstPhone` bigint(20) NOT NULL,
  `SecoundPhone` bigint(20) NOT NULL,
  `RegisteredDate` datetime(6) DEFAULT NULL,
  `UpdateDate` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_medicalcenter`
--

INSERT INTO `website_medicalcenter` (`CenterCode`, `CenterType`, `Password`, `CenterName`, `CenterGov`, `CurrentAddress`, `FirstPhone`, `SecoundPhone`, `RegisteredDate`, `UpdateDate`) VALUES
(1, 'General', '111', 'Demerdash', 'Cairo', 'giza', 1245784, 151245784, '2020-07-27 20:35:04.242136', '2020-07-27 20:35:04.242136'),
(2, 'General', '111', 'El-Asr-El-Eenyy', 'Cairo', '12', 12, 12, '2020-07-09 18:33:07.000000', '2020-07-27 23:22:42.914478'),
(3, 'Genaral', '111', 'El-Saed_Galal', 'Cairo', '12455', 1121212454, 412412110, '2020-07-27 21:14:36.320963', '2020-07-27 21:14:36.320963'),
(51, 'Special', '222', 'El-Shrouq', 'Giza', 'Nazlet El Seman / Harram', 123456468, 12356474, '2020-07-27 21:44:58.902500', '2020-07-27 21:44:58.902500'),
(52, 'Special', '222', 'El-Nile', 'Cairo', '111', 111, 111, '2020-07-09 18:33:07.000000', '2020-08-04 07:29:17.748827');

-- --------------------------------------------------------

--
-- Table structure for table `website_medicalhistory`
--

CREATE TABLE `website_medicalhistory` (
  `PerNationalId_id` bigint(20) DEFAULT NULL,
  `CenterCode` varchar(30) DEFAULT NULL,
  `CenterName` varchar(60) DEFAULT NULL,
  `SynCode` varchar(30) DEFAULT NULL,
  `DoctorNationalId` varchar(30) DEFAULT NULL,
  `AnalystNationalId` varchar(30) DEFAULT NULL,
  `DoctorName` varchar(60) DEFAULT NULL,
  `MedicalReport` longtext DEFAULT NULL,
  `Treatment` longtext DEFAULT NULL,
  `LabCode` varchar(30) DEFAULT NULL,
  `LabName` varchar(60) DEFAULT NULL,
  `AnalysisReport` longtext DEFAULT NULL,
  `RaysReport` longtext DEFAULT NULL,
  `RecordDate` datetime(6) NOT NULL,
  `CurrentTime` datetime(6) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_medicalhistory`
--

INSERT INTO `website_medicalhistory` (`PerNationalId_id`, `CenterCode`, `CenterName`, `SynCode`, `DoctorNationalId`, `AnalystNationalId`, `DoctorName`, `MedicalReport`, `Treatment`, `LabCode`, `LabName`, `AnalysisReport`, `RaysReport`, `RecordDate`, `CurrentTime`, `id`) VALUES
(311, NULL, NULL, '707', NULL, '307', 'Muuhameed ussama', NULL, NULL, '151', 'ALFA', 'Analysis Report', 'break in legs\r\n', '2020-08-02 20:33:20.502618', '2020-08-02 20:33:20.502618', 71),
(311, NULL, NULL, '707', NULL, '307', 'Muuhameed ussama', NULL, NULL, '202', 'El-Nor', '5454', '5445\r\n', '2020-08-02 20:35:41.752880', '2020-08-02 20:35:41.752880', 72),
(311, '1', 'Demerdash', '251', '301', NULL, 'Ali Mohamed Abdelrahman', 'Medical Report \r\nToo Much Headache', 'PyAlcofan\r\nPanadol Extra', NULL, NULL, NULL, NULL, '2020-08-02 20:39:23.798398', '2020-08-02 20:39:23.798398', 73),
(311, '51', 'El-Shrouq', '251', '301', NULL, 'Ali Mohamed Abdelrahman', 'Medical Report:\r\nToo Much Headache', 'PyAlcofan, Panadol Extra	', NULL, NULL, NULL, NULL, '2020-08-02 20:46:04.106627', '2020-08-02 20:46:04.106627', 74),
(311, NULL, 'Special Doctor', '252', '302', NULL, 'Safaa Ali Mohamed', 'Medical Report', 'Congestal, Catafast', NULL, NULL, NULL, NULL, '2020-08-02 20:49:09.038746', '2020-08-02 20:49:09.038746', 75),
(311, NULL, 'Special Doctor', '251', '301', NULL, 'Mostafa Mohamed Abdelrahman', '11122', '11122', NULL, NULL, NULL, NULL, '2020-08-03 23:27:58.149459', '2020-08-03 23:27:58.149459', 76),
(305, NULL, 'Special Doctor', '251', '301', NULL, 'Mostafa Mohamed Abdelrahman', '11', '11', NULL, NULL, NULL, NULL, '2020-08-03 23:28:30.954843', '2020-08-03 23:28:30.954843', 77),
(311, NULL, 'Special Doctor', '254', '304', NULL, 'Nor El-Den Ahmed', '1', '1', NULL, NULL, NULL, NULL, '2020-08-04 07:06:27.618885', '2020-08-04 07:06:27.618885', 78),
(311, '52', 'El-Nile', '251', '301', NULL, 'Mostafa Mohamed Abdelrahman', '21', '21', NULL, NULL, NULL, NULL, '2020-08-04 07:33:12.934878', '2020-08-04 07:33:12.934878', 79),
(311, '52', 'El-Nile', '251', '301', NULL, 'Mostafa Mohamed Abdelrahman', '21', '21', NULL, NULL, NULL, NULL, '2020-08-04 07:36:10.381541', '2020-08-04 07:36:10.381541', 80),
(311, '52', 'El-Nile', '251', '301', NULL, 'Mostafa Mohamed Abdelrahman', '3322', '3322\r\n', NULL, NULL, NULL, NULL, '2020-08-04 07:36:21.015228', '2020-08-04 07:36:21.015228', 81),
(311, '52', 'El-Nile', '251', '301', NULL, 'Mostafa Mohamed Abdelrahman', '5554', '\r\n54445544', NULL, NULL, NULL, NULL, '2020-08-04 07:40:33.392998', '2020-08-04 07:40:33.392998', 82),
(301, '1', 'Demerdash', '251', '301', NULL, 'Mostafa Mohamed Abdelrahman', 'AHNNIIO3 NPONNVEPNPOJNNVEEPONPONPOJVJE;;E\r\nCEPOHCOEHVOENVEIENVPEONVOEOVJNEONOEO', '', NULL, NULL, NULL, NULL, '2020-08-20 23:48:32.596162', '2020-08-20 23:48:32.596162', 83),
(302, '1', 'Demerdash', '251', '301', NULL, 'Mostafa Mohamed Abdelrahman', 'DWDWDWDWDWDWD', 'DWDWDWDWDWDW', NULL, NULL, NULL, NULL, '2020-08-20 23:49:24.555463', '2020-08-20 23:49:24.555463', 84);

-- --------------------------------------------------------

--
-- Table structure for table `website_medicalsyndicatelicense`
--

CREATE TABLE `website_medicalsyndicatelicense` (
  `SynCode` bigint(20) NOT NULL,
  `NationalId` varchar(30) NOT NULL,
  `Specialization1` varchar(50) NOT NULL,
  `Specialization2` varchar(50) NOT NULL,
  `Password` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_medicalsyndicatelicense`
--

INSERT INTO `website_medicalsyndicatelicense` (`SynCode`, `NationalId`, `Specialization1`, `Specialization2`, `Password`) VALUES
(251, '301', 'Batna', 'Bacteria', '666'),
(252, '302', 'Anf w Ozon', 'Bacteria', '666'),
(253, '303', 'Geldia', 'Hasasia', '666'),
(254, '304', 'hasasia', 'gra7a', '666'),
(255, '305', '3eon', 'Gra7a 3eon', '666');

-- --------------------------------------------------------

--
-- Table structure for table `website_personaldata`
--

CREATE TABLE `website_personaldata` (
  `id` int(11) NOT NULL,
  `PerNationalId_id` bigint(20) DEFAULT NULL,
  `FullName` varchar(60) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Job` varchar(50) NOT NULL,
  `BirthGov` varchar(40) NOT NULL,
  `BirthDate` date DEFAULT NULL,
  `CurrentGov` varchar(40) NOT NULL,
  `CurrentAddress` varchar(120) NOT NULL,
  `FirstPhone` bigint(20) NOT NULL,
  `SecoundPhone` bigint(20) NOT NULL,
  `Email` varchar(60) NOT NULL,
  `FirstRelName` varchar(60) NOT NULL,
  `FirstRelPhone` bigint(20) NOT NULL,
  `SecoundRelName` varchar(60) NOT NULL,
  `SecoundRelPhone` bigint(20) NOT NULL,
  `PassportNo` bigint(20) DEFAULT NULL,
  `BloodGroup` varchar(5) DEFAULT NULL,
  `Date` datetime(6) DEFAULT NULL,
  `LabCode` varchar(30) DEFAULT NULL,
  `LabName` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_personaldata`
--

INSERT INTO `website_personaldata` (`id`, `PerNationalId_id`, `FullName`, `Gender`, `Job`, `BirthGov`, `BirthDate`, `CurrentGov`, `CurrentAddress`, `FirstPhone`, `SecoundPhone`, `Email`, `FirstRelName`, `FirstRelPhone`, `SecoundRelName`, `SecoundRelPhone`, `PassportNo`, `BloodGroup`, `Date`, `LabCode`, `LabName`) VALUES
(301, 301, 'Mostafa Mohamed Abdelrahman', 'Male', 'Doctor', 'Giza', '1989-11-01', 'Alexandria', 'Faisal', 11111111, 2222222, 'MostafaAli@yahoo.com', 'Ahmed', 11111111, 'Naser', 2222222, 11111111, 'AB', '2020-07-21 02:39:06.000000', '151', 'ALFA'),
(302, 302, 'Safaa Ali Mohamed', 'Female', 'Doctor', 'giza', '2020-07-01', 'Giza', 'Giza', 1221212, 21212121, 'SafaaAliMohamed@gmail.com', 'ahmed', 1212121212, 'Ziad', 21212121, NULL, 'A+', '2020-07-09 12:53:33.881896', '151', 'ALFA'),
(303, 303, 'anas azam', 'male', 'doctor', 'giza', '2020-07-16', 'cairo', 'cairo', 21524545, 221548547, 'anasazam@gmail.com', 'ahmed', 125454214, 'anas', 221548547, NULL, NULL, '2020-07-09 12:58:38.494173', NULL, NULL),
(304, 304, 'Nor El-Den Ahmed', 'male', 'doctor', 'giza', '2020-07-22', 'giza', 'giza', 215245421, 2154512, 'NorEl-DenAhmed@yahoo.com', 'Nor', 12165464, 'Ahmed', 115458423, NULL, NULL, '0000-00-00 00:00:00.000000', NULL, NULL),
(305, 305, 'Diaa Nour', 'male', 'doctor', 'giza', '2020-07-21', 'giza', 'giza', 1235469874, 135496854, 'DiaaNor@gmail.com', 'ahmed', 11545124, 'Mohamed', 122154621, NULL, NULL, '0000-00-00 00:00:00.000000', NULL, NULL),
(306, 306, 'OmarAhmed', 'Male', 'Analyst', 'Giza', '2020-07-15', 'Cairo', 'Cairo', 1234567481, 1123456784, 'OmarAhmed@gmail.com', 'Ahmed', 2123564, 'Mahmoud', 1123456784, NULL, 'O', '2020-07-09 12:41:35.359659', '203', 'Helath'),
(307, 307, 'Muuhameed ussama', 'Male', 'Analyst', 'Giza', '2020-07-08', 'Giza', 'Cairo', 2135645465, 1212313124, 'MuuhameedUssama@gmail.com', 'Anas', 26313564, 'Ahmed', 213546, NULL, NULL, '2020-07-21 02:39:06.000000', NULL, NULL),
(308, 308, 'Mostafa Ali', 'Male', 'Analyst', 'Giza', '2020-07-14', 'Giza', 'Giza', 1236548974, 1123415674, 'MostafaAli@yahoo.com', 'Anas', 26313564, 'Ahmed', 213546, NULL, NULL, '2020-07-20 02:43:57.000000', NULL, NULL),
(309, 309, 'Safaa Ali  Ahmed', 'female', 'Analyst', 'Giza', '1989-12-31', 'Matruh', 'cairo', 1235644654, 23131545, 'SafaaAliAhmed@gmail.com', 'Anas', 2315646456, 'Ahmed', 232564, 1212121, NULL, '2020-07-27 02:48:33.000000', NULL, NULL),
(310, 310, 'Azaam Yasser', 'Male', 'Analyst', 'Giza', '2020-10-08', 'Giza', 'Giza', 2135645465, 1212313124, 'AzzamYasser@gmail.com', 'Anas', 26313564, 'Ahmed', 232564, 510, NULL, '2020-07-09 12:41:35.359659', NULL, NULL),
(311, 311, 'Mahmoud Ahmed Reyad Naser', 'Male', 'Carpentar', 'Giza', '1989-12-31', 'Giza', 'Giza', 2135645465, 1212313124, 'MahmoudAhmed@gmail.com', 'Anas', 2315646456, 'Ahmed', 213546, 511, 'AB', '2020-07-20 05:10:18.000000', NULL, NULL),
(312, 312, 'Amal Saad', 'female', 'Teacher', 'giza', '2020-08-02', 'cairo', 'Madinet Nasr', 1235644654, 23164865989, 'AmalSaad@gmail.com', 'ahmed', 125454214, 'Naseer', 124574423, NULL, 'O', '2020-07-27 02:57:56.000000', NULL, NULL),
(313, 313, 'George Hemdan Wasoof', 'Male', 'Singer', 'Giza', '2020-07-14', 'Giza', 'Giza', 123564, 1231564, 'George@gmail.com', 'Ahhmed', 2556465, 'Anas', 1231564, NULL, 'B', '2020-07-13 03:03:04.000000', NULL, NULL),
(314, 314, 'Noura Saed Hadary', 'female', 'Driver', 'giza', '2020-07-21', 'giza', 'Giza', 1235469874, 135496854, 'Noura@gmail.com', 'ahmed', 233454, 'Mohamed', 122154621, NULL, 'A', '2020-07-09 15:31:02.632336', NULL, NULL),
(315, 315, 'Naglaa Marawan Diaa', 'female', 'Teacher', 'Giza', '2020-07-13', 'Giza', 'Giza', 1236546, 231544231, 'Naglaa@gmail.com', 'Norhan', 122548774, 'Samar', 12341567, NULL, 'O', '2020-07-28 03:03:04.000000', NULL, NULL),
(316, 316, 'Samah Anwar Abdallah', 'Male', 'Engineer', 'South Sinai', '2020-07-21', 'Beheira', 'giza', 1234567456, 115235478, 'SamahAnwar@yahoo.com', 'ahmed', 1234854, 'mamdoh', 2165474, 515, NULL, '2020-07-25 14:04:28.265004', NULL, NULL),
(317, 317, 'Ahmed Mohamed Ali', 'Male', 'Carpentar', 'Red Sea', '2020-07-07', 'Beheira', 'Itay', 123564454, 123654674, 'AhmedMohamedAli@gmail.com', 'ahmed', 254687654, 'mahmoud', 1236547894, 517, NULL, '2020-07-25 14:36:19.141571', NULL, NULL),
(318, 318, 'Diaa Ahmed Mahmoud ', 'Male', 'Carpenter', 'Matruh', '1999-06-19', 'Giza', 'Faisal', 123123123, 123123123, 'DiaaAhmed@gmail.com', 'Saed', 12365474, 'Kenzy', 1121544412, 231546, NULL, '2020-08-03 19:01:29.516785', NULL, NULL),
(319, 319, 'Nehal ahmed Hany', 'Female', 'Teacher', 'South Sinai', '1978-05-15', 'Red Sea', 'Giza', 3216541610, 3215216, 'Nehal@yahoo.com', 'Khaled', 126548541, 'Amr', 1156485642, 21554201542, NULL, '2020-08-03 02:49:56.025327', NULL, NULL),
(3036, 320, 'Fares Hazem Ahmed', 'Male', 'Student', 'Giza', '1989-07-01', 'Alexandria', '6 October City', 1111111111, 1111111111, 'faresss@gmail.com', 'Khaled', 102165402, 'Daren', 24156421, 2215442, NULL, '2020-07-21 02:39:06.000000', NULL, NULL),
(3042, 321, 'Gana Mohamed Hessan', 'Female', 'Student', 'Beni Suef', '2005-05-12', 'Alexandria', 'behaira', 1111111, 1111111, 'Ganaa@gmail.com', 'Ahmed', 1111111, 'Mohamed', 1111111, 1111111, NULL, '2020-08-03 20:33:38.119978', NULL, NULL),
(3044, 12345678912345, 'ahmed Ibrahim', 'Male', 'it manage', 'Cairo', '2020-08-06', 'Cairo', 'ain helwan', 1286022006, 1008748162, 'a@a.com', 'ahmed', 1008748162, 'Mohamed', 1286022006, 123456, NULL, '2020-08-06 00:33:24.926513', NULL, NULL),
(3045, 1234567891232020, 'Ahmed Ibrahim saleh', 'Male', 'engineering ', 'Cairo', '1989-01-04', 'Cairo', 'ain helwan', 1008748162, 1286022006, 'engahmedibrahim780@gmail.com', 'ahmed mohmed', 1289600085, 'aya ahmed', 12790319881, 2030, NULL, '2020-08-21 00:08:57.973547', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `website_personlab`
--

CREATE TABLE `website_personlab` (
  `id` int(11) NOT NULL,
  `Date` datetime(6) DEFAULT NULL,
  `LabCode_id` bigint(20) NOT NULL,
  `PerNationalId_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_personlab`
--

INSERT INTO `website_personlab` (`id`, `Date`, `LabCode_id`, `PerNationalId_id`) VALUES
(1, '2020-08-08 01:35:43.983419', 151, 301);

-- --------------------------------------------------------

--
-- Table structure for table `website_personmedicalcenter`
--

CREATE TABLE `website_personmedicalcenter` (
  `id` int(11) NOT NULL,
  `CurrentTime` datetime(6) NOT NULL,
  `CenterCode_id` bigint(20) NOT NULL,
  `PerNationalId_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `website_personmedicalcenter`
--

INSERT INTO `website_personmedicalcenter` (`id`, `CurrentTime`, `CenterCode_id`, `PerNationalId_id`) VALUES
(1, '2020-08-08 01:35:19.971824', 1, 301);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `website_analyst`
--
ALTER TABLE `website_analyst`
  ADD PRIMARY KEY (`AnalystCode`);

--
-- Indexes for table `website_analystlabhistory`
--
ALTER TABLE `website_analystlabhistory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `website_analystlabhi_LabCode_id_fb1d7fcd_fk_website_l` (`LabCode_id`);

--
-- Indexes for table `website_analystworkonlab`
--
ALTER TABLE `website_analystworkonlab`
  ADD PRIMARY KEY (`id`),
  ADD KEY `website_analystworko_AnalystCode_id_09ee6d6b_fk_website_a` (`AnalystCode_id`),
  ADD KEY `website_analystworko_LabCode_id_cf9d4064_fk_website_l` (`LabCode_id`);

--
-- Indexes for table `website_citizen`
--
ALTER TABLE `website_citizen`
  ADD PRIMARY KEY (`PerNationalId`);

--
-- Indexes for table `website_doctor`
--
ALTER TABLE `website_doctor`
  ADD PRIMARY KEY (`SynCode`);

--
-- Indexes for table `website_doctorperson`
--
ALTER TABLE `website_doctorperson`
  ADD PRIMARY KEY (`id`),
  ADD KEY `website_doctorperson_SynCode_id_04f9ea3f_fk_website_d` (`SynCode_id`),
  ADD KEY `website_doctorperson_PerNationalId_id_1e369689_fk_website_c` (`PerNationalId_id`);

--
-- Indexes for table `website_docworkoncenter`
--
ALTER TABLE `website_docworkoncenter`
  ADD PRIMARY KEY (`id`),
  ADD KEY `website_docworkoncenter_CenterCode_id_547c7b26` (`CenterCode_id`),
  ADD KEY `website_docworkoncenter_SynCode_id_f537366e` (`SynCode_id`);

--
-- Indexes for table `website_healthministrylicensecenter`
--
ALTER TABLE `website_healthministrylicensecenter`
  ADD PRIMARY KEY (`CenterCode`);

--
-- Indexes for table `website_healthministrylicenselab`
--
ALTER TABLE `website_healthministrylicenselab`
  ADD PRIMARY KEY (`MinLabCode`);

--
-- Indexes for table `website_laboratory`
--
ALTER TABLE `website_laboratory`
  ADD PRIMARY KEY (`LabCode`);

--
-- Indexes for table `website_medicalanalystlicense`
--
ALTER TABLE `website_medicalanalystlicense`
  ADD PRIMARY KEY (`AnalystCode`);

--
-- Indexes for table `website_medicalcenter`
--
ALTER TABLE `website_medicalcenter`
  ADD PRIMARY KEY (`CenterCode`);

--
-- Indexes for table `website_medicalhistory`
--
ALTER TABLE `website_medicalhistory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `website_medicalhisto_PerNationalId_id_5e223d5f_fk_website_c` (`PerNationalId_id`);

--
-- Indexes for table `website_medicalsyndicatelicense`
--
ALTER TABLE `website_medicalsyndicatelicense`
  ADD PRIMARY KEY (`SynCode`);

--
-- Indexes for table `website_personaldata`
--
ALTER TABLE `website_personaldata`
  ADD PRIMARY KEY (`id`),
  ADD KEY `website_personaldata_PerNationalId_id_5f3b1b96_fk_website_c` (`PerNationalId_id`);

--
-- Indexes for table `website_personlab`
--
ALTER TABLE `website_personlab`
  ADD PRIMARY KEY (`id`),
  ADD KEY `website_personlab_LabCode_id_9d2e244f_fk_website_l` (`LabCode_id`),
  ADD KEY `website_personlab_PerNationalId_id_74a26c82_fk_website_c` (`PerNationalId_id`);

--
-- Indexes for table `website_personmedicalcenter`
--
ALTER TABLE `website_personmedicalcenter`
  ADD PRIMARY KEY (`id`),
  ADD KEY `website_personmedica_CenterCode_id_57e0fe44_fk_website_m` (`CenterCode_id`),
  ADD KEY `website_personmedica_PerNationalId_id_39fceffa_fk_website_c` (`PerNationalId_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `website_analystlabhistory`
--
ALTER TABLE `website_analystlabhistory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `website_analystworkonlab`
--
ALTER TABLE `website_analystworkonlab`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `website_doctorperson`
--
ALTER TABLE `website_doctorperson`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `website_docworkoncenter`
--
ALTER TABLE `website_docworkoncenter`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `website_medicalhistory`
--
ALTER TABLE `website_medicalhistory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT for table `website_personaldata`
--
ALTER TABLE `website_personaldata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3046;

--
-- AUTO_INCREMENT for table `website_personlab`
--
ALTER TABLE `website_personlab`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `website_personmedicalcenter`
--
ALTER TABLE `website_personmedicalcenter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `website_analystlabhistory`
--
ALTER TABLE `website_analystlabhistory`
  ADD CONSTRAINT `website_analystlabhi_LabCode_id_fb1d7fcd_fk_website_l` FOREIGN KEY (`LabCode_id`) REFERENCES `website_laboratory` (`LabCode`);

--
-- Constraints for table `website_analystworkonlab`
--
ALTER TABLE `website_analystworkonlab`
  ADD CONSTRAINT `website_analystworko_AnalystCode_id_09ee6d6b_fk_website_a` FOREIGN KEY (`AnalystCode_id`) REFERENCES `website_analyst` (`AnalystCode`),
  ADD CONSTRAINT `website_analystworko_LabCode_id_cf9d4064_fk_website_l` FOREIGN KEY (`LabCode_id`) REFERENCES `website_laboratory` (`LabCode`);

--
-- Constraints for table `website_doctorperson`
--
ALTER TABLE `website_doctorperson`
  ADD CONSTRAINT `website_doctorperson_PerNationalId_id_1e369689_fk_website_c` FOREIGN KEY (`PerNationalId_id`) REFERENCES `website_citizen` (`PerNationalId`),
  ADD CONSTRAINT `website_doctorperson_SynCode_id_04f9ea3f_fk_website_d` FOREIGN KEY (`SynCode_id`) REFERENCES `website_doctor` (`SynCode`);

--
-- Constraints for table `website_docworkoncenter`
--
ALTER TABLE `website_docworkoncenter`
  ADD CONSTRAINT `website_docworkoncen_CenterCode_id_547c7b26_fk_website_m` FOREIGN KEY (`CenterCode_id`) REFERENCES `website_medicalcenter` (`CenterCode`),
  ADD CONSTRAINT `website_docworkoncen_SynCode_id_f537366e_fk_website_d` FOREIGN KEY (`SynCode_id`) REFERENCES `website_doctor` (`SynCode`);

--
-- Constraints for table `website_medicalhistory`
--
ALTER TABLE `website_medicalhistory`
  ADD CONSTRAINT `website_medicalhisto_PerNationalId_id_5e223d5f_fk_website_c` FOREIGN KEY (`PerNationalId_id`) REFERENCES `website_citizen` (`PerNationalId`);

--
-- Constraints for table `website_personaldata`
--
ALTER TABLE `website_personaldata`
  ADD CONSTRAINT `website_personaldata_PerNationalId_id_5f3b1b96_fk_website_c` FOREIGN KEY (`PerNationalId_id`) REFERENCES `website_citizen` (`PerNationalId`);

--
-- Constraints for table `website_personlab`
--
ALTER TABLE `website_personlab`
  ADD CONSTRAINT `website_personlab_LabCode_id_9d2e244f_fk_website_l` FOREIGN KEY (`LabCode_id`) REFERENCES `website_laboratory` (`LabCode`),
  ADD CONSTRAINT `website_personlab_PerNationalId_id_74a26c82_fk_website_c` FOREIGN KEY (`PerNationalId_id`) REFERENCES `website_citizen` (`PerNationalId`);

--
-- Constraints for table `website_personmedicalcenter`
--
ALTER TABLE `website_personmedicalcenter`
  ADD CONSTRAINT `website_personmedica_CenterCode_id_57e0fe44_fk_website_m` FOREIGN KEY (`CenterCode_id`) REFERENCES `website_medicalcenter` (`CenterCode`),
  ADD CONSTRAINT `website_personmedica_PerNationalId_id_39fceffa_fk_website_c` FOREIGN KEY (`PerNationalId_id`) REFERENCES `website_citizen` (`PerNationalId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
