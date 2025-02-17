import google.generativeai as genai
# import os
import streamlit as st
# import plotly.express as px
import pandas as pd

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
    .experience-item {
        padding: 10px;
        border-left: 2px solid #ff4b4b;
        margin: 10px 0;
    }
    .project-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .project-card h4 {
        color: #ff4b4b;
        margin-bottom: 10px;
    }
    .tools {
        color: #0066cc;
        font-size: 0.9em;
    }
    a {
        color: #ff4b4b;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    .education-item {
        padding: 20px;
        margin: 10px 0;
        border-left: 3px solid #ff4b4b;
        background-color: #ffffff;
        border-radius: 0 10px 10px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .education-item h4 {
        color: #ff4b4b;
        margin-bottom: 5px;
    }
    .education-item p {
        color: #2c3e50;
        margin: 5px 0;
    }
    .education-item .percentage {
        color: #0066cc;
        font-weight: bold;
    }
    .highlight-text {
        background: linear-gradient(120deg, #ff4b4b20 0%, #ff4b4b20 100%);
        padding: 0.2rem 0.5rem;
        border-radius: 0.3rem;
    }
    .card {
        border: 1px solid #eee;
        padding: 1.5rem;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    .card:hover {
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    .download-button {
        background-color: #ff4b4b;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 20px;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .download-button:hover {
        background-color: #ff3333;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transform: translateY(-2px);
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
        💻 Passionate about Programming & Development   
        🌟 Always eager to learn and grow
    """)
    
    # Add custom CSS for the download button
    st.markdown("""
        <style>
        .download-button {
            background-color: #ff4b4b;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 20px;
            transition: all 0.3s ease;
            border: none;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .download-button:hover {
            background-color: #ff3333;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            transform: translateY(-2px);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Download Resume Button
    st.markdown("""
        <a href="https://drive.google.com/file/d/1VlQ1vKi-lcwDacUhYAxJKOaz_fPPWPLI/view?usp=drive_link" 
           class="download-button" 
           target="_blank">
           📄 Download Resume
        </a>
    """, unsafe_allow_html=True)

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
        Electronics and Telecommunication and later specializing in the field of computer scienc. 
        Sameer is also interested in the field of computer vision . Sameer is also 
        working on his core java skills and Development skills . Sameer is  also preparing for the placements in the field of software 
        engineering , and core electronics companies also ,
        for that he is preparing for interviews , soft skills also with general aptitude also,he is also currently working at Tech Mahindra as a Technical support Trainee.
        These are some languages and Technologies that Sameer has worked on:
        - Java
        - Python
        - C++
        - SQL
        - HTML/CSS
        - JavaScript
        - Linux
        - Git & GitHub
        - AWS
        - JetBrains IntelliJ IDEA
        - Eclipse IDE
        - Visual Studio Code
        - MySQL
 
        
        Sameer's Email: sbmungase2003@gmail.com
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
st.header("🚀 Skills & Technologies")

# Create three columns for different skill categories
tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    st.markdown("""
    #### 💻 Programming Languages
    - Java
    - SQL
    - JavaScript (Basic)
    - HTML/CSS
    """)

with tech_col2:
    st.markdown("""
    #### 🛠️ Tools & Technologies
    - Linux
    - Git & GitHub
    - AWS
    - JetBrains IntelliJ IDEA
    """)

with tech_col3:
    st.markdown("""
    #### 🎯 Hobbies
    - Mobile Photography
    - Reading
    - Listening to Music
    - Learning New Skills
    """)

# Experience Section
st.markdown("---")
st.header("💼 Experience")

# Software Development Intern
st.markdown("""
<div class="experience-item">
    <h4>Software Development and AIML Intern | Makers Lab, Tech Mahindra - Pune</h4>
    <p><em>Jan 2025 - Present</em></p>
    <ul>
        <li>Currently working as a development trainee with a focus on Java programming and basic development tasks</li>
        <li>Acquired hands-on experience in Java programming, debugging, and understanding core development workflows</li>
        <li>Developing expertise in software lifecycle management, professional coding practices, and JavaScript development</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Java Programming Intern
st.markdown("""
<div class="experience-item">
    <h4>Java Programming Intern | Codealpha - Virtual</h4>
    <p><em>June 2024 - Aug 2024</em></p>
    <ul>
        <li>Gained hands-on experience in Java development and core java concepts during my internship</li>
        <li>Successfully contributed to projects by implementing Java concepts like Collection Framework, Object Oriented Programming and more</li>
        <li>Learned about benefits of learning in public and how to use platforms like Git, GitHub which are version control systems</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Projects Section
st.markdown("---")
st.header("🛠️ My Projects")

# SplitBook Project
st.markdown("""
<div>
    <h4>🔄 <a href="https://github.com/sameermungase/SplitBook" target="_blank">SplitBook - Expense Management System</a></h4>
    <p>SplitBook is a comprehensive expense management system designed to simplify the process of tracking and 
    splitting expenses among multiple users. The application features a user-friendly dashboard for real-time 
    expense monitoring, detailed reporting capabilities for financial insights. Built using Spring Boot, it ensures 
    robust performance and scalability for managing personal and group finances efficiently.</p>
    <p class="tools"><strong>Tools Used:</strong> Spring boot, Java, Hibernate, Maven, MySQL</p>
</div>
""", unsafe_allow_html=True)

# Hotel Management System
st.markdown("""
<div>
    <h4>🏨 <a href="https://github.com/sameermungase/codealpha_tasks.git" target="_blank">Hotel Management System</a></h4>
    <p>Implemented a hotel management system using the java frameworks and core java concepts in which added 
    important features like check room availability, make reservations, payment processing, etc. Gained hands-on 
    experience in real-time data handling and applied core programming concepts effectively.</p>
    <p class="tools"><strong>Tools Used:</strong> Core Java, Object Oriented Programming, Collection Framework, MySQL</p>
</div>
""", unsafe_allow_html=True)

# FileGuard Project
st.markdown("""
<div>
    <h4>🔒 <a href="https://github.com/sameermungase/FileGuard" target="_blank">FileGuard - File Encryption System</a></h4>
    <p>FileGuard is a Java-based application designed for managing hidden files. It features user registration and login 
    with OTP authentication, and allows users to hide and unhide files securely. The application interacts with a 
    MySQL database to store user and file data, ensuring data integrity and security.</p>
    <p class="tools"><strong>Tools Used:</strong> Java, JavaFX, MySQL, Maven, SMTP API</p>
</div>
""", unsafe_allow_html=True)

# Electronics Projects Section
st.subheader("⚡ Electronics Projects")
electronics_projects = [
    "Home Appliances Automation",
    "Trinetra - Visual Aid Device",
    "Smart Blind Stick"
]
for project in electronics_projects:
    st.markdown(f"- {project}")

# College Section
st.markdown("---")
st.header("🎓 My College")
st.image("imagee/geca.jpeg", use_container_width=True)

# Education Section
st.markdown("---")
st.header("📚 Education")

# B.Tech
st.markdown("""
<div class="education-item">
    <h4>Bachelor of Technology</h4>
    <p><em>Electronics and Telecommunication Engineering (2021-2025)</em></p>
    <p>Government College Of Engineering Aurangabad, Chhatrapati Sambhajinagar</p>
    <p class="percentage">Percentage: 77.23%</p>
</div>
""", unsafe_allow_html=True)

# HSC
st.markdown("""
<div class="education-item">
    <h4>Higher Secondary Certification (HSC)</h4>
    <p><em>2020-2021</em></p>
    <p>Sanjivani Junior College, Kopargon</p>
    <p class="percentage">Percentage: 87.00%</p>
</div>
""", unsafe_allow_html=True)

# SSC
st.markdown("""
<div class="education-item">
    <h4>Secondary School Certification (SSC)</h4>
    <p><em>2018-2019</em></p>
    <p>Janata Vidyalaya Yeola</p>
    <p class="percentage">Percentage: 92.80%</p>
</div>
""", unsafe_allow_html=True)

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
    st.markdown("📧 sbmungase2003@gmail.com")

st.header("Contact Me")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send Message")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey;'>© 2024 Sameer Mungase. All rights reserved.</p>", 
    unsafe_allow_html=True
)

st.markdown("---")
st.header("📅 Timeline")
st.markdown("""
<style>
.timeline-item {
    padding: 15px;
    margin: 10px 0;
    border-left: 2px solid #ff4b4b;
    position: relative;
}
.timeline-item::before {
    content: '';
    position: absolute;
    left: -8px;
    top: 20px;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #ff4b4b;
}
.timeline-item h4 {
    color: #ff4b4b;
    margin: 0;
}
.timeline-item p {
    margin: 5px 0;
    color: #2c3e50;
}
</style>
<div class="timeline">
    <div class="timeline-item">
        <h4>2025</h4>
        <p>Tech Mahindra Internship</p>
        <p>Completing B.Tech in Electronics and Telecommunication</p>
    </div>
    <div class="timeline-item">
        <h4>2024</h4>
        <p>CodeAlpha Internship</p>
    </div>
    <div class="timeline-item">
        <h4>2021</h4>
        <p>Started B.Tech at Government College of Engineering, Aurangabad</p>
        <p>Completed HSC with 87.00%</p>
    </div>
    <div class="timeline-item">
        <h4>2019</h4>
        <p>Completed SSC with 92.80% from Janata Vidyalaya Yeola</p>
    </div>
</div>
""", unsafe_allow_html=True)
