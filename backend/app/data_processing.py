
import pandas as pd

def load_sales_data():
    return pd.read_csv("backend/data/sales_data.csv")

def calculate_dynamic_price(base_price, demand_factor):
    return base_price * (1.0 + demand_factor)




