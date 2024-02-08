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

######################################## tabs ########################################
listTabs =["Home", "About Me", "Projects I've Worked On", "Achievements and Awards", "Extracirricular/School Activities"]
whitespace = 0

## Fills and centers each tab label with em-spaces
tabs = st.tabs([s.center(whitespace,"\u2001") for s in listTabs])

#"Home" tab
with tabs[0]:
    style = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk&display=swap');
        [data-testid="stAppViewContainer"] {            
            background: linear-gradient(45deg,#61096B, #840984, #630970, #48085F);
        }
        [data-testid="stHeader"]{   
            background: linear-gradient(45deg, #370849, #2F095A, #16096B);
        }
        [data-testid=stSidebar] {
            background: linear-gradient(#370849, #2F095A, #16096B);
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 0px;
        }
        .stTabs [data-baseweb="tab"] {
            max-width: 100%; /* Adjust this value to your needs */
            height: 50px;
            background: linear-gradient(45deg,#840984, #630970, #48085F);
            border-radius: 4px 4px 0px 0px;
            gap: 0px;
            padding-top: 10px;
            padding-bottom: 10px;
            padding-left: 76px;
            padding-right: 76px;
            margin-bottom: -2px;
            color: #FFFFFF;
            font-size: 24px;
        }
        .stTabs [aria-selected="true"] {
            background-color: linear-gradient(45deg,#2E085F, #14085F, #08145F);
        }
        .block-container {
            color: #290B35; /* White */
            font-family: 'Space Grotesk', sans-serif;
            margin-right: auto; /* Centers the container when its width is less than max-width */
            margin-left: auto;
        }
        .subtitle {
            font-family: 'Space Grotesk';
            font-size: 24px;
            font-weight: bold;
            padding-bottom: 0em;
            margin-bottom: 0em;
        }
        ul {
            font-family: 'Space Grotesk';
            font-size: 23px;
            margin-top: 0.5em;
            margin-bottom: 0em;
        }
    </style>
    """
    
    st.markdown(style, unsafe_allow_html=True)
    # Create two columns. The first column will take up 65% of the screen, and the second column will take up the remaining 35%.
    col1, col2 = st.columns([60,50])

    # Add content to the first column.
    with col1:
        st.markdown("""
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Courgette&display=swap');
                .block-container {
                    margin-top: 1rem;
                    padding-top: 2rem;
                    padding-bottom: 0.5rem;
                    color: #ECBCEC; 
                    font-family: 'Courgette', cursive;
                    text-align: center;
                    height: 10vh;
                }
                .big-font {
                    font-size:100px !important;
                    font-family: 'Courgette', cursive;
                    margin-bottom: -1rem !important;
                    padding-top=-5rem;
                }
                .small-font{
                    font-size: 38px !important;
                    font-family: 'Courgette';
                }
                .new-text{
                    color: #FC3FFC;
                }
                .new-text2{
                    color: #F792F7;
                }
            </style>
            <div class="big-font"><b>Hi, I'm <span class="new-text">Jophy</span></b></div>
            <div class="small-font"><span class="new-text2"><b>Sophomore in Manalapan High School's Science and Engineering Magnet Program </span></b></div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="section">
                <ul>
                    <b>With a natural curiosity and a passion for problem-solving, my interests lie in utilizing biomedical engineering, AI, and finance to create impactful innovations. This website is just the first chapter of my story, with each tab unfolding a different facet. So, feel free to explore and discover the person behind the code and the unwavering drive to innovate. </b>
                </ul>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="section">
                <div class="subtitle"><span class="new-text2"><b>Contact me at: jophy2467@gmail.com </span></b> </div>
        
            </div>
        """,  unsafe_allow_html=True)

    Add an image to the second column.
    with col2:
        st.image('https://assets-global.website-files.com/64a383adeb16ab63d6b7ef95/64a3aa73a25bdfc44785aced_Virus.svg')
        
    # Add a spacer at the end of the content.
    st.markdown("<div style='height:-800px;'></div>", unsafe_allow_html=True)

#"About me" tab
with tabs[1]:
    style = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk&display=swap');
        .block-container {
            color: #290B35; /* White */
            font-family: 'Space Grotesk', sans-serif;
            margin-right: auto; /* Centers the container when its width is less than max-width */
            margin-left: auto;
        }
        .subtitle {
            font-family: 'Space Grotesk';
            font-size: 24px;
            font-weight: bold;
            padding-bottom: 0em;
            margin-bottom: 0em;
        }
        ul {
            font-family: 'Space Grotesk';
            font-size: 23px;
            margin-top: 0.5em;
            margin-bottom: 0em;
        }
    </style>
    """
    st.markdown("""
        <div style="text-align: center;">
            <div class="small-font" style="display: inline-block; border-radius: 20px 20px 20px 20px; color: #F9D9FD; background: rgba(232, 170, 239, 0.3); padding-left: 40px; padding-right: 40px;" >
                <b>About Me</b>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Add a spacer
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div style="background-color: rgba(214, 140, 240, 0.3); padding: 10px; border-radius: 20px;">
                <ul><b>Background</b></ul>
                <ul>Hi, I'm Jophy, a sophomore enrolled in the Science and Engineering Magnet Program at Manalapan High School. I have a passion for exploring the intersections of science, technology, and finance. Since third grade, I've immersed myself in the world of music, playing both the piano and violin. Beyond academics, I enjoy teaching kids to code and contribute my time as a volunteer at my county museum.</ul>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background-color: rgba(197, 140, 240, 0.3); padding: 10px; border-radius: 20px;">
                <ul><b>Classes Taken</b></ul>
                <ul>Enrolled in a rigorous program, I've taken classes such as:</ul>
                <ul>2022-2023: AP Biology, AP Microeconomics, Computer Programming and Engineering Design, Honors Algebra 2</ul>
                <ul>2023-present: AP Statistics, AP Chemistry, AP U.S. Government and Politics, AP Macroecomics, AP Precalculus, AP Chinese Language and Culture</ul>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div style="background-color: rgba(170, 140, 240, 0.3); padding: 10px; border-radius: 20px;">
                <ul><b>Future Goals</b></ul>
                <ul>Looking ahead, my aspirations extend into the realms of biomedical engineering, AI, and finance. My ultimate goal is to pursue it in college, where I hope to weave them together to make a positive impact on the world. Whether through innovative technologies, sustainable finance practices, or ethical AI solutions, I am committed to contributing to positive change and improvement.</ul>
            </div>
        """, unsafe_allow_html=True)


#"Awards" tab
with tabs[3]:
    style = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk&display=swap');
        .block-container {
            color: #290B35; /* White */
            font-family: 'Space Grotesk', sans-serif;
            padding-left: 5em;
            padding-right: -5em;
            height: 100vh;
        }
        .subtitle {
            font-family: 'Space Grotesk';
            font-size: 24px;
        }
        ul {
            font-family: 'Space Grotesk';
            font-size: 23px;
            margin-top:0;
            
        }
    </style>
    """
    st.markdown("""
        <div style="text-align: center;">
            <div class="small-font" style="display: inline-block; border-radius: 20px 20px 20px 20px; color: #F9D9FD; background: rgba(232, 170, 239, 0.3); padding-left: 40px; padding-right: 40px;" >
                <b>Achievements and Awards</b>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Add a spacer
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="display: flex; justify-content: space-between;">
            <div style="background-color: rgba(214, 140, 240, 0.3); padding-left: 15px; padding-right: 15px; padding-top:1px; padding-bottom: 1px; border-radius: 20px; text-align: left; width: 49%;">
                <ul><b>STEM Awards:</b></ul>
                <div style="text-align: left; word-wrap: break-word; max-width: 75%; float: left;">
                    <ul>January 2023: HackFRee Hack of Distinction
                        <li>Participated in school district's annual 24-hour hackathon</li>
                        <li>Project was Nook to Nest, which focused on helping out displaced people in cases of natural disasters</li>
                    </ul>
                </div>
                <div style="text-align: right; direction: rtl; padding-right: 30px; word-wrap: break-word; max-width: 80%; float:right;">
                    <ul>July 2023: Best Research Presentation Third Place
                        <li>Participated in a research academy that accepts around 50 students nationally, held at Princeton University</li>
                        <li>Project was focused on reducing climate change and carbon emissions through using AI algorithms to minimize data storage </li>
                    </ul>
                </div>
                <div style="text-align: left; word-wrap: break-word; max-width: 75%; float: left;">
                    <ul>August 2023: Student Engineering Creativity Convention (SECC) Third Place
                        <li>Worked in a team of 5 to train an autonomous AWS DeepRacer model using reinforcement learning</li>
                        <li>Presented results at the University of Texas at Dallas to a panel of judges</li>
                    </ul>
                </div>
                <div style="text-align: right; direction: rtl; padding-right: 20px; word-wrap: break-word; max-width: 80%; float: right;">
                    <ul>December 2023: World AI Competition for Youth (WAICY) AI Showcase Track Finalist
                        <li>Participated in the world's largest AI competition for youth, with 3200+ participants across 58+ countries and 600+ projects in 2022</li>
                        <li>Project was NutriGuide, which was an application that utilizes a trained YOLO object detection model and OpenAI API to give tailored nutritional insights </li>
                    </ul>
                </div>
                <div style="text-align: left;word-wrap: break-word; max-width: 75%; float: left;">
                    <ul>December 2023: World AI Competition for Youth (WAICY) Generative Art Track Fourth Place
                        <li>Project involved documenting thought process and steps to create AI-generated art based on the theme, "Joys of Family"</li>
                        <li>Special WAICY award cateogry</li>
                    </ul>
                </div> 
                <div style="text-align: right; direction: rtl; padding-right: 20px; word-wrap: break-word; max-width: 80%; float: right;">
                    <ul>December 2023: National STEM Challenge Finalist
                        <li>Participated in the nation's largest STEM challenge, utilized project NutriGuide</li>
                        <li>Prize: 2-months of Codédex Club, and an Invitation to attend an EXPLR’s Private STEM Master Classes Series </li>
                    </ul>
                </div>
                <div style="text-align: left;word-wrap: break-word; max-width: 75%; float: left;">
                    <ul>December 2023: NJ04 Congressional App Challenge Honorable Mention
                        <li>Project was CultureConnect, which utilized various technologes such as NLP to connect users from different regions in the world, enhancing their cultural awareness and language abilities</li>
                        <li>Received signed letter and certificate from congressional representative</li>
                    </ul>
                </div> 
                <div style="clear: both;"></div>    
            </div>
            <div style="background-color: rgba(197, 140, 240, 0.3); padding-left: 15px; padding-right: 15px; padding-top:1px; padding-bottom: 1px; border-radius: 20px; text-align: left; width: 49%;">
                <ul><b>Music and Other Awards:</b></ul>
                <div style="text-align: right; direction: rtl; padding-right: 30px; word-wrap: break-word; max-width: 80%; float:right;">
                    <ul>June 2021: ABRSM Music Theory Grade 5 with Distinction
                        <li>Score: 70/75</li>
                    </ul>
                </div>
                <div style="text-align: left; word-wrap: break-word; max-width: 75%; float: left;">
                    <ul>February 2022: International Music and Arts Society (IMAS) Talented Young Musician Olympia Gold in Violin
                        <li>Invited to perform at Merkin Concert Hall in New York City</li>
                    </ul>
                </div>
                <div style="text-align: right; direction: rtl; padding-right: 30px; word-wrap: break-word; max-width: 80%; float:right;">
                    <ul>March 2022: ABRSM Piano Performance Grade 8 with Distinction
                        <li>Score: 137/150</li>
                    </ul>
                </div>
                <div style="text-align: left; word-wrap: break-word; max-width: 75%; float: left;">
                    <ul>May 2023: Gold Presidential Volunteer Service Award
                        <li>Over 100 hours of volunteer work</li>
                    </ul>
                </div>
                <div style="text-align: right; direction: rtl; padding-right: 30px; word-wrap: break-word; max-width: 80%; float:right;">
                    <ul>September 2023: ABRSM Violin Performance Grade 8 </ul>
                </div>
                <div style="text-align: left; word-wrap: break-word; max-width: 75%; float: left;">
                    <ul>January 2024: Gold Presidential Volunteer Service Award
                        <li>Over 100 hours of volunteer work</li>
                    </ul>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

#"Extracirricular/School Activities" tab
with tabs[4]:
    style = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk&display=swap');
        .block-container {
            color: #290B35; /* White */
            font-family: 'Space Grotesk', sans-serif;
            padding-left: 5em;
            padding-right: -5em;
            height: 100vh;
        }
        .subtitle {
            font-family: 'Space Grotesk';
            font-size: 24px;
        }
        ul {
            font-family: 'Space Grotesk';
            font-size: 23px;
            margin-top:0;
        }
    </style>
    """
    st.markdown("""
        <div style="text-align: center;">
            <div class="small-font" style="display: inline-block; border-radius: 20px 20px 20px 20px; color: #F9D9FD; background: rgba(232, 170, 239, 0.3); padding-left: 40px; padding-right: 40px;" >
                <b>Extracirricular/School Activities</b>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Add a spacer
    st.markdown("<br>", unsafe_allow_html=True)

    # Create two columns
    col1, col2 = st.columns([3,1])

    # First column
    with col1:
        st.markdown("""
            <div style="background-color: rgba(214, 140, 240, 0.3); padding-left: 15px; padding-right: 15px; padding-top:1px; padding-bottom: 1px; border-radius: 20px; text-align: left; width: 100%; display: flex; flex-direction: column;">
                <ul><b>School Activities:</b></ul>
                <ul>In my school community, I've taken part in various activites, such as:
                    <li>First Tech Robotics (FTC) Competition Team Member: Collaborating with a team within the Robotics Club to actively participate in ongoing FTC competitions. Currently serving in the software department, contributing to the development and optimization of code for robotic systems</li>
                    <li>Computer Science Club Co-President: Instruct high school students in coding skills, equipping them for participation and success in coding competitions</li>
                    <li>HackFRee Leadership Team Member and Mentor: Collaborating in the planning and execution of the district's annual hackathon and providing mentorship to young coding enthusiasts</li>
                    <li>Bravecast Anchor: Anchor for the recorded segments of the school's weekly news broadcast</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    Second column
    with col2:
        # List of image URLs or local image paths
        image= "https://www.frhsd.com/cms/lib/NJ01912687/Centricity/Template/GlobalAssets/images///Logos/MAN%20Emboss.png"

        st.image(image, width=320)  # Adjust width as needed

    # Add a spacer
    st.markdown("<br>", unsafe_allow_html=True)

    col3, col4 = st.columns([1,2])
    
        # Second column
    with col3:
        # List of image URLs or local image paths
        images = ["https://us.123rf.com/450wm/grgroup/grgroup1707/grgroup170701171/81583377-blue-shading-silhouette-of-programming-window-with-script-of-code-vector-illustration.jpg?ver=6", 
                "https://media.istockphoto.com/id/1210803911/vector/people-working-together-hackathon-vector-flat-illustration-programmers-work-with-data.jpg?s=612x612&w=0&k=20&c=yoTjL26kAyCebnpuA-DelwoSOf1EBmazkl8HKragWTw=",
                "https://pbs.twimg.com/profile_images/621358312739762176/70SLpg5g_400x400.png",
                "https://media.istockphoto.com/id/1283924155/vector/cartoon-violin-and-bow.jpg?s=612x612&w=0&k=20&c=x9-AZhdk2Ff6f-cgzfrfKCDDtJgwFnq6OxpRNhHaLxs="]

        for i in range(0, len(images), 2):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f'<img src="{images[i]}" style="border-radius: 20px; width: 220px">', unsafe_allow_html=True)
            if i + 1 < len(images):
                with col2:
                    st.markdown(f'<img src="{images[i+1]}" style="border-radius: 20px; width: 220px">', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)  # Add a line break after each pair of images
            
    with col4:
        st.markdown("""
            <div style="background-color: rgba(170, 140, 240, 0.3); padding-left: 15px; padding-right: 15px; padding-top:1px; padding-bottom: 1px; border-radius: 20px; text-align: left; width: 100%; display: flex; flex-direction: column;">
                <ul><b>Extracirricular Activities:</b></ul>
                <ul>Outside of school, I take part in various activities around my community, which include: </li>
                    <li>Computer Science Instructor and Teaching Assistant: Served as a teaching assistant since the age of 13 and conducted Office Hours to help students from diverse coding experiences and backgrounds, ranging from beginners in elementary school to advanced students preparing for the AP Computer Science A exam in May. Started as an instructor at the age of 15, where I teach Computer Science to students in languages such as Java and Python and monitor student progress to report to parents and staff</li>
                    <li>Hackathon Judge and Mentor: Helped organize and judge for the Computer Science Academy's hackathon
                    <li>Docent at the Monmouth Musuem: Tour guide for my county's museum, where I lead tours for visitors and help out with various events</li>
                    <li>Director of Science at the International Youth STEM Society: Help come up with 8 workshop ideas to conduct in my local community each month, advocating for accessibility to STEM</li>
                    <li>Violinist for the New Jersey State Youth Orchestra: Meet up weekly to rehease and perform for the community as a part of the Chamber Ensemble</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
