# Detection of CAN Attacks Using Machine Learning

This project provides a **Machine Learning**-based solution for detecting attacks targeting the **CAN (Controller Area Network)** protocol used in autonomous vehicles. The application includes an interactive web interface to simulate attacks and predict their occurrence in real-time.

## 🚀 Features

- **Simulation of CAN attacks**: DoS, Fuzzy, and Impersonation.
- **Real-time prediction** powered by a Machine Learning model.
- **User-friendly interface** built with HTML, CSS, and JavaScript.
- **Flask backend** to integrate the prediction model.

## 🛠️ Project Structure

### 1. Machine Learning Models
Implemented models include:
- **Decision Tree**
- Random Forest
- SVM
- k-NN
- Naive Bayes
- Gradient Boosting
- Logistic Regression

**Best performing model**: Decision Tree.

### 2. Web Interface
- **Frontend**: HTML, CSS, JavaScript.
- **Simulation**: Form to submit CAN attack data.
- **Results**: Real-time prediction display.

### 3. Flask Backend
- Handles user requests.
- Integrates the pre-trained model for attack detection.

## 📦 Installation

### Prerequisites
- Python 3.8+
- Flask
- Pandas, NumPy, Scikit-learn, Matplotlib
- Joblib (for loading models)
- A modern web browser