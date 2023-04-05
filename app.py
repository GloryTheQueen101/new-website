import streamlit as st
from PIL import Image


st.set_page_config(page_title="My Website", page_icon=":blue_heart:", layout="centered")

img_contact_from = Image.open("images/Commission #17.webp")
img_contact_from_1 = Image.open("images/GEO1.webp")
img_contact_from_2 = Image.open("images/strider icon.webp")
img_contact_from_3 = Image.open("images/TBN #3.webp")
img_contact_from_4 = Image.open("images/Reef.webp")
img_contact_from_5 = Image.open("images/Reef.webp")


with st.container():
    st.subheader("Hi, I am Glory!")
    st.title("An Artist")
    st.write("I love to draw dragons, and am currently learning how to draw humans and ferals.")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Can/Can't Do")
        st.write("##")
        st.subheader("I Can Do:")
        st.markdown('<font size="4">&#10085; Dragons (WoF/Non-WoF)</font>', unsafe_allow_html=True)
        st.markdown('<font size="4">&#10085; Some Ferals (Depends on complexity.)</font>', unsafe_allow_html=True)
        st.markdown('<font size="4">&#10085; Headshots/Icons</font>', unsafe_allow_html=True)
        st.markdown('<font size="4">&#10085; Fullbodies</font>', unsafe_allow_html=True)
        st.markdown('<font size="4">&#10085; Customs</font>', unsafe_allow_html=True)
        st.write("##")
        st.subheader("I CAN'T Do:")
        st.markdown('<font size="4">&#10085; Humanoids</font>', unsafe_allow_html=True)
        st.markdown('<font size="4">&#10085; NSFW Stuff (Light gore excluded)</font>', unsafe_allow_html=True)
        st.write("##")
        st.write("I am most active on Discord (_glory-#1574), and you can send a friend request if you are interested in commissioning me ^^")



with st.container():
    st.write("---")
    st.header("My Art")
    st.write("##")
    st.write("##")
    image_column, text_column, image_column_1 = st.columns((1, 1, 1))

    with image_column:
        st.image(img_contact_from)
    with text_column:
        st.subheader("Icons")
        st.markdown('<font size="3">&#10085; Sketch - 80 DA Pts</font>', unsafe_allow_html=True)
        st.markdown('<font size="3">&#10085; Colored Sketch - 120 DA Pts</font>', unsafe_allow_html=True)
        st.markdown('<font size="3">&#10085; Colored Lineart - 240 DA Pts</font>', unsafe_allow_html=True)
        st.markdown('<font size="3">&#10085; Colored and Shaded Lineart - 400 DA Pts</font>', unsafe_allow_html=True)
    with image_column_1:
        st.image(img_contact_from_1)

with st.container():
    image_column_2, image_column_3, image_column_4 = st.columns((1, 1, 1))
    with image_column_2:
            st.image(img_contact_from_2)
    with image_column_3:
            st.image(img_contact_from_3)
    with image_column_4:
            st.image(img_contact_from_4)

with st.container():
    st.write("##")

with st.container():
    image_column_5, text_column_1, image_column_6 = st.columns((1, 1, 1))




