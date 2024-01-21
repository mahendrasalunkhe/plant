import streamlit as st

st.set_page_config(
    page_title="Etha-GlassWindow",
    page_icon="https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/etha-earth-logo.png?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "Glass window for your home"
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
    background-image: url("https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/SlidingWindow.png?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ");
    background-size: cover;
}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

head_col1, head_col2, head_col3 = st.columns([0.04, 0.26, 0.7])
head_col1.image("https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/etha-earth-logo.png?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ")
logo_name = '<p style="font-family:sans-serif; color:Orange; font-size: 32px;"><b>Etha Glass Window</b></p>'
head_col2.markdown(logo_name, unsafe_allow_html=True)

head2_col1, head2_col2, head2_col3 = st.columns([3, 2, 1])
content = """
<p style="font-family:sans-serif; color:#101010; font-size: 16px;">Welcome to Etha Glass Window, your premier destination for glass sliding windows in Mumbai, India. We understand the importance of windows in transforming the look and feel of your home or office. Our team of experts is dedicated to providing high-quality windows that not only offer exceptional functionality but also serve as a stunning visual centrepiece.</p>
<p style="font-family:sans-serif; color:#101010; font-size: 16px;">We believe that this approach allows for greater customization and adds a touch of elegance to any space. With our wide range of vibrant colours and carefully crafted patterns, you can create a truly unique and personalized environment.</p>
<p style="font-family:sans-serif; color:#101010; font-size: 16px;">Our team will work closely with you to understand your needs and provide tailored solutions that exceed your expectations. Windows is meticulously designed to seamlessly integrate with your existing décor and architectural style.</p>
"""

content_1 = """
<p style="font-family:sans-serif; color:#101010; font-size: 16px;">Ready to transform your space with our glass windows!<br>Mobile:+91 7208005001<br>Email: mahendra.salunkhe@gmail.com<br>Address: Borivali, Mumbai, India.</p>
"""
head2_col3.markdown(content_1, unsafe_allow_html=True)

# st.caption(':Yellow[Mobile]')

