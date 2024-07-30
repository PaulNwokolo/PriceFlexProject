# Will be using a dummy data for this project
# This is a dymanmic pricing model named PriceFlex that aids the users to change or ajust their 
# prices of proucts to be able to meant or have a better price 

import  pandas as pd
import numpy as np 

def gen_dummy_sales(num_rows=200000, num_stores=100,num_products=1000):
    np.random.seed(42)
    
    data = {
        'StoreID': np.random.randint(1, num_stores + 1, num_rows),
        'ProductID': np.random.randint(1, num_products + 1, num_rows),
        'Date': np.random.choice(pd.date_range(start='2024-01-01', periods=365), num_rows),
        'Sales': np.round(np.random.uniform(10.0, 1000.0, num_rows), 2),
        'Customers': np.random.randint(1, 100, num_rows),
        'Promo': np.random.choice([0, 1], num_rows, p=[0.7, 0.3]),
        'StateHoliday': np.random.choice(['0', 'a', 'b', 'c'], num_rows, p=[0.9, 0.03, 0.04, 0.03]),
        'SchoolHoliday': np.random.choice([0, 1], num_rows, p=[0.8, 0.2])
    }
    
    sales_data = pd.DataFrame(data)
    sales_data.to_csv("C:/Users/PAUL/Desktop/PriceFlex/data/sales_data.csv", index=False)
    
    print("Dummy data genrated ")
    
    
    
def gen_dummy_competitor(num_products=1000, competitors_pre_product=5,num_weeks=52):
    np.random.seed(40)
    
    competitor_data = []
    for product_id in range(1, num_products + 1):
        for week in range(num_weeks):
            data = pd.Timestamp('2024-01-01') + pd.Timedelta(weeks=week)
            for _ in range(competitors_pre_product):
                competitor_data.append({
                    'ProductID': product_id,
                    'Date': data,
                    'CompetitorPrice': np.round(np.random.uniform(5.0,500.0), 2)
                    
                })
                
    
    competitor_data = pd.DataFrame(competitor_data)
    competitor_data.to_csv("C:/Users/PAUL/Desktop/PriceFlex/data/competitor_data.csv",index=False)
    print(" The Dummy competitor data created")
    

    
gen_dummy_sales()
gen_dummy_competitor()
