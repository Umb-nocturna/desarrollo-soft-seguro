DELIMITER //
CREATE PROCEDURE `sp_list_avengers`()
BEGIN
    SELECT AV.id, AV.name, AV.url 
    FROM avengers AV
    ORDER BY AV.name ASC;
END //
DELIMITER ;