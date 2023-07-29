import streamlit as st

hide_st_style = """
<style>
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

footer:after {
   content:'©Etha Earth'; 
   visibility: visible;
   display: block;
   position: relative;
   #background-color: red;
   padding: 5px;
   top: 2px;
   text-align: center;
}

.stApp {
    background-image: url("https://github.com/mahendrasalunkhe/plant/blob/main/pallet-green-grass.jpg?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ");
    background-size: cover;
}
</style>
"""

st.set_page_config(
    page_title="Etha Earth",
    page_icon="https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/etha-earth-logo.png?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "Pallet grass or gardan!"
    }
)
st.markdown(hide_st_style, unsafe_allow_html=True)

head_col1, head_col2, head_margin = st.columns((0.3, 0.7, 5))

head_col1.image("https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/etha-earth-logo.png?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ")
new_title = '<p style="font-family:sans-serif; color:darkgreen; font-size: 36px;"><b>Etha Earth</b></p>'
head_col2.markdown(new_title, unsafe_allow_html=True)

