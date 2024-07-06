import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
#Geminai API KEY: AIzaSyC9ek2o79U4tc8JAFcm5EIq3cl14viZVQc
#genai.configure(api_key="AIzaSyC9ek2o79U4tc8JAFcm5EIq3cl14viZVQc")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

# Set RUN the program on port 8502
# streamlit run portfolio_website.py --server.port 8502
# streamlit run portfolio_website.py --server.port 80

#streamlit run your_app.py --server.port 8502


a = "Hi"
b = "Mangala"
# print(f"I call {a}, {b}. !!!")

st.title(f"{b}'s AI Test page, {a} .. !")
st.write("Test with AI ")

col1, col2 = st.columns(2)
with col1:
    st.write("Test with AI ")
with col2:
    st.image("image/Mickey_Mouse.png", caption='My Resized Image -MR.', width=150)
pasona = """ You are Mangala's AI bot. You help people answer questions about your self (i.e Mangala)
             Answer as if you are responding . dont answer in second or third person. If you 
             don't know they answer you simply say "That's a secret".
             Here is more info about Mangala: 
             Mangala is an Engineer"""

user_question = st.text_input("Ask a question")
if st.button("Ask", use_container_width=400):
    print(f"You ask: {user_question} .!")
    #prompt = user_question
    prompt = pasona +"Here is the question that the user asked" + user_question
    response = model.generate_content(prompt)
    print(response.text)
    st.write(response.text)


