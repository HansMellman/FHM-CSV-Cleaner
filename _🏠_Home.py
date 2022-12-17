import streamlit as st
import pandas as pd
from PIL import Image
from st_functions import load_css, st_button

st.set_page_config(
    page_title="FHM CSV Cleaner",
    page_icon="🏒"
)

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('FHM9_2.png'))


st.title("FHM CSV Cleaner")
# image = Image.open('FHM9_2.png')
# st.image(image, use_column_width=False)
st.info(f"This app is for use with Toby's Advanced Stats tool for Franchise Hockey Manager 9. It is intended to isolate data for NHL teams **only** at this present time.\
        See each page heading on the left hand side and follow the instructions on the page.")

icon_size = 20

st_button('youtube', 'https://www.youtube.com/ootpdevelopments', 'Official OOTP Youtube Channel', icon_size)
st_button('twitter', 'https://www.twitter.com/franchisehockey', 'Official FHM Twitter', icon_size)
st_button('twitch', 'https://www.twitch.tv/franchisehockeymanager', 'Official FHM Twitch', icon_size)
st_button('steam', 'https://store.steampowered.com/app/1937470/Franchise_Hockey_Manager_9/', 'Official FHM9 Steam Page', icon_size)
st_button('discord', 'https://discord.com/invite/hhaAgZb', 'Official OOTP Discord', icon_size)















