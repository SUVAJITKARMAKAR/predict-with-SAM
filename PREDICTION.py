# IMPORTING THE REQUIRED MODULES IN THE WORKSPACE
import os
import pickle
import streamlit as stream
from streamlit_option_menu import option_menu



# SETTING PAGE CONFIGURATION
stream.set_page_config(page_title="PREDICT WITH SAM",
            layout="wide",
            page_icon=""
)


    
# GETTING THE WORKING DIRECTORY OF THE app.py
main_directory = os.path.dirname(os.path.abspath(__file__))

#LOADING THE MODEL DATASETS / MODEL TRAININGS
diabetes_model = pickle.load(open(f'{main_directory}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{main_directory}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{main_directory}/saved_models/parkinsons_model.sav', 'rb'))

# SIDEBAR FOR NAVIGATION OF THE PREDICTION PAGE
with stream.sidebar:
    selected = option_menu('DISEASE PREDICTOR', ['DIABETES','CORONARY','PARKINSONISM'], menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# DEFINING THE SIDEPANE

##########################################################################################################
#DIABETES PREDICTION PAGE
if selected == 'DIABETES':

    # PAGE TITLE
    stream.title("DIABETES: ALL YOU NEED TO KNOW!")

    stream.image('https://d2jx2rerrg6sh3.cloudfront.net/images/Article_Images/ImageForArticle_22744_16565132428524067.jpg', use_column_width=True)

    stream.markdown(
            """
            Diabetes is a chronic metabolic disorder characterized by elevated blood sugar levels resulting from defects in insulin production, insulin action, or both.
            Insulin, produced by the pancreas, helps regulate blood sugar levels by facilitating the uptake of glucose from the bloodstream into cells for energy production.
            In individuals with diabetes, this process is impaired, leading to persistent hyperglycemia.
            """
    )

    stream.subheader("TYPE OF DIABETES:")
    stream.markdown(
            """
            - **Type 1 Diabetes**: Autoimmune disease where the body's immune system attacks and destroys the cells in the pancreas that produce insulin.
            - **Type 2 Diabetes**: Most common type of diabetes and occurs when the body becomes resistant to insulin or doesn't produce enough insulin to maintain normal blood sugar levels.
            - **Gestational Diabetes**: Occurs during pregnancy and is caused by hormonal changes that affect insulin sensitivity.
            """
    )

    stream.subheader("SYMPTOMS OF DIABETES:") 
    stream.markdown(
            """
            - Feeling more thirsty than usual.
            - Urinating often.
            - Losing weight without trying.
            - Presence of ketones in the urine. Ketones are a byproduct of the breakdown of muscle and fat that happens when there's not enough available insulin.
            - Feeling tired and weak.
            - Feeling irritable or having other mood changes.
            - Having blurry vision.
            - Having slow-healing sores.
            - Getting a lot of infections, such as gum, skin, and vaginal infections.
            """
    )

    stream.subheader("IMPACT OF DIABETES ON HEALTH:") 
    stream.markdown(
            """
            - **Cardiovascular Disease**: Increased risk of heart disease, heart attack, stroke, and peripheral artery disease due to damage to blood vessels.
            - **Kidney Disease**: Leading cause of kidney failure, resulting from damage to kidney blood vessels and impaired waste filtration.
            - **Neuropathy**: Nerve damage causes numbness, tingling, pain, weakness, and digestive or sexual dysfunction.
            - **Eye Complications**: Diabetic retinopathy, macular edema, cataracts, and glaucoma can lead to vision loss or blindness.
            - **Foot Complications**: Increased susceptibility to foot ulcers, infections, slow wound healing, and potential amputation.
            - **Dental Issues**: Higher risk of gum disease, tooth decay, and tooth loss due to impaired immune function.
            - **Mental Health**: Diabetes management can lead to stress, anxiety, depression, and decreased quality of life.
            """
    )

    stream.subheader("PREVENTION OF DIABETES:")
    stream.markdown(
            """
            Type 1 diabetes can't be prevented.
            But the healthy lifestyle choices that help treat prediabetes, type 2 diabetes, and gestational diabetes can also help prevent them:
            - Eat healthy foods.
            - Get more physical activity.
            - Lose excess pounds.
            """
    )

    # HORIZONTAL LINE
    stream.markdown("<hr>", unsafe_allow_html=True)

    # CHECKING FUNCITON
    stream.header("KNOW IF YOU HAVE DIABETES")
    stream.markdown("""

""")

    # GETTING INPUT FROM THE USER
    col1, col2, col3 = stream.columns(3)

    with col1:
        Pregnancies = stream.text_input('NUMBER OF PREGNANCIES')

    with col2:
        Glucose = stream.text_input('GLUCOSE LEVEL')

    with col3:
        BloodPressure = stream.text_input('BLOOD PRESSURE VALUE')

    with col1:
        SkinThickness = stream.text_input('SKIN THICKNESS VALUE')

    with col2:
        Insulin = stream.text_input('INSULIN LEVEL')

    with col3:
        BMI = stream.text_input('BMI VALUE')

    with col1:
        DiabetesPedigreeFunction = stream.text_input('PEDIGREE FUNCTION VALUE')

    with col2:
        Age = stream.text_input('AGE OF THE PERSON')


    # CODE FILL-UP FOR PREDICTION
    diab_diagnosis = ''
    # CREATING A BUTTON FOR PREDICTION
    if stream.button('DIABETES TEST RESULT'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'THE PERSON IS DIABETIC'
            stream.success(diab_diagnosis)
        else:
            diab_diagnosis = 'THE PERSON IS NOT DIABETIC'
            stream.success(diab_diagnosis)

    # HORIZONTAL LINE
    stream.markdown("<hr>", unsafe_allow_html=True)
##########################################################################################################

##########################################################################################################
# HEART DISEASE PREDICTION PAGE 
if selected == 'CORONARY':

    # PAGE TITLE
    stream.title("CORONARY DISEASE: ALL YOU NEED TO KNOW!")
    stream.image('https://yaledailynews.com/wp-content/uploads/2021/02/yalenews.jpg', use_column_width=True)

    stream.markdown(
            """
            Coronary disease describes a range of conditions that affect the heart. These include:
            - Blood vessel disease, such as coronary artery disease
            - Irregular heartbeats (arrhythmias)
            - Heart problems you're born with (congenital heart defects)
            - Disease of the heart muscle
            - Heart valve disease
            """
    )
    
    stream.subheader("SYMPTOMS OF CORONARY DISEASE:")
    stream.markdown(
            """
            - **Heart attack**: Chest pain or discomfort, upper back or neck pain, indigestion, heartburn, nausea or vomiting, extreme fatigue, upper body discomfort, dizziness, and shortness of breath.
            - **Arrhythmia**: Fluttering feelings in the chest (palpitations).
            - **Heart failure**: Shortness of breath, fatigue, or swelling of the feet, ankles, legs, abdomen, or neck veins.
            """
    )
    
    stream.subheader("RISK FACTORS FOR CORONARY DISEASE:") 
    stream.markdown(
            """
            High blood pressure, high blood cholesterol, and smoking are key risk factors for heart disease. Several other medical conditions and lifestyle choices can also put people at a higher risk for heart disease, including:
            - Diabetes
            - Overweight and obesity
            - Unhealthy diet
            - Physical inactivity
            - Excessive alcohol use
            """
    )

    stream.subheader("PREVENTION OF CORONARY DISEASE:")
    stream.markdown(
            """
            The same lifestyle changes used to manage heart disease may also help prevent it. Trying these heart-healthy tips can help to a great extent:
            - Don't smoke.
            - Eat a diet that's low in salt and saturated fat.
            - Exercise at least 30 minutes a day on most days of the week.
            - Maintain a healthy weight.
            - Reduce and manage stress.
            - Control high blood pressure, high cholesterol and diabetes.
            - Get good sleep. Adults should aim for 7-9 hours of sleep daily.
        """
    )
    

        # HORIZONTAL LINE
    stream.markdown("<hr>", unsafe_allow_html=True)

    # CHECKING FUNCITON
    stream.header("KNOW IF YOU HAVE CORONARY DISEASE")
    stream.markdown("""

""")

    col1, col2, col3 = stream.columns(3)

    with col1:
        age = stream.text_input('AGE')

    with col2:
        sex = stream.text_input('SEX [ MALE : 1, FEMALE : 0 ]')

    with col3:
        cp = stream.text_input('CHEST PAIN TYPES')

    with col1:
        trestbps = stream.text_input('RESTING BLOOD PRESSURE')

    with col2:
        chol = stream.text_input('SERUM CHOLESTORAL IN mg/dl')

    with col3:
        fbs = stream.text_input('FASTING BLOOD SUGAR > 120 mg/dl')

    with col1:
        restecg = stream.text_input('RESTING ELECTROCARDIOGRAPHIC RESULTS')

    with col2:
        thalach = stream.text_input('MAXIMUM HEART RATE ACHIEVED')

    with col3:
        exang = stream.text_input('EXERCISE INDUCED ANGINA')

    with col1:
        oldpeak = stream.text_input('ST DEPRESSION INDUCED BY EXERCISE')

    with col2:
        slope = stream.text_input('SLOPE OF THE PEAK EXERCISE ST SEGMENT')

    with col3:
        ca = stream.text_input('MAJOR VESSELS COLORED BY FLOUROSOPY')

    with col1:
        thal = stream.text_input('THAL: 0 = NORMAL; 1 = FIXED DEFECT; 2 = REVESABLE DEFECT')

    # CODE FOR PREDICTION
    heart_diagnosis = ''
    # CREATING A BUTTON FOR PREDICTION
    if stream.button('HEART DIEASE TEST RESULT'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'THE PERSON IS HAVING HEART DISEASE'
            stream.success(heart_diagnosis)
        else:
            heart_diagnosis = 'THE PERSON DOES NOT HAVE ANY HEART DISEASE'
            stream.success(heart_diagnosis)

        # HORIZONTAL LINE
    stream.markdown("<hr>", unsafe_allow_html=True)
##########################################################################################################

##########################################################################################################
# Parkinson's Prediction Page
if selected == "PARKINSONISM":

    # PAGE TITLE
    stream.title("PARKINSONISM: ALL YOU NEED TO KNOW!")
    stream.image('https://www.labiotech.eu/wp-content/uploads/2023/04/Parkinsons-disease-2.jpg', use_column_width=True)

    stream.markdown(
            """
            Parkinson’s disease is an age-related degenerative brain condition, meaning it causes parts of one's brain to deteriorate.
            It’s best known for causing slowed movements, tremors, balance problems and more.
            Most cases happen for unknown reasons, but some are inherited.
            While this condition is best known for how it affects muscle control, balance and movement, it can also cause a wide range of other effects on one's senses, thinking ability, mental health and more.
            """
    )

    stream.subheader("TYPES OF PARKINSONISM:")
    stream.markdown(
            """
            - *Primary Parkinsonism*: Includes Parkinson’s disease and atypical parkinsonian disorders.
            - *Secondary Parkinsonism*: Includes neurological disorders commonly caused by brain tumors, toxins or medications.
            """
    )

    stream.subheader("CAUSES OF PARKINSONISM:") 
    stream.markdown(
            """
            - Familial Parkinson's disease
            - Idiopathic Parkinson's disease
            - Induced Parkinsonism
            """
    )

    stream.subheader("TREATMENT AND CURE FOR PARKINSONISM:") 
    stream.markdown(
            """
            For now, Parkinson’s disease is not curable, but there are multiple ways to manage its symptoms. The treatments can also vary from person to person, depending on their specific symptoms and how well certain treatments work. Medications are the primary way to treat this condition.
            """
    )

    stream.subheader("PREVENTION OF PARKINSONISM:")
    stream.markdown(
            """
            Parkinson’s disease happens for either genetic reasons or unpredictably. Neither are preventable, and you also can’t reduce your risk of developing it. There are certain high-risk occupations such as farming and welding, but not everyone in these professions develops parkinsonism.
            """
    )

    # HORIZONTAL LINE
    stream.markdown("<hr>", unsafe_allow_html=True)

    # CHECKING FUNCITON
    stream.header("KNOW IF YOU HAVE PARKINSONISM")
    stream.markdown("""

""")


    col1, col2, col3, col4, col5 = stream.columns(5)

    with col1:
        fo = stream.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = stream.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = stream.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = stream.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = stream.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = stream.text_input('MDVP:RAP')

    with col2:
        PPQ = stream.text_input('MDVP:PPQ')

    with col3:
        DDP = stream.text_input('Jitter:DDP')

    with col4:
        Shimmer = stream.text_input('MDVP : SHIMMER')

    with col5:
        Shimmer_dB = stream.text_input('MDVP : SHIMMER(dB)')

    with col1:
        APQ3 = stream.text_input('SHIMMER : APQ3')

    with col2:
        APQ5 = stream.text_input('SHIMMER : APQ5')

    with col3:
        APQ = stream.text_input('MDVP : APQ')

    with col4:
        DDA = stream.text_input('SHIMMER : DDA')

    with col5:
        NHR = stream.text_input('NHR')

    with col1:
        HNR = stream.text_input('HNR')

    with col2:
        RPDE = stream.text_input('RPDE')

    with col3:
        DFA = stream.text_input('DFA')

    with col4:
        spread1 = stream.text_input('SPREAD : 1')

    with col5:
        spread2 = stream.text_input('SPREAD : 2')

    with col1:
        D2 = stream.text_input('D2')

    with col2:
        PPE = stream.text_input('PPE')

    # CODE FOR PREDICTION
    parkinsons_diagnosis = ''


    # CREATING A BUTTON FOR PREDICTION
    if stream.button("PARKINSON TEST RESULT"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "THE PERSON HAS PARKINSON'S DIEASE"
            stream.success(parkinsons_diagnosis)
        else:
            parkinsons_diagnosis = "THE PERSON DOES NOT HAVE PARKINSON DIEASE"
            stream.success(parkinsons_diagnosis)

    # HORIZONTAL LINE
    stream.markdown("<hr>", unsafe_allow_html=True)
##########################################################################################################
