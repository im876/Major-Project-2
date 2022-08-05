import streamlit as st
import numpy as np
import pandas as pd
#from pages import utils
from PIL import  Image

# @st.cache
def app():

    st.markdown("<h4 style='text-align: centre; color: Black;'>Information about Brain Tumor</h4>",
            unsafe_allow_html=True)
    st.write("There are two types of tumours. They are as follows:")
    st.write("1. Benign:Benign tumors don't spread too fast, and have defined boundaries.")
    st.write("2. Malignant:Malignant tumors can easily spread at a rapid rate. They are not restricted and can cause damage to the central nervous system.")
    
    st.write("")
    st.write("")
    st.write("There are various types of brain tumors, but the project focuses on three types of tumor in particular. They are Glioma type of tumor, Meningioma type of tumor, and Pituitary type of tumor. You can click on the buttons given below to access information on these types of tumor.")
    if st.button("Glioma Tumor"):
        st.info("A glioma is a tumor that forms when glial cells grow out of control. Normally, these cells support nerves and help your central nervous system work. Gliomas usually grow in the brain, but can also form in the spinal cord. Gliomas are malignant (cancerous), but some can be very slow growing. They're primary brain tumors, meaning they originate in the brain tissue.")
        display = Image.open('glioma.webp')
        display = np.array(display)
        st.image(display,width=300)

    if st.button("Meningioma Tumor"):
        st.info("A meningioma is a tumor that forms in your meninges, which are three layers of tissue that cover and protect your brain and spinal cord. Meningiomas originate from arachnoid cells in particular, which are cells within the thin, spiderweb-like membrane that covers your brain and spinal cord. This is one of three layers that make up the meninges. Most meningiomas aren’t cancerous (benign), though they can sometimes be cancerous (malignant).")
        display = Image.open('meningioma.webp')
        display = np.array(display)
        st.image(display,width=350)

    if st.button("Pituitary Tumor"):
        st.info("Pituitary tumors are abnormal growths that develop in your pituitary gland. Some pituitary tumors result in too much of the hormones that regulate important functions of your body. Some pituitary tumors can cause your pituitary gland to produce lower levels of hormones. Most pituitary tumors are noncancerous (benign) growths (adenomas).")
        display = Image.open('pituitary.webp')
        display = np.array(display)
        st.image(display,width=300)

    st.write("")
    st.write("")
    st.markdown("<h4 style='text-align: centre; color: Black;'>Symptoms of Brain Tumor</h4>",
            unsafe_allow_html=True)
    st.write("There are various symptoms associated with each of these brain tumours. Some of the most common ones are as follows:")
    st.write("1. Headaches")
    st.write("2. Memory loss")
    st.write("3. Headaches")
    st.write("4. Vertigo or dizziness")
    st.write("5. Vomiting")
    st.write("6. Blurred vision or double vision")
    st.write("7. Confusion")
    st.write("8. Seizures (in adults)")

    st.write("")
    st.write("")
    st.markdown("<h4 style='text-align: centre; color: Black;'>How the diagnosis/detection is performed in traditional approach?</h4>",
            unsafe_allow_html=True)
    st.write("In traditional methods there are three major methods to detect the brain tumor. They are as follows:")
    st.write("1. A neurological exam - Simple tests such as checking vision, hearing, balance and coordination.")
    st.write("2. Imaging Tests - Magnetic resonance imaging  (MRI), computerized tomography (CT) and positron emission tomography (PET).")
    st.write("3. Biopsy - Collecting a tisuue cell and testing the type of brain tumor. For better results.")

    st.write("")
    st.write("")
    st.markdown("<h4 style='text-align: centre; color: Black;'>How the treatment is done post detection?</h4>",
            unsafe_allow_html=True)
    st.write("The type of treatment received will depend on various factors. They are as follows:")
    st.write("1. The type of tumor")
    st.write("2. The size of the tumor")
    st.write("3. The location of the tumor")
    st.write("4. If the tumor has spread to other parts of the CNS or body")
    st.write("5. Possible side effects and overall health")

    st.write("")
    st.write("Click on the buttons below to gain an insight on the treatments available currently.")
    if st.button("Surgery:"):
        st.info("1. Brain tumor location is accessible \n 2. Tissues surrounding sensitive parts of brain can't be removed. \n 3. For small and easy operations. \n 4. Surgery to remove a brain tumor carries risks, such as infection and bleeding, depending upon the location. (eg -eyes may get affected) \n 5. Preferred first for low grade Brain tumor, as well as main parts of the tumor. \n 6. Removing the tumor can improve neurological symptoms, provide tissue for diagnosis and genetic analysis \n 7. Help make other brain tumor treatments more effective \n 8. Craniotomy- Process of removal of brain tumor after removing the part of the skull.")

    if st.button("Radiation Therapy:"):
        st.info("1. Radiation therapy uses high-energy beams, such as X-rays or protons, to kill tumor cells. \n 2. Brachytherapy:is a form of radiation therapy where a sealed radiation source is placed inside or next to the area requiring treatment. \n 3. Close to sensitive areas of the brain are treated easily. \n 4. Children are treated using this method. \n 5. Fatigue, headaches, memory loss, scalp irritation and hair loss are side effects(may occur)")

    if st.button("Radiosurgery:"):
        st.info("1. Gives a highly focused form of radiation treatment to kill the tumor cells in a very small area. \n 2. Receives a very large dose of radiation to kill the tumor cells. \n 3. Gamma Knife or linear accelerator.Radiosurgery is typically done in one treatment, and usually you can go home the same day. \n 4. It is the fastest way.")

    if st.button("Chemotherapy:"):
        st.info("1. Drugs to kill tumor cells. Chemotherapy drugs can be taken orally in pill form or injected into a vein \n 2. The type of brain tumor determines whether to recommend this or not. \n 3. goal of chemotherapy can be to destroy tumor cells remaining after surgery, slow a tumor's growth, or reduce symptoms. \n 4. Others symptoms are kidney damage.")