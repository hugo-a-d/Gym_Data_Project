import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import plotly.express as px

def scale_line_graph(x:pd.Index, y:pd.Series, title: str = "Default Title", xlabel: str = "X Axis", ylabel: str = "Y Axis")-> Axes:
    '''
    creates a graph for scale data, takes the index and a pandas series
    returns a matplotlib axes object
    '''
    ax = sns.lineplot(x=x, y=y)
    ax.set_title(f"{title}")
    ax.set_xlabel(f"{xlabel}")
    ax.set_ylabel(f"{ylabel}")
    
    return ax

def weight_line_graph(df:pd.DataFrame, x:pd.Index, y:str, title:str,):
    fig = px.line(
        df,
        x=x,
        y=[y],
        title=title)
    
    return fig

def Lean_and_fat_line_graph(df:pd.DataFrame, x:pd.Index, y_1:str, y_2:str, title:str):
    fig = px.line(
        df,
        x=x,
        y=[y_1, y_2],
        title=title)
    
    return fig
