import pandas as pd

df = pd.read_csv("user_list.csv")

df["try"] = "1회"

df.drop("Unnamed", axis=1, inplace=True)

df.to_csv("user_list.csv", mode="w", index=False, encoding="utf-8")