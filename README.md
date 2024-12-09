
# Real Estate Price Prediction  
**Course**: AIDI 1003-01  
**Team Members**:  
- **Satish Kumar** (200574904)  
- **Dhyan Trivedi** (200565531)  
- **Anmol Toor** (200578497)  
- **Harsh Patel** (200575814)  

---

## Overview  
This project predicts real estate prices based on various property features using the **House Prices: Advanced Regression Techniques Dataset** from Kaggle. The dataset contains 81 attributes, providing detailed property characteristics that influence housing prices, such as neighborhood, lot size, and overall quality.  

Our approach involves **data preprocessing, feature selection, model development, and evaluation** to construct an accurate machine learning model for predicting sale prices.

---

## Objective  
To develop a robust regression model capable of predicting real estate prices accurately and provide insights into the factors driving price variations.

### Key Outcomes  
- A well-performing model for real estate price prediction.  
- Visualizations highlighting the most influential property features.  
- Deployment-ready code for practical usage via APIs.  

---

## Project Workflow  

### 1. **Data Preparation**  
- Handled missing values, duplicate entries, and data normalization.  
- Encoded categorical variables (One-Hot Encoding for multi-class and Label Encoding for binary categories).  

### 2. **Exploratory Data Analysis (EDA)**  
- Visualized feature distributions, correlations, and outliers using histograms, box plots, and heatmaps.  
- Conducted scatter plots to analyze relationships between features and the target variable (`SalePrice`).  

### 3. **Feature Engineering**  
- Selected key features using statistical techniques and correlation matrices.  
- Dropped redundant or low-impact features for better model performance.

### 4. **Model Training**  
Implemented multiple regression models:  
- **Linear Regression**  
- **Random Forest Regressor**  
- **XGBoost**  
- **Gradient Boosting**  

Used **GridSearchCV** for hyperparameter tuning to optimize model accuracy.

### 5. **Model Evaluation**  
Evaluated models using:  
- **Mean Absolute Error (MAE)**  
- **Mean Squared Error (MSE)**  
- **R² Score**  

### 6. **Model Deployment**  
Developed a RESTful API using Flask to predict house prices based on user-provided property features.

---

## Files and Directory Structure  

```plaintext  
Real_Estate_Price_Prediction/  
├── data/  
│   ├── train.csv          # Training dataset  
│   ├── test.csv           # Testing dataset  
│   ├── data_description.txt  # Detailed feature descriptions  
├── notebooks/  
│   ├── eda.ipynb           # EDA and feature exploration  
│   ├── model_training.ipynb # Training and hyperparameter tuning  
├── src/  
│   ├── preprocess.py      # Data preprocessing scripts  
│   ├── train_model.py     # Model training and saving  
│   ├── app.py             # Flask app for deployment  
├── reports/  
│   ├── proposal.pdf       # Initial project proposal  
│   ├── final_report.pdf   # Final report summarizing findings  
├── README.md              # Project documentation (this file)  
└── requirements.txt       # Dependencies  
```  

---

## Results  

### Final Model Performance  
- **Best Model**: Random Forest Regressor  
- **Metrics**:  
  - R² Score: 0.91  
  - Mean Squared Error: 12,300  

### Key Findings  
- Features such as **Overall Quality**, **GrLivArea**, and **Garage Area** had the strongest correlation with sale prices.  
- Advanced ensemble models like Random Forest and XGBoost significantly outperformed Linear Regression.  

---

## How to Run  

### Prerequisites  
Ensure the following dependencies are installed:  
```bash  
pip install -r requirements.txt  
```  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone <repository-link>  
   cd Real_Estate_Price_Prediction  
   ```  

2. Preprocess the data:  
   ```bash  
   python src/preprocess.py  
   ```  

3. Train the model:  
   ```bash  
   python src/train_model.py  
   ```  

4. Run the Flask app:  
   ```bash  
   python src/app.py  
   ```  

5. Access the API via `http://127.0.0.1:5000`.  

---

## Future Improvements  
- Incorporate external datasets for additional features, e.g., proximity to amenities.  
- Explore deep learning models for improved accuracy.  
- Enhance API with interactive front-end visualizations.  

---

## Acknowledgments  
- **Dataset**: [Kaggle - House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)  
- Georgian College for project support and guidance.  

---
