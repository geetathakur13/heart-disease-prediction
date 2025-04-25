# import streamlit as st
# import pickle
# from streamlit_option_menu import option_menu

# # Page Configuration
# st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# # Hide Streamlit add-ons
# hide_st_style = """
#          <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         header {visibility: hidden;}
#         </style>
#         """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# # Adding Background Image with Reduced Overlay
# background_image_url = "https://content.presspage.com/uploads/2170/475328e9-33c6-4b3e-bfae-c0c09c4f7ee1/1920_gettyimages-ai-clinic-copy.jpeg?10000"

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] {{
#     background-image: url({background_image_url});
#     background-size: cover;
#     background-position: center;
#     background-repeat: no-repeat;
#     background-attachment: fixed;
# }}
# [data-testid="stAppViewContainer"]::before {{
#     content: "";
#     position: absolute;
#     top: 0;
#     left: 0;
#     width: 100%;
#     height: 100%;
#     background-color: rgba(0, 0, 0, 0.4); /* Reduced darkness */
# }}
# </style>
# """
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Load Models Safely
# models = {
#     'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb'))
# }

# # Dropdown for Disease Selection
# selected = st.selectbox(
#     'Disease to Predict',   
#     [
#      'Heart Disease Prediction',
#     ]
# )

# # Function to Create Input Fields
# def display_input(label, key, tooltip, type="text"):
#     if type == "text":
#         return st.text_input(label, key=key, help=tooltip)
#     elif type == "number":
#         return st.number_input(label, key=key, help=tooltip, step=1)

#    # Heart Disease Prediction Page
# if selected == 'Heart Disease Prediction':
#     st.title('Heart Disease Prediction')
#     st.write("Enter the following details to predict heart disease:")
    
#     Age = display_input('Age', 'Enter age of the person', 'age', 'number')
#     Sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
#     ChestPainType = display_input('Chest Pain Type (0-3)', 'Enter chest pain type', 'cp', 'number')
#     RestingBloodPressure = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
#     CholesterolLevel = display_input('Cholesterol Level', 'Enter serum cholesterol', 'chol', 'number')
#     FastingBloodSugar = display_input('Fasting Blood Sugar (>120 mg/dl: 1, else 0)', 'Enter fasting blood sugar', 'fbs', 'number')
#     RestingECG = display_input('Resting ECG (0-2)', 'Enter resting ECG results', 'restecg', 'number')
#     MaxHeartRate = display_input('Max Heart Rate', 'Enter maximum heart rate', 'thalach', 'number')
#     ExerciseInducedAngina = display_input('Exercise Induced Angina (1 = Yes; 0 = No)', 'Enter exercise induced angina', 'exang', 'number')
#     STDepression = display_input('ST Depression', 'Enter ST depression value', 'oldpeak', 'number')
#     SlopeofPeak = display_input('Slope of Peak (0-2)', 'Enter slope value', 'slope', 'number')
#     MajorVessels = display_input('Major Vessels (0-3)', 'Enter number of major vessels', 'ca', 'number')
#     Thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')
    
#     heart_diagnosis = ''
#     if st.button('Heart Disease Test Result'):
#         heart_prediction = models['heart_disease'].predict([[Age, Sex, ChestPainType, RestingBloodPressure, CholesterolLevel, 
#                                                      FastingBloodSugar, RestingECG, MaxHeartRate, ExerciseInducedAngina, 
#                                                      STDepression, SlopeofPeak, MajorVessels, Thal]])

#         # heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
#         heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
#         st.success(heart_diagnosis)
                      
import streamlit as st
import pickle

from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Hide Streamlit elements
hide_st_style = """
         <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Background Image
# background_image_url = "https://content.presspage.com/uploads/2170/475328e9-33c6-4b3e-bfae-c0c09c4f7ee1/1920_gettyimages-ai-clinic-copy.jpeg?10000"
background_image_url = "https://eukardia.gr/wp-content/uploads/2022/11/picture-01.jpg"
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url({background_image_url});
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.3);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Force all text to be dark black
text_color_css = """
<style>
h1, h2, h3, h4, h5, h6, p, label, .stTextInput, .stNumberInput, .stSelectbox, .stButton {
    color: black !important;
}
</style>
"""
st.markdown(text_color_css, unsafe_allow_html=True)

# Load Model
models = {
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
}

# Disease selection
selected = st.selectbox('Disease to Predict', ['Heart Disease Prediction'])

# Input function
def display_input(label, key, tooltip, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Heart Disease Form
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')
    st.write("Enter the following details to predict heart disease:")
    
    Age = display_input('Age', 'Enter age of the person', 'age', 'number')
    Sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
    ChestPainType = display_input('Chest Pain Type (0-3)', 'Enter chest pain type', 'cp', 'number')
    RestingBloodPressure = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    CholesterolLevel = display_input('Cholesterol Level', 'Enter serum cholesterol', 'chol', 'number')
    FastingBloodSugar = display_input('Fasting Blood Sugar (>120 mg/dl: 1, else 0)', 'Enter fasting blood sugar', 'fbs', 'number')
    RestingECG = display_input('Resting ECG (0-2)', 'Enter resting ECG results', 'restecg', 'number')
    MaxHeartRate = display_input('Max Heart Rate', 'Enter maximum heart rate', 'thalach', 'number')
    ExerciseInducedAngina = display_input('Exercise Induced Angina (1 = Yes; 0 = No)', 'Enter exercise induced angina', 'exang', 'number')
    STDepression = display_input('ST Depression', 'Enter ST depression value', 'oldpeak', 'number')
    SlopeofPeak = display_input('Slope of Peak (0-2)', 'Enter slope value', 'slope', 'number')
    MajorVessels = display_input('Major Vessels (0-3)', 'Enter number of major vessels', 'ca', 'number')
    Thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')
    
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([[Age, Sex, ChestPainType, RestingBloodPressure, CholesterolLevel, 
                                                             FastingBloodSugar, RestingECG, MaxHeartRate, ExerciseInducedAngina, 
                                                             STDepression, SlopeofPeak, MajorVessels, Thal]])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.success(heart_diagnosis)
