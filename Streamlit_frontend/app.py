import streamlit as st
import requests 


st.title("PriceFlex DashBoard")

st.sidebar.header("Input Parameters")
competitor_price = st.sidebar.number_input('Competitor Price', value=10.0)
day_of_week = st.sidebar.selectbox('Day of Week', list(range(7)))
hour_of_day = st.sidebar.selectbox('Hour of Day', list(range(24)))

if st.button("Get Recommendation"):
    data = {'competitor_price': competitor_price, 'day_of_week': day_of_week, 'hour_of_day': hour_of_day}
    response = requests.post('https://127.0.0.1:8000/recommend_price', json=data)
    if response.status_code == 200:
        result = response.json()
        st.write(f"Recommended Price: ${result['recommended_price']: .2f}")
        st.write(f"Predicted Demand: ${result['predicted_demand']: .2f}")
    else:
        st.write("Error: Could not retrive recommedation")
        