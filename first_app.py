import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('My first app')


#----------- Write a data frame-----------
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

#------------ Use magic-------------------
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

#=============Draw charts and maps===================================
#-------------Draw a line chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#------------Plot a map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


#==============Add interactivity with widgets==========================
#------------Use checkboxes to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

#------------Use a selectbox for options
# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

#==================Lay out your app=====================================
option_slidebar = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option_slidebar


left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")