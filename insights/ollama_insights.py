import ollama


# ---------------------------------------------------
# GENERATE AI INSIGHTS USING LLAMA 3
# ---------------------------------------------------

def generate_ai_insights(

    stats,
    top_item,
    best_region,
    best_channel,
    best_country,
    correlation,
    trend,
    outlier_count

):

    prompt = f"""

    You are a professional business analyst.

    Analyze the following dataset statistics and generate meaningful business insights.

    Dataset Statistics:

    Total Revenue: {stats['Total Revenue']}

    Total Profit: {stats['Total Profit']}

    Total Units Sold: {stats['Total Units Sold']}

    Top Item Type: {top_item}

    Best Region: {best_region}

    Best Sales Channel: {best_channel}

    Most Profitable Country: {best_country}

    Revenue-Profit Correlation: {correlation}

    Monthly Revenue Trend Value: {trend}

    Outlier Transactions Detected: {outlier_count}

    
    Generate:
    
    - 5 professional business insights
    - Mention trends
    - Mention risks
    - Mention profitability
    - Keep response concise and professional

    """


    response = ollama.chat(

        model='llama3',

        messages=[

            {
                'role': 'user',
                'content': prompt
            }

        ]

    )


    return response['message']['content']
    