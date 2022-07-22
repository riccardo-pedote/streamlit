#streamlit run /Users/rp/Documents/Master/Python/streamlit/model_test.py
import streamlit as st
import joblib
with st.container():
  st.title('MODEL TEST')
  ''
  col1,col2=st.columns(2)
  with col1:
    sup=st.slider('Superficie:',8,20,12)
  with col2:
    coi=st.slider('Coinquilini:',2,10,4)
  ute=st.checkbox('Utenze incluse')
  lr_room=joblib.load('./lr_room.sav')
  pre=round(lr_room.predict([[sup,ute,coi]])[0])
  ''
  st.header(f'Il prezzo stimato è {pre}€')
