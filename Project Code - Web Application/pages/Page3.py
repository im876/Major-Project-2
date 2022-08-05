import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import cv2
import keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
import imutils
from PIL import Image, ImageOps

# @st.cache
def app():

    # on loading a streamlit app we get a warning, this line prevents us from getting that warning
    st.set_option('deprecation.showfileUploaderEncoding', False)

    st.markdown("<h1 style='text-align: center; color: White;'>Detection Page</h1>",
            unsafe_allow_html=True)

    @st.cache(allow_output_mutation=True)
    def load_model():  # loading our model
        model = tf.keras.models.load_model('dense201.h5')
        return model


    model = load_model()
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
        
        if p==0:
            st.info('Glioma Tumor is a type of tumor that occurs in the brain and spinal cord. Gliomas begin in the gluey supportive cells (glial cells) that surround nerve cells and help them function.')
        elif p==2:
            st.info('Meningioma Tumor is a type of tumor that arises from the meninges — the membranes that surround the brain and spinal cord. ')
        elif p==1:
            st.info('No Tumor is detected, however we would advice you to have a complete checkup!')
        else:
            st.info('Pituitary Tumor is a type of tumor that are abnormal growths that develop in your pituitary gland.')
    
    if file is None:
        st.markdown("<h5 style='text-align: center; color: Black;'>Please Upload a File</h5>",
                unsafe_allow_html=True)
    else:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        predictions = import_and_predict(image,model)

