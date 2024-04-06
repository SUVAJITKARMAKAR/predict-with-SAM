import streamlit as stream



stream.set_page_config(
            page_title="About SAM",
            page_icon="ℹ️",
            layout="wide",
            initial_sidebar_state="expanded"
)


def main():
      stream.title("ABOUT SAM")
      stream.image('https://medical-technology.nridigital.com/medical-technology/medical_technology_feb21/ai_models_underestimate_risk/818984/Diagnostic_imaging_mobile.svg', use_column_width=True)

      stream.markdown(
            """
            SAM, named after the initials of its 3 developers - Suvajit, Alwin, and Manoswita, is a cutting-edge disease prediction application designed to empower individuals to proactively manage their health and well-being. Utilizing advanced machine learning algorithms, SAM analyzes various health parameters to predict the likelihood of specific diseases, with a primary focus on diabetes, Parkinson's disease, and coronary disease.
            """
      )

      stream.subheader("MISSION STATEMENT:")
      stream.markdown(
            """
            At SAM, our mission is to revolutionize healthcare by providing accessible and accurate disease prediction tools that empower individuals to take control of their health outcomes. We are committed to leveraging the latest advancements in technology and data science to enhance preventive care and improve health outcomes globally.
            """
      )

      stream.subheader("KEY FEATURES:")
      stream.markdown(
            """
            - **Accurate Disease Prediction**: SAM leverages state-of-the-art machine learning models, particularly the Support Vector Machine (SVM) algorithm, to accurately predict the likelihood of diseases such as diabetes, Parkinson's disease, and heart disease. By analyzing various health parameters, SAM provides personalized risk assessments tailored to each individual.
            - **Disease Knowledge Chatbot**: AskSAM is your 24/7 companion for instant access to accurate and personalized information about various diseases, symptoms, risk factors, and treatment options.
            - **User-Friendly Interface**: SAM features an intuitive and user-friendly interface that makes it easy for users to input their health data and receive instant disease predictions. With clear visualizations and informative feedback, SAM ensures that users can understand and interpret their results with ease.
            - **Privacy and Security**: At SAM, we prioritize the privacy and security of our users' data. We adhere to stringent data protection protocols and industry best practices to safeguard sensitive health information. Users can trust that their data is handled confidentially and securely at all times.
            - **Educational Resources**: In addition to disease predictions, SAM offers educational resources and insights to help users better understand their health risks and make informed lifestyle choices. Through chatbot, and recommendations, SAM empowers users to adopt healthier habits and mitigate disease risks.
            """
      )

      stream.subheader("HOW SAM WORKS:")
      stream.markdown(
            """
            SAM employs a data-driven approach to disease prediction, leveraging a combination of user-provided health data and advanced machine learning techniques. Upon inputting relevant health parameters such as blood glucose levels, blood pressure, and BMI, SAM's SVM model analyzes the data to generate personalized disease risk assessments.
            """
      )

      stream.subheader("ABOUT THE SVM ALGORITHM:")
      stream.markdown(
            """
            Support Vector Machine (SVM) is a powerful machine learning algorithm that excels in classification tasks, making it well-suited for disease prediction. SVM works by finding the optimal hyperplane that separates data points into different classes, maximizing the margin between classes while minimizing classification errors.
            """
      )

      stream.subheader("GET STARTED WITH SAM:")
      stream.markdown(
            """
            Experience the power of SAM for yourself by signing up today! Whether you're interested in monitoring your risk for diabetes, Parkinson's disease, coronary disease, or all of the above, SAM is here to support your journey toward better health and well-being.
            """
      )

      stream.markdown(
            """
            **Join the SAM community and embark on a path to proactive health management today!**
            """
      )


if __name__ == '__main__': 
      main()