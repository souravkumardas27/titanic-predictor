# 🚢 Titanic Survival Prediction

A machine learning project that predicts passenger survival on the Titanic using two different algorithms: **Logistic Regression** and **Random Forest**. The project includes data exploration, model training, and an interactive Streamlit web application.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://titanic-predictor57.streamlit.app)

## 📋 Table of Contents

- [Overview](#overview)
- [Live Demo](#live-demo)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Analysis](#data-analysis)
- [Model Performance](#model-performance)
- [Web Application](#web-application)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project analyzes the famous Titanic dataset to predict passenger survival using machine learning techniques. The analysis includes comprehensive exploratory data analysis (EDA) and implements two different machine learning models to compare their performance.

## 🔗 Live Demo

- Streamlit App: https://titanic-predictor57.streamlit.app

### Key Insights
- **Overall Survival Rate**: 38.38%
- **Best Performing Model**: Random Forest (83.8% accuracy)
- **Logistic Regression**: 80.4% accuracy
- **Key Factors**: Gender, passenger class, and age significantly impact survival

## ✨ Features

- 🔍 **Comprehensive EDA**: Detailed analysis of passenger demographics and survival patterns
- 🤖 **Dual Model Approach**: Logistic Regression and Random Forest classifiers
- 📊 **Data Preprocessing**: Handles missing values and categorical encoding
- 🌐 **Interactive Web App**: User-friendly Streamlit interface for predictions
- 📈 **Model Comparison**: Side-by-side performance evaluation
- 💾 **Model Persistence**: Saved models for easy deployment

## 📁 Project Structure

```
titanic-predictor/
├── 📁 app/
│   └── streamlit_app.py          # Interactive web application
├── 📁 data/
│   ├── 📁 raw/
│   │   ├── train.csv             # Original training data
│   │   └── test.csv              # Original test data
│   └── 📁 processed/
│       ├── titanic_clean.csv     # Cleaned training data
│       ├── titanic_test_clean.csv # Cleaned test data
│       ├── titanic_submission_logreg.csv # Logistic Regression predictions
│       └── titanic_submission_rf.csv     # Random Forest predictions
├── 📁 models/
│   ├── logreg_model.pkl          # Trained Logistic Regression model
│   ├── rf_model.pkl              # Trained Random Forest model
│   └── scaler.pkl                # Feature scaler
├── 📁 notebooks/
│   ├── 01_eda.ipynb              # Exploratory Data Analysis
│   └── 02_model.ipynb            # Model training and evaluation
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/souravkumardas27/titanic-predictor.git
   cd titanic-predictor
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Titanic dataset**
   - Go to [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic/data)
   - Download `train.csv` and `test.csv`
   - Place them in the `data/raw/` directory
   - **📖 Detailed instructions**: See [data/README.md](data/README.md) for complete setup guide
   - Your folder structure should look like:
     ```
     data/
     ├── raw/
     │   ├── train.csv
     │   └── test.csv
     └── processed/ (will be created automatically)
     ```

## 💻 Usage

### Running the Web Application

1. **Start the Streamlit app**
   ```bash
   streamlit run app/streamlit_app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Enter passenger details** in the web interface:
   - Passenger Class (1st, 2nd, or 3rd)
   - Gender (Male/Female)
   - Age
   - Number of siblings/spouses aboard
   - Number of parents/children aboard
   - Fare amount
   - Port of embarkation

4. **View predictions** from both models with survival probabilities

### Running the Jupyter Notebooks

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Open and run the notebooks** in order:
   - `notebooks/01_eda.ipynb` - Data exploration and visualization
   - `notebooks/02_model.ipynb` - Model training and evaluation

## 📊 Data Analysis

### Dataset Overview
- **Training Data**: 891 passengers
- **Test Data**: 418 passengers
- **Features**: 9 after preprocessing
- **Target Variable**: Survival (0 = No, 1 = Yes)

### Key Findings

#### Survival Patterns
- **Gender**: Women had significantly higher survival rates (~74%) compared to men (~19%)
- **Class**: 1st class passengers had the highest survival rate (~63%)
- **Age**: Children under 10 had higher survival rates
- **Family Size**: Moderate family size (2-4 members) showed better survival

#### Data Quality
- **Missing Values**: Handled missing age, fare, and embarked data
- **Feature Engineering**: Created dummy variables for categorical features
- **Outliers**: Identified and handled fare outliers

## 🎯 Model Performance

### Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **Logistic Regression** | 80.4% | 0.80 | 0.80 | 0.80 |
| **Random Forest** | 83.8% | 0.84 | 0.84 | 0.84 |

### Feature Importance (Random Forest)
1. **Sex** - Most important predictor
2. **Fare** - Higher fare associated with survival
3. **Age** - Younger passengers more likely to survive
4. **Pclass** - Higher class associated with survival

## 🌐 Web Application

The Streamlit application provides an intuitive interface for making predictions:

- Try it online: https://titanic-predictor57.streamlit.app

### Features
- **Real-time Predictions**: Instant results as you input data
- **Dual Model Comparison**: Side-by-side predictions from both models
- **Probability Scores**: Survival likelihood percentages
- **Visual Progress Bar**: Overall survival probability visualization
- **Responsive Design**: Works on desktop and mobile devices

### How to Use
1. Fill in the passenger information form
2. Click to generate predictions
3. Compare results from both models
4. View the combined survival probability

## 🔧 Technical Details

### Data Preprocessing
- **Missing Value Handling**: Median imputation for age, mode for embarked
- **Categorical Encoding**: One-hot encoding for embarked, binary for sex
- **Feature Scaling**: StandardScaler for logistic regression
- **Feature Selection**: Removed non-predictive columns (Name, Ticket, Cabin)

### Model Configuration
- **Logistic Regression**: Default parameters with scaled features
- **Random Forest**: 100 estimators, random_state=42
- **Train/Test Split**: 80/20 split with random_state=42

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. © 2025 Sourav Kumar Das. See the [LICENSE](LICENSE) file for full details.

## 🙏 Acknowledgments

- [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic) for the dataset
- [Streamlit](https://streamlit.io/) for the web application framework
- [Scikit-learn](https://scikit-learn.org/) for machine learning algorithms
- [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/) for data manipulation

## 👤 Author

- Name: Sourav Kumar Das
- GitHub: https://github.com/souravkumardas27

## 📞 Contact

If you have any questions or suggestions, please reach out:

- **GitHub Issues**: [Create an issue](https://github.com/souravkumardas27/titanic-predictor/issues)

---

⭐ **Star this repository** if you found it helpful!

 **Happy Predicting!** 
