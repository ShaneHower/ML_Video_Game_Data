SELECT  
CASE When Genre = 'Platform' Then 1
     ELSE 0 
     END AS Is_Platform,
CASE WHEN Genre = 'Sports' Then 1
	 ELSE 0
     END AS Is_Sports,
CASE WHEN Genre = 'Racing' Then 1
	 ELSE 0 
     END AS Is_Racing,
CASE WHEN Genre = 'Role-Playing' THEN 1 
	 ELSE 0 
     END AS Is_RPG,
CASE WHEN Genre = 'Puzzle' THEN 1
	 ELSE 0
     END AS Is_Puzzle,
CASE WHEN Genre = 'Misc' THEN 1 
	 ELSE 0 
     END AS Is_Misc,
CASE WHEN Genre = 'Shooter' THEN 1
	 ELSE 0 
     END AS Is_Shooter,
CASE WHEN Genre = 'Simulation' THEN 1
	 ELSE 0 
     END AS Is_Sim,
CASE WHEN Genre = 'Action' THEN 1
	 ELSE 0 
     END AS Is_Action,
CASE WHEN Genre = 'Fighting' THEN 1
	 ELSE 0 
     END AS Is_Fighting,
CASE WHEN Genre = 'Adventure' THEN 1
	 ELSE 0
     END AS Is_Adventure,
CASE WHEN Genre = 'Strategy' THEN 1
	 ELSE 0
     END AS Is_Strategy   
FROM video_game_data;
