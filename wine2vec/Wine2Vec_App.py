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
  df=pd.read_csv(path+'variety.csv')
  col1,col2=st.columns(2)
  min_p=col1.slider('Min price:',0,100,0)
  max_p=col2.slider('Max price:',0,100,100)
  ''
  if len(pos)>0 or len(neg)>0:
    pos=[i.lower().replace(' ','_') for i in pos]
    neg=[i.lower().replace(' ','_') for i in neg]
    ms=emb.most_similar(positive=pos,negative=neg,topn=77000)
    ms=[i[0].capitalize().replace('_',' ') for i in ms]
    wines=df.variety.to_list()
    top,pri=[],[]
    for i in ms:
      if i in wines:
        p=df.price[df.variety==i].iloc[0]
        if p>min_p and p<max_p:
          top.append(i)
          pri.append(p)
      if len(top)==5:
        break
    for i in range(len(top)):
      st.text(f'• {top[i]} ({round(pri[i])}$)')
  ''
  with st.expander('Wine Chart'):
    st.image(path+'wine_compass.jpg')
  ''
  st.caption('Designed by Riccardo Pedote, Sara Gragnagniello, Isabel Mendez')
