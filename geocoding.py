import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# Load your dataset
data = pd.DataFrame('datasets.csv')

# Initialize Nominatim Geocoder
geolocator = Nominatim(user_agent="geoapi_exercise")

# Function to fetch latitude and longitude
def get_lat_lon(address):
    try:
        location = geolocator.geocode(address, timeout=10)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return None, None

# Add latitude and longitude to the dataset
latitude = []
longitude = []

for index, row in data.iterrows():
    address = f"{row['Area']}, {row['Address']}, {row['City']}"
    lat, lon = get_lat_lon(address)
    latitude.append(lat)
    longitude.append(lon)
    print(f"Processed: {address} -> {lat}, {lon}")
    time.sleep(1)  # Respect Nominatim's rate limit of 1 request/second

data['latitude'] = latitude
data['longitude'] = longitude

# Save the updated dataset
data.to_csv("restaurants_with_coordinates.csv", index=False)
print("Geocoding completed!")

