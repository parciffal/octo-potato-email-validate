import pandas as pd

data = pd.read_csv("./result.csv")
count = 0
for i in data['check']:
    if i == "Valid":
        count += 1

print(count)
