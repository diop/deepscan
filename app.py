import os, sys
import numpy as np
import streamlit as st
from PIL import Image

cover = Image.open("assets/cover.png")


@st.cache
def load_image(img):
    im = Image.open(img)
    return im


def detect_covid19(uploaded_xray):
    return uploaded_xray


def main():
    st.image(cover, use_column_width=True)
    st.title("Covid-19 Detection via Chest X-Ray")
    st.text("by Fodé Diop")

    options = ["Detection", "About"]
    choice = st.sidebar.selectbox("Select Option", options)

    if choice == "Detection":
        image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

        if image_file is not None:
            uploaded = Image.open(image_file)
            st.text("Uploaded Chest X-Ray")

        if st.button("Detect Covid-19"):
            # result_img = detect_covid19(uploaded)
            st.image(uploaded)

            st.success(f"Successfuly Processed X-Ray Image")

    elif choice == "About":
        st.subheader("About Superscan")
        st.markdown("Built with Streamlit by [Fodé Diop](https://www.github.com/diop)")
        st.text("© Copyright 2020 Fodé Diop - MIT License")
        st.success("Dakar Institute of technology")


if __name__ == "__main__":
    main()
