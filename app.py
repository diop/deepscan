import os, sys
import numpy as np
import streamlit as st
from PIL import Image
import tensorflow
import tensorflow.keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

cover = Image.open("assets/cover.png")
model = load_model("models/superscan-model.h5")


@st.cache
def load_image(img):
    im = Image.open(img)
    return im


def detect_covid19(uploaded_xray):
    img = image.load_img(uploaded_xray, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    prediction = model.predict_classes(img)
    return prediction


def main():
    st.image(cover, use_column_width=True)
    st.title("Covid-19 Detection via Chest X-Ray")
    st.text("by Fodé Diop")

    options = ["Detection", "About"]
    choice = st.sidebar.selectbox("Select Option", options)

    if choice == "Detection":
        image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if image_file is not None:
            uploaded = Image.open(image_file)
            st.image(uploaded, caption="Uploaded Image.", use_column_width=True)

        if st.button("Detect Covid-19"):
            st.write("")
            st.write("Detecting...")
            pred = detect_covid19(uploaded)
            st.write(pred)

    elif choice == "About":
        st.subheader("About Superscan")
        st.markdown("Built with Streamlit by [Fodé Diop](https://www.github.com/diop)")
        st.text("© Copyright 2020 Fodé Diop - MIT License")
        st.success("Dakar Institute of technology")


if __name__ == "__main__":
    main()
