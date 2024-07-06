import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

# Set RUN the program on port 8502
# streamlit run portfolio_website.py --server.port 8502
# streamlit run portfolio_website.py --server.port 80

#streamlit run your_app.py --server.port 8502


a = ".. !"
b = "Mangala"
# print(f"I call {a}, {b}. !!!")

st.title(f"{b}'s AI Test page {a} ")
#st.write("Test with AI ")

col1, col2 = st.columns(2)
with col1:
    st.write("Test with AI ")
with col2:
    st.image("image/Mickey_Mouse.png", caption='My Resized Image -MR.', width=150)

persona = """
        You are Mangala AI bot. You help people answer questions about your self (i.e Mangala)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Mangala: 

        Mangala  is an Engineer in the field of Telecommunications, AI and Robotics.
        Mangala obtained his Bachelor’s degree in Telectronics and Telecommunications Engineering
        in Electronics and Telecommunications. He is also developing automation prototypes, 
        which is a one stop solution for learning and building AI and automation projects. 
        Prior to starting his entrepreneurial career, Mangala worked as a design engineer, 
        evaluating and developing rapid prototypes.

        Mangala's Youtube Channel: 
        Mangala's Email: contact@Mangala.com 
        Mangala's Facebook: 
        Mangala's Instagram: 
        Mangala's Linkdin: 
        Mangala's Github :https://github.com/sprx-mr/
        """

user_question = st.text_input("Ask a question")
#user_question = st.text_area("Ask a question")
if st.button("Ask", use_container_width=400):
    if (user_question) =="":
        #print("AAA")
        user_question = "Hi"
    #print(f"You ask: {user_question} .!")
    prompt = user_question
    #prompt = persona +"Here is the question that the user asked" + user_question
    response = model.generate_content(prompt)
    #print(response.text)
    st.write(response.text)




