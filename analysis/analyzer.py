import pandas as pd
import numpy as np


# ---------------------------------------------------
# BASIC STATISTICS
# ---------------------------------------------------

def basic_statistics(df, columns):

    stats = {

        "Total Rows": df.shape[0],

        "Total Columns": df.shape[1],

        "Total Revenue":
            df[columns["revenue"]].sum(),

        "Average Revenue":
            df[columns["revenue"]].mean(),

        "Maximum Revenue":
            df[columns["revenue"]].max(),

        "Minimum Revenue":
            df[columns["revenue"]].min(),

        "Total Profit":
            df[columns["profit"]].sum()
            if "profit" in columns else 0,

        "Average Profit":
            df[columns["profit"]].mean()
            if "profit" in columns else 0,

        "Total Units Sold":
            df[columns["units"]].sum()
            if "units" in columns else 0

    }

    return stats


# ---------------------------------------------------
# TOP ITEM TYPE
# ---------------------------------------------------

def top_item_type(df, columns):

    if "item_type" not in columns:

        return "Not Available"

    item_sales = df.groupby(

        columns["item_type"]

    )[columns["revenue"]].sum()

    return item_sales.idxmax()


# ---------------------------------------------------
# TOP REGION
# ---------------------------------------------------

def top_region(df, columns):

    if "region" not in columns:

        return "Not Available"

    region_sales = df.groupby(

        columns["region"]

    )[columns["revenue"]].sum()

    return region_sales.idxmax()


# ---------------------------------------------------
# BEST SALES CHANNEL
# ---------------------------------------------------

def best_sales_channel(df, columns):

    if "channel" not in columns:

        return "Not Available"

    channel_sales = df.groupby(

        columns["channel"]

    )[columns["revenue"]].sum()

    return channel_sales.idxmax()


# ---------------------------------------------------
# MOST PROFITABLE COUNTRY
# ---------------------------------------------------

def top_country(df, columns):

    if "country" not in columns or "profit" not in columns:

        return "Not Available"

    country_profit = df.groupby(

        columns["country"]

    )[columns["profit"]].sum()

    return country_profit.idxmax()


# ---------------------------------------------------
# CORRELATION ANALYSIS
# ---------------------------------------------------

def correlation_analysis(df, columns):

    if "profit" not in columns:

        return 0

    correlation = df[

        columns["revenue"]

    ].corr(

        df[columns["profit"]]

    )

    return correlation


# ---------------------------------------------------
# TREND ANALYSIS
# ---------------------------------------------------

def monthly_sales_trend(df, columns):

    if "date" not in columns:

        return None, 0


    df[columns["date"]] = pd.to_datetime(

        df[columns["date"]],
        errors="coerce"

    )


    df["Month"] = df[
        columns["date"]
    ].dt.to_period("M")


    monthly_sales = df.groupby(

        "Month"

    )[columns["revenue"]].sum()


    trend = monthly_sales.diff().mean()


    return monthly_sales, trend


# ---------------------------------------------------
# OUTLIER DETECTION
# ---------------------------------------------------

def detect_outliers(df, columns):

    revenue_col = columns["revenue"]


    Q1 = df[revenue_col].quantile(0.25)

    Q3 = df[revenue_col].quantile(0.75)

    IQR = Q3 - Q1


    lower_bound = Q1 - 1.5 * IQR

    upper_bound = Q3 + 1.5 * IQR


    outliers = df[

        (df[revenue_col] < lower_bound) |

        (df[revenue_col] > upper_bound)

    ]


    return outliers.shape[0]