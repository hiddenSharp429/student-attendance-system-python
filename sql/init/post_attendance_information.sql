/*
 Navicat Premium Dump SQL

 Source Server         : cloud
 Source Server Type    : MySQL
 Source Server Version : 50740 (5.7.40-log)
 Source Host           : 43.136.80.11:3306
 Source Schema         : db

 Target Server Type    : MySQL
 Target Server Version : 50740 (5.7.40-log)
 File Encoding         : 65001

 Date: 01/07/2024 15:16:23
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for post_attendance_information
-- ----------------------------
DROP TABLE IF EXISTS `post_attendance_information`;
CREATE TABLE `post_attendance_information` (
  `attendance_id` int(11) NOT NULL,
  `course_id` varchar(10) NOT NULL,
  `course_name` varchar(10) NOT NULL,
  `course_no` int(11) NOT NULL,
  `attendance_start_time` datetime NOT NULL,
  `attendance_end_time` datetime NOT NULL,
  `code` varchar(10) NOT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of post_attendance_information
-- ----------------------------
BEGIN;
INSERT INTO `post_attendance_information` (`attendance_id`, `course_id`, `course_name`, `course_no`, `attendance_start_time`, `attendance_end_time`, `code`) VALUES (1, 'c1', '操作系统原理', 18, '2023-12-31 00:42:19', '2024-01-01 00:42:19', 'c0001');
INSERT INTO `post_attendance_information` (`attendance_id`, `course_id`, `course_name`, `course_no`, `attendance_start_time`, `attendance_end_time`, `code`) VALUES (2, 'c1', '操作系统原理', 17, '2023-12-31 01:33:20', '2024-01-01 01:33:20', 'c0002');
INSERT INTO `post_attendance_information` (`attendance_id`, `course_id`, `course_name`, `course_no`, `attendance_start_time`, `attendance_end_time`, `code`) VALUES (3, 'c1', '操作系统原理', 17, '2023-12-31 14:49:39', '2024-01-01 14:49:39', 'c0003');
INSERT INTO `post_attendance_information` (`attendance_id`, `course_id`, `course_name`, `course_no`, `attendance_start_time`, `attendance_end_time`, `code`) VALUES (4, '1', '1', 1, '2024-01-03 22:16:02', '2024-01-04 22:16:02', '1');
INSERT INTO `post_attendance_information` (`attendance_id`, `course_id`, `course_name`, `course_no`, `attendance_start_time`, `attendance_end_time`, `code`) VALUES (5, '121', '121', 121, '2024-01-08 03:06:04', '2024-01-09 03:06:04', '1211');
INSERT INTO `post_attendance_information` (`attendance_id`, `course_id`, `course_name`, `course_no`, `attendance_start_time`, `attendance_end_time`, `code`) VALUES (6, '1', '操作系统原理', 3, '2024-01-08 11:34:11', '2024-01-09 11:34:11', '1234');
INSERT INTO `post_attendance_information` (`attendance_id`, `course_id`, `course_name`, `course_no`, `attendance_start_time`, `attendance_end_time`, `code`) VALUES (7, 'c1', '操作系统原理', 1, '2024-01-09 19:37:12', '2024-01-10 19:37:12', '123456');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
