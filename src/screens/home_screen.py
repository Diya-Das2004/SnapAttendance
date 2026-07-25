import streamlit as st

from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_base_home_bg,style_base_dashboard
from src.components.footer import footer_home
def home_screen():
    header_home()

    style_base_layout()
    style_base_home_bg()
    style_base_dashboard()
    col1,col2= st.columns(2,gap="large")

    with col1:
        st.header("I am Teacher")
        if st.button('Teacher Portal ↗'):
            st.session_state['login_type']= 'teacher'
            st.rerun()
    with col2:
        st.header("I am Student")
        # st.image("")
        if st.button('Student Portal ↗'):
            st.session_state['login_type']= 'student'
            st.rerun()
    footer_home()
