import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

# Load the trained model
model = load_model('mnist_model.h5')

# Print input shape of the model
print("Model Input Shape:", model.input_shape)

# Load and prepare MNIST test data
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_test = X_test / 255.0
X_test = X_test.reshape(-1, 28, 28, 1)

# Evaluate model accuracy
loss, acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {acc:.4f}")
