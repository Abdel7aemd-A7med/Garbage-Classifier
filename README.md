# 🗑️ Garbage Classification Model

This project is a deep learning model designed to classify garbage into 10 distinct categories using images.  
It was developed as part of a machine learning training program at the **National Telecommunication Institute (NTI)**.  
The goal is to automate waste classification to support recycling and waste management efforts.

---

## 📂 Dataset

The dataset used for this project is publicly available on Kaggle:  
🔗 [Garbage Classification Dataset](https://www.kaggle.com/datasets/sumn2u/garbage-classification-v2)

It contains images grouped into the following 10 categories:
- Battery
- Biological
- Cardboard
- Clothes
- Glass
- Metal
- Paper
- Plastic
- Shoes
- Trash

### ⚠️ Challenges with the Dataset
- The dataset was **not originally provided in CSV format**.
- It was **not split into training and testing sets**, so we had to manually organize it.
- The dataset size was **very small**, which led to **overfitting** during initial training.
- There was **confusion between similar classes**, such as **transparent plastic vs. glass**.

### ✅ Solutions Applied
- Used **data augmentation** (flipping, rotation, zoom, etc.) to increase training data.
- Applied **fine-tuning** on pretrained models to improve class distinction.

---

## 🧠 Model

We experimented with different CNN architectures:

| Model        | Pros / Cons                              |
|--------------|-------------------------------------------|
| ResNet       | Powerful but heavy                        |
| EfficientNet | Balanced performance and size             |
| MobileNetV2  | ✅ Lightweight, ✅ Fast, ✅ High accuracy     |

### ✅ Final Choice: **MobileNetV2**
- Low number of parameters  
- High accuracy  
- Suitable for mobile/edge deployment  

---

## 🚀 How to Use

### 🔴 Live Web App
Use our demo on Hugging Face Spaces:  
👉 [Try it Live](https://huggingface.co/spaces/abdelhamed20/2)

### 🐳 Run Locally Using Docker

Once the container is running, access the app locally at:  
🔗 `http://localhost:7860/` **(only works on your machine)**

> ⚠️ `localhost` is for **local testing only** and not accessible remotely.

## 📓 Notebook
🔗 [View on Kaggle](https://www.kaggle.com/code/abdelhamedahmed2005/garbage-classification)

---

## 📹 Video Demo  
Watch how the model works:  
🎥 [Google Drive Demo](https://drive.google.com/file/d/1QI5EL0ExI8V7jYgFyjWBzCFnYRna1Kd8/view?usp=drive_link)

---

## 📊 Presentation  
Check the project presentation:  
🎞️ [View on Canva](https://www.canva.com/design/DAGvNRwc0Ek/E2qasZn5NQI6407GQfOkhg/edit)

---

## 👨‍💻 Team Members

- **Abdelhamid Ahmed**  
  [LinkedIn](https://www.linkedin.com/in/abdelhamed-ahmed-9428702a7)

- **Moaz Mohamed**  
  [LinkedIn](https://www.linkedin.com/in/moaz-mohamed-545725375)

- **Menna Hamed**  
  [LinkedIn](https://www.linkedin.com/in/mennaelsayedhamed)

- **Islam Mohamed**  
  [LinkedIn](https://www.linkedin.com/in/eslam-mohamed-ouda-57386729a)