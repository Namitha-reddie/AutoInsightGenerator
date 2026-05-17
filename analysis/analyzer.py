import pandas as pd
import numpy as np

# ---------------------------------------------------
# BASIC STATISTICS
# ---------------------------------------------------
def clean_numeric_column(df, column_name):
    df[column_name] = (
        df[column_name]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace("₹", "", regex=False)
    )

    df[column_name] = pd.to_numeric(
        df[column_name],
        errors="coerce"
    )

    return df
def basic_statistics(df, columns):
    revenue_col = columns["revenue"]

    # ---------------------------------------------------
    # CLEAN REVENUE COLUMN
    # ---------------------------------------------------
    df[revenue_col] = (
        df[revenue_col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace("₹", "", regex=False)
    )

    df[revenue_col] = pd.to_numeric(
        df[revenue_col],
        errors="coerce"
    )

    # ---------------------------------------------------
    # CLEAN PROFIT COLUMN
    # ---------------------------------------------------
    if "profit" in columns:
        profit_col = columns["profit"]

        df[profit_col] = (
            df[profit_col]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("$", "", regex=False)
            .str.replace("₹", "", regex=False)
        )

        df[profit_col] = pd.to_numeric(
            df[profit_col],
            errors="coerce"
        )

    # ---------------------------------------------------
    # CLEAN UNITS COLUMN
    # ---------------------------------------------------
    if "units" in columns:
        units_col = columns["units"]

        df[units_col] = pd.to_numeric(
            df[units_col],
            errors="coerce"
        )

    # ---------------------------------------------------
    # GENERATE STATISTICS
    # ---------------------------------------------------
    stats = {
        "Total Rows": df.shape[0],
        "Total Columns": df.shape[1],
        "Total Revenue":
            df[revenue_col].sum(),
        "Average Revenue":
            df[revenue_col].mean(),
        "Maximum Revenue":
            df[revenue_col].max(),
        "Minimum Revenue":
            df[revenue_col].min(),
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

    df = clean_numeric_column(
        df,
        columns["revenue"]
    )

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

    df = clean_numeric_column(
        df,
        columns["revenue"]
    )

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

    df = clean_numeric_column(
        df,
        columns["revenue"]
    )

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

    df = clean_numeric_column(
        df,
        columns["profit"]
    )

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

    df = clean_numeric_column(
        df,
        columns["revenue"]
    )

    df = clean_numeric_column(
        df,
        columns["profit"]
    )

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

    df = clean_numeric_column(
        df,
        columns["revenue"]
    )

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

    df = clean_numeric_column(
        df,
        revenue_col
    )

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