
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import os

st.set_page_config(
    page_title="Road Damage Detection",
    page_icon="🚧",
    layout="wide"
)

st.title("🚧 AI Road Damage Detection")
st.write("Upload a road image to detect cracks and potholes using our trained YOLOv8 model.")

@st.cache_resource
def load_model():
    return YOLO("best.pt")

try:
    model = load_model()
    st.success("AI model loaded successfully!")
except Exception as e:
    st.error(f"Could not load model: {e}")
    st.stop()

uploaded_file = st.file_uploader(
    "Upload a road image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    with st.spinner("Detecting road damage..."):
        results = model.predict(image, conf=0.25, verbose=False)

    annotated = results[0].plot()
    annotated = annotated[:, :, ::-1]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Detection Results")
        st.image(annotated, use_container_width=True)

    boxes = results[0].boxes
    st.subheader("Damage Summary")

    if boxes is not None and len(boxes) > 0:
        counts = {}
        for box in boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            counts[class_name] = counts.get(class_name, 0) + 1

        st.metric("Total damages detected", len(boxes))
        st.write(counts)
    else:
        st.info("No road damage detected in this image.")
