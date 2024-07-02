-- 创建新的考勤记录
CREATE PROCEDURE AddAttendanceRecord(
   IN p_student_id INT,
   IN p_course_id INT,
   IN p_attendance_date DATE,
   IN p_status VARCHAR(10),
   IN p_reason VARCHAR(255)
)
BEGIN
   INSERT INTO Attendance (student_id, course_id, attendance_date, status, reason)
   VALUES (p_student_id, p_course_id, p_attendance_date, p_status, p_reason);
END;