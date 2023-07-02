# mri-cancer-classification
AI Diagnosis Model for Brain Tumors using Teachable Machine
This project demonstrates the development of an AI model using Teachable Machine for diagnosing four types of brain tumors - non-cancerous, pituitary cancer,
meningioma, and glioma. The model is trained on a dataset of MRI images and can predict the type of tumor based on input images. The model is then exported and 
deployed using Streamlit Cloud for easy accessibility.

Dataset
The dataset used for training the model consists of a collection of MRI images of patients with different brain tumors. The images are labeled with one of the 
four tumor types - non-cancerous, pituitary cancer, meningioma, and glioma. The dataset was carefully curated and annotated to ensure accuracy in the model's 
predictions.

Teachable Machine
Teachable Machine is an online platform that allows users to create and train machine learning models without writing code. In this project, 
Teachable Machine was used to build the brain tumor diagnosis model. The platform provides an intuitive interface for importing, labeling, and training 
the model using the provided dataset.

Model Architecture
The AI model for brain tumor diagnosis utilizes a deep learning architecture to process and analyze the MRI images. The specific architecture used may vary 
based on the complexity of the dataset and the desired performance. The model is trained to classify the input images into one of the four tumor types using 
a combination of neUral networks

Exporting the Model
Once the model is trained and validated using Teachable Machine, it can be exported in a format compatible with Streamlit Cloud deployment, in my case Keras.h5. 
Teachable Machine also provides an option to export the model as a TensorFlow.js model, which can be easily integrated into a Streamlit application.

Streamlit Cloud Deployment
Streamlit Cloud is a platform that enables easy deployment and sharing of machine learning applications. The exported model from Teachable Machine can be 
integrated into a Streamlit app, where users can upload MRI images and get real-time predictions on the type of brain tumor. The Streamlit app can be deployed
on Streamlit Cloud, allowing users to access the brain tumor diagnosis tool from anywhere with an internet connection.
