# Variables
jay72 = 1500
ACoHO = 5000
ACredit = 50

# Prepare the data
data = {
    "Week": list(range(1, 53)),
    "Credit": [jay72]*52,
    "Bank": [0]*52
}

# Calculate the values for the 'Credit' and 'Bank' columns
bank = 0
for i in range(len(data["Week"])):
    bank += data["Credit"][i]
    if bank >= ACoHO:
        over = bank - ACoHO
        data["Credit"][i] += over + ACredit
        bank = data["Credit"][i]
    data["Bank"][i] = bank

# Print the data
for i in range(len(data["Week"])):
    print(f"Week: {data['Week'][i]}, Credit: {data['Credit'][i]}, Bank: {data['Bank'][i]}")
