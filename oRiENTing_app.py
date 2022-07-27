import streamlit as st
import pandas as pd
import joblib
import geopy
with st.container():
  st.title('oRiENTing')
  ''
  tab1,tab2=st.tabs(['Appartamento','Stanza'])
  with tab1:
    ''
    ind1=st.text_input('Indirizzo:',key='ind1')
    ''
    col1,col2,col3=st.columns(3)
    with col1:
      sup1=st.slider('Superficie dell\'appartamento:',27,250,27,key='sup1')
    with col2:
      cam1=st.slider('Numero di camere da letto:',1,4,1,key='cam1')
    with col3:
      per1=st.slider('Numero di persone:',1,8,1,key='per1')
    ''
    col1,col2,col3,col4=st.columns(4)
    with col1:
      ute1=st.checkbox('Utenze incluse',key='ute1')
      gia1=st.checkbox('Giardino',key='gia1')
    with col2:
      bap1=st.checkbox('Balcone privato',key='bap1')
      bac1=st.checkbox('Balcone comune',key='bac1')
    with col3:
      lvt1=st.checkbox('Lavatrice',key='lvt1')
      asc1=st.checkbox('Asciugatrice',key='asc1')
    with col4:
      lvs1=st.checkbox('Lavastoviglie',key='lvs1')
      con1=st.checkbox('Condizionatore',key='con1')
    ''
    try:
      geo=geopy.geocoders.Nominatim(user_agent='rp')
      loc=geo.geocode(ind1)
      coo=pd.DataFrame({'lat':loc.latitude,'lon':[loc.longitude]})
      if loc.address.find('Madrid')>-1:
        lr_f=joblib.load('/app/streamlit/lr_mr.sav')
      if loc.address.find('Paris')>-1:
        lr_r=joblib.load('/app/streamlit/lr_pr.sav')
      pre=round(lr_r.predict([[sup1,cam1,per1,gia1,bap1,bac1,con1,lvt1,asc1,lvs1,ute1]])[0])
      st.subheader(f'Il prezzo stimato è {pre}€')
      ''
      with st.expander(loc.address,True):
        st.map(coo)
    except:
      pass
  with tab2:
    ''
    ind2=st.text_input('Indirizzo:',key='ind2')
    ''
    col1,col2,col3=st.columns(3)
    with col1:
      sup2=st.slider('Superficie della stanza:',27,250,27,key='sup2')
    with col3:
      per2=st.slider('Numero di inquilini:',1,8,1,key='per2')
    ''
    col1,col2,col3,col4=st.columns(4)
    with col1:
      ute2=st.checkbox('Utenze incluse',key='ute2')
      gia2=st.checkbox('Giardino',key='gia2')
      wcp2=st.checkbox('WC privato',key='wcp2')
    with col2:
      bap2=st.checkbox('Balcone privato',key='bap2')
      bac2=st.checkbox('Balcone comune',key='bac2')
    with col3:
      lvt2=st.checkbox('Lavatrice',key='lvt2')
      asc2=st.checkbox('Asciugatrice',key='asc2')
    with col4:
      lvs2=st.checkbox('Lavastoviglie',key='lvs2')
      con2=st.checkbox('Condizionatore',key='con2')
    ''
    try:
      geo=geopy.geocoders.Nominatim(user_agent='rp')
      loc=geo.geocode(ind2)
      coo=pd.DataFrame({'lat':loc.latitude,'lon':[loc.longitude]})
      if loc.address.find('Madrid')>-1:
        lr_f=joblib.load('/app/streamlit/lr_mf.sav')
      if loc.address.find('Paris')>-1:
        lr_f=joblib.load('/app/streamlit/lr_pf.sav')
      pre=round(lr_f.predict([[sup2,per2,wcp2,gia2,bap2,bac2,con2,lvt2,asc2,lvs2,ute2]])[0])
      st.subheader(f'Il prezzo stimato è {pre}€')
      ''
      with st.expander(loc.address,True):
        st.map(coo)
    except:
      pass
