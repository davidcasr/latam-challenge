import numpy as np
import pandas as pd
from datetime import datetime

def get_min_diff(row):
    fecha_o = datetime.strptime(row['Fecha-O'], '%Y-%m-%d %H:%M:%S')
    fecha_i = datetime.strptime(row['Fecha-I'], '%Y-%m-%d %H:%M:%S')
    return ((fecha_o - fecha_i).total_seconds()) / 60

def get_delay(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate 'min_diff' and 'delay' columns in the DataFrame.

    Args:
        data (pd.DataFrame): Input DataFrame with 'Fecha-O' and 'Fecha-I'.

    Returns:
        pd.DataFrame: DataFrame with added 'min_diff' and 'delay' columns.
    """
    # Convert columns to datetime if they are not already
    data['Fecha-O'] = pd.to_datetime(data['Fecha-O'], format='%Y-%m-%d %H:%M:%S')
    data['Fecha-I'] = pd.to_datetime(data['Fecha-I'], format='%Y-%m-%d %H:%M:%S')

    # Vectorized calculation of min_diff
    data['min_diff'] = (data['Fecha-O'] - data['Fecha-I']).dt.total_seconds() / 60

    # Calculate the 'delay' column
    threshold_in_minutes = 15
    data['delay'] = np.where(data['min_diff'] > threshold_in_minutes, 1, 0)

    return data
