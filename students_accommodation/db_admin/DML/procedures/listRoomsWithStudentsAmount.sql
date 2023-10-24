USE hostelDB;
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

CALL get_amount_of_students_in_rooms;
