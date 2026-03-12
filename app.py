import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Jesslin Persis Portfolio",
    page_icon="💜",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body {
    height:100%;
    overflow:hidden;
}

html, body, [class*="css"]{
font-family:'Poppins',sans-serif;
}

header{visibility:hidden;}
footer{visibility:hidden;}

.stApp{
height:100vh;
overflow:hidden;
background:linear-gradient(135deg,#1a0026,#32004d,#4b0082);
color:white;
}

.block-container{
padding-top:1rem;
padding-bottom:0rem;
height:82vh;
overflow:hidden;
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
height:75vh;
display:flex;
align-items:center;
justify-content:center;
border-radius:20px;
}

.hero-box{
background:rgba(0,0,0,0.55);
backdrop-filter:blur(10px);
padding:60px;
border-radius:20px;
text-align:center;
max-width:750px;
}

/* project cards */

.project-card{
background:rgba(255,255,255,0.08);
padding:25px;
border-radius:15px;
text-align:center;
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

    st.markdown("""
    <style>
    .block-container{
        overflow:auto;
    }
    </style>
    """, unsafe_allow_html=True)

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
        st.markdown('<div class="project-card">',unsafe_allow_html=True)
        st.subheader("Task Manager Application")
        st.write("A task management application built using Python and Tkinter.")
        st.link_button("GitHub","https://github.com/jesslin23/todo-app")
        st.markdown('</div>',unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="project-card">',unsafe_allow_html=True)
        st.subheader("SonicSync Website")
        st.write("A Music instrument website built using Html, Css, JavaScript")
        st.link_button("Link","https://jesslin23.github.io/instrument_shop/")
        st.markdown('</div>',unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="project-card">',unsafe_allow_html=True)
        st.subheader("Streamlit Portfolio")
        st.write("A personal portfolio website built using Python and Streamlit.")
        st.link_button("Link","https://github.com/jesslin23")
        st.markdown('</div>',unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# CONTACT

elif page == "Contact":

    st.markdown("""
    <style>
    .block-container{
        overflow:auto;
    }
    </style>
    """, unsafe_allow_html=True)

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