__author__ = 'Christian'

import pandas as pd
import numpy as np
from scripts import preprocessing_methods as pm


file_path = "../output/2015.csv"
processed_file_path = "../output/2015_preprocessed.csv"
# readData
df = pd.read_csv(file_path, header=0, sep=';', na_values="NA")

# deleteNA
df["voucherID"] = df["voucherID"].fillna("0")
df = df.dropna()
df = df.reset_index(drop=True)

# adjust datatypes
df["orderDate"] = pd.to_datetime(df["orderDate"])
df["productGroup"] = df["productGroup"].astype(np.int64)
df["voucherAmount"] = df["voucherAmount"].astype(np.int64)

#preprocessing
df = pm.add_voucher_present(df)
df = pm.price_difference_and_ratio(df)
df = pm.total_order_size(df)
df = pm.total_order_price(df)
df = pm.weekend_weekday_month_day(df)
print(df.info())

df.to_csv(processed_file_path, sep=';', index=False, date_format="%Y-%m-%d")