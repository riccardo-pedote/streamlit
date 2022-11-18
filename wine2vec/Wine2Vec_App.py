path='/app/streamlit/wine2vec/'
import streamlit as st
import pandas as pd
from gensim.models import KeyedVectors
with st.container():
  st.image(path+'wine_logo.png',use_column_width=True)
  emb=KeyedVectors.load_word2vec_format(path+'wv.vec',binary=True)
  tokens=[i.capitalize().replace('_',' ') for i in emb.index_to_key]
  pos=st.multiselect('Desired features:',tokens)
  neg=st.multiselect('Undesired features:',tokens)
  ''
  if len(pos)>0 or len(neg)>0:
    pos=[i.lower().replace(' ','_') for i in pos]
    neg=[i.lower().replace(' ','_') for i in neg]
    ms=emb.most_similar(positive=pos,negative=neg,topn=77000)
    ms=[i[0].capitalize().replace('_',' ') for i in ms]
    df=pd.read_csv(path+'variety.csv')
    wines=df.variety.to_list()
    top=[]
    for i in ms:
      if i in wines:
        top.append(i)
      if len(top)==5:
        break
    for i in top:
      st.text('• '+i)
  ''
  with st.expander('Wine Chart'):
    st.image(path+'wine_compass.jpg')
