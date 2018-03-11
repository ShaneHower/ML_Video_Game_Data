
-- first had to clean up the names column of the data 
UPDATE video_game
SET name = SUBSTRING_INDEX(name,'(', 1);

UPDATE video_game_data
SET Name = REPLACE(Name, '+', 'plus');

UPDATE video_game_data
SET Name = REPLACE(Name, '[', '');

UPDATE video_game_data
SET Name = REPLACE(Name, ']', '');

UPDATE video_game_data
SET NAME = REPLACE(Name, '*', '');

UPDATE video_game_data
SET Name = REPLACE(Name, '?', '');

--- Data set 1 that is the original data set with a new row added which assigns an ID for each genre.
SELECT a.*, b.genre_id
FROM video_game a LEFT JOIN (
			      SELECT genre, @rownum:=@rownum + 1 AS genre_id
			      FROM(
				    SELECT DISTINCT Genre 
				    FROM  video_game
				  ) a, (SELECT @rownum:= 0) r) b 
ON a.genre = b.genre;


--- Data set 2 which is all numbered values.  This required the creation of publisher_ID and Platform_ID as well as an experimental row 
--- that assigned a binary value based on if the words 'Dragon', 'Fantasy', or 'Quest' showed up in the title (Was created to guess if
--- a title was an RPG).  This column was called Title_RPG.

SELECT a.year, a.NA_Sales, a.EU_Sales, a.JP_Sales,
a.Other_Sales, a.Global_Sales, a.Critic_Score, a.Critic_Count,
a.User_Score, a.User_Count, b.publisher_ID, c.platform_ID, 
			 CASE WHEN name LIKE('%Dragon%') 
					OR name LIKE('%Quest%') 
                    			OR name LIKE('%Fantasy%')
				  	THEN 1
                  			ELSE 0 
                  			END AS Title_RPG
FROM video_game a LEFT JOIN (
				SELECT publisher, @rownum:=@rownum + 1 AS publisher_id
				FROM(
					SELECT DISTINCT publisher
					FROM  video_game
				     ) a, (SELECT @rownum:= 0) r) b 
ON a.publisher = b.publisher
LEFT JOIN (
		SELECT platform, @rownum:=@rownum + 1 AS platform_id
		FROM(
			SELECT DISTINCT platform
			FROM  video_game
		     ) a, (SELECT @rownum:= 0) r) c 
ON c.platform = a.Platform;
 
