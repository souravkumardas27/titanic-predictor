import streamlit as st
import pandas as pd
import pickle

# ----------------------------
# Load models and scaler
# ----------------------------
with open("models/logreg_model.pkl", "rb") as f:
    logreg = pickle.load(f)

with open("models/rf_model.pkl", "rb") as f:
    rf = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("🚢 Titanic Survival Prediction App")
st.markdown("Enter passenger details below to predict survival probability using two models.")

# ----------------------------
# User Input Section
# ----------------------------
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0, max_value=100, value=25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0)
parch = st.number_input("Number of Parents/Children Aboard (Parch)", min_value=0, max_value=10, value=0)
fare = st.number_input("Passenger Fare", min_value=0.0, value=30.0)
embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

# ----------------------------
# Preprocess User Input
# ----------------------------
sex = 1 if sex == "female" else 0

# Create dummy columns for Embarked (remember: drop_first=True during training)
# So model expects only Embarked_Q and Embarked_S (Embarked_C was dropped)
embarked_Q = 1 if embarked == "Q" else 0
embarked_S = 1 if embarked == "S" else 0

# Combine into DataFrame (exact same order as training columns)
features = pd.DataFrame({
    "PassengerId": [0],  # Placeholder, not used in prediction
    "Pclass": [pclass],
    "Sex": [sex],
    "Age": [age],
    "SibSp": [sibsp],
    "Parch": [parch],
    "Fare": [fare],
    "Embarked_Q": [embarked_Q],
    "Embarked_S": [embarked_S]
})

# ----------------------------
# Scale Features
# ----------------------------
scaled_features = scaler.transform(features)

# ----------------------------
# Predictions
# ----------------------------
logreg_pred = logreg.predict(scaled_features)[0]
rf_pred = rf.predict(scaled_features)[0]

logreg_prob = logreg.predict_proba(scaled_features)[0][1]
rf_prob = rf.predict_proba(scaled_features)[0][1]

# ----------------------------
# Display Results
# ----------------------------
st.subheader("Prediction Results:")
st.write(f"**Logistic Regression Model:** {'🟢 Survived' if logreg_pred == 1 else '🔴 Did Not Survive'} (Probability: {logreg_prob:.2f})")
st.write(f"**Random Forest Model:** {'🟢 Survived' if rf_pred == 1 else '🔴 Did Not Survive'} (Probability: {rf_prob:.2f})")

# ----------------------------
# Combined Insight
# ----------------------------
avg_prob = (logreg_prob + rf_prob) / 2
st.markdown("---")
st.subheader("Overall Survival Likelihood (Average of Both Models):")
st.progress(avg_prob)
st.write(f"**Estimated Survival Probability:** {avg_prob:.2%}")
st.markdown("Thank you for using the Titanic Survival Prediction App! 🚢")