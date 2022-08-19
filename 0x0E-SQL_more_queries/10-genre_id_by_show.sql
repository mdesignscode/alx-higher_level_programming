-- lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.

SELECT tv.title, tv_g.genre_id
FROM tv_shows AS tv
JOIN tv_show_genres AS tv_g
ON tv.id = tv_g.show_id
ORDER BY tv.title, tv_g.genre_id;
