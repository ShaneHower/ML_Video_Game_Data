SELECT a.*, b.genre_id
FROM video_game a LEFT JOIN (
			      SELECT genre, @rownum:=@rownum + 1 AS genre_id
			      FROM(
				    SELECT DISTINCT Genre 
				    FROM  video_game
				  ) a,
			      (SELECT @rownum:= 0) r
			     ) b 
ON a.genre = b.genre;
