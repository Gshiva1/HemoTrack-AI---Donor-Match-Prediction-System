
AI-Powered Donor Prediction System

🎯 Objective:  
A hybrid AI system that predicts potential donors using rule-based logic and a Random Forest classifier, wrapped in an intuitive Streamlit dashboard. This project was built as part of the AI Hackathon for Good initiative.

---

#📊 Key Features

- 🔎 Rule-based donor eligibility matching
- 🌲 Random Forest classifier for prediction
- 🧪 SMOTE balancing to handle class imbalance
- 📂 Upload CSVs and get real-time predictions
- 📉 Accuracy, precision, recall & F1-score reports
- 🖥️ Interactive frontend using Streamlit


#📁 Repository Structure

| File / Folder                     | Description |
|----------------------------------|-------------|
| `app.py`                         | Main Streamlit application file |
| `donor_dataset_with_match.csv`   | Cleaned dataset used for training |
| `donor_match_model.pkl`          | Trained Random Forest model |
| `requirements.txt`               | Python libraries required |
| `README.md`                      | Project overview and instructions |

---

#Getting Started

# Installation

1. Clone the repository:
   git clone https://github.com/your-username/ai-donor-predictor.gitcd ai-donor-predictor

2. Install dependencies:
   
   pip install -r requirements.txt

3. Run the app:
   streamlit run app.py
  

---

## 🌐 Live Demo (Optional)

Deployed on Streamlit Cloud:  
🔗 [View App](https://your-streamlit-app-url)  
> Replace this URL with your deployed app's link.

---

## ⚙️ Tech Stack

- Python 3.10+
- Pandas & NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Faker – for synthetic data generation
- Streamlit – for dashboard interface

---

## 📈 Model Performance (on Test Data)

| Metric     | Score  |
|------------|--------|
| Accuracy   | ~97%   |
| Precision  | High   |
| Recall     | Balanced with SMOTE |
| F1-Score   | Strong for both classes |



## 🤝 Acknowledgments

Developed for AI Hackathon for Good.  
Inspired by real-world donor outreach challenges and optimized using intelligent automation.
