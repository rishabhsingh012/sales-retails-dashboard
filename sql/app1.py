import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------
# Page config
# --------------------------------------------------------------------
st.set_page_config(page_title="Retail Sales Analysis Dashboard", layout="wide")

# --------------------------------------------------------------------
# Load data
# --------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(BASE_DIR / "data" / "cleaned_sales.csv")
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])
    df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])
    return df

df = load_data()

# --------------------------------------------------------------------
# Title
# --------------------------------------------------------------------
st.title("📊 Retail Sales Analysis Dashboard")
st.caption("Analysis of Superstore sales data — profit drivers, regional performance, and customer concentration.")

# --------------------------------------------------------------------
# Sidebar filters
# --------------------------------------------------------------------
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique()),
)

category = st.sidebar.multiselect(
    "Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique()),
)

selected_dates = st.sidebar.date_input(
    "Order Date Range",
    value=(df["Order_Date"].min(), df["Order_Date"].max()),
)
if isinstance(selected_dates, tuple) and len(selected_dates) == 2:
    start_date, end_date = selected_dates
else:
    start_date = end_date = selected_dates

df_filtered = df[
    (df["Region"].isin(region))
    & (df["Category"].isin(category))
    & (df["Order_Date"] >= pd.to_datetime(start_date))
    & (df["Order_Date"] <= pd.to_datetime(end_date))
]

if df_filtered.empty:
    st.warning("No data matches the selected filters. Try widening your selection.")
    st.stop()

# --------------------------------------------------------------------
# KPI row
# --------------------------------------------------------------------
total_sales = df_filtered["Sales"].sum()
total_orders = df_filtered["Order_ID"].nunique()
avg_order_value = total_sales / total_orders if total_orders else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg Order Value", f"${avg_order_value:,.0f}")

st.divider()

# --------------------------------------------------------------------
# Sales by Category & Sub-Category
# --------------------------------------------------------------------
st.subheader("Sales by Category")
cat_data = (
    df_filtered.groupby("Category")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)
fig1 = px.bar(
    cat_data,
    x="Category",
    y="Sales",
    labels={"Sales": "Total Sales ($)"},
    color="Category",
)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Sales by Sub-Category")
subcat_data = (
    df_filtered.groupby("Sub-Category")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)
fig1b = px.bar(
    subcat_data,
    x="Sub-Category",
    y="Sales",
    labels={"Sales": "Total Sales ($)"},
)
st.plotly_chart(fig1b, use_container_width=True)

# --------------------------------------------------------------------
# Sales by Region
# --------------------------------------------------------------------
st.subheader("Sales by Region")
region_data = (
    df_filtered.groupby("Region")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)
fig2 = px.bar(
    region_data,
    x="Region",
    y="Sales",
    labels={"Sales": "Total Sales ($)"},
    color="Region",
)
st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------------------------
# Monthly Sales Trend
# --------------------------------------------------------------------
st.subheader("Monthly Sales Trend")
monthly = (
    df_filtered.set_index("Order_Date")
    .resample("ME")["Sales"]
    .sum()
    .reset_index()
)
fig3 = px.line(
    monthly,
    x="Order_Date",
    y="Sales",
    labels={"Order_Date": "Month", "Sales": "Total Sales ($)"},
    markers=True,
)
st.plotly_chart(fig3, use_container_width=True)

# --------------------------------------------------------------------
# Top 10 Customers
# --------------------------------------------------------------------
st.subheader("Top 10 Customers by Sales")
top_customers = (
    df_filtered.groupby("Customer_Name")["Sales"]
    .sum()
    .nlargest(10)
    .reset_index()
    .rename(columns={"Customer_Name": "Customer", "Sales": "Total Sales ($)"})
)
st.dataframe(top_customers, use_container_width=True, hide_index=True)

# --------------------------------------------------------------------
# Ship Mode breakdown
# --------------------------------------------------------------------
st.subheader("Sales by Ship Mode")
ship_data = (
    df_filtered.groupby("Ship_Mode")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)
fig4 = px.pie(ship_data, names="Ship_Mode", values="Sales", hole=0.4)
st.plotly_chart(fig4, use_container_width=True)

# --------------------------------------------------------------------
# Footer
# --------------------------------------------------------------------
st.divider()
st.caption("Built with Streamlit + Plotly · Data: Sample Superstore dataset")