import streamlit as st
import pandas as pd

from utils.column_mapper import map_columns

from analysis.analyzer import (

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

from insights.ollama_insights import generate_ai_insights

from visualization.charts import (

    plot_monthly_sales,
    plot_category_revenue,
    plot_correlation_heatmap,
    plot_outliers

)


# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(

    page_title="Auto Insight Generator",
    layout="wide"

)


# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📊 Auto Insight Generator")

st.write(

    "Upload a dataset and generate automated business insights."

)


# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_file = st.file_uploader(

    "Upload Dataset File",
    type=["csv", "xlsx", "xls"]

)


# ---------------------------------------------------
# PROCESS DATASET
# ---------------------------------------------------

if uploaded_file is not None:

    try:

        # ---------------------------------------------------
        # READ DATASET
        # ---------------------------------------------------

        file_name = uploaded_file.name


        if file_name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)


        elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):

            df = pd.read_excel(uploaded_file)


        # ---------------------------------------------------
        # COLUMN MAPPING
        # ---------------------------------------------------

        columns = map_columns(df)


        # Validation
        if "revenue" not in columns:

            st.error("Revenue/Sales column not detected.")

            st.stop()


        # ---------------------------------------------------
        # DATASET PREVIEW
        # ---------------------------------------------------

        st.subheader("📄 Dataset Preview")

        st.dataframe(df.head())


        # ---------------------------------------------------
        # GENERATE INSIGHTS BUTTON
        # ---------------------------------------------------

        if st.button("Generate Insights"):


            # ---------------------------------------------------
            # ANALYSIS
            # ---------------------------------------------------

            stats = basic_statistics(df, columns)

            top_item = top_item_type(df, columns)

            best_region = top_region(df, columns)

            best_channel = best_sales_channel(df, columns)

            best_country = top_country(df, columns)

            correlation = correlation_analysis(df, columns)

            monthly_sales, trend = monthly_sales_trend(df, columns)

            outlier_count = detect_outliers(df, columns)


            # ---------------------------------------------------
            # RULE-BASED INSIGHTS
            # ---------------------------------------------------

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


            # ---------------------------------------------------
            # STATISTICS
            # ---------------------------------------------------

            st.subheader("📈 Statistical Summary")


            col1, col2, col3 = st.columns(3)


            col1.metric(

                "Total Revenue",
                f"${stats['Total Revenue']:,.2f}"

            )


            col2.metric(

                "Total Profit",
                f"${stats['Total Profit']:,.2f}"

            )


            col3.metric(

                "Total Units Sold",
                f"{stats['Total Units Sold']:,}"

            )


            # ---------------------------------------------------
            # RULE-BASED INSIGHTS
            # ---------------------------------------------------

            st.subheader("🤖 Generated Insights")


            for insight in insights:

                st.success(insight)


            # ---------------------------------------------------
            # AI SMART INSIGHTS
            # ---------------------------------------------------

            st.subheader("🧠 AI Smart Insights")


            with st.spinner("Generating AI insights..."):

                ai_insights = generate_ai_insights(

                    stats,
                    top_item,
                    best_region,
                    best_channel,
                    best_country,
                    correlation,
                    trend,
                    outlier_count

                )


            st.write(ai_insights)


            # ---------------------------------------------------
            # VISUALIZATIONS
            # ---------------------------------------------------

            st.subheader("📊 Visualizations")


            # Monthly Sales Trend
            if monthly_sales is not None:

                fig1 = plot_monthly_sales(monthly_sales)

                st.pyplot(fig1)


            # Category Revenue
            if "item_type" in columns:

                fig2 = plot_category_revenue(df,columns)

                st.pyplot(fig2)


            # Correlation Heatmap
            fig3 = plot_correlation_heatmap(df)

            st.pyplot(fig3)


            # Outlier Visualization
            fig4 = plot_outliers(df,columns)

            st.pyplot(fig4)


    except Exception as e:

        st.error(f"Error processing dataset: {e}")