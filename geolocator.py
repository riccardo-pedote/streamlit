import streamlit as st
import pandas as pd
import geopy
from geopy import distance
with st.container():
  st.title('GEOLOCATOR')
  ''
  address=st.text_input('Insert an address:')
  try:
    geo=geopy.geocoders.Nominatim(user_agent='rp')
    loc=geo.geocode(address)
    df=pd.DataFrame({'lat':loc.latitude,'lon':[loc.longitude]})
    dist=round(distance.distance((loc.latitude,loc.longitude),(45.5182136,9.2126738)).km)
    ''
    f'Latitude: {loc.latitude} / Longitude: {loc.longitude}'
    f'The address is {dist} km from University of Milano-Bicocca.'
    ''
    with st.expander(loc.address,True):
      st.map(df)
  except:
    pass