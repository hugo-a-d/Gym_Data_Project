import pandas as pd

def create_scaledata_pd(dates:list, weight_kg:list, body_fat:list, muscle_mass:list) -> pd.DataFrame:
    '''creates a dataframe with bodyweight, body fat % and muscle mass %
        currently has a raise value error, will add this as a test/lint'''
    
    if not (len(dates) == len(weight_kg) == len(body_fat) == len(muscle_mass)):
        raise ValueError("All input lists must have the same length")
    
    dates_dt = pd.to_datetime(dates, format="%d/%m/%y")
    
    df = pd.DataFrame({
        "Date": dates_dt,
        "Weight kg": weight_kg,
        "Body Fat %": body_fat,
        "Muscle Mass %": muscle_mass
    })
    
    df.set_index("Date", inplace=True)
    return df


def drop_0_scaledata_pd(df:pd.DataFrame) -> pd.DataFrame:
    ''' takes the scalesdata_pd and removes all rows with with a 0 value'''
    
    cleaned_df = df[(df != 0).all(axis=1)]
    return cleaned_df

def df_by_year(df:pd.DataFrame) -> pd.DataFrame:
    '''Seperates a data frame on year via index. 
    The dict is on the year as the key and df groupby as value'''
    dfs_by_year = {} 

    for year, group in df.groupby(df.index.year):
        dfs_by_year[year] = group
        
    return dfs_by_year


def add_mass_columns(df:pd.DataFrame) -> pd.DataFrame:
    '''works out the lean mass and fat mass based on weight * % / 100'''

    df['Lean Mass kg'] = df['Weight kg'] * df['Muscle Mass %'] / 100
    df['Fat Mass kg'] = df['Weight kg'] * df['Body Fat %'] / 100
    
    df['Lean Mass kg'] = df['Lean Mass kg'].round(2)
    df['Fat Mass kg'] = df['Fat Mass kg'].round(2)
    return df


def remove_outliers(df:pd.DataFrame, column:str) -> pd.DataFrame:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    # Looser bounds for volatile data
    lower_bound = Q1 - 2.5 * IQR
    upper_bound = Q3 + 2.5 * IQR

    data_cleaned = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return data_cleaned
     