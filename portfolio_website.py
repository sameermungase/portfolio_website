import google.generativeai as genai
# import os
import streamlit as st
# import plotly.express as px
import pandas as pd

# Page Configuration
def set_page_config():
    st.set_page_config(
        page_title="Sameer Mungase | Portfolio",
        page_icon="👨‍💻",
        layout="wide"
    )

# CSS Styles
def load_css():
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
            color: #7F00FF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: none;
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
            background: linear-gradient(45deg, #7F00FF, #ff4b4b);
            color: white;
            padding: 15px 30px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 25px;
            transition: all 0.3s ease;
            border: none;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            font-size: 16px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .download-button:hover {
            background: linear-gradient(45deg, #ff4b4b, #7F00FF);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
            transform: translateY(-3px);
        }
        .download-button svg {
            margin-right: 8px;
            vertical-align: middle;
        }

        /* Modern Gradient Headings */
        .section-header {
            background: linear-gradient(120deg, #2C3E50, #3498DB);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }

        .subsection-header {
            background: linear-gradient(120deg, #E74C3C, #F39C12);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 600;
        }

        .card-header {
            background: linear-gradient(120deg, #16A085, #27AE60);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 600;
        }

        /* Update specific section headers */
        .skills-header {
            background: linear-gradient(120deg, #8E44AD, #9B59B6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .experience-header {
            background: linear-gradient(120deg, #2980B9, #3498DB);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .projects-header {
            background: linear-gradient(120deg, #C0392B, #E74C3C);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .education-header {
            background: linear-gradient(120deg, #16A085, #1ABC9C);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .timeline-header {
            background: linear-gradient(120deg, #D35400, #E67E22);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .contact-header {
            background: linear-gradient(120deg, #27AE60, #2ECC71);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
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
        background: linear-gradient(145deg, #ffffff, #f5f5f5);
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
        background: linear-gradient(145deg, #ffffff, #f8f9fa);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        border-left: 4px solid #ff4b4b;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .experience-item:hover {
        transform: translateX(10px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
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

    /* Social Links */
    .social-links {
        display: flex;
        gap: 15px;
        margin: 20px 0;
    }
    .social-link {
        background: linear-gradient(45deg, #7F00FF, #ff4b4b);
        padding: 10px 20px;
        border-radius: 25px;
        color: white !important;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .social-link:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
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

    /* Responsive Design */
    @media (max-width: 768px) {
        .modern-card, .project-card, .experience-item, .education-item {
            margin: 10px 0;
            padding: 15px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# API Configuration
api_key = st.secrets["GOOGLE_API_KEY"]
# api_key =""
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

# Header Section
def header_section():
    header_col1, header_col2 = st.columns([2, 1])
    with header_col1:
        st.markdown("### Hello there! 👋")
        st.title("I'm Sameer Mungase")
        st.markdown("""
            🎓 Electronics & Telecommunication Engineering Student  
            💻 Passionate about Programming & Development   
            🌟 Always eager to learn and grow
        """)
        render_resume_button()
    
    with header_col2:
        st.image("imagee/sam.jpg", width=250)

def render_resume_button():
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

# Skills Section
def skills_section():
    st.markdown("---")
    st.markdown('<h2 class="section-header skills-header">🚀 Skills & Technologies</h2>', unsafe_allow_html=True)
    
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    skills_data = {
        "Programming Languages": {
            "icon": "💻",
            "items": ["Java", "SQL", "JavaScript (Basic)", "HTML/CSS"]
        },
        "Tools & Technologies": {
            "icon": "🛠️",
            "items": ["Linux", "Git & GitHub", "AWS", "JetBrains IntelliJ IDEA"]
        },
        "Hobbies": {
            "icon": "🎯",
            "items": ["Mobile Photography", "Reading", "Listening to Music", "Learning New Skills"]
        }
    }
    
    columns = [tech_col1, tech_col2, tech_col3]
    for (title, data), col in zip(skills_data.items(), columns):
        with col:
            render_skills_card(title, data["icon"], data["items"])

def render_skills_card(title, icon, items):
    items_html = "\n".join([f"<li>{item}</li>" for item in items])
    st.markdown(f"""
    <div class="skills-card">
        <h4>{icon} {title}</h4>
        <ul>{items_html}</ul>
    </div>
    """, unsafe_allow_html=True)

# Experience Section
def experience_section():
    st.markdown("---")
    st.markdown('<h2 class="section-header experience-header">💼 Experience</h2>', unsafe_allow_html=True)
    
    experiences = [
        {
            "title": "Software Development and AIML Intern",
            "company": "Makers Lab, Tech Mahindra - Pune",
            "period": "Jan 2025 - Present",
            "responsibilities": [
                "Currently working as a development trainee with a focus on Java programming and basic development tasks",
                "Acquired hands-on experience in Java programming, debugging, and understanding core development workflows",
                "Developing expertise in software lifecycle management, professional coding practices, and JavaScript development"
            ]
        },
        {
            "title": "Java Programming Intern",
            "company": "Codealpha - Virtual",
            "period": "June 2024 - Aug 2024",
            "responsibilities": [
                "Gained hands-on experience in Java development and core java concepts during my internship",
                "Successfully contributed to projects by implementing Java concepts like Collection Framework, Object Oriented Programming and more",
                "Learned about benefits of learning in public and how to use platforms like Git, GitHub which are version control systems"
            ]
        }
    ]
    
    for exp in experiences:
        render_experience_card(exp)

def render_experience_card(experience):
    responsibilities_html = "\n".join([f"<li>{resp}</li>" for resp in experience["responsibilities"]])
    st.markdown(f"""
    <div class="experience-item">
        <h4>{experience["title"]} | {experience["company"]}</h4>
        <p><em>{experience["period"]}</em></p>
        <ul>{responsibilities_html}</ul>
    </div>
    """, unsafe_allow_html=True)

# Similar functions for other sections...
def projects_section():
    st.markdown("---")
    st.markdown('<h2 class="section-header projects-header">🛠️ My Projects</h2>', unsafe_allow_html=True)
    # Projects implementation
    pass

def education_section():
    st.markdown("---")
    st.markdown('<h2 class="section-header education-header">📚 Education</h2>', unsafe_allow_html=True)
    # Education implementation
    pass

def timeline_section():
    st.markdown("---")
    st.markdown('<h2 class="section-header timeline-header">📅 Timeline</h2>', unsafe_allow_html=True)
    # Timeline implementation
    pass

def contact_section():
    st.markdown("---")
    st.markdown('<h2 class="section-header contact-header">📫 Get in Touch</h2>', unsafe_allow_html=True)
    # Contact implementation
    pass

# Main App
def main():
    set_page_config()
    load_css()
    
    header_section()
    skills_section()
    experience_section()
    projects_section()
    education_section()
    timeline_section()
    contact_section()

# if __name__ == "__main__":
#     main()
