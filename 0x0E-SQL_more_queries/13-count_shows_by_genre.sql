-- Listing all genres from a DB
-- And display the number of shows
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY genre
ORDER BY number_of_shows DESC;
