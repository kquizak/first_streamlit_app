import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Parents New Healthy Diner")

streamlit.header('Vlad\'s Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado T')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)
 
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruits_selected[0] )
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

#streamlit.stop()

streamlit.text("The fruit load list contains:")
def get_fruit_load_list():
 with my_cnx.cursor() as my_cur:
  my_cur.execute("SELECT * from fruit_load_list")
  return my_cur.fetchall()

if streamlit.button('mata'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 my_data_row = get_fruit_load_list()
 streamlit.dataframe(my_data_row)

 #my_cur.execute("insert into fruit_load_list values ('from streamlit')")
