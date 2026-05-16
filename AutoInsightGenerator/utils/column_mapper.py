# ---------------------------------------------------
# DYNAMIC COLUMN MAPPING
# ---------------------------------------------------

def map_columns(df):

    columns = {}

    for col in df.columns:

        col_lower = col.lower()


        # Revenue Mapping
        if "revenue" in col_lower or "sales" in col_lower:

            columns["revenue"] = col


        # Profit Mapping
        elif "profit" in col_lower:

            columns["profit"] = col


        # Units Sold Mapping
        elif "unit" in col_lower or "quantity" in col_lower:

            columns["units"] = col


        # Region Mapping
        elif "region" in col_lower:

            columns["region"] = col


        # Category / Item Type
        elif "item" in col_lower or "category" in col_lower:

            columns["item_type"] = col


        # Sales Channel
        elif "channel" in col_lower:

            columns["channel"] = col


        # Country
        elif "country" in col_lower:

            columns["country"] = col


        # Date
        elif "date" in col_lower:

            columns["date"] = col


    return columns