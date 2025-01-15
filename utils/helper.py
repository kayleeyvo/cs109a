import numpy as np
import pandas as pd

def get_variable_category(df: pd.DataFrame) -> tuple:
    """Helps to organize variables better

    Args:
        df (pd.DataFrame): main dataframe

    Returns:
        tuple: columns of the data frame categorized into 
            discrete, categorical, continuous, binary, 
            and id variables
    """
    discrete_vars = []
    categorical_vars = []
    continuous_vars = []
    binary_vars = []
    id_vars = []
    
    for col in df.columns:
        unique_values = df[col].nunique()
        dtype = df[col].dtype
        
        # IDs
        if unique_values == len(df):
            id_vars.append(col)
        
        # binary variables
        elif unique_values == 2:
            binary_vars.append(col)
        
        # categorical variables
        elif dtype == 'object':
            categorical_vars.append(col)
        
        # continuous variables
        elif np.issubdtype(dtype, np.number) and unique_values > 10:
            continuous_vars.append(col)
        
        # discrete variables
        elif np.issubdtype(dtype, np.number):
            discrete_vars.append(col)
    
    return discrete_vars, categorical_vars, continuous_vars, binary_vars, id_vars

def split_snake_case(s: str) -> str:
    """_summary_

    Args:
        s (str): input string in snake case

    Returns:
        str: output string in title case
    """
    return s.replace('_', ' ').title()