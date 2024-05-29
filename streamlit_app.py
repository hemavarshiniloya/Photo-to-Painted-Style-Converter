import streamlit as st
import numpy as np
from PIL import Image
import base64
import io

st.title("Guess the Drawing")

# Create a canvas component
canvas_result = st.image(
    np.ones((400, 400, 3), dtype=np.uint8) * 255,  # Initialize with a white canvas
    caption="Draw Here",
    use_column_width=True,
    channels="RGB"
)

if canvas_result is not None:
    st.image(canvas_result.image_data)
    img = Image.fromarray((canvas_result.image_data * 255).astype(np.uint8)).convert("RGB")

    if st.button("Submit Drawing"):
        # Convert the image to PNG format
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        # Perform actions based on the drawing
        # For example, you can make a request to a backend server for predictions
