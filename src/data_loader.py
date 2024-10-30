# src/data_loader.py

import os
from dotenv import load_dotenv
import redshift_connector
import pandas as pd

def load_data(query="SELECT * FROM public.data"):
    """
    Connects to an AWS Redshift cluster, executes a specified SQL query, and 
    returns the results as a DataFrame.
    """
    load_dotenv(os.path.join('config', '.env'))
    
    host = os.getenv("REDSHIFT_HOST")
    database = os.getenv("REDSHIFT_DATABASE")
    user = os.getenv("REDSHIFT_USER")
    password = os.getenv("REDSHIFT_PASSWORD")
    port = os.getenv("REDSHIFT_PORT")

    try:
        conn = redshift_connector.connect(
            host=host, database=database, user=user, password=password, port=port
        )
        print("Connected to AWS Redshift.")
    except Exception as e:
        raise ConnectionError(f"Failed to connect to Redshift: {e}")

    try:
        data = pd.read_sql(query, conn)
        conn.close()
        return data
    except Exception as e:
        raise Exception(f"Failed to load data: {e}")