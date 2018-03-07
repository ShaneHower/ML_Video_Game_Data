import pandas as pd
from numpy import array
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score


df1 = pd.read_csv('/Users/shanehower/Desktop/vg_data/publisher_id.csv')
df2 = pd.read_csv('/Users/shanehower/Desktop/vg_data/only_numbered_columns.csv')

def conv_float(x,y):
    x[y] = x[y].astype('float64')
    return x[y]

conv_float(df1,'Critic_Score')
conv_float(df2,'Critic_Score')
conv_float(df1,'Critic_Count')
conv_float(df2, 'Critic_Count')
conv_float(df1, 'User_Count')
conv_float(df2, 'User_Count')
conv_float(df1, 'User_Score')
conv_float(df2, 'User_Score')

feature_labels = list(df2.columns.values)

#changing the list to a numpy array which can be used for color in matplotlib. This is the y which is our 12 genres.
y = array(list(df1['Genre_Code']))
#This is a 13-D feature set
X = array(df2)

#split into training and test sets
X_train, X_test,y_train, y_test = train_test_split(X,y, test_size=0.4, random_state=0)

# create a random forest classifier not sure what all these hyper parameters do
# n_estimators is how many trees n_jobs is the # of jobs to run in parallel for both
# fit and predeictm if -1 the number of jobs is set to the number of cores
clf = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs= -1)

#Train the classifier
clf.fit(X_train,y_train)

#Print the name and gini importance of each feature
for feature in zip(feature_labels, clf.feature_importances_):
    print(feature)

#Select features that are over 0.12 in importance from clf
sfm = SelectFromModel(clf, threshold= 0.12)

#Train the Selector
sfm.fit(X_train,y_train)

#print the features with an importance over 0.12
for feature_list_index in sfm.get_support(indices=True):
    print(feature_labels[feature_list_index])

# Transform the data to create a new dataset containing only important features
# must do this for the train AND the test

X_important_train = sfm.transform(X_train)
X_important_test = sfm.transform(X_test)

# Need a new random forest to fit our new sets that contain only the important features
clf_important = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)

#Train the classifier on important feature data
clf_important.fit(X_important_train, y_train)

#Apply the full featured classifier first so we can compare accuracy
y_pred = clf.predict(X_test)
# so this is ALL features
print(accuracy_score(y_test, y_pred))

#This is the 2 features
y_important_pred = clf_important.predict(X_important_test)

print(accuracy_score(y_test, y_important_pred))
