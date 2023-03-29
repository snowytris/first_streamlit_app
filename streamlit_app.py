
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


fruit_to_add = st.text_input("Ajouter un fruit")
add_fruit = st.button("Add fruit!")

if add_fruit:
  with conn.cursor() as c:
    c.execute(f"""
    INSERT INTO fruit_load_list VALUES 
    ('{fruit_to_add}');
    """)

# Display all fruits
with conn.cursor() as c:
  all_fruits = c.execute("SELECT * FROM fruit_load_list;").fetchall()
  st.dataframe(all_fruits)
  
  
