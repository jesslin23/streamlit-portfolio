import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Jesslin Persis Portfolio",
    page_icon="💜",
    layout="wide"
)

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body {
    height:100%;
}

html, body, [class*="css"]{
font-family:'Poppins',sans-serif;
}

header{visibility:hidden;}
footer{visibility:hidden;}

.stApp{
min-height:100vh;
background:linear-gradient(135deg,#1a0026,#32004d,#4b0082);
color:white;
}

.block-container{
padding-top:1rem;
padding-bottom:2rem;
}

/* page animation */

.page{
animation:slideFade 0.6s ease;
}

@keyframes slideFade{
from{
opacity:0;
transform:translateY(30px);
}
to{
opacity:1;
transform:translateY(0);
}
}

/* hero section */

.hero{
background-image:url("bg2.jpg");
background-size:cover;
background-position:center;
min-height:70vh;
display:flex;
align-items:center;
justify-content:center;
border-radius:20px;
padding:20px;
}

.hero-box{
background:rgba(0,0,0,0.55);
backdrop-filter:blur(10px);
padding:60px;
border-radius:20px;
text-align:center;
max-width:750px;
width:100%;
}

/* project cards */

.project-card{
background:rgba(255,255,255,0.08);
padding:25px;
border-radius:15px;
text-align:center;
height:100%;
}

.project-icon{
font-size:60px;
color:#c084fc;
margin-bottom:15px;
}

/* footer */

.footer{
position:fixed;
bottom:0;
left:0;
width:100%;
background:#12001f;
text-align:center;
padding:10px;
}

.footer img{
width:28px;
margin:8px;
transition:0.3s;
}

.footer img:hover{
transform:scale(1.2);
}

/* MOBILE RESPONSIVE */

@media (max-width:768px){

.hero-box{
padding:30px;
}

.hero-box h1{
font-size:28px;
}

.hero-box p{
font-size:14px;
}

.project-card{
margin-bottom:20px;
}

.block-container{
padding-left:1rem;
padding-right:1rem;
}

}

</style>
""", unsafe_allow_html=True)

# NAVBAR + RESUME BUTTON

nav1, nav2 = st.columns([6,1])

with nav1:
    page = st.radio(
    "",
    ["Home","About","Skills","Projects","Contact"],
    horizontal=True,
    label_visibility="collapsed"
    )

with nav2:
    with open("resume.pdf","rb") as file:
        st.download_button(
            "Download Resume",
            file,
            "Jesslin_Persis_Resume.pdf"
        )

# HOME PAGE

if page == "Home":

    st.markdown('<div class="page">', unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <div class="hero-box">
            <h1 style="font-size:40px;">Jesslin Persis M</h1>
            <h5 style="color:#d8b4ff;">Computer Science Engineering Student</h5>
            <p style="font-size:16px;">
            Passionate and goal-driven Computer Science Engineering student with a strong
            foundation in <b>Python</b>, <b>Java</b>, and <b>MySQL</b>. Skilled in problem solving
            and developing efficient applications with a strong understanding of
            <b>Object Oriented Programming</b>. Seeking an entry level Software Developer role
            to apply technical expertise and contribute to impactful real-world solutions.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ABOUT PAGE

elif page == "About":

    st.markdown('<div class="page">', unsafe_allow_html=True)

    col1,col2 = st.columns([2,1])

    with col1:

        st.header("About Me")

        st.write("""
I am a **passionate Computer Science Engineering student** with strong interest in
software development and problem solving.

My strongest technical skills include **Python and MySQL**, and I have built
multiple projects using **Python and its libraries such as Tkinter and Streamlit**
to develop interactive applications.

I also have knowledge of **Java (basics), HTML and CSS**, which helps me understand
both programming logic and basic web development.

Through my projects, I have focused on writing **clean code, developing efficient
applications, and applying Object Oriented Programming principles**.

I am currently seeking an **entry level Software Developer role** where I can apply
my technical knowledge, continue learning new technologies, and contribute to
building impactful real-world solutions.
""")

    with col2:
        st.image("profile.jpg", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# SKILLS

elif page == "Skills":

    st.markdown('<div class="page">', unsafe_allow_html=True)

    st.header("Technical Skills")

    col1,col2 = st.columns(2)

    with col1:
        st.write("Python")
        st.progress(0.95)

        st.write("Java (Basics)")
        st.progress(0.60)

        st.write("HTML")
        st.progress(0.75)

    with col2:
        st.write("MySQL")
        st.progress(0.90)

        st.write("Tkinter")
        st.progress(0.85)

        st.write("Streamlit")
        st.progress(0.85)

        st.write("CSS")
        st.progress(0.70)

    skills = pd.DataFrame({
        "Skill":["Python","MySQL","Tkinter","Streamlit","HTML","CSS","Java"],
        "Level":[95,90,85,85,75,70,60]
    })

    st.bar_chart(skills,x="Skill",y="Level")

    st.markdown('</div>', unsafe_allow_html=True)

# PROJECTS

elif page == "Projects":

    st.markdown('<div class="page">', unsafe_allow_html=True)

    st.header("Projects")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="project-card">
        <div class="project-icon">
        <i class="fa-solid fa-list-check"></i>
        </div>
        <h3>Task Manager Application</h3>
        <p>A task management application built using Python and Tkinter.</p>
        <a href="https://github.com/jesslin23/todo-app" target="_blank">
        <button style="padding:8px 16px;border-radius:8px;background:#0e1117;color:white;border:none;">Link</button>
        </a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card">
        <div class="project-icon">
        <i class="fa-solid fa-music"></i>
        </div>
        <h3>SonicSync Website</h3>
        <p>A Music instrument website built using Html, Css, JavaScript</p>
        <a href="https://jesslin23.github.io/instrument_shop/" target="_blank">
        <button style="padding:8px 16px;border-radius:8px;background:#0e1117;color:white;border:none;">Link</button>
        </a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="project-card">
        <div class="project-icon">
        <i class="fa-solid fa-user"></i>
        </div>
        <h3>Streamlit Portfolio</h3>
        <p>A personal portfolio website built using Python and Streamlit.</p>
        <a href="https://github.com/jesslin23" target="_blank">
        <button style="padding:8px 16px;border-radius:8px;background:#0e1117;color:white;border:none;">Link</button>
        </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# CONTACT

elif page == "Contact":

    st.markdown('<div class="page">', unsafe_allow_html=True)

    st.header("Contact Me")

    with st.form("contact_form"):

        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")

        submit = st.form_submit_button("Send Message")

        if submit:
            st.success("Message sent successfully!")

    st.markdown('</div>', unsafe_allow_html=True)

# FOOTER

st.markdown("""
<div class="footer">

<a href="mailto:jesslinpersis@gmail.com">
<img src="https://cdn-icons-png.flaticon.com/512/732/732200.png">
</a>

<a href="https://github.com/jesslin23">
<img src="https://cdn-icons-png.flaticon.com/512/733/733553.png">
</a>

<a href="https://www.linkedin.com/in/jesslin-persis-m-a37020259/">
<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
</a>

<p style="font-size:13px;">© 2026 Jesslin Persis</p>

</div>
""", unsafe_allow_html=True)