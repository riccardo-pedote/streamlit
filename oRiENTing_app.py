import streamlit as st
import matplotlib.image as image
import pandas as pd
import joblib
import geopy
from geopy.distance import distance
import shapefile
from shapely.geometry import Point
from shapely.geometry import shape
path='/app/streamlit/'
geo=geopy.geocoders.Nominatim(user_agent='rp')
with st.container():
  st.image(image.imread(path+'logo.png'))
  tab1,tab2=st.tabs(['Appartamento','Stanza'])
  with tab1:
    ''
    ind1=st.text_input('Indirizzo:',key='ind1')
    ''
    col1,col2,col3=st.columns(3)
    with col1:
      sup1=st.slider('Superficie dell\'appartamento:',25,250,50,key='sup1')
    with col2:
      cam1=st.slider('Numero di camere da letto:',1,4,1,key='cam1')
    with col3:
      per1=st.slider('Numero di persone:',1,8,2,key='per1')
    ''
    col1,col2,col3,col4=st.columns(4)
    with col1:
      ute1=st.checkbox('Utenze incluse',key='ute1')
      gia1=st.checkbox('Giardino',key='gia1')
    with col2:
      bal1=st.checkbox('Balcone',key='bal1')
      lvt1=st.checkbox('Lavatrice',key='lvt1')
    with col3:
      asc1=st.checkbox('Asciugatrice',key='asc1')
      lvs1=st.checkbox('Lavastoviglie',key='lvs1')
    with col4:
      con1=st.checkbox('Condizionatore',key='con1')
    ''
    try:
      loc1=geo.geocode(ind1)
      coo1=pd.DataFrame({'lat':[loc1.latitude],'lon':[loc1.longitude]})
      if loc1.address.find('Madrid')>-1:
        i=1
        ds=shapefile.Reader(path+'madrid_shapes.shp')
        dp=pd.read_csv(path+'madrid_prices.csv')
        mod1=joblib.load(path+'lr_mf.sav')
        poi1=pd.read_csv(path+'madrid_poi.csv')
      if loc1.address.find('Paris')>-1:
        i=3
        ds=shapefile.Reader(path+'paris_shapes.shp')
        dp=pd.read_csv(path+'paris_prices.csv')
        mod1=joblib.load(path+'lr_pf.sav')
        poi1=pd.read_csv(path+'paris_poi.csv')
      dpr1=min(dp.Prezzo)
      for s in range(len(ds.shapes())):
        if Point(loc1.longitude,loc1.latitude).within(shape(ds.shapes()[s])):
          dpr1=ds.records()[s][i]
      for p in dp.index:
        if dpr1==dp.Distretto[p]:
          dpr1=dp.Prezzo[p]
      dis1=[]; nam1=[]
      for t in ['Metro','Treno','Supermarket','Coworking','Università','Ospedale']:
        d1=100
        for i in poi1[poi1.Tipologia==t].index:
          if distance((loc1.latitude,loc1.longitude),(poi1.Latitudine[i],poi1.Longitudine[i])).km<d1:
            d1=distance((loc1.latitude,loc1.longitude),(poi1.Latitudine[i],poi1.Longitudine[i])).km
            n1=poi1.Nome[i]
        dis1.append(round(d1*1000)); nam1.append(n1)
      pre1=round(mod1.predict([[dpr1,cam1,sup1,per1,gia1,bal1,con1,lvt1,asc1,lvs1,ute1,
                                dis1[0],dis1[1],dis1[2],dis1[3],dis1[4],dis1[5]]])[0])
      st.subheader(f'L\'affitto mensile stimato dell\'appartamento è {pre1}€')
      ''
      with st.expander('Punti di interesse:',True):
        ''
        f'- La metro più vicina è "{nam1[0]}" e dista {dis1[0]}m'
        f'- Il treno più vicino è "{nam1[1]}" e dista {dis1[1]}m'
        f'- Il supermarket più vicino è "{nam1[2]}" e dista {dis1[2]}m'
        f'- Il coworking più vicino è "{nam1[3]}" e dista {dis1[3]}m'
        f'- L\'università più vicina è "{nam1[4]}" e dista {dis1[4]}m'
        f'- L\'ospedale più vicino è "{nam1[5]}" e dista {dis1[5]}m'
        ''
      ''
      with st.expander(loc1.address,False):
        st.map(coo1)
    except:
      if ind1!='':
        st.subheader('Indirizzo non valido! Provane un altro.')
  with tab2:
    ''
    ind2=st.text_input('Indirizzo:',key='ind2')
    ''
    col1,col2=st.columns(2)
    with col1:
      sup2=st.slider('Superficie della stanza:',6,30,10,key='sup2')
    with col2:
      per2=st.slider('Numero di inquilini:',1,8,4,key='per2')
    ''
    col1,col2,col3,col4=st.columns(4)
    with col1:
      ute2=st.checkbox('Utenze incluse',key='ute2')
      gia2=st.checkbox('Giardino',key='gia2')
    with col2:
      bal2=st.checkbox('Balcone',key='bal2')
      lvt2=st.checkbox('Lavatrice',key='lvt2')
    with col3:
      asc2=st.checkbox('Asciugatrice',key='asc2')
      lvs2=st.checkbox('Lavastoviglie',key='lvs2')
    with col4:
      con2=st.checkbox('Condizionatore',key='con2')
      wcp2=st.checkbox('WC privato',key='wcp2')
    ''
    try:
      loc2=geo.geocode(ind2)
      coo2=pd.DataFrame({'lat':[loc2.latitude],'lon':[loc2.longitude]})
      if loc2.address.find('Madrid')>-1:
        i=1
        ds=shapefile.Reader(path+'madrid_shapes.shp')
        dp=pd.read_csv(path+'madrid_prices.csv')
        mod2=joblib.load(path+'lr_mr.sav')
        poi2=pd.read_csv(path+'madrid_poi.csv')
      if loc2.address.find('Paris')>-1:
        i=3
        ds=shapefile.Reader(path+'paris_shapes.shp')
        dp=pd.read_csv(path+'paris_prices.csv')
        mod2=joblib.load(path+'lr_pr.sav')
        poi2=pd.read_csv(path+'paris_poi.csv')
      dpr2=min(dp.Prezzo)
      for s in range(len(ds.shapes())):
        if Point(loc2.longitude,loc2.latitude).within(shape(ds.shapes()[s])):
          dpr2=ds.records()[s][i]
      for p in dp.index:
        if dpr2==dp.Distretto[p]:
          dpr2=dp.Prezzo[p]
      dis2=[]; nam2=[]
      for t in ['Metro','Treno','Supermarket','Coworking','Università','Ospedale']:
        d2=100
        for i in poi2[poi2.Tipologia==t].index:
          if distance((loc2.latitude,loc2.longitude),(poi2.Latitudine[i],poi2.Longitudine[i])).km<d2:
            d2=distance((loc2.latitude,loc2.longitude),(poi2.Latitudine[i],poi2.Longitudine[i])).km
            n2=poi2.Nome[i]
        dis2.append(round(d2*1000)); nam2.append(n2)
      pre2=round(mod2.predict([[dpr2,sup2,per2,wcp2,gia2,bal2,con2,lvt2,asc2,lvs2,ute2,
                                dis2[0],dis2[1],dis2[2],dis2[3],dis2[4],dis2[5]]])[0])
      st.subheader(f'L\'affitto mensile stimato della stanza è {pre2}€')
      ''
      with st.expander('Punti di interesse:',True):
        ''
        f'- La metro più vicina è "{nam2[0]}" e dista {dis2[0]}m'
        f'- Il treno più vicino è "{nam2[1]}" e dista {dis2[1]}m'
        f'- Il supermarket più vicino è "{nam2[2]}" e dista {dis2[2]}m'
        f'- Il coworking più vicino è "{nam2[3]}" e dista {dis2[3]}m'
        f'- L\'università più vicina è "{nam2[4]}" e dista {dis2[4]}m'
        f'- L\'ospedale più vicino è "{nam2[5]}" e dista {dis2[5]}m'
        ''
      ''
      with st.expander(loc2.address,False):
        st.map(coo2)
    except:
      if ind2!='':
        st.subheader('Indirizzo non valido! Provane un altro.')
