__author__ = 'Christian'

import pandas as pd


def get_data_as_array(df: pd.DataFrame, column_name: str):
    column_data = []
    for value in df[column_name]:
        column_data.append(value)

    return column_data


def save_as_csv(df, name):
    df.to_csv("../output/"+name+".csv", index=False, header=True)