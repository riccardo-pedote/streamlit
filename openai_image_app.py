# streamlit run /Users/rp/Documents/Python/streamlit/openai_image_app.py
import openai,PIL,requests,io,streamlit as st
openai.api_key='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'
#url='https://st.ilfattoquotidiano.it/wp-content/uploads/2022/09/15/Roger-Federer-690x362.jpg'
con1=st.container()
with con1:
  st.title('OpenAI Image Generator')
  st.text('')
  text=st.text_input('Write a description:')
  st.text('')
  b=st.button('GENERATE')
  if b:
    response=openai.Image.create(prompt=text,n=1,size='1024x1024')
    url=response['data'][0]['url']
    b=False
  try:
    st.text('')
    st.image(url)
    st.text('')
    buf=io.BytesIO()
    PIL.Image.open(requests.get(url,stream=True).raw).save(buf,format='png')
    st.download_button('DOWNLOAD',data=buf.getvalue(),mime='image/png',
     file_name=text+'.png')
  except:
    pass
