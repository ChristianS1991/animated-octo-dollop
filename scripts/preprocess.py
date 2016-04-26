__author__ = 'Christian'

import pandas as pd
import numpy as np
from scripts import preprocessing_methods as pm

# readData
df = pd.read_csv("../data/orders_train.txt", header=0, sep=';', na_values="NA")

# deleteNA
df["voucherID"] = df["voucherID"].fillna("0")
df = df.dropna()
df = df.reset_index()

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
print(df.tail())

