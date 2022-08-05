#backup file of original detection code.
import streamlit as st  # importing streamlit and tensorflow
import tensorflow as tf
import cv2
import keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
import numpy as np
import imutils
from PIL import Image, ImageOps


# on loading a streamlit app we get a warning, this line prevents us from getting that warning
st.set_option('deprecation.showfileUploaderEncoding', False)
# code snippet to add the icon and text to the page
st.set_page_config(page_title='IJI SYSTEMS', page_icon="🖖")


# code to reduce the padding between modules and buttons
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
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#e8eef9"
textColor = "#000000"
font = "sans serif"

# this line prevent us from loading the model again and again and will help in storing the model in cache once it has been loaded


@st.cache(allow_output_mutation=True)
def load_model():  # loading our model
    model = tf.keras.models.load_model('dense201.h5')
    return model


model = load_model()
# defining the header or title of the page that the user will be seeing

st.markdown("<h1 style='text-align: center; color: Black;'>Brain Tumor Classifier</h1>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Black;'>Input the IMAGE and Scroll for the Prediction Results</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: Black;'>TEAM - IJI </h4>",
            unsafe_allow_html=True)
st.sidebar.header("What is this Project about?")
st.sidebar.text(
    "It is a Deep learning solution to detection of Brain Tumor using MRI Scans.")
st.sidebar.header("What does it do?")
st.sidebar.text(
    "The user can upload their MRI scan and the model will try to predict whether or not the user has Brain Tumor or not.")
st.sidebar.header("What tools where used to make this?")
st.sidebar.text("The Model was made using a dataset from Kaggle along with using Kaggle notebooks to train the model. We made use of Tensorflow, Keras as well as some other Python Libraries to make this complete project. To deply it on web, we used ngrok and Streamlit!")


# accepting the image input from the user
file = st.file_uploader("Please upload your MRI Scan", type=["jpg", "png"])

# our prediction method that will accept the data and the model and would give us a prediction
def import_and_predict(image_data, model):
    opencvImage = cv2.cvtColor(np.array(image_data), cv2.COLOR_RGB2BGR)
    img = cv2.resize(opencvImage, (150, 150))
    img = img.reshape(1, 150, 150, 3)
    o = model.predict_on_batch(img)
    p = np.argmax(o, axis=1)[0]
    r = o[0][p]*100
    if p == 0:
        s = 'Glioma Tumor'
    elif p == 1:
        st.success(f'The model predicts that there is no tumor and is {r} percent sure')
    elif p == 2:
        s = 'Meningioma Tumor'
    else:
        s = 'Pituitary Tumor'

    if p != 1:
        st.success(f'The Model predicts that it is a {s} and is {r} sure')


if file is None:
    st.markdown("<h5 style='text-align: center; color: Black;'>Please Upload a File</h5>",
                unsafe_allow_html=True)
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image,model)
    #class_names = ['glioma_tumor','pituitary_tumor','no_tumor','meningioma_tumor']
    #string = "The patient most likely has:"+ class_names[np.argmax(predictions)]
    # st.success(string)
    # st.success(predictions)

