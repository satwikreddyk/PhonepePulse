import streamlit as st
import plotly.express as px
import mysql.connector
import pandas as pd

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "israel",
    "database": "phonepe",
}

def fetch_data():
    connection = mysql.connector.connect(**db_config)
    query = "SELECT * FROM your_table"
    df = pd.read_sql(query, connection)
    connection.close()
    return df

st.title("PhonePe Pulse Dashboard")

data = fetch_data()

transaction_types = data["Transaction_Type"].unique()
instrument_types = data["Instrument_Type"].unique()

selected_transaction = st.selectbox("Select Transaction Type", transaction_types)
selected_instrument = st.selectbox("Select Instrument Type", instrument_types)

filtered_data = data[(data["Transaction_Type"] == selected_transaction) & (data["Instrument_Type"] == selected_instrument)]

fig = px.bar(filtered_data, x="Count", y="Amount", title=f"{selected_transaction} - {selected_instrument}")
st.plotly_chart(fig)
