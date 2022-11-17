import streamlit as st
import glob
import os
import time
import pandas as pd
from PIL import ImageFile, Image
ImageFile.LOAD_TRUNCATED_IMAGES = True

st.markdown("# Abhi's Pics")
st.sidebar.markdown("# Abhi")
path = "/app/abhi/abhi/Pics"
filenames = glob.glob(os.path.join(path, "*"))
placeholder = st.empty()

for filename in filenames:
    image = Image.open(filename)
    placeholder.image(image, caption='Abhi latest Pics')
    time.sleep(4)
