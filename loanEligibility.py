import pandas as pd
import matplotlib.pyplot as plt

#Function to plot histograms to identify population distribution
def plothistogram(column):
    dataFrame[column].hist(bins=50, alpha=0.5, edgecolor='black', linewidth=1, facecolor='green')
    plt.title("{0} Histogram".format(column))
    plt.xlabel("Amount")
    plt.ylabel("Frequency")
    plt.show()

#Function to plot boxplots to identify population distribution and outliers
def plotboxplot(column,by='none'):
    if by=="none":
        dataFrame.boxplot(column=column)
    else:
        dataFrame.boxplot(column=column,by=by)

    plt.title("{0} Boxplot".format(column))
    plt.show()


#Read the dataset from the csv into a Data Frame
dataFrame = pd.read_csv("C:\\Users\\vinya\\Documents\\GitHub\\Loan-Prediction-Data-Analytics\\datasets\\train.csv") 
"""Exploring the data set
1. Look at the headings and some sample values of the columns
2. Check the completeness and basic analysis using describe
3. Check population distribution using histograms and box plots"""

#1
print("Headings and sample values are: \n")
print(dataFrame.head(5))
#adding a column as combined income(applicant + co-applicant) to check loan approval statistics for that
dataFrame['CombinedIncome'] = dataFrame['ApplicantIncome'] + dataFrame['CoapplicantIncome']


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

#3
print("Plotting histograms and box plots:")
for plotCol in ['ApplicantIncome', 'CombinedIncome', 'LoanAmount']:
    plothistogram(plotCol)
    plotboxplot(plotCol)

#Box plots to check distribution of applicants based on education and gender
plotboxplot('ApplicantIncome','Education')
plotboxplot('ApplicantIncome','Gender')

""" Analyzing impact of features on loan approval"""
for colHeader in ['Credit_History', 'Property_Area', 'Self_Employed', 'Dependents']:
    # check the frequency of values in credit history column
    valFreq = dataFrame[colHeader].value_counts()
    print('Credit History column values:')
    print(valFreq)
    valLoanProb = dataFrame.pivot_table(values='Loan_Status', index=[colHeader],
                                        aggfunc=lambda x: x.map({'Y': 1, 'N': 0}).mean())
    print('\nPossibility of getting loan based on {0}'.format(colHeader))
    print(valLoanProb.rename(columns={'Loan_Status': 'Loan_Approval_Probability'}))

    """PLotting the above calculated figures as bar graphs"""
    # subplot 1
    fig = plt.figure(figsize=(8, 4))
    subplot1 = fig.add_subplot(1, 2, 1)
    valFreq.plot(kind='bar', alpha=0.5, edgecolor='black', linewidth=1, facecolor='green')
    subplot1.set_xlabel(colHeader)
    subplot1.set_ylabel('Count of Applicants')
    subplot1.set_title("Applicants by {0}".format(colHeader))

    # subplot 2
    subplot2 = fig.add_subplot(1, 2, 2)
    valLoanProb.plot(kind='bar', alpha=0.5, edgecolor='black', linewidth=1, facecolor='green')
    subplot2.set_xlabel(colHeader)
    subplot2.set_ylabel('Probability of getting loan')
    subplot2.set_title("Probability based on {0}".format(colHeader))
    plt.show()


