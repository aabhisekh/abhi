import streamlit as st
import glob
import os
import time
import pandas as pd
from PIL import ImageFile, Image
#ImageFile.LOAD_TRUNCATED_IMAGES = True

st.markdown("# Turkey & Egypt Few Pics - Mom and Abhi")
st.sidebar.markdown("# Mom and ABhi")
path = "/app/abhi/Turkey"
filenames = glob.glob(os.path.join(path, "*"))
placeholder = st.empty()

for filename in filenames:
    image = Image.open(filename)
    placeholder.image(image, caption='Few Pics - Mom and Abhi - Turkey & Egypt - Dec 2022')
    time.sleep(4)
