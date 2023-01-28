import streamlit as st

hide_st_style = """
<style>
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

footer:after {
   content:'©Vertical Plant'; 
   visibility: visible;
   display: block;
   position: relative;
   #background-color: red;
   padding: 5px;
   top: 2px;
   text-align: center;
}


.stApp {
    background-image: url("https://img.wallpapersafari.com/desktop/1600/900/82/66/paOWM4.jpg");
    background-size: cover;
}
</style>
"""

st.set_page_config(
    page_title="Vertical Plant",
    page_icon="https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/71020327.png?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "# Vertical plant creator!"
    }
)
st.markdown(hide_st_style, unsafe_allow_html=True)

head_col1, head_col2, head_margin = st.columns((1, 1, 4))

head_col1.image("https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/71020327.png?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ")
new_title = '<p style="font-family:sans-serif; color:darkgreen; font-size: 36px;"><b>Etha Vertical Earth</b></p>'
head_col2.markdown(new_title, unsafe_allow_html=True)

