import streamlit as stream
import time

# PREDEFINIED QUESTION WITH THIER RESPECTIVE ANSWERS
questions_pairs_ask = {
      "hi": "Hello there SAM this side ! How are you today ?",
      "hey there": "Hi, I am SAM. Ask me any health related questions",
      "who are you": "I am SAM - named after my developers. S for SUVAJIT, A for ALWIN, M for MANOSWITA. Isn't it cool",
      "can i ask you a question": "Yes sure ! Go ahead.",
      "bye": "GoodBye for now"
}

def chat():
      stream.title("AskSAM")
      stream.write("Meet AskSAM - Your wellness AI assistant that answers your health related queirs in one click")

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
                  time.sleep(3)
                  stream.info(questions_pairs_ask[user_input])
            else:
                  stream.info("SAM : ")
                  stream.info("Sorry, I don't understand that question.")


      # HORIZONTAL LINE
      stream.markdown("<hr>", unsafe_allow_html=True)

if __name__ == "__main__":
      chat()



