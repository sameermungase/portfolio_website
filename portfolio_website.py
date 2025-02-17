import google.generativeai as genai
# import os
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Sameer Mungase | Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        font-size: 3rem !important;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# API Configuration
api_key = st.secrets["GOOGLE_API_KEY"]
# api_key =""
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

# Header Section
header_col1, header_col2 = st.columns([2, 1])
with header_col1:
    st.markdown("### Hello there! 👋")
    st.title("I'm Sameer Mungase")
    st.markdown("""
        🎓 Electronics & Telecommunication Engineering Student  
        💻 Passionate about Programming & Computer Vision  
        🌟 Always eager to learn and grow
    """)
with header_col2:
    st.image("imagee/sam.jpg", width=250)

# AI Chatbot Section
st.markdown("---")
st.header("💬 Let's Chat!")
with st.expander("Chat with Sameer's AI Assistant"):
    persona = """
        You are Sameer AI bot. You help people answer questions about your self (i.e Sameer Mungase).
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Sameer: 
         
        Sameer Mungase is an Undergraduate Student in the field of Electronics and telecommunication engineering at Government college 
        of engineering , Chatrapati Sambhaji Nagar(Aurangabad)
        Sameer is also interested in programming and DSA in java and also started learning python. Sameer is obtaining his Bachelor's degree in
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
    user_question = st.text_input("Ask me anything about Sameer:", placeholder="Example: What are Sameer's interests?")
    if st.button("Ask", type="primary", use_container_width=True):
        with st.spinner("Thinking..."):
            prompt = persona + "Here is the question that the user asked: " + user_question
            response = model.generate_content(prompt)
            st.write(response.text)

# Skills Section
st.markdown("---")
st.header("🚀 My Skills")
skills_col1, skills_col2 = st.columns(2)

with skills_col1:
    st.subheader("Technical Skills")
    st.progress(70, "DSA")
    st.progress(80, "Core Java")
    st.progress(75, "Linux")
    
with skills_col2:
    st.subheader("Other Skills")
    st.progress(50, "Python")
    st.progress(50, "Computer Networks")

# Projects Section
st.markdown("---")
st.header("🛠️ My Projects")
proj_col1, proj_col2 = st.columns(2)

with proj_col1:
    with st.container():
        st.subheader("⚡ Electronics Projects")
        for project in ["Home Appliances Automation", "Trinetra - Visual Aid Device", "Smart Blind Stick"]:
            st.markdown(f"- {project}")

with proj_col2:
    with st.container():
        st.subheader("💻 Software Projects")
        for project in ["AI Chatbot", "Hotel Management System", "Portfolio Website"]:
            st.markdown(f"- {project}")

# College Section
st.markdown("---")
st.header("🎓 My College")
st.image("imagee/geca.jpeg", use_column_width=True)

# Contact Section
st.markdown("---")
st.header("📫 Get in Touch")
contact_col1, contact_col2, contact_col3 = st.columns(3)

with contact_col1:
    st.markdown("#### Social Links")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/sameer-mungase-b341b6286/)")
    st.markdown("[📺 YouTube](https://www.youtube.com/@sam.-_)")
    
with contact_col2:
    st.markdown("#### More Links")
    st.markdown("[📸 Instagram](https://www.instagram.com/sameer_mungase)")
    st.markdown("[💻 GitHub](https://github.com/sameermungase)")
    
with contact_col3:
    st.markdown("#### Email")
    st.markdown("📧 sameer49@geca.ac.in")
    st.markdown("📧 snwopierce111@gmail.com")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey;'>© 2024 Sameer Mungase. All rights reserved.</p>", 
    unsafe_allow_html=True
)
