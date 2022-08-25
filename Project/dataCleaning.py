import pandas as pd
import csv

df = pd.read_csv("Project/total_stars.csv")

del df["Luminosity"]
del df["Star_name"]
del df["distance_from_earth"]
del df["Mass"]
del df["Radius"]

final_data = df.dropna()
final_data.reset_index(drop=True, inplace=True)

final_data.to_csv("Project/final_data.csv")