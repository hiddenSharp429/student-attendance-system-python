-- 展示某个学生的所有考勤记录。
CREATE VIEW StudentAttendanceView AS
SELECT s.student_id, s.name, c.course_name, a.attendance_date, a.status
FROM Student s
JOIN Attendance a ON s.student_id = a.student_id
JOIN Course c ON a.course_id = c.course_id;

-- 展示某门课程的所有考勤记录。
CREATE VIEW CourseAttendanceView AS
SELECT c.course_id, c.course_name, t.name as teacher_name, a.attendance_date, a.status
FROM Course c
JOIN Teacher t ON c.teacher_id = t.teacher_id
JOIN Attendance a ON c.course_id = a.course_id;

-- 展示所有代审批的请假申请。
CREATE VIEW PendingLeaveApplicationsView AS
SELECT l.leave_id, s.name as student_name, c.course_name, l.leave_date, l.reason
FROM LeaveApplication l
JOIN Student s ON l.student_id = s.student_id
JOIN Course c ON l.course_id = c.course_id
WHERE l.status = '待审批';