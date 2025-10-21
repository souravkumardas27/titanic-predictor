# 📊 Data Directory

This directory contains the Titanic dataset and processed data files for the survival prediction project.

## 📁 Directory Structure

```
data/
├── raw/                    # Original dataset files
│   ├── train.csv          # Training data (891 passengers)
│   └── test.csv           # Test data (418 passengers)
└── processed/             # Cleaned and processed data
    ├── titanic_clean.csv  # Cleaned training data
    ├── titanic_test_clean.csv # Cleaned test data
    ├── titanic_submission_logreg.csv # Logistic Regression predictions
    └── titanic_submission_rf.csv     # Random Forest predictions
```

## 🔽 How to Get the Data

### Option 1: Download from Kaggle (Recommended)

1. **Create a Kaggle account** (if you don't have one)
   - Go to [kaggle.com](https://www.kaggle.com)
   - Sign up for a free account

2. **Download the dataset**
   - Visit the [Titanic Competition Data page](https://www.kaggle.com/c/titanic/data)
   - Click "Download All" or download individual files
   - Extract the zip file

3. **Place files in correct location**
   ```bash
   # Copy the files to the data/raw/ directory
   cp train.csv data/raw/
   cp test.csv data/raw/
   ```

### Option 2: Using Kaggle API

1. **Install Kaggle API**
   ```bash
   pip install kaggle
   ```

2. **Set up API credentials**
   - Go to your Kaggle account settings
   - Create a new API token
   - Place `kaggle.json` in `~/.kaggle/` (or `C:\Users\YourUsername\.kaggle\` on Windows)

3. **Download the dataset**
   ```bash
   kaggle competitions download -c titanic
   unzip titanic.zip
   mv train.csv data/raw/
   mv test.csv data/raw/
   ```

## 📋 Dataset Information

### Training Data (`train.csv`)
- **Size**: 891 passengers
- **Features**: 12 columns
- **Target**: Survived (0 = No, 1 = Yes)

### Test Data (`test.csv`)
- **Size**: 418 passengers
- **Features**: 11 columns (no Survived column)
- **Purpose**: Final predictions for submission

### Column Descriptions
- `PassengerId`: Unique passenger identifier
- `Survived`: Target variable (0 = No, 1 = Yes)
- `Pclass`: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
- `Name`: Passenger name
- `Sex`: Gender (male/female)
- `Age`: Age in years
- `SibSp`: Number of siblings/spouses aboard
- `Parch`: Number of parents/children aboard
- `Ticket`: Ticket number
- `Fare`: Passenger fare
- `Cabin`: Cabin number
- `Embarked`: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

## 🔄 Data Processing

The raw data goes through several preprocessing steps:

1. **Missing Value Handling**
   - Age: Filled with median age
   - Fare: Filled with median fare
   - Embarked: Filled with mode

2. **Feature Engineering**
   - Sex: Converted to binary (0 = male, 1 = female)
   - Embarked: One-hot encoded (dummy variables)
   - Removed: Name, Ticket, Cabin (non-predictive)

3. **Output Files**
   - `titanic_clean.csv`: Processed training data
   - `titanic_test_clean.csv`: Processed test data
   - `titanic_submission_*.csv`: Model predictions

## ⚠️ Important Notes

- **Data Privacy**: Raw data files are in `.gitignore` and won't be pushed to GitHub
- **File Size**: The dataset is small (~100KB) and safe to download
- **License**: Data is publicly available for educational purposes
- **Updates**: Processed files are generated automatically when running the notebooks

## 🚨 Troubleshooting

### Common Issues

1. **"File not found" errors**
   - Ensure `train.csv` and `test.csv` are in `data/raw/`
   - Check file names are exactly `train.csv` and `test.csv`

2. **Permission errors**
   - Make sure you have write permissions in the project directory
   - Try running as administrator if on Windows

3. **Kaggle download issues**
   - Verify your Kaggle account is set up correctly
   - Check your internet connection
   - Ensure you're logged into Kaggle

### Getting Help

If you encounter issues:
1. Check the main [README.md](../README.md) for setup instructions
2. Open an issue on GitHub
3. Contact the project maintainer

---

📝 **Note**: This data directory is automatically ignored by Git to protect your data privacy. The processed files will be generated when you run the analysis notebooks.
