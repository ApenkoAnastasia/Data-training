USE hostelDB;
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

CALL get_rooms_with_different_sex;
