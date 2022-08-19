-- lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each.

SELECT name AS number_of_shows, COUNT(genre_id) AS genre
FROM tv_show_genres
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name
ORDER BY COUNT(genre_id) DESC;
