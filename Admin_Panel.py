import streamlit as st
import pandas as pd
import os

def admin_panel():
    st.title(':lock: Admin Panel')
    
    # Initialize authentication status to False
    authenticated = False
    
    # Display login form if user is not yet authenticated
    if not authenticated:
        st.write('Enter your login credentials below:')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        if st.button('Login'):
            if username == 'admin' and password == '1234':
                st.success('Logged in as admin')
                authenticated = True  # Set authentication status to True
            else:
                st.error('Incorrect username or password')
    
    # Display table if user is authenticated
    if authenticated:
        st.write('Recommendations History:')
        if not os.path.exists('recommendations.csv'):
            st.warning('No data found')
        else:
            df = pd.read_csv('recommendations.csv')
            st.write(df)
            
        # Display second dataframe
        st.write('Feedback details:')
        if not os.path.exists('feedback.csv'):
            st.warning('No data found')
        else:
            df2 = pd.read_csv('feedback.csv', names=['name', 'email', 'message', 'rating'], header=None)
            st.write(df2)
