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

# Single consolidated CSS block
st.markdown("""
    <style>
    /* Base styles */
    .main {
        padding: 2rem;
    }

    /* Text gradients */
    .gradient-text {
        background: linear-gradient(45deg, #FF5C58, #FF9F59);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }

    /* Override Streamlit's default headers */
    .css-10trblm, .css-1q8dd3e, h1, h2, h3, h4 {
        background: linear-gradient(45deg, #FF5C58, #FF9F59) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 700 !important;
    }

    /* Cards base style */
    .card-base {
        background: linear-gradient(145deg, #fff5f5, #ffe5e5);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        border-left: 4px solid #FF5C58;
        box-shadow: 0 4px 15px rgba(255, 92, 88, 0.1);
        transition: all 0.3s ease;
    }
    .card-base:hover {
        transform: translateX(10px);
        box-shadow: 0 6px 20px rgba(255, 92, 88, 0.2);
        background: linear-gradient(145deg, #ffe5e5, #ffd5d5);
    }

    /* Extend card styles */
    .skills-card, .project-card, .experience-item, .education-item {
        composes: card-base;
    }

    /* Card content */
    .card-base h4 {
        color: #FF5C58;
        margin-bottom: 15px;
    }
    .card-base p, .card-base li {
        color: #2C3E50;
    }

    /* Download button */
    .download-button {
        background: linear-gradient(45deg, #FF5C58, #FF9F59);
        color: white;
        padding: 15px 30px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 25px;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 92, 88, 0.2);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .download-button:hover {
        background: linear-gradient(45deg, #FF9F59, #FF5C58);
        box-shadow: 0 6px 20px rgba(255, 92, 88, 0.3);
        transform: translateY(-3px);
    }

    /* Social links */
    .social-link {
        background: linear-gradient(45deg, #FF5C58, #FF9F59);
        padding: 10px 20px;
        border-radius: 25px;
        color: white !important;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .social-link:hover {
        background: linear-gradient(45deg, #FF9F59, #FF5C58);
        transform: translateY(-3px);
    }

    /* Responsive design */
    @media (max-width: 768px) {
        .card-base {
            margin: 10px 0;
            padding: 15px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Add this enhanced CSS at the beginning after your existing CSS
st.markdown("""
    <style>
    /* Modern Card Design */
    .modern-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .modern-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    /* Project Cards */
    .project-card {
        background: linear-gradient(145deg,rgb(218, 85, 85), #f5f5f5);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        border-left: 4px solid #7F00FF;
        transition: all 0.3s ease;
    }
    .project-card:hover {
        transform: translateX(10px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .project-card h4 {
        color: #7F00FF;
        font-size: 1.3rem;
        margin-bottom: 15px;
    }

    /* Experience Cards */
    .experience-item {
        background: #ffffff;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        border-left: 4px solid #FF6B6B;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .experience-item:hover {
        transform: translateX(10px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    }
    .experience-item h4 {
        color: #FF6B6B;
        margin-bottom: 10px;
        font-size: 1.2rem;
    }
    .experience-item p {
        color: #2C3E50;
        margin: 8px 0;
    }
    .experience-item em {
        color: #666;
        font-style: italic;
    }
    .experience-item ul {
        color: #2C3E50;
        margin-top: 10px;
        padding-left: 20px;
    }
    .experience-item li {
        margin: 8px 0;
        line-height: 1.5;
    }

    /* Timeline Enhancement */
    .timeline-item {
        background: linear-gradient(145deg, #ffffff, #f8f9fa);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        border-left: 4px solid #7F00FF;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .timeline-item::before {
        background: linear-gradient(45deg, #7F00FF, #ff4b4b);
        box-shadow: 0 0 10px rgba(127,0,255,0.5);
    }

    /* Education Cards */
    .education-item {
        background: linear-gradient(145deg, #ffffff, #f8f9fa);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        border-left: 4px solid #7F00FF;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .education-item:hover {
        transform: translateX(10px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    }

    /* Contact Form Styling */
    .stTextInput > div > div {
        border-radius: 10px !important;
    }
    .stTextArea > div > div {
        border-radius: 10px !important;
    }
    .stButton > button {
        background: linear-gradient(45deg, #7F00FF, #ff4b4b) !important;
        color: white !important;
        border: none !important;
        padding: 15px 30px !important;
        border-radius: 25px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2) !important;
    }

    /* Section Headers */
    h1, h2, h3, h4 {
        background: linear-gradient(45deg, #7F00FF, #ff4b4b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold !important;
    }

    /* Skills Section */
    .skills-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .skills-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    }

    /* Electronics List */
    .electronics-list {
        color: #2C3E50;
        margin: 10px 0;
        padding-left: 20px;
    }
    .electronics-list li {
        margin: 8px 0;
        line-height: 1.5;
        font-size: 1rem;
        color: #2C3E50;
    }
    </style>
""", unsafe_allow_html=True)

# Add this CSS for modern gradient headings
st.markdown("""
    <style>
    /* Modern Gradient Headings */
    .header-main, .skills-header, .experience-header, .projects-header, 
    .college-header, .timeline-header, .education-header, .contact-header {
        background: linear-gradient(45deg, #FF5C58, #FF9F59);  /* Coral to Orange gradient */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }

    /* Update h1-h4 general styling to match */
    h1, h2, h3, h4 {
        background: linear-gradient(45deg, #FF5C58, #FF9F59);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

# Add to your CSS
st.markdown("""
    <style>
    .electronics-list {
        color: #2C3E50;
        margin: 10px 0;
        padding-left: 20px;
    }
    .electronics-list li {
        margin: 8px 0;
        line-height: 1.5;
        font-size: 1rem;
        color: #2C3E50;
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
    st.markdown('<h1 class="name-title">I\'m Sameer Mungase</h1>', unsafe_allow_html=True)
    st.markdown("""
        🎓 Electronics & Telecommunication Engineering Student  
        💻 Passionate about Programming & Development   
        🌟 Always eager to learn and grow
    """)
    
    # Updated Download Resume Button with icon
    st.markdown("""
        <a href="https://drive.google.com/file/d/1VlQ1vKi-lcwDacUhYAxJKOaz_fPPWPLI/view?usp=drive_link" 
           class="download-button" 
           target="_blank">
           <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
               <path d="M8 2a5.53 5.53 0 0 0-3.594 1.342c-.766.66-1.321 1.52-1.464 2.383C1.266 6.095 0 7.555 0 9.318 0 11.366 1.708 13 3.781 13h8.906C14.502 13 16 11.57 16 9.773c0-1.636-1.242-2.969-2.834-3.194C12.923 3.999 10.69 2 8 2zm2.354 6.854-2 2a.5.5 0 0 1-.708 0l-2-2a.5.5 0 1 1 .708-.708L7.5 9.293V5.5a.5.5 0 0 1 1 0v3.793l1.146-1.147a.5.5 0 0 1 .708.708z"/>
           </svg>
           Download Resume
        </a>
    """, unsafe_allow_html=True)

with header_col2:
    st.image("imagee/sam.jpg", width=250)

# AI Chatbot Section
st.markdown("---")
st.markdown('<h2 class="chat-header">💬 Let\'s Chat!</h2>', unsafe_allow_html=True)
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
st.markdown('<h2 class="skills-header">🚀 Skills & Technologies</h2>', unsafe_allow_html=True)

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    st.markdown("""
    <div class="skills-card">
        <h4>💻 Programming Languages</h4>
        <ul>
            <li>Java</li>
            <li>SQL</li>
            <li>JavaScript (Basic)</li>
            <li>HTML/CSS</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tech_col2:
    st.markdown("""
    <div class="skills-card">
        <h4>🛠️ Tools & Technologies</h4>
        <ul>
            <li>Linux</li>
            <li>Git & GitHub</li>
            <li>AWS</li>
            <li>JetBrains IntelliJ IDEA</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tech_col3:
    st.markdown("""
    <div class="skills-card">
        <h4>🎯 Hobbies</h4>
        <ul>
            <li>Mobile Photography</li>
            <li>Reading</li>
            <li>Listening to Music</li>
            <li>Learning New Skills</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Projects Section
st.markdown("---")
st.markdown('<h2 class="projects-header">🛠️ My Projects</h2>', unsafe_allow_html=True)

# SplitBook Project
st.markdown("""
<div class="project-card">
    <h4>🔄 SplitBook - Expense Management System</h4>
    <p>SplitBook is a comprehensive expense management system designed to simplify the process of tracking and 
    splitting expenses among multiple users. The application features a user-friendly dashboard for real-time 
    expense monitoring, detailed reporting capabilities for financial insights. Built using Spring Boot, it ensures 
    robust performance and scalability for managing personal and group finances efficiently.</p>
    <p class="tools"><strong>Tools Used:</strong> Spring boot, Java, Hibernate, Maven, MySQL</p>
</div>
""", unsafe_allow_html=True)

# Hotel Management System
st.markdown("""
<div class="project-card">
    <h4>🏨 Hotel Management System</h4>
    <p>Implemented a hotel management system using the java frameworks and core java concepts in which added 
    important features like check room availability, make reservations, payment processing, etc. Gained hands-on 
    experience in real-time data handling and applied core programming concepts effectively.</p>
    <p class="tools"><strong>Tools Used:</strong> Core Java, Object Oriented Programming, Collection Framework, MySQL</p>
</div>
""", unsafe_allow_html=True)

# FileGuard Project
st.markdown("""
<div class="project-card">
    <h4>🔒 FileGuard - File Encryption System</h4>
    <p>FileGuard is a Java-based application designed for managing hidden files. It features user registration and login 
    with OTP authentication, and allows users to hide and unhide files securely. The application interacts with a 
    MySQL database to store user and file data, ensuring data integrity and security.</p>
    <p class="tools"><strong>Tools Used:</strong> Java, JavaFX, MySQL, Maven, SMTP API</p>
</div>
""", unsafe_allow_html=True)

# Electronics Projects Section
st.markdown('<h3 class="subsection-header">⚡ Electronics Projects</h3>', unsafe_allow_html=True)
st.markdown("""
<div class="project-card">
    <h4>Electronics Hardware Projects</h4>
    <ul class="electronics-list">
        <li>Home Appliances Automation</li>
        <li>Trinetra - Visual Aid Device</li>
        <li>Smart Blind Stick</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Experience Section
st.markdown("---")
st.markdown('<h2 class="experience-header">💼 Experience</h2>', unsafe_allow_html=True)

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

# College Section
st.markdown("---")
st.markdown('<h2 class="college-header">🎓 My College</h2>', unsafe_allow_html=True)
st.image("imagee/geca.jpeg", use_container_width=True)

# Timeline Section
st.markdown("---")
st.markdown('<h2 class="timeline-header">📅 Timeline</h2>', unsafe_allow_html=True)
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

# Education Section
st.markdown("---")
st.markdown('<h2 class="education-header">📚 Education</h2>', unsafe_allow_html=True)

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
st.markdown('<h2 class="contact-header">📫 Get in Touch</h2>', unsafe_allow_html=True)
contact_col1, contact_col2, contact_col3 = st.columns(3)

with contact_col1:
    st.markdown("#### Social Links")
    st.markdown("""
    <div class="social-links">
        <a href="https://linkedin.com/in/sameer-mungase-b341b6286/" class="social-link">LinkedIn</a>
        <a href="https://github.com/sameermungase" class="social-link">GitHub</a>
        <a href="https://instagram.com/sameer_mungase" class="social-link">Instagram</a>
    </div>
    """, unsafe_allow_html=True)
    
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
