# safety_wears_yolo
## 🦺 PPE Detection Using YOLOv8 — Project Summary

This project focuses on building a **Personal Protective Equipment (PPE) detection system** using a fine-tuned **YOLOv8n** model. The goal is to automatically detect whether workers are wearing the required safety equipment in industrial environments.

### 📌 Key Features

* Detection of **15 safety-wear classes** (helmets, vests, gloves, masks, etc.).
* Model trained using a **combined dataset** of images from several open-source PPE datasets (mainly Roboflow).
* Real-time detection supported through webcam or video streams.
* Lightweight model (**YOLOv8n**) suitable for edge devices.

### 🚀 Model Training

* Training was performed **offline on images**, not CCTV footage.
* The dataset merges annotations from different sources to create a **generalized training set**.
* The model can be significantly improved by adding **real images from the company** (same cameras, environment, lighting, workers).

### 🎥 Real-Time Inference

* The trained YOLOv8n model works with both **single images and live video**.
* A real-time demo was successfully tested using the **laptop webcam**.

### 🧩 Deployment

* The model can run on:

  * A standard computer (CPU or GPU)
  * A **Raspberry Pi** (performance improves using a **Google Coral TPU**)
* No GPU is strictly required for inference, but it boosts speed.



