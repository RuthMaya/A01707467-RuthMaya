# -*- coding: utf-8 -*-
"""EvidenciaFinalUF6_A01707467.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dKJ4I2T4wzTdk74Zy6P0KG_3bPaTMef6
"""

import streamlit as st
import pandas as pd
import numpy as np
st.title('Police Incident Reports from 2018 to 2020 in San Francisco')
df = pd.read_csv("https://drive.google.com/drive/folders/1Hd2HOFknGccrm11VSdDp5N9-ADkboWvZ")
st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')
mapa=pd.DataFrame(
    np.random.randn(1000, 2) * [3, 2] + [37.76, -122.4],
    columns=['lat', 'lon'])
mapa = mapa.dropna()
st.map(mapa.astype(int))