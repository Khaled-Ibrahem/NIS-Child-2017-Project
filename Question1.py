# Question 1¶
# Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.

# This function should return a dictionary in the form of (use the correct numbers, do not round numbers):

#     {"less than high school":0.2,
#     "high school":0.4,
#     "more than high school but not college":0.2,
#     "college":0.2}

import pandas as pd

def proportion_of_education():
    df = pd.read_csv("assets/NISPUF17.csv", index_col=0)
    counts = df["EDUC1"].value_counts(normalize=True)  # returns proportions directly
    
    return {
        "less than high school": counts[1],
        "high school": counts[2],
        "more than high school but not college": counts[3],
        "college": counts[4]
    }
