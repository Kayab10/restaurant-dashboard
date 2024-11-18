import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Kayab Khan',
    page_icon='🫂',
)
image = 'https://i.pinimg.com/736x/53/b6/90/53b690bca338c46241b921072271a194.jpg'
st.logo(image=image,size='large')
st.title('About')
st.write('So, this is my project on resturant data analysis and plotting them on map')
st.header('go to recommend section on sidebar for project')
st.write('you may argue that this is not Machine Learning project and youre right, it is not, it is simple GEOSPATIAL project.' 
         ' however this project uses many data science techniques, such as feature engineering, data analysis')
st.write('for this project i used two data set one from a fake shady intern company and one from kaggle of swiggy dataset,'
         ' but swiggy dataset did not contain cooordinates so i had to use a geooding libraies to gather all the coordaintes from address and city data available'
         ' that took me almost 4 hours')
st.write('it is not a extraordinary project, and utilises basic conditional arguments in the backend '
         ' i will do a recommendation system that utilises content based filtering and collaborative based filtering after my exam,')

st.write(' i did this to understand geospatial projects')
st.write('more to come after exam, abhi chemistry padne ja raha 😎')



# .\venv\Scripts\activate