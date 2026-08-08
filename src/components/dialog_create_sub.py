import streamlit as st
from src.database.db import create_subject

@st.dialog('Create new subject')
def create_subject_dialog(teacher_id):
    st.write('Enter the details of the subject')
    sub_id= st.text_input('Subject_code',placeholder="CS101")
    sub_name= st.text_input("Subject Name", placeholder="Introduction to Computer Science")
    sub_Section= st.text_input("Section", placeholder="A")

    if st.button("Create subject now", type='primary',width='stretch'):
        if sub_id and sub_name and sub_Section:
            try:
                create_subject(teacher_id,sub_id,sub_name,sub_Section,)
                st.toast('Subject Created Successfully!')
                st.rerun()
            except Exception as e:
                st.error(f"Error:{str(e)}")
        else:
            st.warning('Please fil the fields')
