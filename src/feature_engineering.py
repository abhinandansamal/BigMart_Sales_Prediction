# src/feature_engineering.py

from sklearn.preprocessing import LabelEncoder
import pandas as pd

def feature_engineering(df):
    """
    Perform feature engineering including encoding and creating new features.
    """
    # Encoding categorical variables
    le = LabelEncoder()
    col_encode = ["item_fat_content", "outlet_identifier", "outlet_size", "outlet_location_type", "outlet_type"]
    for col in col_encode:
        df[col] = le.fit_transform(df[col])

    # Creating new feature
    df["outlet_age"] = 2024 - df["outlet_establishment_year"]
    df = df.drop(columns=["outlet_establishment_year"])

    # One-hot encoding
    df = pd.get_dummies(df)
    
    return df