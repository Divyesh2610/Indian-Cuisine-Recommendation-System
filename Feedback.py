import streamlit as st
import csv

def run_feedback():
    st.header(":mailbox: Share Your Feedback With Us!")
    
    # Proceed to rate the recommender system
    rating_options = ['Select your rating', '1', '2', '3', '4', '5']
    rating = st.selectbox('Rate our recommender system:', rating_options)

    # Takes user's details
    name = st.text_input('Name')
    email = st.text_input('Email')
    message = st.text_area('Message')

    if st.button('Submit'):
        fieldnames = ['Name', 'Email', 'Message', 'Rating']
        # Upon submission, the details will be stored to a csv file
        with open('feedback.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()  # Write column names if file is empty
            writer.writerow({'Name': name, 'Email': email, 'Message': message, 'Rating': rating})
        st.success('Thank you for your feedback!')

    # Using local css file 
    def local_class(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_class("style/style.css")
