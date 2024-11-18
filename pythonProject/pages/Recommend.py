import pandas as pd
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from streamlit_folium import st_folium
import os
image = 'https://i.pinimg.com/736x/53/b6/90/53b690bca338c46241b921072271a194.jpg'
st.logo(image=image,size='large')

file_path = os.path.join(os.path.dirname(__file__), "../data/restaurant.csv")
df = pd.read_csv(file_path)

# Split cuisines into multiple rows
df['Food type'] = df['Food type'].str.split(',')
df = df.explode(('Food type'))

st.title("Restaurant Recommendation System")

city = st.selectbox("select City:",df['City'].unique())
df_city = df[df['City'] == city]
cuisine = st.selectbox('cuisine:',df_city['Food type'].unique())
filtered_df = df_city[df_city['Food type'] == cuisine]

center_lat = filtered_df["latitude"].mean()
center_lon = filtered_df["longitude"].mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=6)

marker_cluster = MarkerCluster().add_to(m)
for _, row in filtered_df.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"{row['Restaurant']} ({row['Food type']})"
    ).add_to(marker_cluster)

st_data = st_folium(m,width=1000,height=600)