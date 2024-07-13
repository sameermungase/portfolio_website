import google.generativeai as genai
# import os
import streamlit as st

api_key = st.secrets["GOOGLE_API_KEY"]
# api_key =""
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hello :wave:")
    st.title("I am Sameer Mungase")

with col2:
    st.image("imagee/sam.jpg", width=300)

persona = """
        You are Sameer AI bot. You help people answer questions about your self (i.e Sameer Mungase).
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Sameer: 
         
        Sameer Mungase is an Undergraduate Student in the field of Electronics and telecommunication engineering at Government college 
        of engineering , Chatrapati Sambhaji Nagar(Aurangabad)
        Sameer is also interested in programming and DSA in java and also started learning python. Sameer is obtaining his Bachelor’s degree in
        Electronics and Telecommunication and later specializing in the field of computer scienc maybe. 
        Sameer is also interested in the field of computer vision . Sameer is also 
        working on his core java skills . Sameer is  also preparing for the placements in the field of software 
        engineering , and core electronics companies also ,
        for that he is preparing for interviews , soft skills also with general aptitude also.
        
 
        Sameer's Youtube Channel: www.youtube.com/@sam.-_
        Sameer's Email: .com snwopierce111@gmail.com
        Sameer's Instagram: https://www.instagram.com/sameer_mungase?utm_source=qr&igsh=dWs3N2QyNTA0OXls
        Sameer's Linkdin: https://www.linkedin.com/in/sameer-mungase-b341b6286/
        Sameer's Github :https://github.com/sameermungase
        """

st.title(" ")

st.title("Sameer's chatbot")

st.write("Ask me anything about Sameer Mungase")

user_question= st.text_input("ask")
if st.button("Ask", use_container_width=400):
    prompt = persona +"Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("My recommended learning resourse for computer vision ")

with col2:
    st.video("https://youtu.be/k2EahPgl0ho?si=0_QAgPW66W5Ng55X")

st.write(" ")

st.title("My Skills")
st.slider("DSA", 0, 100, 70)
st.slider("Core Java", 0, 100, 85)
st.slider("Linux", 0, 100, 75)
st.slider("Python", 0 ,100 ,50)
st.slider("Generative AI" ,0 ,100 ,50)

st.title(" ")

st.title("My College")

st.image("imagee/geca.jpeg", width=700)

st.title("My Projects")
col1, col2 = st.columns(2)
with col1:
    st.subheader("My Electronics Projects")
    st.write("- Home Appliances Automation")
    st.write("- Trinetra (a device which will help visually impared persons detect obstable")
    st.write("- FIR filters")

with col2:
    st.subheader("My Coding Projects")
    st.write("AI chatbot")
    st.write("Hotel Management System")
    
st.title(" ")


st.subheader(" ")
st.write("Reach me at:")
st.title("For any inquiries, email at:")
st.subheader("snowpierce.222@gmail.com")
