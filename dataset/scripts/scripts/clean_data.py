import pandas as pd

df = pd.read_csv("dataset/trends_data.csv")

df.drop_duplicates(inplace=True)

df["Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]

df.to_csv("dataset/cleaned_trends.csv", index=False)

print("Data cleaned successfully!")
