import pandas as pd
from scripts import preprocessing_utility as util
from datetime import date


def add_voucher_present(df: pd.DataFrame):
    data = []
    for value in df["voucherID"]:
        voucher_id = value
        if voucher_id == "0":
            data.append(0)
        else:
            data.append(1)

    series = pd.Series(data)
    df["voucher_present"] = series;

    assert isinstance(df, pd.DataFrame)
    return df


def price_difference_and_ratio(df: pd.DataFrame):
    price_data = util.get_data_as_array(df, "price")
    rrp_data = util.get_data_as_array(df, "rrp")
    quantity_data = util.get_data_as_array(df, "quantity")

    new_data_difference = []
    new_data_ratio = []
    for i in range(len(price_data)):
        difference = rrp_data[i] - (price_data[i] / quantity_data[i])
        new_data_difference.append(difference)
        if price_data[i] == 0:
            ratio = difference / price_data[i]
        else:
            ratio = 0
        new_data_ratio.append(ratio)

    df["rrp_price_difference"] = pd.Series(new_data_difference)
    df["rrp_price_difference_ratio"] = pd.Series(new_data_ratio)
    assert isinstance(df, pd.DataFrame)
    return df


def total_order_size(df: pd.DataFrame):
    order_ids_data = util.get_data_as_array(df, "orderID")
    quantity_data = util.get_data_as_array(df, "quantity")

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


def total_order_price(df: pd.DataFrame):
    order_ids_data = util.get_data_as_array(df, "orderID")
    price_data = util.get_data_as_array(df, "price")
    voucher_amount_data = util.get_data_as_array(df, "voucherAmount")

    temp_dic = {}
    for i in range(len(order_ids_data)):
        if order_ids_data[i] in temp_dic.keys():
            temp_dic[order_ids_data[i]] = temp_dic[order_ids_data[i]] + price_data[i]
        else:
            temp_dic[order_ids_data[i]] = price_data[i]

    total_price_data = []
    cleaned_total_price_data = []
    for i in range(len(order_ids_data)):
        total_price_data.append(temp_dic[order_ids_data[i]])
        cleaned_total_price_data.append(temp_dic[order_ids_data[i]] - voucher_amount_data[i])

    df["totalOrderPrice"] = pd.Series(total_price_data)
    df["cleanedTotalOrderPrice"] = pd.Series(cleaned_total_price_data)
    assert isinstance(df, pd.DataFrame)
    return df


def weekend_weekday_month_day(df: pd.DataFrame):
    order_date_data = util.get_data_as_array(df, "orderDate")

    new_data_weekend = []
    new_data_weekday = []
    new_data_month = []
    new_data_day = []

    for i in range(len(order_date_data)):
        date_array = str(order_date_data[i]).split(" ")[0].split("-")
        day = int(date_array[2])
        month = int(date_array[1])
        year = int(date_array[0])
        date_for_row = date(year, month, day)
        weekday = date_for_row.weekday()
        # Set the weekday for the date (0 = Monday, 6 = Sunday)
        new_data_weekday.append(weekday)
        # Set if the date is on a weekend
        if weekday == 5 or weekday == 6:
            new_data_weekend.append(1)
        else:
            new_data_weekend.append(0)
        # Set month
        new_data_month.append(date_for_row.month)
        # Set day
        new_data_day.append(date_for_row.day)

    df["day"] = pd.Series(new_data_day)
    df["month"] = pd.Series(new_data_month)
    df["weekEnd"] = pd.Series(new_data_weekend)
    df["weekDay"] = pd.Series(new_data_weekday)

    assert isinstance(df, pd.DataFrame)
    return df

