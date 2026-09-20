# sales-retails-dashboard
# Retail Sales Analysis Dashboard

An interactive dashboard that turns raw retail sales data into clear business insights. Data is cleaned and transformed with **Pandas**, stored in **SQLite**, and explored through a **Streamlit** app with **Plotly** charts.

![Dashboard screenshot](screenshots/dashboard.png)
<!-- Replace with your own screenshot. Add 1-2 more if you can (e.g., filters, category view). -->

## Why I built this

Retail teams need to know what is selling, where, and when. This project walks through the full analyst workflow: clean messy data, store it in a database, query it with SQL, and present the results in a dashboard that a non-technical person can use.

## Features

- **Data cleaning pipeline:** handles [missing values, duplicates, inconsistent dates/categories] using Pandas
- **SQLite database:** cleaned data stored in tables and queried with SQL
- **Interactive filters:** filter by [date range, region, product category]
- **KPI summary:** [total sales, total profit, number of orders, average order value]
- **Visualizations:** [monthly sales trend, top products, sales by region/category] built with Plotly

## Key insights

<!-- Fill these in from your own analysis. Specific numbers make this section valuable. -->
- [e.g., Category X generated Y% of total revenue]
- [e.g., Sales peak in month Z]
- [e.g., Region A outperforms Region B by N%]

## Tech stack

| Area | Tools |
|---|---|
| Language | Python |
| Data processing | Pandas, NumPy |
| Database | SQLite |
| Dashboard | Streamlit |
| Charts | Plotly |

## Project structure

```
retail-sales-dashboard/
├── app.py                # Streamlit dashboard
├── data/
│   ├── raw/              # original dataset
│   └── sales.db          # SQLite database (generated)
├── clean_data.py         # cleaning and loading script
├── requirements.txt
├── screenshots/
└── README.md
```
<!-- Adjust file names to match your actual repo. -->

## Getting started

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/retail-sales-dashboard.git
   cd retail-sales-dashboard
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Prepare the data**
   ```bash
   python clean_data.py
   ```

4. **Run the dashboard**
   ```bash
   streamlit run app.py
   ```
   The app opens at `http://localhost:8501`.

## Dataset

[Name of the dataset and source link, e.g., Kaggle]. The data covers [time period] and includes [orders, products, regions, sales, profit].

## Future improvements

- Deploy on Streamlit Community Cloud
- Add sales forecasting
- Add customer segmentation

## Author

**Rishabh Singh**
B.Tech CSE, Patel College of Science and Technology, Indore
[LinkedIn](https://www.linkedin.com/in/rishabh-singh-84aab8419) • rishabh30.cse@gmail.com
