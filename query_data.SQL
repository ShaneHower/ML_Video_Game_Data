Select *, 
	CASE Genre
    When 'Strategy' Then 1
    When 'Sports' Then 2
    When 'Simulation' Then 3 
    When 'Shooter' Then 4 
    When 'Role-Playing' Then 5
    When 'Racing' Then 6
    When 'Puzzle' Then 7 
    When 'Platform' Then 8
    When 'Misc' Then 9
    When 'Fighting' Then 10 
    When 'Adventure' Then 11
    When 'Action' Then 12 
    ELSE 0 
    END AS Genre_Code
FROM video_game;
