__author__ = 'Christian'

import pandas as pd
import numpy as np
from scripts import preprocessing_utility as util
from datetime import date

# readData
df = pd.read_csv("../data/orders_train.txt", header=0, sep=';', na_values="NA")

print(df.info())
# deleteNA
df["voucherID"] = df["voucherID"].fillna("0")
df = df.dropna()
df = df.reset_index(drop=True)

# adjust datatypes
df["orderDate"] = pd.to_datetime(df["orderDate"])
df["productGroup"] = df["productGroup"].astype(np.int64)
df["voucherAmount"] = df["voucherAmount"].astype(np.int64)

index_list = []
index_list2 = []

column = df.columns.get_loc("orderDate")

for index, row in df.iterrows():
    if "2014-07" in str(row["orderDate"]) or "2014-08" in str(row["orderDate"]):
        index_list.append(index)
    if "2015" in str(row["orderDate"]):
        index_list2.append(index)

df_same_months = df.ix[index_list]
df_2015 = df.ix[index_list2]




df_same_months.to_csv('../output/same_months.csv', sep=';', index=False, date_format="%Y-%m-%d")
df_2015.to_csv('../output/2015.csv',sep=';', index=False, date_format="%Y-%m-%d")

print(df.info())