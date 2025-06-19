
# GBC Smart Waste Sorting — AgileProjectManagement

This project is a garbage classification app built as part of our AASD 4013 Agile Methodologies course. It follows Scrum practices, with collaborative sprints, version control, model training, and evaluation pipelines.

## 🚀 Project Overview

The app uses a Convolutional Neural Network (CNN) trained on the TrashNet dataset to classify garbage images into six categories: cardboard, glass, metal, paper, plastic, and trash. The goal is to simulate a real-world machine learning product lifecycle using agile workflows.

---

## 📁 Folder Structure

```
AgileProjectManagement/
├── Data/                  # Raw, processed, outputs, visualizations
│   ├── raw data/
│   ├── processed data/
│   ├── training outputs/
│   └── visualizations/
├── Models/                # Model exports (e.g., .h5, .pkl)
├── Notebooks/             # Jupyter notebooks (EDA, training, API, etc.)
├── Dashboard/             # Frontend code (e.g., Streamlit, React)
├── Utils/                 # Helper scripts (loaders, preprocessors)
```

---

## 🧠 Key Components

- `model_training.ipynb`: Trains CNN using MobileNetV2
- `eda_preprocessing.ipynb`: Resizes, normalizes, splits dataset
- `evaluation_metrics.ipynb`: Accuracy, confusion matrix, etc.
- `api_integration.ipynb`: Backend logic for model inference
- `Dashboard/`: UI for image upload and classification
- `.gitkeep`: Used in empty folders to ensure Git tracks them

---

## 🧑‍🤝‍🧑 Team Roles

- **Scrum Master**: Biraj Gautam
- **Model Team**: Samskar, Binaya, Nathan
- **Backend**: Frank
- **Frontend/UI**: Radwan
- **QA + Evaluation**: Ronak, Vivek, Amir
- **Report/Slides**: Louis
- **Data Collection**: Adin

---

## 🧪 Tech Stack

- Python, TensorFlow, Keras, Pandas
- Jupyter Notebooks
- Flask/FastAPI (backend)
- Streamlit or HTML/CSS (frontend)
- GitHub Projects / Jira (task tracking)

---

## 🗓️ Agile Workflow

- 2 Sprints completed with full Scrum cycles
- Tasks tracked using GitHub Projects
- Includes: Sprint planning, daily stand-ups, review, and retrospective
- Burndown charts and user stories available in the `/Report/` folder (to be added)

---

## 📝 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/BirajGtm/GBC-Smart-Waste-Sorting.git
   cd AgileProjectManagement
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run notebooks step by step:
   - Preprocess data
   - Train and export model
   - Run predictions via API or UI

---

## ✅ License

This project is for academic purposes only, created as part of coursework at GBC.
