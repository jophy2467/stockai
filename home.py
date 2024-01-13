import numpy as np
import os
import sys
import pandas as pd
import plotly.figure_factory as ff
import streamlit as st
DIR = os.getcwd()
sys.path.insert(0, DIR)
#from streamlit_style import apply_style

# App title and header
st.set_page_config(page_title="Jophy Lin", page_icon=None, layout="wide", initial_sidebar_state="collapsed")

# Rest of your code...
#apply_style()
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-right: 3rem;
            padding-left: 3rem;
            background-color: #FFB6C1; /* Baby Pink */
            color: #FFFFFF; /* White */
        }
        .tabs.tabItem {
            color: #FF69B4 !important; /* Hot Pink */
            background-color: transparent; /* Add this line if you want to ensure the background is transparent when not active */
        }
        .tabs.tabItem.active {
            color: #FFB6C1 !important; /* Baby Pink */
            background-color: red !important; /* Red background color for active tab */
        }
        .big-font {
            font-size: 60px !important;
            margin-bottom: -2rem !important;
        }
        .small-font {
            font-size: 30px !important;
        }
    </style>
""", unsafe_allow_html=True)

   


######################################## tabs ########################################
listTabs =["About Me", "Projects I've Worked On", "Achievements and Awards", "Extracirricular Activities", "School Activities"]

whitespace = 3
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Courgette&display=swap');
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-right: 3rem;
            padding-left: 3rem;
            color: #FFFFFF; /* White */
            font-family: 'Courgette', cursive;
        }
        .big-font {
            font-size:70px !important;
            font-family: 'Courgette', cursive;
            margin-bottom: -2rem !important; 
        }
    </style>

    <div class="big-font">Hi, I'm Jophy!</div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Courgette&display=swap');
        .block-container {
            padding-right: 3rem;
            padding-left: 3rem;
            color: #FFFFFF; /* White */
            font-family: 'Courgette', cursive;
        }
        .small-font{
            font-size: 30px !important;
            font-family: 'Courgette';
        }
    </style>
    <div class="small-font">Welcome to my website</div>
""", unsafe_allow_html=True)

## Fills and centers each tab label with em-spaces
tabs = st.tabs([s.center(whitespace,"\u2001") for s in listTabs])

with tabs[0]:
    style = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk&display=swap');
        .block-container {
            padding-right: 3rem;
            padding-left: 3rem;
            color: #FFFFFF; /* White */
            font-family: 'Space Grotesk', sans-serif;
        }

        .title {
            font-family: 'Space Grotesk';
            margin-top: -1.5rem !important;
            font-size: 30px;
            font-weight: bold;
            padding-bottom: 0.5em;
        }
        .subtitle {
            font-family: 'Space Grotesk';
            font-size: 24px;
            font-weight: bold;
            padding-bottom: 0.5em;
            margin-bottom: -0.5em;
        }
        ul {
            font-family: 'Space Grotesk';
            font-size: 20px;
            margin-top: 0.5em;
            margin-bottom: 1em;
        }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <div class="subtitle">Background:</div>
            <ul>
                Hey there! I'm Jophy, a passionate high school student currently navigating the world of science, engineering, and finance. As a student enrolled in the Science and Engineering Magnet Program at Manalapan High School (Class of 2026), I've delved deep into challenging courses, fostering my love for STEM.
            </ul>
            <ul>
                Driven by a keen interest in biomedical engineering and a flair for finance, I strive to merge the best of both worlds. My journey isn't just confined to the classroom; I actively engage in a multitude of activities, from teaching coding at an online computer science academy to contributing my insights at hackathons.
            </ul>
            <ul>
                Beyond academics and STEM, you'll find me exploring the realms of piano and violin performance, where I've achieved notable milestones like the ABRSM Piano and Violin Performance Grade 8. Join me on this journey as I balance the intricacies of science, technology, and my love for the arts!
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <div class="subtitle">Passions and Interests:</div>
            <ul>
                My heart lies in the realms of biomedical engineering and finance. The prospect of applying engineering principles to solve medical challenges fascinates me. Simultaneously, I'm drawn to the intricacies of finance, envisioning a future where I can merge both disciplines for innovative solutions in healthcare.
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <div class="subtitle">Academic Focus:</div>
            <ul>
                Navigating the challenging landscape of the Science and Engineering Magnet Program at Manalapan High School, I've embarked on a journey of intellectual exploration and academic excellence. My commitment to mastering diverse subjects and pushing the boundaries of my understanding has shaped a focused academic trajectory. Here's a snapshot of the courses that have played a pivotal role in shaping my educational experience:
                <li>AP Biology (2022-2023)</li>
                <li>AP Microeconomics (2022-2023)</li>
                <li>Computer Programming and Engineering Design (2022-2023)</li>
                <li>AP Chemistry (2023-present)</li>
                <li>AP Statistics (2023-present)</li>
                <li>AP U.S. Government and Politics (2023-present)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <div class="subtitle">Projects:</div>
            <ul>
                I've undertaken various projects, ranging from utilizing Artificial Intelligence for climate change and sustainability to creating innovative applications. For detailed information, please refer to the "Projects I've Worked On" tab.
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <div class="subtitle">Achievements and Awards:</div>
            <ul>
                My journey has been marked by recognition and I enjoy participating in competitions to broaden my skills and learn. For a comprehensive list, explore the "Achievements and Awards" tab.
            <u1>
        </div>
    """,  unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <div class="subtitle">Extracirricular Activities:</div>
            <ul>
                Engaging in diverse extracurriculars, my activities range from volunteering in non-profits to teaching children to code. A glimpse of my involvement can be found in the "Extracurricular Activities" tab.
            </ul>
        </div>
    """,  unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <div class="subtitle">School Activities:</div>
            <ul>
                Within my school, I'm involved in various activities. Explore the "School Activities" tab for a detailed overview.
            </ul>
        </div>
    """,  unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <div class="subtitle">Future Goals:</div>
            <ul>
                Looking ahead, I aspire to pursue a career in biomedical engineering, combining my passion for technology with a commitment to improving healthcare solutions. Alongside biomedical engineering, I also aim to major in finance, leveraging financial knowledge to contribute to the strategic development of innovative biomedical technologies.
            </ul>
        </div>
    """,  unsafe_allow_html=True)

    st.markdown("""
        <div class="section">
            <div class="subtitle">Contact me:</div>
            <ul>
                Feel free to reach out to me via email at jophy2467@gmail.com. I'm excited to connect and discuss shared interests, collaborations, or any inquiries you may have.
        </div>
    """,  unsafe_allow_html=True)


#################################### college ready ####################################
with tabs[1]:
        st.markdown("##### Projects I've Worked On")
        # Program Overview
        st.markdown("<h2 style='font-size: 36px; margin-bottom: 0;'>AI Education Program for High School Students</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-size: 24px; margin-top: 0;'>Program Overview</h3>", unsafe_allow_html=True)

        st.markdown("""
        Our AI Education Program for High School Students is designed to provide an engaging and challenging curriculum that will introduce students to the exciting world of artificial intelligence. Through a series of hands-on projects and activities, students will learn the fundamentals of AI and machine learning and gain practical experience using cutting-edge technologies.

        Our program is taught by experienced AI professionals who are passionate about sharing their knowledge and expertise with the next generation of innovators. With a focus on real-world applications and problem-solving, students will develop critical thinking skills and gain a competitive edge in college and beyond.

        Here are some key highlights of our program:
        """)

        # Program Details
        st.markdown("<h3 style='font-size: 24px;'>Program Details</h3>", unsafe_allow_html=True)

        # Goal
        st.markdown("<h4 style='font-size: 18px;'>Goal</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Introduce students to the fundamentals of AI and machine learning
        - Develop critical thinking skills and problem-solving abilities
        - Provide practical experience using cutting-edge AI technologies
        """)

        # Who
        st.markdown("<h4 style='font-size: 18px;'>Who</h4>", unsafe_allow_html=True)
        st.markdown("""
        - High school students who are interested in computer science and technology
        - Students who want to gain a competitive edge in college and beyond
        - Students who are passionate about innovation and problem-solving
        """)

        # When we teach
        st.markdown("<h4 style='font-size: 18px;'>When We Teach</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our program is offered on a rolling basis throughout the year
        - Students can enroll at any time and complete the program at their own pace
        - All materials and resources are available online, 24/7
        """)

        # How we teach
        st.markdown("<h4 style='font-size: 18px;'>How We Teach (Project-Driven)</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our program is project-driven, with a focus on real-world applications and problem-solving
        - Students will work on a series of hands-on projects and activities that will help them develop practical skills and gain experience with cutting-edge AI technologies
        - Projects are designed to be challenging and engaging, encouraging students to think creatively and work collaboratively
        """)

        # What will student learn
        st.markdown("<h4 style='font-size: 18px;'>What Will Students Learn</h4>", unsafe_allow_html=True)
        st.markdown("""
        - The fundamentals of AI and machine learning
        - Practical experience using cutting-edge AI technologies
        - Critical thinking and problem-solving skills
        - Collaboration and teamwork
        - Effective communication and presentation skills
        - A competitive edge in college and beyond
        """)

        # College Application
        st.markdown("<h4 style='font-size: 24px;'>College Application</h4>", unsafe_allow_html=True)
        st.markdown("""Our AI education program for high school students provides an excellent opportunity for students to explore AI technologies and their real-world applications.
        By participating in our program, students will develop hands-on experience in developing AI solutions, learn how to think critically about AI's impact on society,
        and prepare themselves for college and future careers in AI and related fields. We invite all high school students who are interested in AI to join our program
        and take the first step towards becoming AI experts.""")

#################################### on-demand ####################################
with tabs[3]:
        st.markdown("##### Extracirricular Activities")
        # Program Overview
        st.markdown("<h2 style='font-size: 36px; margin-bottom: 0;'>On-demand, Per-Request Training and Consulting Program</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-size: 24px; margin-top: 0;'>Program Overview</h3>", unsafe_allow_html=True)

        st.markdown("""
        At our on-demand training program, we understand that everyone's learning needs are unique. That's why we offer a customizable and flexible approach to learning. With our program, you can choose the technology you want to learn and our experts will teach you based on your specific needs.
        """)

        # Program Details
        st.markdown("<h3 style='font-size: 24px;'>How it works:</h3>", unsafe_allow_html=True)

        # Goal
        st.markdown("<h4 style='font-size: 18px;'>Goal</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our on-demand training program is designed to help you stay ahead of the curve in the rapidly-evolving field of technology, and to give you the skills and knowledge you need to succeed in your career.
        - Whether you are looking to advance in your current job or explore new career opportunities, our program can help you achieve your goals.
        - By participating in our program, you will join a community of like-minded learners who are passionate about technology and committed to lifelong learning.
        """)

        # Who
        st.markdown("<h4 style='font-size: 18px;'>Who</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our on-demand training program is designed for individuals who are interested in expanding their knowledge and skills in the field of technology, including AI and other state-of-the-art technologies.
        - Whether you are a student, a working professional, or simply someone who wants to stay ahead of the curve, our program is perfect for anyone who wants to learn and grow in their career.
        - Our program is open to anyone, regardless of their prior experience or education level.
        """)

        # When we teach
        st.markdown("<h4 style='font-size: 18px;'>When We Teach</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our program is offered on a rolling basis throughout the year
        - Students can enroll at any time and complete the program at their own pace
        - All materials and resources are available online, 24/7
        """)

        # what
        st.markdown("<h4 style='font-size: 18px;'>What</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our program offers a wide range of topics to choose from, including AI, automation, main stream technologies, and expert help and consulting.
        - With our program, you can choose which topic you want to learn and bid on the price you are willing to pay. Our experts will then work with you to design a personalized training program that meets your specific needs and goals.
        - You will have access to high-quality learning materials, including videos, tutorials, and hands-on projects, all designed to help you master the topic of your choice.
        """)

        # how
        st.markdown("<h4 style='font-size: 18px;'>How</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our program is entirely on-demand, which means you can learn at your own pace and on your own schedule.
        - You will have access to our team of expert instructors, who will provide personalized guidance and support throughout your learning journey.
        - Our program is designed to be interactive and engaging, with plenty of opportunities for hands-on learning and collaboration with other learners.
        """)

        # on-demand
        st.markdown("<h4 style='font-size: 24px;'>On-demand, per-request or consulting</h4>", unsafe_allow_html=True)
        st.markdown("""At our on-demand training program, we are committed to helping individuals and businesses succeed in the rapidly changing world of technology.
        Whether it's AI, automation, web development, mobile app development, or expert help and consulting, we have the expertise and resources to help our customers achieve their learning goals.""")



#################################### math and programming ####################################
with tabs[2]:
        st.markdown("##### Achievements and Awards")
        # Program Overview
        st.markdown("<h2 style='font-size: 36px; margin-bottom: 0;'>Programming and Math Together for K-12 Students</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-size: 24px; margin-top: 0;'>Program Overview</h3>", unsafe_allow_html=True)

        st.markdown("""
        Our program combines the power of technology, programming, and math to create a unique learning experience for K-12 students. Small class sizes and flexible scheduling ensure that every student gets the attention and support they need to succeed.
        """)

        # Program Details
        st.markdown("<h3 style='font-size: 24px;'>How it works:</h3>", unsafe_allow_html=True)


        # Who
        st.markdown("<h4 style='font-size: 18px;'>Who</h4>", unsafe_allow_html=True)
        st.markdown("""
        - The program is designed for all K-12 students who are interested in developing their programming and math skills.
        - Students with no prior experience in programming or math are welcome to join the program.
        - Our instructors are experienced in teaching students of all ages and skill levels.
        """)

        # What
        st.markdown("<h4 style='font-size: 18px;'>What</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our program combines programming and math to create a unique learning experience that will help students develop problem-solving, critical thinking, and analytical skills.
        - We cover topics such as coding fundamentals, algorithms, data structures, and mathematical concepts such as algebra, geometry, and calculus.
        - Our program uses project-based learning to engage students and help them apply their skills to real-world problems.
        """)

        # How
        st.markdown("<h4 style='font-size: 18px;'>How</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our program is designed to be flexible and adaptable to each student's needs and interests.
        - We offer small class sizes, which allow our instructors to provide personalized attention and support to each student.
        - Our program is offered both online and in-person, with a range of scheduling options to fit any student's schedule.
        """)

        # how
        st.markdown("<h4 style='font-size: 18px;'>Why</h4>", unsafe_allow_html=True)
        st.markdown("""
        - We believe that programming and math are essential skills for the future and can provide students with many opportunities for personal and professional growth.
        - By combining programming and math, we help students develop a unique skill set that will set them apart in a competitive job market.
        - Our program provides a supportive and encouraging learning environment where students can explore their interests and reach their full potential.
        """)

        # on-demand
        st.markdown("<h4 style='font-size: 24px;'>Math Is Programming? or Programming Is Math?</h4>", unsafe_allow_html=True)
        st.markdown("""Our Tech Programming and Math Together program is designed to provide K-12 students with a unique and engaging learning experience. By combining programming and math, we aim to foster critical thinking, problem-solving, and creativity skills in our students. Our small class sizes and flexible schedule allow students to receive personalized attention and learn at their own pace. Our experienced instructors guide students through hands-on projects and real-world applications, giving them the skills and knowledge they need to succeed in a rapidly evolving tech industry.

Whether your child is just starting out in their programming and math journey or looking to take their skills to the next level, our program has something to offer. We believe that by inspiring the next generation of tech innovators, we can help shape a better future for everyone.""")

with tabs[4]:
        st.markdown("##### School Activities")
        # Program Overview
        st.markdown("<h2 style='font-size: 36px; margin-bottom: 0;'>On-demand, Per-Request Training and Consulting Program</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-size: 24px; margin-top: 0;'>Program Overview</h3>", unsafe_allow_html=True)

        st.markdown("""
        At our on-demand training program, we understand that everyone's learning needs are unique. That's why we offer a customizable and flexible approach to learning. With our program, you can choose the technology you want to learn and our experts will teach you based on your specific needs.
        """)

        # Program Details
        st.markdown("<h3 style='font-size: 24px;'>How it works:</h3>", unsafe_allow_html=True)

        # Goal
        st.markdown("<h4 style='font-size: 18px;'>Goal</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our on-demand training program is designed to help you stay ahead of the curve in the rapidly-evolving field of technology, and to give you the skills and knowledge you need to succeed in your career.
        - Whether you are looking to advance in your current job or explore new career opportunities, our program can help you achieve your goals.
        - By participating in our program, you will join a community of like-minded learners who are passionate about technology and committed to lifelong learning.
        """)

        # Who
        st.markdown("<h4 style='font-size: 18px;'>Who</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our on-demand training program is designed for individuals who are interested in expanding their knowledge and skills in the field of technology, including AI and other state-of-the-art technologies.
        - Whether you are a student, a working professional, or simply someone who wants to stay ahead of the curve, our program is perfect for anyone who wants to learn and grow in their career.
        - Our program is open to anyone, regardless of their prior experience or education level.
        """)

        # When we teach
        st.markdown("<h4 style='font-size: 18px;'>When We Teach</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our program is offered on a rolling basis throughout the year
        - Students can enroll at any time and complete the program at their own pace
        - All materials and resources are available online, 24/7
        """)

        # what
        st.markdown("<h4 style='font-size: 18px;'>What</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our program offers a wide range of topics to choose from, including AI, automation, main stream technologies, and expert help and consulting.
        - With our program, you can choose which topic you want to learn and bid on the price you are willing to pay. Our experts will then work with you to design a personalized training program that meets your specific needs and goals.
        - You will have access to high-quality learning materials, including videos, tutorials, and hands-on projects, all designed to help you master the topic of your choice.
        """)

        # how
        st.markdown("<h4 style='font-size: 18px;'>How</h4>", unsafe_allow_html=True)
        st.markdown("""
        - Our program is entirely on-demand, which means you can learn at your own pace and on your own schedule.
        - You will have access to our team of expert instructors, who will provide personalized guidance and support throughout your learning journey.
        - Our program is designed to be interactive and engaging, with plenty of opportunities for hands-on learning and collaboration with other learners.
        """)

        # on-demand
        st.markdown("<h4 style='font-size: 24px;'>On-demand, per-request or consulting</h4>", unsafe_allow_html=True)
        st.markdown("""At our on-demand training program, we are committed to helping individuals and businesses succeed in the rapidly changing world of technology.
        Whether it's AI, automation, web development, mobile app development, or expert help and consulting, we have the expertise and resources to help our customers achieve their learning goals.""")
