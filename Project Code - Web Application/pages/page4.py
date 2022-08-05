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
    st.header("Backend Results")
    st.markdown("<h4 style='text-align: left; color: Black;'>1. Classification Report</h4>",unsafe_allow_html=True)

    image = Image.open('C:/Users/admin/app/class_report.PNG')
    st.image(image, use_column_width=True)
    st.write("A classification report, gives information about the quality of the predictions. There are factors like, precision, recall, f1-score and accuracy. The numbers 0,1,2, and 3 are the numbers of the labels, in order of glioma, no-tumor, meningioma and pituitary tumor. \n The metrics are calculated by using true and false positives, true and false negatives. Positive and negative in this case are generic names for the predicted classes. There are four ways to check if the predictions are right or wrong: \n 1. TN / True Negative: when a case was negative and predicted negative. \n 2. TP / True Positive: when a case was positive and predicted positive. \n 3. FN / False Negative: when a case was positive but predicted negative. \n 4. FP / False Positive: when a case was negative but predicted positive")
    st.write("")
    st.write("• Precision is the accuracy of positive predictions.")
    st.write("Precision = TP/(TP + FP)")
    st.write("")
    st.write("• Recall is Fraction of positives that were correctly identified.")
    st.write("Recall = TP/(TP+FN)")
    st.write("")
    st.write("• F1 score is the percentage of positive predictions that were correct.")
    st.write("F1 Score = 2*(Recall * Precision) / (Recall + Precision)")
    
    st.write("")
    st.write("")
    st.markdown("<h4 style='text-align: left; color: Black;'>2. Confusion matrix</h4>",unsafe_allow_html=True)

    image = Image.open('C:/Users/admin/app/confusion_matrix.PNG')
    st.image(image, use_column_width=True)
    st.write("Confusion matrix is an evaluation parameter which gives an insight into the model accuracy by comparing the actual and predicted outputs with each other. As it can be observed, the model has a very high accuracy and is able to correctly classify images into their correct class.")