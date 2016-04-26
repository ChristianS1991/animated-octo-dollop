__author__ = 'Christian'

import pandas as pd
from scripts import preprocessing_utility as util


def add_voucher_present(df: pd.DataFrame):
    data = []
    for value in df["voucherID"]:
        voucherid = value
        if voucherid == "0":
            data.append(0)
        else:
            data.append(1)

    series = pd.Series(data)
    df["voucher_present"] = series;

    assert isinstance(df, pd.DataFrame)
    return df


def price_difference(df: pd.DataFrame):
    price_data = util.get_data_as_array(df,"price")
    rrp_data = util.get_data_as_array(df,"rrp")
    quantity_data = util.get_data_as_array(df,"quantity")

    new_data = []
    for i in range(len(price_data)):
        difference = rrp_data[i] - (price_data[i] / quantity_data[i])
        new_data.append(difference)

    df["rrp_price_difference"] = pd.Series(new_data)
    assert isinstance(df, pd.DataFrame)
    return df


def total_order_size(df: pd.DataFrame):
    order_ids_data = util.get_data_as_array(df,"orderID")
    quantity_data = util.get_data_as_array(df,"quantity")

    temp_dic = {}
    for i in range(len(order_ids_data)):
        if order_ids_data[i] in temp_dic.keys():
            temp_dic[order_ids_data[i]] = temp_dic[order_ids_data[i]] + quantity_data[i]
        else:
            temp_dic[order_ids_data[i]] = quantity_data[i]

    new_data = []
    for i in range(len(order_ids_data)):
        new_data.append(temp_dic[order_ids_data[i]])

    df["totalOrderSize"] = pd.Series(new_data)
    assert isinstance(df, pd.DataFrame)
    return df
