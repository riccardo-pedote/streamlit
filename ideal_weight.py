#streamlit run /Users/rp/Documents/Master/Python/streamlit/ideal_weight.py
import streamlit as st
with st.sidebar:
  um=st.radio('Unit of measure:',['Metric','Imperial'])
  st.text('')
  st.caption('By Riccardo Pedote')
con1=st.container()
with con1:
  st.title('Ideal Body Weight Calculator')
  st.text('')
  if um=='Metric':
    h=st.slider('Height (cm):',140,200,170,1)
    st.text('')
    sex=st.selectbox('Gender:',['Male','Female'])
    s=0 if sex=='Male' else 0.1
    w=round(22*((h/100-s)**2))
    st.text('')
    st.text('')
    st.subheader(f'Your ideal body weight is {w}kg.')
  else:
    col1,col2=st.columns(2)
    with col1:
      hf=st.slider('Height (ft):',4,6,5,1)
    with col2:
      hi=st.slider('Height (in):',0.,12.,6.,0.5)
    st.text('')
    sex=st.selectbox('Gender:',['Male','Female'])
    s=0 if sex=='Male' else 0.1
    w=round(22*((hf/3.281+hi/39.37-s)**2)*2.2)
    st.text('')
    st.text('')
    st.subheader(f'Your ideal body weight is {w}lb.')
