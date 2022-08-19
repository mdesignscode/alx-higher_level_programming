-- lists all shows contained in the database hbtn_0d_tvshows.

SELECT tv.title, tv_g.genre_id
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS tv_g
ON tv.id = tv_g.show_id
ORDER BY tv.title, tv_g.genre_id;
