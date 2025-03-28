import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('mnist_model.h5')

# Title and description
st.title("MNIST Digit Classifier ✨")
st.write("Upload an image of a handwritten digit (0-9) to classify.")

# File uploader
uploaded_file = st.file_uploader("Choose a digit image...", type="png")

if uploaded_file is not None:
    # Preprocess image
    image = Image.open(uploaded_file).convert('L')
    image = image.resize((28, 28))
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape(1, 28, 28)

    # Prediction
    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction)

    # Show results
    st.image(image, caption="Uploaded Image", width=150)
    st.write(f"### 🎉 Prediction: {predicted_class}")

import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('mnist_model.h5')

# Show the model summary
model.summary()
