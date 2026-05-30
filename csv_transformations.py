import pandas as pd
import numpy as np
import sqlite3

df = pd.read_csv("meso1.csv", quotechar='"', skipinitialspace=True, dtype=str)


columns = ["LOADING PROGRESSION", "SETS","REPS","REST","WEEK 10","WEEK 11","WEEK 12","WEEK 13","WEEK 14","WEEK 15","WEEK 16","WEEK 17","WEEK 18","WEEK 19","WEEK 20", "WEEK 21"]
df_2 = df.drop(columns=columns)
df_3 = df_2[df_2 != "MAIN COMPONENT"]
df_4 = df_3.set_index('WORK OUT A CHEST FOCUIS')
df_4.columns = [c.strip().lower().replace(' ', '_') for c in df_4.columns]
df_5 = df_4.where(pd.notna(df_4), None)

week_cols = [c for c in df.columns if c.startswith("week_")]

for col in week_cols:
    df_5[col] = df_5[col].apply(lambda x: str(x).replace(",", "|") if x is not None else None)
    


week_cols = [c for c in df_5.columns if c.startswith("week_")]

for col in week_cols:
    df_5[col] = df_5[col].apply(
        lambda x: str(x).replace("*", "x") if pd.notna(x) else None
    )

#print(df_5)

conn = sqlite3.connect("sql_db/gym_data.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS workout_1 (
    exercise TEXT,
    sets TEXT,
    reps TEXT,
    rest TEXT,
    loading_progression TEXT,
    week_1 TEXT,
    week_2 TEXT,
    week_3 TEXT,
    week_4 TEXT,
    week_5 TEXT,
    week_6 TEXT,
    week_7 TEXT,
    week_8 TEXT,
    week_9 TEXT
)
""")
