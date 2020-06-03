import os, sys
import numpy as np
import streamlit as st
from PIL import Image
import tensorflow
import tensorflow.keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

cover = Image.open("assets/cover.png")
# model = load_model("models/superscan-model.h5")
model = load_model("models/covid-19.h5")


def detect_covid19(uploaded_xray):
    img = image.img_to_array(uploaded_xray)
    img = np.expand_dims(img / 255, axis=0)
    data = np.asarray(img, dtype="int32")
    prediction = model.predict(data)
    labels = {0: "Covid", 1: "Normal"}
    label_indice = 0 if prediction[0, 0] <= 0.5 else 1
    confidence_score = prediction[0, 0] if label_indice == 1 else 1 - prediction[0, 0]
    if label_indice == 0:
        st.error(
            f" Patient Result : { labels[label_indice] } ,\n Confidence Score : { confidence_score }"
        )
    else:
        st.success(
            f" Patient Result : { labels[label_indice] } ,\n Confidence Score : { confidence_score }"
        )
    return ""


def main():
    st.image(cover, use_column_width=True)
    st.title("Covid-19 Detection via Chest X-Ray")
    st.text("by Fodé Diop")

    options = ["Detection", "About"]
    choice = st.sidebar.selectbox("Select Option", options)

    if choice == "Detection":
        image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if image_file is not None:
            # TODO: Change image size to 331 by 331 for new covid-19 model
            uploaded = image.load_img(image_file, target_size=(331, 331))
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
