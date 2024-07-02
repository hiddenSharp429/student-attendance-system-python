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

 Date: 01/07/2024 15:16:32
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for student_information
-- ----------------------------
DROP TABLE IF EXISTS `student_information`;
CREATE TABLE `student_information` (
  `stu_id` varchar(10) NOT NULL,
  `stu_name` varchar(4) NOT NULL,
  `sex` varchar(1) DEFAULT NULL,
  `age` int(2) DEFAULT NULL,
  `institute` varchar(6) DEFAULT NULL,
  `major` varchar(10) DEFAULT NULL,
  `class_no` varchar(10) DEFAULT NULL,
  `dormitory` varchar(6) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`stu_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of student_information
-- ----------------------------
BEGIN;
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611001', '代青草', '女', 18, '工学院', '计算机科学与技术', '1', 'A901', '12345678901', '2101@outlook.com', '123456');
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611004', '吴茵', '女', 18, '工学院', '计算机科学与技术', '4', 'A904', '12345678904', '2104@outlook.com', '123456');
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611003', '陈彩怡', '女', 18, '工学院', '计算机科学与技术', '3', 'A903', '12345678903', '2103@outlook.com', '123456');
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611007', '祝子贤', '男', 19, '工学院', '计算机科学与技术', '6', 'A907', '12345678907', '2107@outlook.com', '123456');
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611006', '陈尚铭', '男', 19, '工学院', '计算机科学与技术', '5', 'A906', '12345678906', '2106@outlook.com', '123456');
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611010', '杨锦', '男', 19, '工学院', '计算机科学与技术', '7', 'A910', '12345678900', '2100@outlook.com', '123456');
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611008', '陆伟', '男', 19, '工学院', '计算机科学与技术', '6', 'A908', '12345678908', '2108@outlook.com', '123456');
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611009', '梁根华', '男', 19, '工学院', '计算机科学与技术', '7', 'A909', '12345678909', '2109@outlook.com', '123456');
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611002', '殷海珊', '女', 18, '工学院', '计算机科学与技术', '2', 'A902', '12345678902', '2102@outlook.com', '123456');
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611005', '曾渝翔', '男', 19, '工学院', '计算机科学与技术', '5', 'A905', '12345678905', '2105@outlook.com', '123456');
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611011', '张三', '男', 20, '工学院', '计算机科学与技术', '1', 'A991', '1234567890', '2100@outlook.com', '123456');
INSERT INTO `student_information` (`stu_id`, `stu_name`, `sex`, `age`, `institute`, `major`, `class_no`, `dormitory`, `phone`, `email`, `password`) VALUES ('2021611012', '李四', '男', 20, '工学院', '计算科学', '1', 'D501', '1234567890', '1231@example.com', '123456');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
