import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import page1,page2,Page3,page4,page5# import your pages here

# Create an instance of the app 
app = MultiPage()

# on loading a streamlit app we get a warning, this line prevents us from getting that warning
st.set_option('deprecation.showfileUploaderEncoding', False)
# code snippet to add the icon and text to the page
st.set_page_config(page_title='IJI SYSTEMS', page_icon="C:/Users/admin/app/logo.png")

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

# settings to set user interface visuals
primaryColor = "#2214c7"
backgroundColor = "#c6efef"
secondaryBackgroundColor = "#e8eef9"
textColor = "#000000"
font = "sans serif"

st.markdown("<h1 style='text-align: center; color: Black;'>Brain Tumor Detection System</h1>",
            unsafe_allow_html=True)
# Add all your application here
app.add_page("Welcome Page", page1.app)
app.add_page("Information About Brain Tumour", page2.app)
app.add_page("Detection System", Page3.app)
app.add_page("Backend Results",page4.app)
app.add_page("Team Information", page5.app)
#app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()