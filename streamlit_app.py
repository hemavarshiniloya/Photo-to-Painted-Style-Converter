import streamlit as st
import numpy as np
import requests
from PIL import Image, ImageOps
import base64
import io
from streamlit_drawable_canvas import st_canvas

import streamlit as st

def main():
    st.title("Draw on the Canvas")
    
    # Create a canvas component
    canvas_result = st.canvas(
        fill_color="white",
        stroke_width=5,
        stroke_color="black",
        background_color="white",
        width=400,
        height=400,
        drawing_mode="freedraw",
        key="canvas"
    )

    # Use the canvas data (optional)
    if canvas_result:
        st.image(canvas_result.image_data)

if __name__ == "__main__":
    main()


if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
    img = Image.fromarray((canvas_result.image_data * 255).astype(np.uint8)).convert("RGB")

    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    if st.button("Submit Drawing"):
        response = requests.post("http://127.0.0.1:5000/predict", json={"image": f"data:image/png;base64,{img_str}"})
        if response.status_code == 200:
            guess = response.json().get('guess')
            st.write(f"The model guesses: {guess}")
        else:
            st.write("There was an error in the prediction process.")

