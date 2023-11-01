import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_dataset

def analyze_data(n, file):
    df = load_dataset(file)
    file_header = ['AEP_MW', 'COMED_MW', 'DAYTON_MW', 'DEOK_MW', 'DOM_MW', 'DUQ_MW', 'EKPC_MW', 'FE_MW', 'NI_MW']
    df['hour'] = df.index.hour
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    sns.set(style='darkgrid')
    fig, ax = plt.subplots(figsize=(12, 9))
    sns.boxplot(x="month", y=file_header[n], data=df, hue="month", legend=False)
    ax.set_title("Energy Consumption/Month")
    plt.show()
