import streamlit as st

hide_st_style = """
<style>
header {visibility: visible;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

footer:after {
   content:'© Wind World (India) Limited, Developed by SCADA'; 
   visibility: visible;
   display: block;
   position: relative;
   #background-color: red;
   padding: 5px;
   top: 2px;
   text-align: center;
}
.css-uc1cuc{
  height: 0rem;
}

.css-18e3th9 {
    padding: 1rem
}

.stApp {
    background-image: url("https://img.wallpapersafari.com/desktop/1600/900/82/66/paOWM4.jpg");
    background-size: cover;
}
</style>
"""

#st.set_page_config(page_title="Plant", layout="wide", page_icon=":shark:", initial_sidebar_state="collapsed")
import streamlit as st

st.set_page_config(
    page_title="Vertical Plant",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# vertical plant creator!"
    }
)
st.markdown(hide_st_style, unsafe_allow_html=True)

head_col1, head_col2, head_margin = st.columns((1, 1, 4))
head_col1.image(r"https://github.com/mahendrasalunkhe/plant/blob/main/logo.jpg")
new_title = '<p style="font-family:sans-serif; color:darkgreen; font-size: 36px;"><b> Vertical Earth</b></p>'
head_col2.markdown(new_title, unsafe_allow_html=True)

