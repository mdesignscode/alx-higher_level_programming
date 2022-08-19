-- lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT tv.title, tv_g.genre_id
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS tv_g
ON tv.id = tv_g.show_id
WHERE genre_id IS NULL
ORDER BY tv.title, tv_g.genre_id;
