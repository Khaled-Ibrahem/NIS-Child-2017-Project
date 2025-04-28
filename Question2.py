# Question 2
# Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.

# This function should return a tuple in the form (use the correct numbers:

# (2.5, 0.1)


import pandas as pd

def average_influenza_doses():
    # Read the dataset
    df = pd.read_csv("assets/NISPUF17.csv", index_col=0)

    # Filter rows where breastfed status is known (1 or 2) and P_NUMFLU is not NaN
    df = df[df['CBF_01'].isin([1, 2]) & df['P_NUMFLU'].notna()]
    
    # Subset for breastfed and not breastfed
    breastfed = df[df['CBF_01'] == 1]
    not_breastfed = df[df['CBF_01'] == 2]

    # Calculate average number of flu doses
    avg_breastfed = breastfed['P_NUMFLU'].mean()
    avg_not_breastfed = not_breastfed['P_NUMFLU'].mean()

    return (avg_breastfed, avg_not_breastfed)
