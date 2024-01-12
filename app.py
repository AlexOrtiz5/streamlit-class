import streamlit as st 
import pandas as pd
import src.functions as func

def main():
    st.title('Supermarket Sales Dashboard')

    data = func.load_data()
    
    # Sidebar
    st.sidebar.header('Controls')
    min_rating = st.sidebar.slider('Minimun Rating', min_value=0, max_value=10, value=5, step=1)
    
    # Filters
    filter_data = data.loc[data['Rating'] >= min_rating]
    summary = func.get_summary(filter_data)
    
    # Display summary stats
    st.write("### Summary Statistics")
    st.dataframe(summary)
    
    # Display raw data
    st.write("### Raw Data")
    st.dataframe(filter_data)
    
    # Plotting
    st.write("### Sales Over Time")
    st.pyplot(func.plot_sales_over_time(filter_data))

if __name__ == '__main__':
    main()