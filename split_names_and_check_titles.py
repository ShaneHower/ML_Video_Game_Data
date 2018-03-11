import pandas as pd

df1 = pd.read_csv('/Users/shanehower/Desktop/vg_data/Genre_code_vg_cleaned_names.csv')
df2 = pd.read_csv('/Users/shanehower/Desktop/vg_data/only_numbered_columns.csv')

#for some reason some names were not consider strings so this conversion had to happen first
df1['Name'] = df1['Name'].astype('str')

# list of names
list_name = list(df1['Name'].unique())

# Join then split 
split_name = ' '.join(list_name)
split_name = split_name.split()

# check each title for the unique name and add it to the dataframe containing only number values.
for i in split_name:
    df2[i] = df1['Name'].str.contains(i, na = False)

#export to csv so we can use it in the feature selection script.
df2.to_csv('Multi_label_python.csv')
