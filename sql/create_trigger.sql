-- 程人数改变或者课程人数达到一定的值时触发该机制
CREATE TRIGGER UpdateCourseStudentCount
AFTER INSERT ON CourseSelection
FOR EACH ROW
BEGIN
   UPDATE Course
   SET student_count = student_count + 1
   WHERE course_id = NEW.course_id;
END;