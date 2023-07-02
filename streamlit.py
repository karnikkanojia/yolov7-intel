import tempfile
import streamlit as st
import pandas as pd
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os
#import tensorflow as tf
#import tensorflow_hub as hub
import time ,sys
import urllib.request
import urllib
import cv2
import numpy as np
import time
import sys
from demp import*

def main():
    st.title("Object Detection using Intel")
    st.sidebar.title("Settings")
    st.sidebar.subheader("Parameters")
    st.markdown(
        """
        <style>
        [data-testid="stSiderbar"][aria-expanded="true]>div:first-child{
        width:300px;
        }
        [data-testid="stSiderbar"][aria-expanded="true]>div:first-child{
        width:300px;
        margin-left:-300px;
        }
        </style>
        """,
        unsafe_allow_html=True


    )

    app_model=st.sidebar.selectbox("Choose the App Model",['About App','Run on Image','Run on Video','Run on WenCam'])

    if app_model=='About App':
        st.markdown('In this project we are using intel model to do Object Detection on Videos using Streamlit')
        st.markdown(
        """
        <style>
        [data-testid="stSiderbar"][aria-expanded="true]>div:first-child{
        width:300px;
        }
        [data-testid="stSiderbar"][aria-expanded="true]>div:first-child{
        width:300px;
        margin-left:-300px;
        }
        </style>
        """,
        unsafe_allow_html=True

    )

    elif app_model=="Run on WenCam":
        stframe5=st.empty()
        run_object_web(stframe5,source=0, flip=True, use_popup=False)
  
    elif app_model=="Run on Image" :
        img_file_buffer=st.sidebar.file_uploader("Upload an image",type=["jpg","jpeg","png"]) 
        DEMO_IMAGE="D:\\autonomous vechicle\\traffic.jpg"
        if img_file_buffer is not None:
            img=cv2.imread(img_file_buffer)
            image=np.array(Image.open(img_file_buffer))
            st.sidebar.text('Original Image')
            st.sidebar.image(image)
            stframe5=st.empty()
            run_on_image(img_file_buffer,stframe5)
        else:
            img=cv2.imread(DEMO_IMAGE)
            image=np.array(Image.open(DEMO_IMAGE))
            st.sidebar.text('Original Image')
            st.sidebar.image(image)
            stframe5=st.empty()
            run_on_image(img_file_buffer,stframe5)




    elif app_model=="Run on Video":
        #confidence=st.sidebar.slider('Confidence',min_value=0.0,max_value=1.0)
        st.markdown(
            """
            <style>
            [data-testid="stSiderbar"][aria-expanded="true]>div:first-child{
            width:300px;
            }
            [data-testid="stSiderbar"][aria-expanded="true]>div:first-child{
            width:300px;
            margin-left:-300px;
            }
            </style>
            """,
            unsafe_allow_html=True

        )
        st.sidebar.markdown('---')
        video_file_buffer=st.sidebar.file_uploader("Upload the video",type=["mp4","avi","mov","asf"])

        DEMO_VIDEO='D:\\autonomous vechicle\\Los Angeles 4K - California Glow - Scenic Drive - 2160.mp4'
        #tffile=tempfile.NamedTemporaryFile(suffix='.mp4',delete=False)
        #tffile.write(video_file_buffer.read())
        demo_vid=open(DEMO_VIDEO,'rb')
        demo_bytes=demo_vid.read()
        st.sidebar.text("Input video")
        st.sidebar.video(demo_bytes)
        tffile=tempfile.NamedTemporaryFile(suffix=".mp4",delete=False)
        tffile.name=DEMO_VIDEO
        #tffile.write(video_file_buffer.read())
        stframe=st.empty()
        st.markdown("<hr/>",unsafe_allow_html=True)
        kpi1,kpi2=st.columns(2)
        with kpi1:
            st.markdown("INFERENCE TIME")
            kpi1_text=st.markdown("0")
        with kpi2:
            st.markdown("FPS")
            kpi2_text=st.markdown("0")
        st.markdown("<hr/>",unsafe_allow_html=True)
        stframe2=st.empty()
        stframe3=st.empty()
        kpi3,kpi4=st.columns(2)
        with kpi3:
            st.markdown("INFERENCE TIME")
            kpi3_text=st.markdown("0")
        with kpi4:
            st.markdown("FPS")
            kpi4_text=st.markdown("0")
        stframe4=st.empty()
        run_object_detection(tffile.name,stframe,stframe2,kpi1_text,kpi2_text,flip=True, use_popup=False)
        #run_object_detection_yolo(DEMO_VIDEO,stframe3,stframe4,kpi3_text,kpi4_text)
        



if __name__=='__main__':
    try:
        main()
    except SystemExit:
        pass