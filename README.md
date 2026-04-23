#Sales Forecast Prediction using MLOps

## Project Overview
This project implements an end-to-end MLOps pipeline to predict future sales revenue based on business inputs such as advertising spend, market trends, and sales pipeline strength.  

The system automates:
- Data ingestion
- Data preprocessing
- Model training and evaluation
- Model deployment
- Continuous integration and delivery (CI/CD)

This ensures scalability, consistency, and minimal manual intervention.


## Business Objective
The goal is to build an automated system that helps organizations:
- Predict future sales (weekly, monthly, quarterly)
- Improve decision-making
- Optimize marketing and supply chain strategies
- Reduce risks in sales forecasting
- Establish benchmarks for future analysis


## Features
- Machine Learning-based sales prediction
- Automated CI/CD pipeline using GitHub Actions
- Model training and evaluation
- Deployment using Streamlit on Hugging Face
- Interactive visualization of predictions
- End-to-end automation pipeline


## Tech Stack
- **Programming:** Python
- **ML Models:** Scikit-learn (Random Forest, etc.)
- **Visualization:** Matplotlib
- **Deployment:** Streamlit
- **CI/CD:** GitHub Actions
- **Model Hosting:** Hugging Face
- **Containerization:** Docker


##  Project Structure
Sales-Forecast/
│
├── .github/
│ └── workflows/
│ └── pipeline.yml # CI/CD pipeline
│
├── app.py # Streamlit application
├── best_model.pkl # Trained ML model
├── requirements.txt # Dependencies
├── README.md # Project documentation



##  Data Pipeline
1. Data is collected and registered on Hugging Face dataset space  
2. Data cleaning and preprocessing is performed  
3. Dataset is split into training and testing sets  
4. Processed data is stored and reused  



## Model Training & Evaluation
- Multiple models can be used:
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - XGBoost
- Hyperparameter tuning is performed
- Model is evaluated using performance metrics
- Best model is saved and registered



##  CI/CD Pipeline
- Automated using GitHub Actions
- Triggered on every push to the `main` branch
- Handles:
  - Dependency installation
  - Pipeline execution
  - Automation of ML workflow
- Ensures reproducibility and continuous integration



##  Deployment
- Application is deployed using **Streamlit**
- Hosted on **Hugging Face Spaces**
- Users can interactively input values and get predictions

---

##  Input Features
- Advertising Spend (₹)
- Market Trend Index (0–100)
- Sales Pipeline Strength (%)
- Region (North, South, East, West)
- Season (Q1, Q2, Q3, Q4)


##  Output
- 💰 Predicted Sales Value
- 📊 Visualization comparing inputs vs predicted sales

---

## Screenshots (Added in Notebook / Report)
- GitHub repository structure  
- GitHub Actions workflow execution  
- Streamlit application UI  
- Prediction output with graph  



##  GitHub Repository
🔗 [View Project Repository](https://github.com/neethidinesh19-pixel/Sales-Forecast)

---

## Conclusion
This project demonstrates a complete MLOps workflow integrating machine learning, automation, and deployment.  

The solution enables:
- Efficient sales forecasting  
- Automated workflows  
- Scalable deployment  
- Improved business decision-making  


##  Future Improvements
- Add real-time data ingestion  
- Use advanced models (XGBoost, Deep Learning)  
- Add API-based deployment  
- Enhance UI/UX of Streamlit app  

---

## Author
**Neethi D**  
GitHub: https://github.com/neethidinesh19-pixel
