def generate_insights(

    stats,
    top_item,
    best_region,
    best_channel,
    best_country,
    correlation,
    trend,
    outlier_count

):

    insights = []

    
    # Revenue Insights
    if stats["Total Revenue"] > 10000000:
        insights.append(
            "The business generated very high overall revenue."
        )


    # Profit Insights
    if stats["Total Profit"] > 0:
        insights.append(
            "The business is operating at an overall profit."
        )


    # Units Sold Insight
    if stats["Total Units Sold"] > 500000:
        insights.append(
            "A large number of products were sold across all regions."
        )


    # Top Item Insight
    insights.append(
        f"The highest revenue-generating item type is {top_item}."
    )


    # Region Insight
    insights.append(
        f"The region with highest sales is {best_region}."
    )


    # Sales Channel Insight
    insights.append(
        f"{best_channel} sales channel contributes the most revenue."
    )


    # Country Insight
    insights.append(
        f"{best_country} generated the highest overall profit."
    )


    # Correlation Insight
    if correlation > 0.7:
        insights.append(
            "There is a strong positive correlation between revenue and profit."
        )

    elif correlation > 0.3:
        insights.append(
            "There is a moderate relationship between revenue and profit."
        )

    else:
        insights.append(
            "Revenue and profit show weak correlation."
        )


    # Trend Insight
    if trend > 0:
        insights.append(
            "Monthly revenue shows an increasing trend."
        )

    else:
        insights.append(
            "Monthly revenue shows a declining trend."
        )


    # Outlier Insight
    if outlier_count > 0:
        insights.append(
            f"{outlier_count} unusual revenue transactions were detected."
        )

    else:
        insights.append(
            "No major revenue outliers detected."
        )

    
    return insights