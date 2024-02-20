-- Create a database
CREATE DATABASE IF NOT EXISTS hostelDB;
USE hostelDB;

-- Create the Rooms table
DROP TABLE IF EXISTS room_list;
CREATE TABLE IF NOT EXISTS room_list(
    ID BIGINT  UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
    room_id INT UNSIGNED NOT NULL UNIQUE,
    room_name VARCHAR(15) NOT NULL,
    PRIMARY KEY (ID)
);

-- Create the Students table
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

DELIMITER //
CREATE PROCEDURE IF NOT EXISTS get_rooms_with_different_sex()
BEGIN
	WITH cte_students_sex AS (
		SELECT rl.room_name,
			COUNT(DISTINCT(sl.sex)) AS count_sex
		FROM room_list rl LEFT JOIN students_list sl
			ON rl.room_id = sl.room_id
		GROUP BY rl.room_name
	)
	SELECT cs.room_name
	FROM cte_students_sex AS cs
	WHERE cs.count_sex > 1;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE IF NOT EXISTS get_max_average_age()
BEGIN
	WITH cte_students_age AS (
		SELECT rl.room_name,
			sl.student_name,
			TIMESTAMPDIFF(YEAR, sl.birthday, curdate()) AS age
		FROM room_list rl LEFT JOIN students_list sl
			ON rl.room_id = sl.room_id
		GROUP BY rl.room_name, sl.student_name, age
	),
	cte_avg_age AS (
		SELECT cs.room_name,
			AVG(cs.age) AS average_age
		FROM cte_students_age AS cs
		GROUP BY cs.room_name
	),
	cte_max_avg AS (
		SELECT ca.room_name,
			ca.average_age
		FROM cte_avg_age AS ca
		WHERE ca.average_age IS NOT NULL
		ORDER BY ca.average_age DESC
		LIMIT 5
	)
	SELECT cmax.room_name,
		cmax.average_age
	FROM cte_max_avg AS cmax;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE IF NOT EXISTS get_min_average_age()
BEGIN
	WITH cte_students_age AS (
		SELECT rl.room_name,
			sl.student_name,
			TIMESTAMPDIFF(YEAR, sl.birthday, curdate()) AS age
		FROM room_list rl LEFT JOIN students_list sl
			ON rl.room_id = sl.room_id
		GROUP BY rl.room_name, sl.student_name, age
	),
	cte_avg_age AS (
		SELECT cs.room_name,
			AVG(cs.age) AS average_age
		FROM cte_students_age AS cs
		GROUP BY cs.room_name
	),
	cte_min_avg AS (
		SELECT ca.room_name,
			ca.average_age
		FROM cte_avg_age AS ca
		WHERE ca.average_age IS NOT NULL
		ORDER BY ca.average_age
		LIMIT 5
	)

	SELECT cmin.room_name,
		cmin.average_age
	FROM cte_min_avg AS cmin;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE IF NOT EXISTS get_amount_of_students_in_rooms()
BEGIN
	SELECT rl.room_name,
		COUNT(sl.student_name) AS students_amount
	FROM room_list rl LEFT JOIN students_list sl
		ON rl.room_id = sl.room_id
	GROUP BY rl.room_name;
END//
DELIMITER ;
