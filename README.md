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

Unfortunately, this made the prediction even less accurate.  There was not a Gini importance score higher than 0.1.    

