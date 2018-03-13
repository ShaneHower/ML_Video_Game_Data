import pandas as pd
from numpy import array
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score,precision_recall_curve, precision_score, recall_score

df1 = pd.read_csv('*Desired Target Data*')
df2 = pd.read_csv('*Desired Data Frame containing the features*')

#had to convert a few variable types to float
def conv_float(x,y):
    x[y] = x[y].astype('float64')
    return x[y]

for i in ['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']:
    conv_float(df2, i)

# list of features
feature_labels = list(df2.columns.values)

#changing the list to a numpy array which can be used for color in matplotlib. This is the y which is our 12 genres.
y = array(list(df1['Is_RPG']))
#This is a 13-D feature set
X = array(df2)

#split into training and test sets
X_train, X_test,y_train, y_test = train_test_split(X,y, test_size=0.4, random_state=0)

# create a random forest classifier
# n_estimators is how many trees n_jobs is the # of jobs to run in parallel for both
# fit and predeictm if -1 the number of jobs is set to the number of cores
clf = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs= -1)

#Train the classifier
clf.fit(X_train,y_train)

sorted_feature = []
#Print the name and gini importance of each feature
for feature in zip(feature_labels, clf.feature_importances_):
    sorted_feature.append(feature)

#sort features from high to low by the second element of the tuple
sorted_feature = sorted(sorted_feature, key= lambda tup: tup[1], reverse= True)

for i in sorted_feature:
    print(i)

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


#Precision and Recall
p_score = precision_score(y_test, y_important_pred)
r_score = recall_score(y_test, y_important_pred)
average_precision = average_precision_score(y_test, y_important_pred)
print("precision: {0}".format(p_score))
print("recall: {0}".format(r_score))
print('Average precision-recall score: {0:0.2f}'.format(average_precision))

precision, recall, _ = precision_recall_curve(y_test, y_pred)

plt.step(recall, precision, color = 'b', alpha = 0.2, where='post')
plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.xlim([0.0,1.05])
plt.ylim([0.0,1.0])
plt.title('Precision-recall curve: AP = {0:0.2f}'.format(average_precision))
plt.show()
