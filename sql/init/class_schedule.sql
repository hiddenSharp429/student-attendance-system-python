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

 Date: 01/07/2024 15:15:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for class_schedule
-- ----------------------------
DROP TABLE IF EXISTS `class_schedule`;
CREATE TABLE `class_schedule` (
  `schedule_id` int(11) NOT NULL,
  `course_id` varchar(10) NOT NULL,
  `day_of_week` varchar(10) NOT NULL,
  `start_time` int(11) NOT NULL,
  `end_time` int(11) NOT NULL,
  `start_week` int(10) NOT NULL DEFAULT '3',
  `end_week` int(10) NOT NULL DEFAULT '18',
  `id` int(10) NOT NULL,
  PRIMARY KEY (`schedule_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of class_schedule
-- ----------------------------
BEGIN;
INSERT INTO `class_schedule` (`schedule_id`, `course_id`, `day_of_week`, `start_time`, `end_time`, `start_week`, `end_week`, `id`) VALUES (1, 'c2', '5', 3, 5, 3, 18, 0);
INSERT INTO `class_schedule` (`schedule_id`, `course_id`, `day_of_week`, `start_time`, `end_time`, `start_week`, `end_week`, `id`) VALUES (2, 'c1', '4', 8, 9, 3, 18, 0);
INSERT INTO `class_schedule` (`schedule_id`, `course_id`, `day_of_week`, `start_time`, `end_time`, `start_week`, `end_week`, `id`) VALUES (3, 'c3', '2', 3, 4, 3, 18, 0);
INSERT INTO `class_schedule` (`schedule_id`, `course_id`, `day_of_week`, `start_time`, `end_time`, `start_week`, `end_week`, `id`) VALUES (4, 'c4', '5', 3, 5, 3, 18, 0);
INSERT INTO `class_schedule` (`schedule_id`, `course_id`, `day_of_week`, `start_time`, `end_time`, `start_week`, `end_week`, `id`) VALUES (5, 'c5', '4', 6, 7, 3, 18, 0);
INSERT INTO `class_schedule` (`schedule_id`, `course_id`, `day_of_week`, `start_time`, `end_time`, `start_week`, `end_week`, `id`) VALUES (6, 'c6', '1', 1, 2, 3, 18, 0);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
