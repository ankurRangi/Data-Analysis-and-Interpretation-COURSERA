# Importing necessary libraries

import pandas as pd
import numpy
import seaborn
import matplotlib.pyplot as plt

path = 'C:/Users/ankur/OneDrive/Desktop/IIITD/Semester 8/Coursera/gapminder.csv'
dataset = pd.read_csv(path)

# Extracting three columns from the dataset to perform functions and get some insights
variables = numpy.array([dataset.columns[6], dataset.columns[-1], dataset.columns[-7]])
# o/p: ['femaleemployrate' 'urbanrate' 'lifeexpectancy']

# Replacing all the empty values with numpy.nan
for colname in variables:
    dataset[colname] = dataset[colname].replace(" ", 0)
    dataset[colname] = pd.to_numeric(dataset[colname])

dataset['fe_num'] = ""
dataset['urb'] = ""
dataset['lyf'] = ""

# Data Management for 'femaleemployrate'
dataset.loc[dataset[variables[0]] < 20, 'fe_num'] = "1"
dataset.loc[(dataset[variables[0]] >= 20) & (dataset[variables[0]] < 40), 'fe_num'] = "2"
dataset.loc[(dataset[variables[0]] >= 40) & (dataset[variables[0]] < 60), 'fe_num'] = "3"
dataset.loc[(dataset[variables[0]] >= 60) & (dataset[variables[0]] < 80), 'fe_num'] = "4"
dataset.loc[dataset[variables[0]] >= 80, 'fe_num'] = "5"

dataset.loc[dataset['fe_num'] == "1", 'fe_num_label'] = 20
dataset.loc[dataset['fe_num'] == "2", 'fe_num_label'] = 40
dataset.loc[dataset['fe_num'] == "3", 'fe_num_label'] = 60
dataset.loc[dataset['fe_num'] == "4", 'fe_num_label'] = 80
dataset.loc[dataset['fe_num'] == "5", 'fe_num_label'] = 100

# Data Management for 'urbanrate'
dataset.loc[dataset[variables[1]] >= 75, 'urb'] = "3"
dataset.loc[(dataset[variables[1]] < 75) & (dataset[variables[1]] >= 25), 'urb'] = "2"
dataset.loc[dataset[variables[1]] < 25, 'urb'] = "1"

dataset.loc[dataset['urb'] == "3", 'urb_label'] = 100
dataset.loc[dataset['urb'] == "2", 'urb_label'] = 75
dataset.loc[dataset['urb'] == "1", 'urb_label'] = 25

# Data Management for 'lifeexpectancy'
dataset.loc[dataset[variables[2]] < 45, 'lyf'] = "1"
dataset.loc[(dataset[variables[2]] >= 45) & (dataset[variables[2]] < 55), 'lyf'] = "2"
dataset.loc[(dataset[variables[2]] >= 55) & (dataset[variables[2]] < 65), 'lyf'] = "3"
dataset.loc[(dataset[variables[2]] >= 65) & (dataset[variables[2]] < 75), 'lyf'] = "4"
dataset.loc[dataset[variables[2]] >= 75, 'lyf'] = '5'

dataset.loc[dataset['lyf'] == "1", 'lyf_label'] = 45
dataset.loc[dataset['lyf'] == "2", 'lyf_label'] = 55
dataset.loc[dataset['lyf'] == "3", 'lyf_label'] = 65
dataset.loc[dataset['lyf'] == "4", 'lyf_label'] = 75
dataset.loc[dataset['lyf'] == "5", 'lyf_label'] = 100

analyse_dataset = dataset[['fe_num', 'urb', 'lyf', 'fe_num_label', 'urb_label', 'lyf_label']].copy()

analyse_dataset[analyse_dataset.columns[0]] = analyse_dataset[analyse_dataset.columns[0]].replace("", "NaN")
analyse_dataset[analyse_dataset.columns[1]] = analyse_dataset[analyse_dataset.columns[1]].replace("", "NaN")
analyse_dataset[analyse_dataset.columns[2]] = analyse_dataset[analyse_dataset.columns[2]].replace("", "NaN")

############################################################################################################

# html = analyse_dataset.to_html()
# text_file = open("index.html", "w")
# text_file.write(html)
# text_file.close()
counter = 3
df = pd.DataFrame()
for col in analyse_dataset.columns[:3]:
    print("\nAnalysis on the variable: " + col)
    final_data = pd.DataFrame()

    analyse_dataset[col] = pd.to_numeric(analyse_dataset[col])
    fre = analyse_dataset[col].value_counts().sort_index()
    per = round((analyse_dataset.groupby(col).size() * 100 / len(dataset)), 2)
    cum_fre = analyse_dataset[col].value_counts().sort_index().cumsum()
    cum_per = ((cum_fre / fre.sum()) * 100)

    final_data[col] = range(len(fre) + 1)
    final_data['Frequency'] = fre
    final_data['Percentage'] = per
    final_data['Cumulative_Frequency'] = cum_fre
    final_data['Cumulative_Percentage'] = cum_per
    final_data = final_data.drop(labels=0, axis=0)
    print(final_data.to_string(index=False))

    # Now plotting the data
    unique = analyse_dataset[analyse_dataset.columns[counter]].unique()
    unique = sorted(unique.astype(int))
    final_data['label'] = unique

    seaborn.barplot(x='label', y='Frequency', data=final_data)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

    # if col == 'urb':
    #     df['urb_fre'] = final_data['Frequency']
    # elif col == 'lyf':
    #     df = pd.concat([df, final_data['Frequency']], ignore_index=True, axis=1)

    counter = counter + 1

# analyse_dataset['lyf_label'] = (pd.to_numeric(analyse_dataset['lyf_label'])).astype(int)
# analyse_dataset['urb_label'] = (analyse_dataset['urb_label']).astype(int)
# print(analyse_dataset)

scat = seaborn.regplot(y='urbanrate', x='lifeexpectancy', data=dataset)
plt.xlabel("Urban Population Rate")
plt.ylabel("Life Expectancy")
plt.show()
