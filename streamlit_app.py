import streamlit as st

st.set_page_config(
    page_title="Etha-Glasswindoe",
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

.css-z5fcl4 {
    padding:3rem
}
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

head_col1, head_col2, head_col3 = st.columns([0.04, 0.26, 0.7])
head_col1.image("https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/etha-earth-logo.png?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ")
logo_name = '<p style="font-family:sans-serif; color:Orange; font-size: 32px;"><b>Etha-earthpallet</b></p>'
head_col2.markdown(logo_name, unsafe_allow_html=True)

content = """
<p style="font-family:sans-serif; color:#101010; font-size: 15px;">Discover a Green Balcony Oasis! Let our premium grass solutions transform your balcony into a lush, low-maintenance space. Embrace nature and create a relaxing outdoor space to unwind.</p>
<p style="font-family:sans-serif; color:#101010; font-size: 15px;">Our dedicated team of experts is passionate about greening urban areas. With their guidance and installation services, turning your balcony into a green paradise is easy.</p>
<p style="font-family:sans-serif; color:#101010; font-size: 15px;">Experience the beauty of nature right at your doorstep today!<br>Mobile:+91 7208005001<br>Email: mahendra.salunkhe@gmail.com<br>Address: Borivali, Mumbai, India.</p>
"""
head_col3.markdown(content, unsafe_allow_html=True)

# st.caption(':Yellow[Mobile]')

