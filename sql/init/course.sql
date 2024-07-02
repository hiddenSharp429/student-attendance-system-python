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

 Date: 01/07/2024 15:16:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `course_id` varchar(10) NOT NULL,
  `teacher_id` varchar(10) NOT NULL,
  `course_name` varchar(10) NOT NULL,
  `teacher_name` varchar(10) NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of course
-- ----------------------------
BEGIN;
INSERT INTO `course` (`course_id`, `teacher_id`, `course_name`, `teacher_name`) VALUES ('c1', 'T001', '操作系统原理', '张老师');
INSERT INTO `course` (`course_id`, `teacher_id`, `course_name`, `teacher_name`) VALUES ('c2', 'T001', '软件工程', '张老师');
INSERT INTO `course` (`course_id`, `teacher_id`, `course_name`, `teacher_name`) VALUES ('c3', 'T006', '编译原理', '吴老师');
INSERT INTO `course` (`course_id`, `teacher_id`, `course_name`, `teacher_name`) VALUES ('c4', 'T007', '软件工程', '恒老师');
INSERT INTO `course` (`course_id`, `teacher_id`, `course_name`, `teacher_name`) VALUES ('c5', 'T002', 'ELC4', 'Banana');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
