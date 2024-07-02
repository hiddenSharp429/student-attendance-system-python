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

 Date: 01/07/2024 15:16:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for teacher_information
-- ----------------------------
DROP TABLE IF EXISTS `teacher_information`;
CREATE TABLE `teacher_information` (
  `teacher_id` varchar(10) NOT NULL,
  `teacher_name` varchar(10) NOT NULL,
  `sex` varchar(1) NOT NULL,
  `age` int(11) NOT NULL,
  `institute` varchar(6) DEFAULT NULL,
  `major` varchar(10) DEFAULT NULL,
  `email` varchar(20) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `office` varchar(10) DEFAULT NULL,
  `home` varchar(10) DEFAULT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of teacher_information
-- ----------------------------
BEGIN;
INSERT INTO `teacher_information` (`teacher_id`, `teacher_name`, `sex`, `age`, `institute`, `major`, `email`, `phone_number`, `office`, `home`, `password`) VALUES ('T001', '张老师', '男', 35, '计算机', '计算机科学与技术', '1@email.com', '12345678901', 'OfficeA', 'HomeA', '123456');
INSERT INTO `teacher_information` (`teacher_id`, `teacher_name`, `sex`, `age`, `institute`, `major`, `email`, `phone_number`, `office`, `home`, `password`) VALUES ('T002', '王老师', '女', 40, '数学', '应用数学', '2@email.com', '12345678902', 'OfficeB', 'HomeB', '123456');
INSERT INTO `teacher_information` (`teacher_id`, `teacher_name`, `sex`, `age`, `institute`, `major`, `email`, `phone_number`, `office`, `home`, `password`) VALUES ('T003', '李老师', '男', 38, '物理', '光电子学', '3@email.com', '12345678903', 'OfficeC', 'HomeC', '123456');
INSERT INTO `teacher_information` (`teacher_id`, `teacher_name`, `sex`, `age`, `institute`, `major`, `email`, `phone_number`, `office`, `home`, `password`) VALUES ('T004', '赵老师', '女', 42, '化学', '有机化学', '4@email.com', '12345678904', 'OfficeD', 'HomeD', '123456');
INSERT INTO `teacher_information` (`teacher_id`, `teacher_name`, `sex`, `age`, `institute`, `major`, `email`, `phone_number`, `office`, `home`, `password`) VALUES ('T005', '陈老师', '男', 36, '生物', '生物工程', '5@email.com', '12345678905', 'OfficeE', 'HomeE', '123456');
INSERT INTO `teacher_information` (`teacher_id`, `teacher_name`, `sex`, `age`, `institute`, `major`, `email`, `phone_number`, `office`, `home`, `password`) VALUES ('T006', '吴老师', '男', 35, '计算机', '大数据科学与技术', '6@email.com', '12345678906', 'OfficeA', 'HomeA', '123456');
INSERT INTO `teacher_information` (`teacher_id`, `teacher_name`, `sex`, `age`, `institute`, `major`, `email`, `phone_number`, `office`, `home`, `password`) VALUES ('T007', '恒老师', '女', 40, '计算机', '软件工程', '7@email.com', '12345678907', 'OfficeB', 'HomeB', '123456');
INSERT INTO `teacher_information` (`teacher_id`, `teacher_name`, `sex`, `age`, `institute`, `major`, `email`, `phone_number`, `office`, `home`, `password`) VALUES ('T008', 'Dr.Smith', '男', 40, '计算机', '计算机科学与计算', '8@example.com', '12345678908', 'OfficeF', 'HomeF', '123456');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
