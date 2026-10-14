import pandas as pd

data = {"Student":["Conor", "Pmeddy", "Dan","Kristen", "Cody"],"Score":[12,90,45,67,99], "Age": [21,23,22,25,26]}

df = pd.DataFrame(data)
#print(df)

df = df[["Student", "Score"]]
df_row_removed = df.dropna()
print(df_row_removed)