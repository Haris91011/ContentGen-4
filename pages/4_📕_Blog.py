import streamlit as st
from streamlit_chat import message
from streamlit_Utilities import *
st.set_page_config(
    page_title="Ryan_Blog",
    page_icon="🐥"
)

openapi_key = st.secrets["open_ai_key"]
# openai.api_key = api_key.key
openai.api_key = openapi_key
SerpAPIWrapper.serp_api_key = st.secrets["serp_api_key"]
if 'blogP' not in st.session_state:
    st.session_state['blogP'] = []
if 'blogI' not in st.session_state:
    st.session_state['blogI'] = []
if 'blogT' not in st.session_state:
    st.session_state['blogT'] = []
if 'blogS' not in st.session_state:
    st.session_state['blogS'] = []
if 'blogC' not in st.session_state:
    st.session_state['blogC'] = []
if 'blogSE' not in st.session_state:
    st.session_state['blogSE'] = []
if 'blogL' not in st.session_state:
    st.session_state['blogL'] = []
if 'blogSa' not in st.session_state:
    st.session_state['blogSa'] = []
st.title('Blog Content Generator Demo')
user_prompt = st.text_input('Write Your Topic.')
st.sidebar.title('Enter your Title')
str_prompt = st.sidebar.text_input('Write Your Title:')
BlogT,BlogS,BlogC,BlogI,BlogL,BlogSE=st.columns(6)
if user_prompt:
    with BlogT:
        if st.button("Blog Title", use_container_width=True):
            st.session_state['blogT']=blogMultiTitleGenerator(user_prompt)

    # global_pro=str_prompt
if str_prompt:
    with BlogS:
        if st.sidebar.button("Blog Structure", use_container_width=True):
            # str_prompt="Hi"
            print("1")
            print(str_prompt)
            print("-----------------------------------------------")
            st.session_state['blogS'] = generate_Blog_Structure(str_prompt)
            st.session_state['blogSa']=st.session_state['blogS']
    with BlogC:
        if st.sidebar.button("Blog Content",use_container_width=True):
            print("1")
            print(len(st.session_state['blogSa']))
            print("-----------------------------------------------")
            st.session_state['blogC']=generate_Blog_Content(str_prompt, st.session_state['blogSa'])
    with BlogI:
        if st.sidebar.button("Blog Image", use_container_width=True):
            print(str_prompt)
            print(st.session_state['blogC'])
            print("-----------------------------------------------")
            blogRefineText=blogMultiPromptGenerator(str_prompt,st.session_state['blogC'])
            st.session_state['blogI']=generate_multi_thumbnail_background(blogRefineText)
    with BlogSE:
        if st.sidebar.button("Blog SEO", use_container_width=True):
            print("4")
            print(str_prompt)
            print("-----------------------------------------------")
            st.session_state['blogSE']=generate_Blog_SEO(str_prompt)
    with BlogL:
        if st.sidebar.button("Blog Links", use_container_width=True):
            print("5")
            print(str_prompt)
            print("-----------------------------------------------")
            blogLink=topic_generate(str_prompt)
            st.session_state['blogL']=blog_repo_links(blogLink)
if st.session_state['blogT']:
    st.header("Blog Title")
    for i in range(0,len(st.session_state['blogT'])):
        message(st.session_state['blogT'][i])
if st.session_state['blogS']:
    st.header("Blog Structure")
    message(st.session_state['blogS'])
if st.session_state['blogC']:
    st.header("Blog Content")
    message(st.session_state['blogC'])
if st.session_state['blogI']:
    st.header("Blog Image Generated")
    # st.write("Blog Image")
    for i in range(0,3): 
        st.image(st.session_state['blogI'][i],caption='Generated Image',use_column_width=True)
if st.session_state['blogSE']:
    st.header("Blog SEO words Generated")
    # st.write("Blog SEO")
    message(st.session_state['blogSE'])
if st.session_state['blogL']:
    st.write("Blog Links")
    message(st.session_state['blogL'])