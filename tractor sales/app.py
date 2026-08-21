import streamlit as st
import pandas as pd
import pickle


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Tractor Sales Prediction",
    page_icon="🚜",
    layout="wide"
)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():

    with open("tractor_sales_model.pkl", "rb") as file:
        model = pickle.load(file)

    return model


@st.cache_resource
def load_columns():

    with open("tractor_sales_columns.pkl", "rb") as file:
        columns = pickle.load(file)

    return columns


model = load_model()
columns = load_columns()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🚜 Tractor Sales Prediction")

st.write(
    "Machine Learning application for predicting "
    "monthly tractor sales."
)

st.divider()


# --------------------------------------------------
# INPUT
# --------------------------------------------------

st.subheader("Enter Prediction Information")

col1, col2 = st.columns(2)


with col1:

    year = st.number_input(
        "Year",
        min_value=2003,
        max_value=2050,
        value=2026
    )

    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=1
    )

    lag_1 = st.number_input(
        "Previous Month Sales",
        min_value=0.0,
        value=200.0
    )

    lag_2 = st.number_input(
        "Sales 2 Months Ago",
        min_value=0.0,
        value=200.0
    )

    lag_3 = st.number_input(
        "Sales 3 Months Ago",
        min_value=0.0,
        value=200.0
    )


with col2:

    lag_12 = st.number_input(
        "Sales 12 Months Ago",
        min_value=0.0,
        value=200.0
    )

    rolling_3 = st.number_input(
        "3 Month Rolling Average",
        min_value=0.0,
        value=200.0
    )

    rolling_6 = st.number_input(
        "6 Month Rolling Average",
        min_value=0.0,
        value=200.0
    )


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if st.button("🔮 Predict Tractor Sales"):

    # Calculate time index
    time_index = (year - 2003) * 12 + (month - 1)

    # Create input dataframe
    input_data = pd.DataFrame({
        "Month_Number": [month],
        "Year_Number": [year],
        "Time_Index": [time_index],
        "Lag_1": [lag_1],
        "Lag_2": [lag_2],
        "Lag_3": [lag_3],
        "Lag_12": [lag_12],
        "Rolling_Mean_3": [rolling_3],
        "Rolling_Mean_6": [rolling_6]
    })

    # Ensure same feature order
    input_data = input_data[columns]

    # Prediction
    prediction = model.predict(input_data)[0]

    # Sales cannot be negative
    prediction = max(0, prediction)


    # --------------------------------------------------
    # RESULT
    # --------------------------------------------------

    st.divider()

    st.subheader("Prediction Result")

    st.metric(
        "Predicted Tractor Sales",
        f"{prediction:,.0f}"
    )

    st.success(
        f"Estimated tractor sales: {prediction:,.0f}"
    )