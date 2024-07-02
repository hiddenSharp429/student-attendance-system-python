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

 Date: 01/07/2024 15:15:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for attendance_information
-- ----------------------------
DROP TABLE IF EXISTS `attendance_information`;
CREATE TABLE `attendance_information` (
  `stu_id` varchar(10) NOT NULL,
  `course_id` varchar(10) NOT NULL,
  `course_no` int(11) NOT NULL,
  `teacher_id` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `status` int(11) NOT NULL,
  `signin_time` time DEFAULT NULL,
  `signout_time` time DEFAULT NULL,
  `reason` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`stu_id`,`course_id`,`course_no`,`teacher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of attendance_information
-- ----------------------------
BEGIN;
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611001', 'c1', 1, 'T001', '2023-01-01', 1, '08:30:00', '12:30:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611001', 'c1', 2, 'T001', '2023-01-01', 2, NULL, NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611001', 'c1', 10, 'T001', '2024-01-01', 2, NULL, NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611001', 'c4', 1, 'T006', '2023-01-01', 1, '08:30:00', '12:30:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611002', 'c3', 2, 'T001', '2023-01-02', 1, '09:00:00', '13:00:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611002', 'c5', 2, 'T007', '2023-01-02', 1, '09:00:00', '13:00:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611003', 'c1', 2, 'T001', '2023-01-02', 1, '09:00:00', '13:00:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611003', 'c4', 2, 'T006', '2023-01-02', 1, '09:00:00', '13:00:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611004', 'c1', 3, 'T001', '2023-01-03', 2, NULL, NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611004', 'c4', 3, 'T006', '2023-01-03', 0, NULL, NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611005', 'c2', 5, 'T001', '2023-01-05', 2, NULL, NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611005', 'c4', 4, 'T006', '2023-01-04', 1, '10:30:00', '14:30:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611006', 'c1', 2, 'T001', '2023-01-01', 0, '00:00:00', NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611006', 'c3', 3, 'T001', '2023-01-03', 0, NULL, NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611006', 'c5', 3, 'T007', '2023-01-03', 0, NULL, NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611007', 'c3', 4, 'T001', '2023-01-04', 1, '10:30:00', '14:30:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611007', 'c5', 4, 'T007', '2023-01-04', 1, '10:30:00', '14:30:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611008', 'c2', 1, 'T001', '2023-01-01', 1, '08:30:00', '12:30:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611008', 'c4', 5, 'T006', '2023-01-05', 0, NULL, NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611009', 'c1', 4, 'T001', '2023-01-04', 1, '10:30:00', '14:30:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611009', 'c4', 1, 'T006', '2023-01-01', 1, '08:30:00', '12:30:00', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611010', 'c1', 16, 'T001', '2024-01-01', 1, '14:56:20', '14:56:20', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611010', 'c3', 5, 'T001', '2023-01-05', 0, NULL, NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611010', 'c5', 5, 'T007', '2023-01-05', 0, NULL, NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611011', 'c1', 14, 'T001', '2024-01-03', 0, NULL, NULL, '生病请假');
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611011', 'c1', 15, 'T001', '2023-01-01', 0, NULL, NULL, NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611011', 'c1', 16, 'T001', '2024-01-01', 1, '14:56:20', '14:56:20', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611011', 'c1', 17, 'T001', '2024-01-03', 3, NULL, NULL, '生病请假');
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611012', 'c1', 16, 'T001', '2024-01-01', 1, '14:56:20', '14:56:20', NULL);
INSERT INTO `attendance_information` (`stu_id`, `course_id`, `course_no`, `teacher_id`, `date`, `status`, `signin_time`, `signout_time`, `reason`) VALUES ('2021611012', 'c1', 17, 'T001', '2024-01-01', 1, '14:49:39', '14:49:39', NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
