import streamlit as st
import requests

API_KEY = config['APi_KEY']
URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

request = requests.get(URL)

data = request.json()

title = data["title"]

explanation = data["explanation"]

img_url = data["url"]

r = requests.get(img_url)
img = r.content

with open('image.jpg', "wb") as file:
    file.write(img)

st.header(title)
st.image("image.jpg")
st.write(explanation)
