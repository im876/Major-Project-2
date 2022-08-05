from ctypes import alignment
from tkinter import CENTER
import streamlit as st
import numpy as np
import pandas as pd
#from pages import utils
from PIL import  Image

# @st.cache
def app():

    padding = 0
    st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

    #st.markdown("<h3 style='text-align: center; color: Black;'>By IJI</h3>",unsafe_allow_html=True)
    st.header("Made with ❤️ by :")
    display = Image.open('Logo.png')
    display = np.array(display)
    col1, col2 , col3= st.columns(3)
    
    #col1.title("Ishan Modi")
    #col1.subheader("B150953039")
    #col2.title("Ishan Srivastava")
    #col2.subheader("B150953023")
    #col3.title("Janhavi Panambor")
    #col3.subheader("B150953045")

    col1,col2=st.columns(2)
    with col1:
            st.subheader("Ishan Modi")
    with col2:
            st.subheader("B150953039")
    with col1:
            st.subheader("Ishan Srivastava")
    with col2:
            st.subheader("B150953023")
    with col1:
            st.subheader("Janhavi Panambor")
    with col2:
            st.subheader("B150953045")
