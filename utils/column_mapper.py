# ---------------------------------------------------
# DYNAMIC COLUMN MAPPING
# ---------------------------------------------------
def map_columns(df):
    columns = {}
    for col in df.columns:
        
        col_lower = col.lower().strip().replace("_", " ")

        # ---------------------------------------------------
        # REVENUE / SALES / AMOUNT
        # ---------------------------------------------------
        if any(keyword in col_lower.replace(" ", "") for keyword in [
 
       "revenue",
       "sales",
       "amount",
       "totalamount",
        "totalsales"
]):
         columns["revenue"] = col
            

        # ---------------------------------------------------
        # PROFIT
        # ---------------------------------------------------
        if any(keyword in col_lower for keyword in [
            "profit",
            "margin",
            "earnings",
            "income"
        ]):
            columns["profit"] = col

        # ---------------------------------------------------
        # UNITS / QUANTITY
        # ---------------------------------------------------
        if any(keyword in col_lower for keyword in [
            "unit",
            "quantity",
            "qty"
        ]):
            columns["units"] = col

        # ---------------------------------------------------
        # REGION
        # ---------------------------------------------------
        if "region" in col_lower:
            columns["region"] = col

        # ---------------------------------------------------
        # ITEM TYPE / CATEGORY / PRODUCT
        # ---------------------------------------------------
        if any(keyword in col_lower for keyword in [
            "item",
            "category",
            "product"
        ]):
            columns["item_type"] = col

        # ---------------------------------------------------
        # SALES CHANNEL
        # ---------------------------------------------------
        if "channel" in col_lower:
            columns["channel"] = col

        # ---------------------------------------------------
        # COUNTRY
        # ---------------------------------------------------
        if "country" in col_lower:
            columns["country"] = col

        # ---------------------------------------------------
        # DATE
        # ---------------------------------------------------
        if "date" in col_lower:
            columns["date"] = col

    return columns 