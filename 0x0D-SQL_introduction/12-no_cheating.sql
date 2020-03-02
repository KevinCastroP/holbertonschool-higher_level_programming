-- Cheating is bad update the attribute score in a table
UPDATE `second_table`
SET `score` = 10
WHERE `second_table`.`name`='Bob';
