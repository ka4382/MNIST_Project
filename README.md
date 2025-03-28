## 🎯 MNIST Classification with Streamlit

This project implements a neural network model to classify handwritten digits from the MNIST dataset. It also provides an interactive web interface using **Streamlit** to predict digits.

---

### 🚀 **Features**
- ✅ Model trained on MNIST dataset.
- ✅ Save and load model using `mnist_model.h5`.
- ✅ Interactive UI to upload images and predict.
- ✅ Streamlit web app for user interaction.

---

### 📝 **Project Structure**
```
MNIST_Project/
├── mnist_app.py        # Streamlit app
├── mnist_model.py      # Model training and saving
├── mnist_model.h5      # Saved Keras model
├── requirements.txt    # Required dependencies
└── test_model.py       # Model testing script
```

---

### ⚡️ **Setup Instructions**
```bash
# Clone the repo
git clone https://github.com/ka4382/MNIST_Project.git

# Change directory
cd MNIST_Project

# Create virtual environment
python -m venv mnist_env

# Activate environment
# On Windows
mnist_env\Scripts\activate
# On Mac/Linux
source mnist_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run mnist_app.py
```

---

### 📸 **How It Works**
1. Upload a handwritten digit image.
2. Model predicts the digit and displays the result.

---

### 🤝 **Contributing**
Feel free to fork, improve, and submit PRs. Happy coding! 😄

---

### 📧 **Contact**
For any questions or support, reach out at:
- ✉️ Email: [aljapurkarthik@gmail.com]
- 🔗 GitHub: [ka4382](https://github.com/ka4382)

