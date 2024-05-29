import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Sidebar configuration options for drawing tool
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:",
    ("point", "freedraw", "line", "rect", "circle", "transform")
)

# Sidebar options for stroke width, stroke color, background color, and background image
stroke_width = st.sidebar.slider("Stroke width:", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius:", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex:")
bg_color = st.sidebar.color_picker("Background color hex:", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

# Checkbox for real-time canvas updates
realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=150,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)

# Display the canvas image if available
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)

# Display the JSON data if available
if canvas_result.json_data is not None:
    # Convert JSON data to a pandas DataFrame for easier display
    objects = pd.json_normalize(canvas_result.json_data["objects"])
    # Convert object columns to strings (PyArrow compatibility)
    for col in objects.select_dtypes(include=['object']).columns:
        objects[col] = objects[col].astype("str")
    st.dataframe(objects)
