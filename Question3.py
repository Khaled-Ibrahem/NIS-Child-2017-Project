# It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.

# This function should return a dictionary in the form of (use the correct numbers):

#     {"male":0.2,
#     "female":0.4}
# Note: To aid in verification, the chickenpox_by_sex()['female'] value the autograder is looking for starts with the digits 0.0077.

import pandas as pd 
def chickenpox_by_sex():
    # read the csv file 
    df = pd.read_csv('assets/NISPUF17.csv', index_col=0)

    # filtring the rows to get all the vaccinated with or withouth chickenpox
    df = df[(df['HAD_CPOX'].isin([1,2])) & (df['P_NUMVRC'].dropna() != 0)]

    # getting the rows for male with or without chickenpox
    male_chickenpox = df[(df['HAD_CPOX'] == 1) & (df['SEX'] == 1)]
    male_not_chickenpox = df[(df['HAD_CPOX'] == 2) & (df['SEX'] == 1)]
    female_chickenpox = df[(df['HAD_CPOX'] == 1) & (df['SEX'] == 2)]
    female_not_chickenpox = df[(df['HAD_CPOX'] == 2) & (df['SEX'] == 2)]

    # calculating the ratio for both males and females
    male_ratio = len(male_chickenpox['SEX'])
    male_not_ratio = len(male_not_chickenpox['SEX'])
    female_ratio = len(female_chickenpox['SEX'])
    female_not_ratio = len(female_not_chickenpox['SEX'])
    
    return {
        "male": male_ratio / male_not_ratio,
        "female": female_ratio / female_not_ratio
    }
