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

 Date: 01/07/2024 15:16:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for course_selection
-- ----------------------------
DROP TABLE IF EXISTS `course_selection`;
CREATE TABLE `course_selection` (
  `course_id` varchar(10) NOT NULL,
  `student_id` varchar(10) NOT NULL,
  `teacher_id` varchar(10) NOT NULL,
  `course_name` varchar(10) NOT NULL,
  `teacher_name` varchar(10) NOT NULL,
  `semester` varchar(10) NOT NULL DEFAULT '2023',
  PRIMARY KEY (`course_id`,`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of course_selection
-- ----------------------------
BEGIN;
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c1', '2021611001', 'T001', '操作系统原理', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c1', '2021611003', 'T001', '操作系统原理', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c1', '2021611004', 'T001', '操作系统原理', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c1', '2021611006', 'T001', '操作系统原理', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c1', '2021611009', 'T001', '操作系统原理', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c1', '2021611011', 'T001', '操作系统原理', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c2', '2021611002', 'T001', '软件工程', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c2', '2021611005', 'T001', '软件工程', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c2', '2021611006', 'T001', '软件工程', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c2', '2021611007', 'T001', '软件工程', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c2', '2021611008', 'T001', '软件工程', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c2', '2021611010', 'T001', '软件工程', '张老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c3', '2021611001', 'T006', '编译原理', '吴老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c3', '2021611003', 'T006', '编译原理', '吴老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c3', '2021611004', 'T006', '编译原理', '吴老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c3', '2021611005', 'T006', '编译原理', '吴老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c3', '2021611008', 'T006', '编译原理', '吴老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c3', '2021611009', 'T006', '编译原理', '吴老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c4', '2021611002', 'T007', '软件工程', '恒老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c4', '2021611006', 'T007', '软件工程', '恒老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c4', '2021611007', 'T007', '软件工程', '恒老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c4', '2021611010', 'T007', '软件工程', '恒老师', '2023');
INSERT INTO `course_selection` (`course_id`, `student_id`, `teacher_id`, `course_name`, `teacher_name`, `semester`) VALUES ('c5', '2021611001', 'T002', 'ELC4', 'Banana', '2023');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
