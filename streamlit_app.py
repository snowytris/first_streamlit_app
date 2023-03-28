
from snowflake.connector import connect
import streamlit as st


conn = connect(**st.secrets["snowflake"])
cursor = conn.cursor()

# Execute some SQL in the warehouse
cursor.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION();")
# Fetch the results
one_row = cursor.fetchone()

st.title("Coucou")
st.text(one_row)
