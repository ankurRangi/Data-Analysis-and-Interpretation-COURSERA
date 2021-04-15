#Importing necessary libraries
import pandas as pd
import numpy

path = 'C:/Users/ankur/OneDrive/Desktop/IIITD/Semester 8/Coursera/gapminder.csv'
dataset = pd.read_csv(path)

#printing the columns of the dataset
print(dataset.columns)

#Creating a numpy array to add tree variables to create frequency table.
lst = numpy.array([dataset.columns[7], dataset.columns[-5], dataset.columns[-2]])

#Iterating over these three variables in the lst
for col in lst:

    print('##############################################')
    print('\t\t '+col)
    print('##############################################')

    #Counting the values from the respective column
    c = dataset[col].value_counts(sort=False)

    # Computing the percentage for the respective column
    p = dataset[col].value_counts(sort=False, normalize=True)
    print('Count for ' + col)
    print('________________')
    print('Value\t\t\t\tCount')
    print(c)
    print('\nPercentage for ' + col)
    print('_____________________')
    print('Value\t\t\t\tPercentage')
    print(p)

    # c1 = dataset.groupby(col).size()
    # print(c1)
    # p1 = (dataset.groupby(col).size() * 100)/len(dataset)
    # print(p1)
    print('\n')


