import streamlit as st
import google.generativeai as genai

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
        /* All your CSS styles here */
        </style>
    """, unsafe_allow_html=True)

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
    st.header("🚀 Skills & Technologies")
    
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

# Experience Section
def experience_section():
    st.markdown("---")
    st.header("💼 Experience")
    
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
    # Projects implementation
    pass

def education_section():
    # Education implementation
    pass

def timeline_section():
    # Timeline implementation
    pass

def contact_section():
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

if __name__ == "__main__":
    main()
