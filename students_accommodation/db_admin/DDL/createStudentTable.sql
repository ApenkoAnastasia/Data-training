USE hostelDB;
DROP TABLE IF EXISTS students_list;
CREATE TABLE IF NOT EXISTS students_list(
    ID BIGINT  UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
    student_id INT UNSIGNED NOT NULL UNIQUE,
    student_name VARCHAR(50) NOT NULL,
    birthday DATETIME,
    sex VARCHAR(15) NOT NULL,
    room_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (room_id) REFERENCES hostelDB.room_list(room_id) ON UPDATE CASCADE ON DELETE CASCADE
);
