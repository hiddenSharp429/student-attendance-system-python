-- 表 1 学生实体表
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    class_no VARCHAR(10),
    email VARCHAR(100),
    password VARCHAR(50)
);

-- 表 2 教师实体表
CREATE TABLE Teacher (
    teacher_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(50)
);

-- 表 3 课程实体表
CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    teacher_id INT,
    description TEXT,
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

-- 表 4 考勤实体表
CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    attendance_date DATE,
    status VARCHAR(20),
    reason TEXT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- 表 5 请假申请实体表
CREATE TABLE LeaveApplication (
    leave_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    leave_date DATE,
    reason TEXT,
    status VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- 表 6 考勤任务实体表
CREATE TABLE AttendanceTask (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT,
    teacher_id INT,
    task_date DATE,
    code VARCHAR(20),
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

-- 表 7 课程表实体表
CREATE TABLE ClassSchedule (
    schedule_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT,
    day_of_week VARCHAR(10),
    start_time TIME,
    end_time TIME,
    location VARCHAR(100),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- 表 8 请假缺勤状态记录实体表
CREATE TABLE LeaveRecord (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    teacher_id INT,
    status VARCHAR(20),
    week INT,
    date DATE,
    leave_reason TEXT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

-- 表 9 每位老师的课程信息实体表
CREATE TABLE TeacherSchedule (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    teacher_id INT,
    course_id INT,
    course_name VARCHAR(100),
    date DATE,
    section VARCHAR(20),
    semester VARCHAR(20),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- 表 10 学生学期考勤记录实体表
CREATE TABLE StudentAttendanceRecord (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    student_name VARCHAR(100),
    course_id INT,
    teacher_id INT,
    date DATE,
    semester VARCHAR(20),
    status VARCHAR(20),
    reason TEXT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

-- 表 11 课程考勤状态实体表
CREATE TABLE CourseAttendance (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT,
    student_id INT,
    student_name VARCHAR(100),
    teacher_id INT,
    date DATE,
    status VARCHAR(20),
    leave_reason TEXT,
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

-- 表 12 单独课程信息实体表
CREATE TABLE CourseInfo (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    teacher_id INT,
    description TEXT,
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

-- 表 13 学生每学期课程考勤情况实体表
CREATE TABLE StudentCourseAttendance (
    student_id INT,
    course_id INT,
    semester VARCHAR(20),
    total_attendance INT,
    total_absent INT,
    total_late INT,
    PRIMARY KEY (student_id, course_id, semester),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- 表 14 IP和API访问关系实体表
CREATE TABLE IPApiAccess (
    access_id INT PRIMARY KEY AUTO_INCREMENT,
    ip_address VARCHAR(45),
    api_endpoint VARCHAR(255),
    access_date DATE,
    access_port INT,
    access_count INT
);

-- 表 15 IP黑名单实体表
CREATE TABLE IPBan (
    ban_id INT PRIMARY KEY AUTO_INCREMENT,
    ip_address VARCHAR(45),
    mac_address VARCHAR(255),
    ban_date DATE,
    ban_duration INT
);