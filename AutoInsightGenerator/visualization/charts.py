import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------
# MONTHLY SALES TREND
# ---------------------------------------------------

def plot_monthly_sales(monthly_sales):

    fig, ax = plt.subplots(figsize=(10, 5))

    monthly_sales.plot(

        kind="line",
        marker="o",
        ax=ax

    )

    ax.set_title("Monthly Sales Trend")

    ax.set_xlabel("Month")

    ax.set_ylabel("Revenue")

    return fig


# ---------------------------------------------------
# CATEGORY REVENUE CHART
# ---------------------------------------------------

def plot_category_revenue(df, columns):

    if "item_type" not in columns:

        return None


    category_sales = df.groupby(

        columns["item_type"]

    )[columns["revenue"]].sum().sort_values(ascending=False)


    fig, ax = plt.subplots(figsize=(10, 5))


    category_sales.plot(

        kind="bar",
        ax=ax

    )


    ax.set_title("Revenue by Category")

    ax.set_xlabel("Category")

    ax.set_ylabel("Revenue")

    return fig


# ---------------------------------------------------
# CORRELATION HEATMAP
# ---------------------------------------------------

def plot_correlation_heatmap(df):

    fig, ax = plt.subplots(figsize=(8, 5))

    numeric_df = df.select_dtypes(include=["number"])

    sns.heatmap(

        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        ax=ax

    )

    ax.set_title("Correlation Heatmap")

    return fig


# ---------------------------------------------------
# OUTLIER VISUALIZATION
# ---------------------------------------------------

def plot_outliers(df, columns):

    revenue_col = columns["revenue"]


    fig, ax = plt.subplots(figsize=(8, 5))


    sns.boxplot(

        y=df[revenue_col],
        ax=ax

    )


    ax.set_title("Outlier Detection")

    return fig