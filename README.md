# ML_Video_Game_Data
NOTE: this project is still being worked on. 
This project attempts to construct a model which will predict the genre of a game based on important features (such as the developer, sales and year of release). 

## Query the Data With SQL 

Before writing queries for the data I had to clean up the 'name' column.  Many of the names had parentheses with extra info. 
```
Star Wars Battlefront (2015)
GranTurismo (PSP)
Ghostbusters: The Video Game (DS Version)
Need for Speed (2015)
```
This was done with SUBSTRING_INDEX.  It deleted all text to the right of the first parenthesis.   
```
UPDATE video_game
SET name = SUBSTRING_INDEX(name,'(', 1);
```
I needed two data sets.  The first data set assigned a number value for each genre.  This would be my y value, the value which will be the target array.  The second set was a set of selected features.  If these features were strings they were then converted into numerical ID's.  Columns were added to experiment with new features such as assigning a binary value to titles with names like "Quest", "Fantasy", or "Dragon". This feature would suggest that such a title would be an RPG.

## Feature Selection
I used a Random Forest Classifier to determine the Gini Importance of each feature and then tested the prediction accuracy of the most important features.  The highest scored features were 'year' and 'publisher_ID'.  
```
('year', 0.13005406070026165)
('NA_Sales', 0.089904957130345214)
('EU_Sales', 0.07260498069548442)
('JP_Sales', 0.057750998861481391)
('Other_Sales', 0.048306608705714738)
('Global_Sales', 0.11818121043717715)
('Critic_Score', 0.059801046552611536)
('Critic_Count', 0.056623250344442898)
('User_Score', 0.050311115297393537)
('User_Count', 0.056836872777804595)
('publisher_ID', 0.17245136612221484)
('platform_ID', 0.079366220646172908)
('Title_RPG', 0.0078073117288951334)
```
The full feature accuracy test resulted in a value of 0.3739 while the selected feature accuracy test resulted in a value of 0.3146.

## Experimenting to Increase Accuracy
To try and increase the accuracy score for this prediction model I decided to experiment and see if the names could give any indication as to what a game's genre is.  The way I approached this problem was to create a list of unique names and check if a title contained any of those names.  It would then create a new column and assign that entry 'True' if that word was in the title or 'False' otherwise.  so for instance, let's say I have this data set:  
![before name split](https://user-images.githubusercontent.com/34482822/37256623-bfc2b13e-2533-11e8-8206-c215156ed72c.png)

After running through the python script I would end up with a new data set:
![after name split](https://user-images.githubusercontent.com/34482822/37256629-d3abf0a2-2533-11e8-9b50-02443bef3c07.png)

Unfortunately, this made the prediction even less accurate.  There was not a Gini importance score higher than 0.1. As you could guess, this also created a tremendous amount of features.  These were a few of Gini importance scores.
```
('Wii', 0.0002298817063839135)
('Sports', 0.00048535764702372362)
('Super', 0.0014892024887904979)
('Mario', 0.00039889619846502104)
('Bros.', 0.00011786916624944699)
('Kart', 0.00022619694561400733)
('Resort', 0.00010219451420683444)
('Pokemon', 0.00016330194273440419)
('Red/Pokemon', 4.1832118225979434e-06)
('Blue', 0.00029074344591355406)
('Tetris', 0.00018446474938745266)
('New', 0.00040730233964280922)
```
## Multi Label attempt
Above was a single label multi class attempt (Genre was the label, the classes were the 12 different genre names).  I then tried a multi label binary class strategy as a final attempt to increase the accuracy of the prediction.  In order to do this I had to create a new column representing the name of each genre and assign a binary value (True or False) for each game.  Here is an example data set that will demonstrate how this works.  The original data frame will look like this:   


![screen shot 2018-03-11 at 2 17 14 pm](https://user-images.githubusercontent.com/34482822/37256898-58f028fc-2537-11e8-9795-c86ae68c3589.png)

After running the SQL script we'll end up with a data frame which looks like this:

![screen shot 2018-03-11 at 2 19 02 pm](https://user-images.githubusercontent.com/34482822/37256901-70976b64-2537-11e8-820e-f2aca988e0c9.png)
