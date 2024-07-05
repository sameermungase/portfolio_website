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
         
        Sameer Mungase is an Undergraduate Student in the field of Electronics and telecommunication engineering.
        Sameer is also interested in programming and DSA in java and also started learning python. Sameer is obtaining his Bachelor’s degree in
        Electronics and Telecommunication and later specializing in the field of computer scienc maybe. 
        Sameer is also interested in the field of computer vision . Sameer is also 
        working on his core java skills . Sameer is  also preparing for the placements in the field of software 
        engineering , and core electronics companies also ,
        for that he is preparing for interviews , soft skills also with general aptitude also.
        
 
        Murtaza's Youtube Channel: www.youtube.com/@sam.-_
        Murtaza's Email: .com snwopierce111@gmail.com
        Murtaza's Facebook: https://www.facebook.com/murtazasworkshop
        Murtaza's Instagram: https://www.instagram.com/sameer_mungase?utm_source=qr&igsh=dWs3N2QyNTA0OXls
        Murtaza's Linkdin: https://www.linkedin.com/in/sameer-mungase-b341b6286/
        Murtaza's Github :https://github.com/sameermungase
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

st.title(" ")

st.title("About My College")

st.image("imagee/geca.jpeg", width=700)


st.title(" ")
st.title("Some memories of college")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("imagee/img (1).jpg", width=200)
    st.image("imagee/img (2).jpg", width=200)
    st.image("imagee/img (3).jpg", width=200)

with col2:
    st.image("imagee/img (4).jpg", width=200)
    st.image("imagee/img (5).jpg", width=200)
    st.image("imagee/img (6).jpg", width=200)

with col3:
    st.image("imagee/img (7).jpg", width=200)
    st.image("imagee/img (8).jpg", width=200)
    st.image("imagee/img (9).jpg", width=200)

st.subheader(" ")
st.write("Reach me at:")
st.title("For any inquiries, email at:")
st.subheader("snowpierce.222@gmail.com")