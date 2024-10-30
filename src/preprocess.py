# src/preprocess.py

import pandas as pd

def preprocess_data(df):
    """
    Performs preprocessing steps on the input DataFrame.
    """
    df = df.dropna(subset=['item_weight'])  # Example: dropping rows where 'item_weight' is missing
    replacement_dict = {
        'item_fat_content': {
            'low fat': 'Low Fat',
            'LF': 'Low Fat',
            'reg': 'Regular'
        }
    }
    df.replace(replacement_dict, inplace=True)
    return df