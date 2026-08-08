import streamlit as st

def header_home():
    # st.header("SNAP CLASS")
    logo_url="https://png.pngtree.com/png-vector/20190324/ourmid/pngtree-vector-male-student-icon-png-image_862310.jpg"
    st.markdown(f"""
        <div style=" display:flex;flex-direction:column; align-items:center: justify-content:center; margin-bottom:30px; margin-top:10px">
            <img src={logo_url} style='height:150px;'  />
            <h1 style= 'text-align:center; color:#05057e'>SNAP CLASS</h1>
        </div>


""",unsafe_allow_html= True)

def header_dashboard():
    # st.header("SNAP CLASS")
    logo_url="https://png.pngtree.com/png-vector/20190324/ourmid/pngtree-vector-male-student-icon-png-image_862310.jpg"
    st.markdown(f"""
        <div style=" display:flex; align-items:center: justify-content:center; gap:10px; margin-top:10px">
            <img src={logo_url} style='height:100px;'  />
            <h2 style= 'text-align:left; color:#87CEFA'>SNAP CLASS</h2>
        </div>
""",unsafe_allow_html= True)
