-- lists all Comedy shows in the database hbtn_0d_tvshows

SELECT title
FROM tv_shows AS tv
JOIN tv_show_genres AS tv_g
ON tv.id = tv_g.show_id
WHERE genre_id = (
    SELECT id FROM tv_genres WHERE name = 'Comedy')
ORDER BY title;
