import streamlit as stream
import time

# PREDEFINED QUESTION WITH THEIR RESPECTIVE ANSWERS
questions_pairs_ask = {
      "hi": "Hello there, SAM this side! How are you today?",
      "hey there": "Hi, I am SAM. Ask me any health-related questions",
      "who are you": "I am SAM - named after my developers... S for SUVAJIT, A for ALWIN, M for MANOSWITA. Isn't that cool?",
      "can i ask you a question": "Yes, sure! Go ahead.",
      "thank you": "Always there to help!",
      "what is heart disease": "Heart disease refers to a range of conditions that affect the heart's structure and function, including coronary artery disease, heart failure, arrhythmias, and congenital heart defects.",
      "different types of heart disease": "Common types of heart disease include coronary artery disease (narrowing or blockage of coronary arteries), heart failure (inability of the heart to pump enough blood), arrhythmias (irregular heartbeats), and congenital heart defects (heart abnormalities present at birth).",
      "risk factors for heart disease": "Risk factors for heart disease include high blood pressure, high cholesterol, smoking, diabetes, obesity, physical inactivity, unhealthy diet, excessive alcohol consumption, and family history of heart disease.",
      "symptoms of heart disease": "Symptoms of heart disease may include chest pain or discomfort, shortness of breath, fatigue, palpitations, swelling in the legs, ankles, or abdomen, and dizziness or lightheadedness.",
      "heart disease diagnosis": "Heart disease can be diagnosed through various tests such as electrocardiogram (ECG), echocardiogram, stress tests, cardiac catheterization, and blood tests for cardiac biomarkers.",
      "lifestyle changes for preventing heart disease": "Lifestyle changes that can help prevent heart disease include regular exercise, maintaining a healthy weight, quitting smoking, managing stress, limiting alcohol intake, and following a balanced diet low in saturated and trans fats, cholesterol, and sodium.",
      "dietary change recommendations for heart health": "Heart disease refers to a range of conditions that affect the heart's structure and function, including coronary artery disease, heart failure, arrhythmias, and congenital heart defects.",
      "medications prescribed for heart disease": "Commonly prescribed medications for heart disease include statins (to lower cholesterol), beta-blockers (to control blood pressure and heart rate), ACE inhibitors (to widen blood vessels and lower blood pressure), and antiplatelet drugs (to prevent blood clots).",
      "complications of untreated heart disease": "Complications of untreated heart disease can include heart attack, stroke, heart failure, arrhythmias, and sudden cardiac arrest.",
      "latest advancements in heart disease treatment": "Advancements in the treatment of heart disease include minimally invasive procedures such as transcatheter aortic valve replacement (TAVR), advancements in cardiac imaging techniques, and the development of new medications targeting specific pathways involved in heart disease.",
      "role of exercise in preventing heart disease": "Regular exercise helps prevent heart disease by improving cardiovascular health, lowering blood pressure, reducing cholesterol levels, and maintaining a healthy weight.",
      "what is diabetes": "Diabetes is a chronic condition characterized by high blood sugar levels due to either insufficient insulin production or ineffective use of insulin by the body.",
      "different types of diabetes": "The main types are type 1, type 2, and gestational diabetes. Type 1 is autoimmune, type 2 is insulin resistance, and gestational occurs during pregnancy.",
      "risk factors for diabetes": "Risk factors include obesity, family history, physical inactivity, high blood pressure, and gestational diabetes history.",
      "symptoms of diabetes": "Symptoms include increased thirst, frequent urination, hunger, weight loss, fatigue, blurred vision, and slow wound healing.",
      "diabetes diagnosis": "Diagnosis is through blood tests like fasting glucose, oral glucose tolerance, and A1C tests.",
      "lifestyle changes to manage diabetes": "Lifestyle changes include a balanced diet, regular exercise, weight management, blood sugar monitoring, adequate sleep, and stress management.",
      "dietary change recommendations for diabetes management": "Emphasize fruits, vegetables, whole grains, lean proteins, and healthy fats while limiting refined carbs, sugary foods, and saturated fats.",
      "common medications prescribed for diabetes": "Medications include insulin, metformin, sulfonylureas, meglitinides, and newer classes like DPP-4 inhibitors and SGLT2 inhibitors.",
      "complications of untreated diabetes": "Complications include heart disease, stroke, kidney disease, nerve damage, eye problems, and foot issues.",
      "can diabetes be inherited": "Yes, genetics contribute to diabetes risk, but lifestyle factors also play a significant role.",
      "role of exercise in affecting blood sugar levels in diabetes": "Exercise lowers blood sugar by increasing insulin sensitivity and improving overall health.",
      "what is parkinsons disease": "Parkinson's disease is a progressive neurological disorder affecting movement, characterized by symptoms like tremors, slowness, and stiffness.",
      "early signs and symptoms of parkinsons disease": "Early signs include tremors, bradykinesia (slowness), rigidity, impaired balance, and changes in handwriting.",
      "causes of parkinson's disease": "The exact cause is unclear, but it involves a combination of genetic and environmental factors leading to dopamine-producing neuron degeneration.",
      "diagnosis of parkinsons disease": "Diagnosis involves medical history, physical exam, and symptom assessment, as there's no specific test.",
      "stages of parkinsons disease": "It progresses through five stages, from mild symptoms to severe motor and non-motor symptoms.",
      "side effects of parkinsons disease medications": "Common side effects include nausea, dizziness, hallucinations, dyskinesia, and sleep disturbances.",
      "benefit of exercise for people with parkinsons disease": "Exercise improves mobility, balance, and overall fitness, potentially slowing disease progression and enhancing mood and cognition.",
      "bye": "Goodbye for now!"
}

def chat():
      stream.title("AskSAM")
      stream.write("Meet AskSAM - Your wellness AI assistant that answers your health related queries in one click")

      # HORIZONTAL LINE
      stream.markdown("<hr>", unsafe_allow_html=True)

      # Text input for user query
      user_input = stream.text_input("YOU:", "")

      # Send button to submit user query
      if stream.button("ASK"):
            if user_input.lower() == 'bye':
                  stream.info("SAM: ")
                  stream.info(questions_pairs_ask['bye'])
            elif user_input in questions_pairs_ask:
                  stream.info("SAM : ")
                  time.sleep(5)
                  stream.info(questions_pairs_ask[user_input])
            else:
                  time.sleep(5)
                  stream.info("SAM : ")
                  stream.info("Sorry, I can't fetch your answer right now.")


      # HORIZONTAL LINE
      stream.markdown("<hr>", unsafe_allow_html=True)

if __name__ == "__main__":
      chat()



