# 🐟 Fish Species Classification and Disease Detection using Machine Learning

This project presents an intelligent system that classifies freshwater fish species and detects common fish diseases using deep learning. Designed to assist aquaculture farmers, researchers, and enthusiasts, the system is equipped with real-time inference, a user-friendly web interface, and an alert system to notify users of potential diseases in fish.

---

## 🔍 Project Overview

* **Domain**: Artificial Intelligence (AI) in Aquaculture
* **Tech Stack**: Python, TensorFlow, Flask, HTML, CSS, JavaScript
* **Model Architecture**:

  * CNN (ResNet50) for **Fish Species Classification**
  * SSD MobileNet V2 for **Fish Disease Detection**
* **Interface**: Web-based UI with live prediction and alert support
* **Deployment**: Local machine (can be adapted for cloud or edge devices)

---

## 📌 Features

* 📷 Upload images of fish to classify species
* 🐠 Detect and label fish diseases from image input
* 📊 View confidence scores and model predictions
* ⚠️ Real-time visual and audio alerts if a disease is detected
* ↺ Responsive frontend with live image preview
* 📈 Model accuracy \~97.8% for disease classification

---

## 🧠 Machine Learning Models

### 1. Fish Species Classification

* **Model**: ResNet50 CNN
* **Input**: 224x224 RGB images
* **Output**: Predicted fish species (e.g., Rohu, Katla, Tilapia, etc.)
* **Training**: Custom dataset of freshwater fish species
* **Accuracy**: \~95.6%

### 2. Fish Disease Detection

* **Model**: SSD MobileNet V2 (Object Detection)
* **Input**: Image of infected fish
* **Output**: Detected disease with bounding box (e.g., Dropsy, Fin Rot)
* **Classes**: 7 common fish diseases
* **Accuracy**: \~97.8%

---

## 📂 Project Structure

```
project-root/
│
├── model/                  # Trained model files (.h5, .pb, etc.)
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML frontend templates
├── app.py                  # Flask backend server
├── predict.py              # Model inference logic
├── requirements.txt        # Required Python packages
└── README.md               # Project description (this file)
```

---

## 🚀 Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Mugilnsenthil/fish-disease-detection.git
cd fish-disease-detection
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Server

```bash
python app.py
```

### 5. Open in Browser

Navigate to `http://127.0.0.1:5000` to access the web interface.

---

## 📸 Sample Usage

1. Upload a clear image of a fish.
2. The system will:

   * Identify the species using the ResNet50 model.
   * Detect any visible disease using SSD MobileNet V2.
3. If a disease is detected:

   * A red alert border appears.
   * An audio alarm is triggered.
4. Results and confidence scores are displayed in the UI.

---

## 🔮 System Architecture

The system consists of the following core modules:

* **Frontend (HTML/JS)**: UI for uploading images, displaying prediction results and alerts
* **Flask Backend**: Handles API requests, processes images, loads ML models
* **ML Model**: Deep learning models for fish classification and disease detection
* **Alert System**: Audio/visual feedback when a disease is detected

---

## 📚 Module Descriptions

### 1. User Module

Users upload fish images, receive predictions, and get alerted in case of disease.

### 2. Frontend Module

React/HTML-based UI that supports image upload, preview, and displaying results.

### 3. API Module

Bridges frontend and backend, sending image data and receiving prediction results.

### 4. Backend Module

Flask server that handles requests, preprocesses images, and invokes ML models.

### 5. Model Module

Contains ResNet50 and SSD MobileNet V2 models for classification and detection.

### 6. Alert Module

Triggers visual/audio alerts for disease-detected cases.

---

## 🔧 Testing and Results

### Unit Testing

Each module was tested independently including API endpoints, image preprocessing, and frontend interactions.

### Integration Testing

Full pipeline testing ensured end-to-end functionality from upload to alert.

### Functional Testing

Tested with all 7 disease classes and healthy fish images to validate classification and alert generation.

### Cross-Platform Testing

Tested across major browsers (Chrome, Firefox, Edge) and OS (Windows, Linux).

### Final Results

* Classification Accuracy: **\~97.8%**
* Average Prediction Latency: **\~500ms**
* Alert System Reliability: **100%** for disease cases

---

## 📅 Conclusion

This system demonstrates how deep learning can enhance aquaculture through real-time monitoring of fish species and diseases. With high accuracy, real-time alerts, and a clean user interface, this project stands as a practical application of AI in fish farming. The integration of a disease detection pipeline ensures timely identification and mitigation of fish health issues, potentially reducing economic losses and improving fish welfare.

---

## 🌐 Future Work

* Add webcam/dashcam video input for continuous detection
* Expand disease classes using larger datasets
* Deploy to edge devices like Jetson Nano or Raspberry Pi
* Integrate cloud logging for fish health history
* Build a mobile app using React Native or Flutter

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Mugilan Senthil**
Artificial Intelligence and Data Science
[GitHub: Mugilnsenthil](https://github.com/Mugilnsenthil)
