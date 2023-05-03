# Necessary modules are loaded
import streamlit as st 
import recommender_system
import Feedback
import Admin_Panel
from streamlit_option_menu import option_menu
from PIL import Image

# Loading the image 
Logo_Image = Image.open('Ingredients.jpg')

# Displays title, description & logo with the help of sidebar function 
with st.sidebar:
    st.sidebar.image(Logo_Image, width=300)
    st.header("Welcome to Our Recommender System.")
    st.write("Our recommender system provides recommendations based on the ingredients similarity between recipes.")
    st.write("Provide the recipe of your choice, then our system will analyse ingredients of the particular recipe and will match the recipes with similar recipes in our database and provide recipes along with ingredients, directions and url as well.")

# Creating menu options
selected = option_menu(
    menu_title = None,
    options=['Recommender System','Feedback','Admin Panel'],
    orientation="horizontal",
    )

# Redirecting towards menu option when selected
if selected == 'Recommender System':
    recommender_system.app()
if selected == 'Feedback':
    Feedback.run_feedback()
if selected == 'Admin Panel':
    Admin_Panel.admin_panel()
