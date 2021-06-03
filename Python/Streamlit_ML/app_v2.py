import streamlit as st
import cv2
from PIL import Image,ImageEnhance
import numpy as np
import os




def main():
    favicon="logo.png"
    st.set_page_config(page_title='ML APP', page_icon = favicon, layout = 'wide', initial_sidebar_state = 'auto')
    st.title("Face Detection App")
    st.text("Build with Streamlit and OpenCV")
    #st.video("cursorAutodrawing.mp4")
     
    activities = ["Detection","About"]
    choice = st.sidebar.selectbox("Select Activity",activities)
    
    if choice == 'Detection':
        st.subheader("Face Detection")
        
        image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg','mp4'])
   
    
  
        
    #image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg','.mp4'])
        
    
          
if __name__=='__main__':
    main();   


    