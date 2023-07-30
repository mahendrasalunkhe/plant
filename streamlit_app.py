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

head_col1, head_col2, head_margin = st.columns((0.3, 2.7, 3))
head_col1.image("https://raw.githubusercontent.com/mahendrasalunkhe/plant/main/etha-earth-logo.png?token=GHSAT0AAAAAAB6A64EQU6FTCLAC4KQUJNPKY6VR5ZQ")
logo_name = """<p style="font-family:sans-serif; color:Orange; font-size: 36px;"><b>Etha-earthpallet</b></p>
<br><br>
<p style="font-family:sans-serif; color:Green; font-size: 12px;">Welcome to the Green Balcony Oasis!

Transform your balcony into a lush and vibrant green space with our premium grass solutions. At Green Balcony Oasis, we believe that even the smallest outdoor areas can be transformed into beautiful and relaxing havens. Whether you have a cozy apartment balcony or a spacious terrace, we have the perfect grass options to suit your needs.

Why Choose Grass for Your Balcony?

Natural Beauty: Bring the beauty of nature to your balcony with our lush and realistic grass. Enjoy the soothing greenery that adds a touch of serenity to your urban oasis.

Low Maintenance: Say goodbye to mowing and watering! Our artificial grass requires minimal upkeep, freeing up your time to simply enjoy your balcony retreat.

Year-Round Greenery: No matter the season, your balcony will stay green and vibrant with our all-weather grass. Enjoy the beauty of nature every day, no matter the weather outside.

Soft and Comfortable: Our premium grass is not only beautiful but also soft to the touch. Create a cozy and comfortable outdoor space where you can relax and unwind.

Pet-Friendly: If you have furry friends, worry not! Our grass is pet-friendly, easy to clean, and resistant to stains, making it a perfect surface for your pets to play on.

UV Resistant: Our artificial grass is designed to withstand the harsh effects of the sun, ensuring that it remains green and vibrant for years to come.

Our Grass Products:

Balcony Bliss: Ideal for smaller balconies, this compact and low-pile grass option brings a touch of green without overwhelming the space. It's perfect for adding a natural touch to your urban dwelling.

Terrace Tranquility: Transform your terrace into a relaxing oasis with our Terrace Tranquility grass. Its lush and luxurious appearance will make you feel like you're surrounded by nature.

Pet Paradise: For pet owners, our Pet Paradise grass is the ultimate solution. It offers a durable and pet-friendly surface that your furry companions will love.

All-Season Elegance: No matter the weather, our All-Season Elegance grass stays green and beautiful year-round, giving your balcony a fresh and inviting look no matter the season.

Create Your Green Balcony Oasis Today!

Revitalize your balcony and make it a place of comfort and tranquility with our premium grass products. Whether you're looking to create a relaxing retreat, a play area for your pets, or a vibrant outdoor space for entertaining guests, Green Balcony Oasis has the perfect grass solution for you.

Contact us now to explore our range of products and to get expert advice on creating your own green paradise. Embrace the beauty of nature on your balcony with Green Balcony Oasis!</p>"""
head_col2.markdown(logo_name, unsafe_allow_html=True)


