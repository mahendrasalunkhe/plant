import streamlit as st

st.set_page_config(
    page_title="Etha-earthpallet",
    page_icon="https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/etha-earth-logo.png?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "Earth material Pallets, example grass, wooden, mud, gardan!"
    }
   
)

hide_st_style = """
<style>
header {visibility: hidden;}
MainMenu {visibility: hidden;}
footer {visibility: hidden;}

footer:after {
   content:'©Etha-earthpallet'; 
   visibility: visible;
   display: block;
   position: relative;
   #background-color: red;
   padding: 5px;
   top: 2px;
   text-align: center;
}
    
.stApp {
    background-image: url("https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/pallet-green-grass.jpg?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ");
    background-size: cover;
}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

head_col1, head_col2, head_margin = st.columns((0.3, 2.7, 3), use_container_width=True)
head_col1.image("https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/etha-earth-logo.png?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ")
logo_name = '<p style="font-family:sans-serif; color:Orange; font-size: 36px;"><b>Etha-earthpallet</b></p>'
head_col2.markdown(logo_name, unsafe_allow_html=True, use_container_width=True)

content = 
"""
<p style="font-family:sans-serif; color:darkgreen; font-size: 12px;">Discover a Green Balcony Oasis! Let our premium grass solutions transform your balcony into a lush, low-maintenance space. Embrace nature and create a relaxing outdoor space to unwind.</p>
<p style="font-family:sans-serif; color:tomato; font-size: 12px;">Our dedicated team of experts is passionate about greening urban areas. With their guidance and installation services, turning your balcony into a green paradise is easy.</p>

<p style="font-family:sans-serif; color:darkyellow; font-size: 12px;">Experience the beauty of nature right at your doorstep today!</p>
<p style="font-family:sans-serif; color:red; font-size: 12px;">Mobile: 7208005001</p>
<p style="font-family:sans-serif; color:Orange; font-size: 12px;">Email: mahendra.salunkhe@gmail.com</p>
"""
st.markdown(content, unsafe_allow_html=True)

# st.caption(':tomato[Discover a Green Balcony Oasis! Let our premium grass solutions transform your balcony into a lush, low-maintenance space. Embrace nature and create a relaxing outdoor space to unwind.]') 

# st.caption(':green[Our dedicated team of experts is passionate about greening urban areas. With their guidance and installation services, turning your balcony into a green paradise is easy.]')

# st.caption(':orange[Experience the beauty of nature right at your doorstep today!]')
# st.caption(':Yellow[Mobile: 7208005001]')
# st.caption(':red[Email: mahendra.salunkhe@gmail.com]')

