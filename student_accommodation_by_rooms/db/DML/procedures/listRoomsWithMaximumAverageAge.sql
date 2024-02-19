USE hostelDB;
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
