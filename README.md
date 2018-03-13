# ML_Video_Game_Data 
This project attempts to construct a model which will predict if a game belongs to the RPG genre based on important features (such as the developer, sales and year of release). 

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
I needed two data sets.  The first data set gave a binary value to each row which indicated if a game was an RPG (1) or not (0).  This would be my y value, the value which will be the target array.  The second set was a set of selected features.  If these features were strings they were then converted into numerical ID's.  Columns were added to experiment with new features such as assigning a binary value to titles with names like "Quest", "Fantasy", or "Dragon". This feature would suggest that such a title would be an RPG.

## Feature Selection
I used a Random Forest Classifier to determine the Gini Importance of each feature and then tested the prediction accuracy of the most important features.  The highest scored features were 'publisher_ID'and 'JP_Sales'.  Here are the scores from highest to lowest. 
```
('publisher_ID', 0.18022073942406219)
('JP_Sales', 0.12845992481189905)
('year', 0.11848553171147959)
('Global_Sales', 0.10741830360290834)
('platform_ID', 0.071075695936882538)
('User_Count', 0.066368160246393956)
('NA_Sales', 0.059255530505788398)
('EU_Sales', 0.049575393564702808)
('Critic_Count', 0.049539872228269673)
('User_Score', 0.048877610502863128)
('Critic_Score', 0.047943435079066704)
('Title_RPG', 0.038613839312572333)
('Other_Sales', 0.03416596307311124)
```
The full feature accuracy test and selected feature accuracy test resulted in a value of 92%.  That's pretty high! However, is our model actually good at predicting if an unknown game is an RPG.  The way we can test this is by looking at the precision and recall scores.  Precision is the percentage of true positives(predicted true and were actually true) out of the all predicted values (both true positives and false positives).  This answers the question "how many selected items are relevant?".  Recall, on the other hand, is the percentage of true positives out of all true values (false negatives-pred false but were true, and true positives).  This answers the question "how many relevant items were selected?".  SKlearn has a quick method of finding both of these.
```
p_score = precision_score(y_test, y_important_pred)
r_score = recall_score(y_test, y_important_pred)
```
Our precision score was 53%, which means 53% of our predictions were predicted true and were actually true. Our Recall was 26%, which means out of all the games that were RPGs, we predicted that 26% of them were in the RPG genre while predicting 74% were not.  Both of these are low values which means that, even though our accuracy is high, this model does not make very good predictions.  

The reason precision and recall are better metrics to determine the usefulness of a model is because accuracy returns a value of all predictions over all possible values (TP + FP)/ (TP + FP + TN + FN).  This means that, if only a small percentage of our data is in the RPG genre, our accuracy will be higher because we will likely be guessing that a game is not an RPG most of the time.  High precision means most of our guesses were right while high recall means that out of all the RPGs we predicted most of them correctly.  Unfortunately, this is not what our scores show.  Below is a visual aid showing the precision-recall curve: 

![figure_1](https://user-images.githubusercontent.com/34482822/37307147-58aa713e-2610-11e8-90ab-89fd88181bdd.png)

## Experimenting
To try and increase the Precision/ Recall score for this prediction model I decided to experiment and see if the names could help our prediction.  The way I approached this problem was to create a list of unique names and check if a title contained any of those names.  It would then create a new column and assign that entry 'True' if that word was in the title or 'False' otherwise.  so for instance, let's say I have this data set:  
![before name split](https://user-images.githubusercontent.com/34482822/37256623-bfc2b13e-2533-11e8-8206-c215156ed72c.png)

After running through the python script I would end up with a new data set:
![after name split](https://user-images.githubusercontent.com/34482822/37256629-d3abf0a2-2533-11e8-9b50-02443bef3c07.png)

Once this python script was applied to the data, I ran it through the model once more.  Our accuracy stayed at 92% for our selected features, however, there was not a Gini importance score higher than 0.01. As you could guess, this also created a tremendous amount of features (11,047).  These were a few of Gini importance scores.
#### Highest Gini Importance 
```
('JP_Sales', 0.029354910983696695)
('Unnamed: 0', 0.018351900225702045)
('publisher_ID', 0.017511158250049563)
('Global_Sales', 0.017380643803780377)
('year', 0.015155475873391094)
('NA_Sales', 0.013747328445000276)
('User_Count', 0.013643938172559019)
('platform_ID', 0.012177256447408843)
('EU_Sales', 0.012049350879789171)
('Critic_Count', 0.010917642625512645)
('User_Score', 0.01060711768162452)
('Other_Sales', 0.0096580896133686093)
('Critic_Score', 0.0093791033194381875)
('Title_RPG', 0.0091095749319983418)
('Dungeon', 0.0087256851922068012)
('Fantasy', 0.008140674170992979)
('Tales', 0.0056895931458593018)
('Online', 0.0056726082607470776)
('on', 0.0049626779158669426)
('Dragon', 0.0046917916373075451)
```

#### Lowest Gini Importance
```
('Slightly', 0.0)
('Sugar', 0.0)
('Spice!', 0.0)
('Anoko', 0.0)
('Suteki', 0.0)
('Nanimokamo', 0.0)
('Kanokon:', 0.0)
('Esuii', 0.0)
('Tsukigime', 0.0)
("Ranko's", 0.0)
('Shirayuki', 0.0)
('Kajitsu:', 0.0)
('Scarlett:', 0.0)
('Nichijou', 0.0)
('Kyoukaisen', 0.0)
('Breach', 0.0)
('3000', 0.0)
('Nauts', 0.0)
('Plushees', 0.0)
('LMA', 0.0)
```
Our precision remained the same at 53%, but our recall had a significant decrease at 11%.  So this experiment did not really help our predictions.  Below is the Precision-Recall curve for this data set.

![figure_1](https://user-images.githubusercontent.com/34482822/37310459-56cd2cf8-261a-11e8-94b3-b1eb537e1dec.png)

## Conclusion 
After trying a few different strategies to increase the prediction capabilities of this model we still had very low Precision and Recall scores.  This leads us to believe that our data does not have relevant features to make these kind of predictions.  We need new features prehaps covering ground such as average age or gender of consumers, length of games, multiplayer capabilities, etc.
