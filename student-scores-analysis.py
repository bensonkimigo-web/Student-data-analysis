import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
    "Math": [85, np.nan, 78, 90, 92, 88, np.nan],
    "English": [78, 82, np.nan, 85, 90, np.nan, 75],
    "Science": [92, 88, 79, np.nan, 85, 91, 87]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

df['Math'].fillna(df['Math'].mean(), inplace=True)
df['English'].fillna(df['English'].mean(), inplace=True)
df['Science'].fillna(df['Science'].mean(), inplace=True)

print("\nData after cleaning missing values:")
print(df)

print("\nAverage Scores:")
for subject in ["Math", "English", "Science"]:
    avg = np.mean(df[subject])
    print(f"{subject}: {avg:.2f}")

df_sorted = df.sort_values(by="Math", ascending=False)
print("\nData sorted by Math scores (highest to lowest):")
print(df_sorted)

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Math"], color='skyblue', label='Math')
plt.bar(df["Name"], df["English"], bottom=df["Math"], color='lightgreen', label='English')
plt.bar(df["Name"], df["Science"], bottom=df["Math"]+df["English"], color='salmon', label='Science')
plt.ylabel("Scores")
plt.title("Student Scores in Subjects")
plt.legend()
plt.show()