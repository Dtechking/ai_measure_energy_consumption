import pandas as pd

def load_dataset(dataset_path):
    try:
        df = pd.read_csv(dataset_path)
    except FileNotFoundError as e:
        print(f"Error: {e}. Please check if the file exists in the correct directory.")
        return None
    df = df.set_index('Datetime')
    df.index = pd.to_datetime(df.index)
    return df
