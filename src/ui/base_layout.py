import streamlit as st


def style_base_home_bg():
    st.markdown("""
        <style>
            .stApp{
                background: #E6E6FA !important;
            }
            .stApp div[data-testid="stColumn"]{
                background-color:#87CEFA !important;
                padding: 2.5rem !important;
                border-radius:5rem !important;
            }
            
        </style>

""",unsafe_allow_html= True)
    
def style_base_dashboard():
    st.markdown("""
        <style>
            .stApp{
                background: #E6E6FA !important;
            }
            
        </style>
""",unsafe_allow_html= True)
    
def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Lilita+One&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&family=Lilita+One&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Google+Sans:ital,opsz,wght@0,17..18,400..700;1,17..18,400..700&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&family=Lilita+One&display=swap');
            #MainMenu, footer, header{
                visibility: hidden;
            }
            .block-container{
                padding-top:1.5rem !important;
            }

            h1{
                font-family:'Archivo Black',sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color: #00008B!important;
                text-align='center'!important;
            }
            h2{
                font-family:'Archivo Black',sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color: #00008B!important;
                text-align='center'!important;
            }
            h3,h4,p{
                font-family:'Libre-Caslon',sans-serif !important;
            }
            button[kind="primary"]{
                background-color: #0000CD !important; 
                border-radius: 1.5rem !important;
                color:white !important;
                padding:10p 20px !important;
                border:none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            button[kind="secondary"]{
                background-color: #EB459E !important; 
                border-radius: 1.5rem !important;
                color:white !important;
                padding:10p 20px !important;
                border:none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            button[kind="tertiary"]{
                background-color: black !important; 
                border-radius: 1.5rem !important;
                color:white !important;
                padding:10p 20px !important;
                border:none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            button:hover{
                transform:scale(1.10)
            }
        </style>
""",unsafe_allow_html= True)
