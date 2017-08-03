import pandas as pd


#Read the dataset from the csv into a Data Frame
dataFrame = pd.read_csv("C:\\Users\\vinya\\PycharmProjects\\loanEligibility\\datasets\\train.csv") 
"""Exploring the data set
1. Look at the headings and some sample values of the columns
2. Check the completeness and basic analysis using describe
3. Check population distribution using histograms and box plots"""

#1
print("Headings and sample values are: \n")
print(dataFrame.head(5))

#2
print("\nStatistical description of the columns: \n")
print(dataFrame.describe())
print("\nColumn-wise count of values:")
print(dataFrame.count())    #Specfies the number of values in the data frame
print("\nFrequency of each value in each column: \n")
for columnName in ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',	'Credit_History',
                   'Property_Area', 'Loan_Status']:
    print("\nFrequency of values in {0}: ".format(columnName))
    print(dataFrame[columnName].value_counts())
