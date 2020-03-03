-- Lists all cities contained in the database hbtn_0d_usa
-- Displaying cities.id, cities.name, states.name
SELECT cities.id, cities.name, states.name
FROM states
     RIGHT JOIN cities ON cities.sate_id = states.id;
