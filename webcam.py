import streamlit as st
from PIL import Image


def render_bw_image(img):
    img = Image.open(img)
    img = img.convert('L')
    st.image(img)


st.header("Color to Grayscale Converter")
st.subheader("Take a pic and make it GRAY :eyes:")

# img_src_option = st.radio(label="Select an image source:",
#                           options=["Webcam", "Upload"],
#                           key="img_src")
img_src_option = st.selectbox(label="Select an image source:",
                              options=["Select...",
                                       "Webcam",
                                       "Upload"],
                              index=0,
                              key="img_src")

if img_src_option == "Webcam":
    with st.expander("Start camera"):
        user_image = st.camera_input("Camera")
        if user_image:
            render_bw_image(user_image)
        # if camera_image:
        #     img = Image.open(camera_image)
        #     gray_camera_img = img.convert('L')
        #     st.image(gray_camera_img)
elif img_src_option == "Upload":
    user_image = st.file_uploader("Upload Image")
    if user_image:
        render_bw_image(user_image)

    # if uploaded_image:
    #     img = Image.open(uploaded_image)
    #     gray_camera_img = img.convert('L')
    #     st.image(gray_camera_img)

