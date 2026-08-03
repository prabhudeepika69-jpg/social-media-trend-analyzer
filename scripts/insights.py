import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/trends_data.csv")

df["Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]

top_topics = df.groupby("Topic")["Engagement"].sum()

plt.figure(figsize=(8, 5))
top_topics.plot(kind="bar")

plt.title("Topic Engagement")
plt.xlabel("Topic")
plt.ylabel("Engagement")

plt.savefig("reports/topic_chart.png")

print("Chart created successfully!")
