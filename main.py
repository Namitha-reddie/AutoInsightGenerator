from visualization.charts import (

    plot_monthly_sales,
    plot_category_revenue,
    plot_correlation_heatmap,
    plot_outliers

)
from analysis.analyzer import (

    load_dataset,
    basic_statistics,
    top_item_type,
    top_region,
    best_sales_channel,
    top_country,
    correlation_analysis,
    monthly_sales_trend,
    detect_outliers

)

from insights.insight_generator import generate_insights


# Load Dataset
df = load_dataset("dataset/sales.csv")


# Basic Statistics
stats = basic_statistics(df)


# Business Analysis
top_item = top_item_type(df)

best_region = top_region(df)

best_channel = best_sales_channel(df)

best_country = top_country(df)


# Advanced Analytics
correlation = correlation_analysis(df)

monthly_sales, trend = monthly_sales_trend(df)

outlier_count = detect_outliers(df)


# Generate Insights
insights = generate_insights(

    stats,
    top_item,
    best_region,
    best_channel,
    best_country,
    correlation,
    trend,
    outlier_count

)


# Display Statistics
print("\n========== DATASET STATISTICS ==========\n")

for key, value in stats.items():

    print(f"{key}: {value}")


# Display Insights
print("\n========== GENERATED INSIGHTS ==========\n")

for insight in insights:

    print(f"✅ {insight}")
# ---------------------------------------------------
# VISUALIZATIONS
# ---------------------------------------------------

plot_monthly_sales(monthly_sales)

plot_category_revenue(df)

plot_correlation_heatmap(df)

plot_outliers(df)