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
    video_file = open('C:/Users/admin/app/intro.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    st.markdown("<h3 style='text-align: left; color: Black;'>What is this project about?</h3>",
            unsafe_allow_html=True)
    st.text("It is a Deep learning solution to detection of Brain Tumor using MRI Scans.")

    st.markdown("<h3 style='text-align: left; color: Black;'>What does it do?</h3>",
            unsafe_allow_html=True)
    st.text("The user can upload their MRI scan and the model will try to predict whether or not")
    st.text("the user has Brain Tumor or not.")

    st.markdown("<h3 style='text-align: left; color: Black;'>What tools where used to make this?</h3>",
            unsafe_allow_html=True)
    st.text("The Model was made using a dataset from Kaggle along with using Kaggle notebooks to")
    st.text("train the model. We made use of Tensorflow, Keras as well as some other Python")
    st.text("Libraries to make this complete project.")
