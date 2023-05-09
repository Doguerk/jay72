import pandas as pd
import numpy as np

# Variables
jay72 = 1500
ACoHO = 5000
ACredit = 50

# Prepare dataframe
df = pd.DataFrame({
    "Week": np.arange(1, 53),
    "Credit": jay72,
    "Bank": 0
})

# Calculate the values for the 'Credit' and 'Bank' columns
bank = 0
for i in range(df.shape[0]):
    bank += df.loc[i, "Credit"]
    if bank >= ACoHO:
        over = bank - ACoHO
        df.loc[i, "Credit"] += over + ACredit
        bank = df.loc[i, "Credit"]
    df.loc[i, "Bank"] = bank

# Print the dataframe
print(df)
