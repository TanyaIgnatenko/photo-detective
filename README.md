# 🧠 Photo Modifications Detection (CNN-based Image Forgery Detection)

The goal of this project is to **detect image insertions and tampering** using **Convolutional Neural Networks (CNNs)** and **automated object-level forgery generation**.  
It automatically identifies whether an image has been digitally modified by detecting **content-level inconsistencies**.

🏆 **Winner of the ISSC-2018 Conference Competition (1st Place)**  
📘 [Research Paper / Publication](https://e-lib.nsu.ru/reader/bookView.html?params=UmVzb3VyY2UtMzg2OQ/cGFnZTAwMDAwMA)  
🖥️ [Live Demo](https://photo-detective-front-3opm.vercel.app/) | [Frontend Code](https://github.com/TanyaIgnatenko/photo-detective-front)  
📄 [Project Presentation (PDF)](https://github.com/TanyaIgnatenko/photo-detective/blob/main/Presentation.pdf)

---

## 🚀 Overview

This project explores **AI-based digital image forensics** — detecting manipulated or forged images through machine learning.  
A **custom CNN model** was trained to classify whether an photo is *original* or *tampered* by learning visual patterns introduced during the application of the insertion modification

To improve realism and robustness, I built a **data automation pipeline** that generates synthetic image forgeries using **segmentation-based object insertion**.

---

## 🔍 Approach

- 🧩 **Automated Forgery Generation:**  
  Developed a Python script that **detects meaningful objects** in source images using **SLIC segmentation** and **K-Means clustering** on **Gabor texture features**, then inserts them into target images to simulate realistic tampering.  

- 🧠 **Feature Extraction and Learning:**  
  A custom **CNN architecture** was trained on a **balanced dataset** of authentic and forged images.  
  The network learns spatial and texture inconsistencies that often arise during digital edits.  

- 📊 **Evaluation Metrics:**  
  Measured using **Accuracy, Precision, Recall, F1-score**, and **ROC-AUC**.  
  Achieved ≈ **84.3% accuracy** on a test set of 1000 photos.

---

## ⚙️ Key Features

- 🔁 Automated **image modification generator** using segmentation + clustering  
- 📸 Detects **insertion forgeries** at pixel and region level  
- 🧮 Custom **CNN architecture** with convolutional + dense layers  
- ⚙️ Applied Error Level Analysis (ELA) as a preprocessing step — the resulting ELA images were used as input to the CNN to emphasize compression and tampering artifacts.
- 🧰 Built with **Python, TensorFlow/Keras, OpenCV**  
- 📈 Visualizations for training metrics 
- 🐳 Implemented and deployed backend REST API using Flask, Python  + React frontend
---

## 🧪 Model Performance

| Metric | Value |
|:-------|:------|
| Accuracy | 84.3% |

---

## 🧰 Tech Stack

- **Python**
- **TensorFlow / Keras**
- **OpenCV**
- **Flask, React deployed on Vercel**

---

## 🧩 Example Workflow

1. **Source and target images** are selected automatically.  
2. **Segmentation (SLIC + K-Means)** detects object-like regions.  
3. A **selected object** is inserted into a new image (simulating tampering).  
4. Images are labeled and passed into the **CNN classifier**.  
5. Model outputs **probability of manipulation**.  

---

## 🎓 Author

**Tatyana Ignatenko**  
AI Engineer in Computer Vision and NLP  
🔗 [LinkedIn](www.linkedin.com/in/tatyana-ignatenko) • [GitHub](https://github.com/TanyaIgnatenko)

---

## 🏁 Summary

> This project combines **deep learning**, **computer vision**, and **data automation** to detect image tampering.  
> By generating synthetic forgeries through object insertion, it demonstrates how **AI can support digital forensics and authenticity verification** — a topic increasingly relevant in finance, media, and cybersecurity.
