import streamlit as st
import pandas as pd
import numpy as np
import plotly as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from bokeh.plotting import figure
import matplotlib.pyplot as plt

st.title(':blue[**_Police Incident Reports from 2018 to 2020 in San Francisco_**]')

df = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")

st.markdown('The data shown below belongs to **_incident reports in the city of San Francisco_**, from the year **_2018 to 2020_**, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa = pd.DataFrame()
mapa['Date'] = df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Incident Subcategory'] = df['Incident Subcategory']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()

subset_data2 = mapa
police_district_input = st.sidebar.multiselect(
'Police District',
mapa.groupby('Police District').count().reset_index()['Police District'].tolist())
if len(police_district_input) > 0:
    subset_data2 = mapa[mapa['Police District'].isin(police_district_input)]

subset_data1 = subset_data2
neighborhood_input = st.sidebar.multiselect(
'Neighborhood',
subset_data2.groupby('Neighborhood').count().reset_index()['Neighborhood'].tolist())
if len(neighborhood_input) > 0:
    subset_data1 = subset_data2[subset_data2['Neighborhood'].isin(neighborhood_input)]

subset_data = subset_data1
incident_input = st.sidebar.multiselect(
'Incident Category',
subset_data1.groupby('Incident Category').count().reset_index()['Incident Category'].tolist())
if len(incident_input) > 0:
    subset_data = subset_data1[subset_data1['Incident Category'].isin(incident_input)]
            
subset_data    
    
st.markdown('It is important to mention that any police district can answer to any incident,**_the neighborhood in which it happened is not related to the police district_**.')    
st.markdown(':blue[**Crime locations in San Francisco**]')
st.map(subset_data)

st.markdown(':blue[**Crimes ocurred per day of the week**]')
data = [
    go.Line(
        x=subset_data['Day'].value_counts().index,
        y=subset_data['Day'].value_counts().values,
        marker=dict(
            color='#105196'
        )
    )
]
layout = go.Layout(
    xaxis=dict(title='Day'),
    yaxis=dict(title='Frecuency')
)
graf1 = go.Figure(data=data, layout=layout)
st.plotly_chart(graf1, use_container_width=True)


st.markdown(':blue[**Crimes ocurred per date**]')
st.line_chart(subset_data['Date'].value_counts())

st.markdown(':blue[**Crimes ocurred per year**]')
data = [
    go.Line(
        x=df['Incident Year'].value_counts().index,
        y=df['Incident Year'].value_counts().values,
        marker=dict(
            color='#105196'
        )
    )
]
layout = go.Layout(
    xaxis=dict(title='Incident Year'),
    yaxis=dict(title='Frecuency')
)
grafn = go.Figure(data=data, layout=layout)
st.plotly_chart(grafn, use_container_width=True)

st.markdown(':blue[**Type of crimes committed**]')
data = [
    go.Bar(
        x=subset_data['Incident Category'].value_counts().index,
        y=subset_data['Incident Category'].value_counts().values,
        marker=dict(
            color='#d0e0f1'
        )
    )
]
layout = go.Layout(
    xaxis=dict(title='Incident Category'),
    yaxis=dict(title='Frecuency')
)
graf2 = go.Figure(data=data, layout=layout)
st.plotly_chart(graf2, use_container_width=True)

agree = st.button(':violet[**Click to see Incident Subcategories**]')
if agree:
    st.markdown(':blue[**Subtype of crimes committed**]')
    data = [
        go.Bar(
            x=subset_data['Incident Subcategory'].value_counts().index,
            y=subset_data['Incident Subcategory'].value_counts().values,
            marker=dict(
                color='#72a3d6'
            )
        )
    ]
    layout = go.Layout(
        xaxis=dict(title='Incident Subcategory'),
        yaxis=dict(title='Frecuency')
    )
    graf2 = go.Figure(data=data, layout=layout)
    st.plotly_chart(graf2, use_container_width=True)

st.markdown(':blue[**_Resolution status_**]')
fig1, ax1 = plt.subplots()
labels = subset_data['Resolution'].unique()
ax1.pie(subset_data['Resolution'].value_counts(), labels=labels, autopct='%1.1f%%', startangle=20)
st.pyplot(fig1)

st.sidebar.markdown('''
---
:blue[**Ruth Maya López  /  A01707467**]
''')