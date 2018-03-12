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
I used a Random Forest Classifier to determine the Gini Importance of each feature and then tested the prediction accuracy of the most important features.  The highest scored features were 'JP_Sales' and 'publisher_ID'.  
```
('year', 0.11848553171147959)
('NA_Sales', 0.059255530505788398)
('EU_Sales', 0.049575393564702808)
('JP_Sales', 0.12845992481189905)
('Other_Sales', 0.03416596307311124)
('Global_Sales', 0.10741830360290834)
('Critic_Score', 0.047943435079066704)
('Critic_Count', 0.049539872228269673)
('User_Score', 0.048877610502863128)
('User_Count', 0.066368160246393956)
('publisher_ID', 0.18022073942406219)
('platform_ID', 0.071075695936882538)
('Title_RPG', 0.038613839312572333)
```
The full feature accuracy test and selected feature accuracy test resulted in a value of 92%.  That's pretty high! However, is our model actually good at predicting if an unknown game is an RPG.  The way we can test this is by looking at the precision and recall scores.  Precision is the percentage of true positives(predicted true and were actually true) out of the all predicted values (both true positives and false positives).  This answers the question "how many selected items are relevant?".  Recall, on the other hand, is the percentage of true positives out of all true values (false negatives-pred false but were true, and true positives).  This answers the question "how many relevant items were selected?".  SKlearn has a quick method of finding both of these.
```
p_score = precision_score(y_test, y_important_pred)
r_score = recall_score(y_test, y_important_pred)
```
The reason precision and recall are better metrics to determine the usefulness of a model is because accuracy returns a value of all predictions over all possible values (TP + FP)/ (TP + FP + TN + FN).  This means that, if only a small percentage of our data is in the RPG genre, our accuracy will be higher because we will likely be guessing that a game is not an RPG most of the time.  High precision means most of our guesses were right while high recall means that out of all the RPGs we predicted most of them.  Unfortunately, this is not what our scores show.  Below is a visual aid showing the precision-recall curve: 

![figure_1](https://user-images.githubusercontent.com/34482822/37307147-58aa713e-2610-11e8-90ab-89fd88181bdd.png)

## Experimenting to Increase Accuracy
To try and increase the accuracy score for this prediction model I decided to experiment and see if the names could increase the prediction accuracy.  The way I approached this problem was to create a list of unique names and check if a title contained any of those names.  It would then create a new column and assign that entry 'True' if that word was in the title or 'False' otherwise.  so for instance, let's say I have this data set:  
![before name split](https://user-images.githubusercontent.com/34482822/37256623-bfc2b13e-2533-11e8-8206-c215156ed72c.png)

After running through the python script I would end up with a new data set:
![after name split](https://user-images.githubusercontent.com/34482822/37256629-d3abf0a2-2533-11e8-9b50-02443bef3c07.png)

Unfortunately, this made the prediction even less accurate.  There was not a Gini importance score higher than 0.1. As you could guess, this also created a tremendous amount of features (11,047).  These were a few of Gini importance scores.  The most important still being JP_Sales and Publisher_ID.
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
Precision and Recall are listed below along with the precision recall curve.
```
precision: 0.5327868852459017
recall: 0.11149228130360206
Average precision-recall score: 0.14
```
![figure_1](https://user-images.githubusercontent.com/34482822/37305761-f0f693c8-260b-11e8-97b4-376e8aa8aac9.png)

## Multi Label attempt
Above was a single label multi class attempt (Genre was the label, the classes were the 12 different genre names).  I then tried a multi label binary class strategy as a final attempt to increase the accuracy of the prediction.  In order to do this I had to create a new column representing the name of each genre and assign a binary value (True or False) for each game.  Here is an example data set that will demonstrate how this works.  The original data frame will look like this:   


![screen shot 2018-03-11 at 2 17 14 pm](https://user-images.githubusercontent.com/34482822/37256898-58f028fc-2537-11e8-9795-c86ae68c3589.png)

After running the SQL script we'll end up with a data frame which looks like this:

![screen shot 2018-03-11 at 2 19 02 pm](https://user-images.githubusercontent.com/34482822/37256901-70976b64-2537-11e8-820e-f2aca988e0c9.png)
