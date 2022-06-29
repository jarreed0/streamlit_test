# Run main_page.py first
import streamlit as st
import pandas as pd

# Set the page name
st.sidebar.markdown("# Worksheet Page")

# Load in data, and cache it so we don't have to load in a lot of data on refresh.
@st.cache
def get_data():
    return pd.read_csv("data.csv").drop(['_c0'],axis=1) #use different data here maybe
df = get_data()

# Write a header that says "Learning how to use Streamlit"
st.markdown("Learning how to use Streamlit 🎈")


# Create a check box labeled "Show data" that when checked, displays the dataframe
show_data = st.checkbox("Show data")
if show_data:
	st.write(df)


# Create a slider that allows the user to choose a range between two years from our movie dataset
min_year, max_year = st.slider('Year', value=(2000,2010), min_value=1950, max_value=2020)

# start_color, end_color = st.select_slider(
#      'Select a range of color wavelength',
#      options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
#      value=('red', 'blue'))
# st.write('You selected wavelengths between', start_color, 'and', end_color)
