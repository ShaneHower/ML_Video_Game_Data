# ML_Video_Game_Data
NOTE: this project is still being worked on. 
This project attempts to construct a model which will predict what genre a video game is based on features such as the developer, sales and year it was released. 

## Query the Data With SQL 
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


