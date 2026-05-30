import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import plotly.express as px
from utils import *

# TO DO
# add error corection/noramlization for the mass data


dates = ("14/09/25", "12/10/25", "26/10/24", "2/11/24", "9/11/24", "16/11/24", "23/11/24", "30/11/24", "7/12/24","14/12/24", "21/12/24", "28/12/24",
         "4/1/25", "11/1/25", "18/1/25", "25/1/25", "1/2/25", "8/2/25", "13/2/25", "15/2/25", "23/2/25", "27/2/25", "4/3/25", "6/3/25", "11/3/25", "20/3/25", "27/3/25", "3/4/25", "8/4/25", "10/4/25", "1/5/25", "7/5/25", "15/5/25", "17/5/25", "22/5/25", "14/6/25", "3/7/25", "12/7/25", "22/7/25", "24/7/25", "7/8/25", "28/8/25", "4/9/25", "6/9/25", "11/9/25", "9/10/25", "30/10/25", "8/11/25", "13/11/25", "15/11/25", "18/11/25", "20/11/25", "24/11/25", "27/11/25", "4/12/25", "13/12/25", "20/12/25", "30/12/25",
         "6/1/26", "10/1/26", "17/1/26", "24/1/26", "31/1/26", "5/2/26", "11/2/26", "14/2/26", "23/2/26", "26/2/26", "2/3/26", "5/3/26", "9/3/26", "11/3/26", "13/3/26", "16/3/26", "20/3/26")
weight_kg = (93.1, 91.6, 93.3, 93, 92.7, 92.6, 91.6, 91.8, 93.2, 92.1, 92, 91.6, 92.5, 92.1, 91.3, 91.2, 89.8, 90.0, 90.1, 90.2, 92, 90.5, 91, 91.9, 90.3, 92.1, 89.7, 90.9, 91.3, 90, 91.7, 92.6, 92.7, 93.1, 92.1, 93.5, 93.1, 92.9, 95.7, 95.0, 96.9, 94.2, 96.4, 96.0, 95.6, 94.9, 96.4, 96.9, 96.1, 95.5, 95.7, 96.2, 95.9, 94.7, 95.4, 95.9, 96.0, 97.0, 96.0, 95.4, 93.7, 95.2, 95.4, 94.1, 94.3, 95.7, 96.1, 95.5, 96, 96.5, 95.3, 94.6, 94.3, 94.1, 94.2)
body_fat = (0, 0, 0, 0, 0, 0, 24.2, 0, 15.6, 17.0, 0, 0, 0, 17.8, 15.6, 15.3, 22.4, 22.1, 19.4, 36.5, 11.7, 35.4, 24.1, 18.9, 26.6, 25.3, 35.5, 28.2, 25.7, 24.3, 18.3, 31.7, 17.1, 18.4, 15.9, 28.9, 41.2, 25.1, 33.9, 33.0, 32.4, 25.8, 19.4, 12.5, 23.4, 25.7, 25.9, 35.0, 21.3, 18.5, 36.7, 27.1, 30.6,  26.2, 28.3, 14.1, 21.6, 22.0, 23.8, 29.8, 37.4, 34.8, 20, 26.6, 20.5, 21.2, 20.2, 29.5, 19.2, 18.8, 26.1, 25.3, 20.4, 28.1, 36.4)
muscle_mass = (0, 0, 0, 0, 0, 0, 40.6, 0, 46.3, 45.5, 0, 0, 0, 42, 46, 46.5, 41.6, 42, 40.7, 30.5, 52.3, 31.7, 35, 41.3, 33.9, 43.1, 32.6, 40.9, 46.3, 40.4, 44.1, 38, 42.2, 41.4, 46.3, 37, 14, 37.8, 32.5, 37.0, 31.8, 40.7, 43.4, 48.3, 44.6, 42.7, 31.0, 31.9, 39.8, 33.9, 33.8, 39.9, 37.6, 42.6, 41.6, 39.9, 44.4, 43.8, 41.8, 36.5, 33.4, 32, 43.2, 38.5, 40.3, 39.7, 32.9, 36, 50, 55.7, 43.7, 37.8, 40.2, 36, 34.3)


raw_df = create_scaledata_pd(dates, weight_kg, body_fat, muscle_mass)
cleaned_df = drop_0_scaledata_pd(raw_df)
mass_df = add_mass_columns(cleaned_df)


dfs_by_year = df_by_year(cleaned_df)
df_2024 = dfs_by_year[2024]
df_2025 = dfs_by_year[2025]
df_2026 = dfs_by_year[2026]

mass_df_outlier = remove_outliers(mass_df, "Lean Mass kg")
mass_df_outlier = remove_outliers(mass_df, "Fat Mass kg")
print(mass_df_outlier)
#print(df_2025.describe())



#print(cleaned_df)
#print(raw_df.describe())
#print(cleaned_df.describe())

corr_2025 = df_2025[['Weight kg','Muscle Mass %','Body Fat %']].corr()
corr_df = cleaned_df[['Weight kg','Muscle Mass %','Body Fat %']].corr()
corr_mass = mass_df[['Weight kg','Muscle Mass %','Body Fat %', "Lean Mass kg", "Fat Mass kg"]].corr()
# this shows as muscle increases body fat decreases, which is nice
#print(corr_2025)
#print(corr_mass)
#sns.pairplot(cleaned_df[['Weight kg','Muscle Mass %','Body Fat %']])
#sns.pairplot(df_2025[['Weight kg', "Muscle Mass %", "Body Fat %"]])
sns.pairplot(mass_df[['Weight kg','Muscle Mass %','Body Fat %', "Lean Mass kg", "Fat Mass kg"]])


fig_line = weight_line_graph(mass_df_outlier,mass_df_outlier.index,"Weight kg", "Weight Line Graph")
fig_line.show()

fig_lean_line = Lean_and_fat_line_graph(mass_df_outlier,mass_df_outlier.index,"Lean Mass kg", "Fat Mass kg", "Lean and Fat Mass Line Graph")
fig_lean_line.show()

#fig_area = px.area(
#    test,
#    x=test.index,
#    y=["weight_kg", "muscle_mass_kg"],
#    title="Weight vs Muscle Mass Over Time"
#)

#fig_area.show()


# don't know if this will be useful 
#cleaned_df['weight_change'] = cleaned_df['Weight kg'].diff()
#cleaned_df['fat_change'] = cleaned_df['Body Fat %'].diff()
#cleaned_df = cleaned_df.fillna(0)
#histograms of each column
#raw_df['Weight kg'].hist()
#raw_df['Muscle Mass %'].hist()
#raw_df['Body Fat %'].hist()


plt.show()