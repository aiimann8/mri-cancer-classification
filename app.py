import streamlit as st
import tensorflow as tf
from PIL import Image
from img_classification import teachable_machine_classification
st.set_page_config(layout="wide")
#st.divider()
st.title("Diagnòstic MRI de tumors cerebrals amb IRM")
st.header("Brain Tumor MRI Classification")

uploaded_file = st.file_uploader("Puja una imatge IRM en format JPG per diagnosticar si conté alguna tipologia (o no) de càncer cerebral (Glioma, Meningioma o Pituitari)", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imatge IRM pujada', use_column_width=True)
    st.write("")
    st.write("Classificant...")
    label = teachable_machine_classification(image, 'keras_model.h5')
    if label == 0:
        st.subheader("L'escàner IRM té un glioma")
    if label == 1:
        st.subheader("L'escàner IRM té un meningioma")
    if label == 2:
        st.subheader("L'escàner IRM té un tumor pituitàri")
    if label == 3:
        st.subheader("L'escàner és sa")
        
        
st.title("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ")
#st.divider()
st.title("Dades gràfiques del model d'Intel·ligència artificial (100 èpoques, 512 lots i 0,001 learning rate) ")     
st.header("Matriu de confusió")
from PIL import Image
image = Image.open('Matriu de confusió (100 èpoques, 512 lots i 0,001 learning rate).png')
st.image(image, caption='',use_column_width=False)

st.title("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ")
st.header("Precisió per èpoques")
from PIL import Image
image = Image.open('Accuracy per epoch (100 epochs, 512 batch size, o,001 learning rate).png')
st.image(image, caption='',use_column_width=False)

st.title("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ")
st.header("Pèrdua per èpoques")
from PIL import Image
image = Image.open('Loss per epoch (100 epochs, 512 batch size, 0,001 learning rate).png')
st.image(image, caption='',use_column_width=False)
