# 🚜 Tractor Sales Prediction

A Machine Learning project to predict **monthly tractor sales** using historical sales data.

## 🔍 Project Workflow

```text
EDA → Preprocessing → Feature Engineering
→ Linear Regression → Evaluation → Pickle → Streamlit
```

## ⚙️ Features

* Month & Year
* Time Index
* Lag features (`Lag_1`, `Lag_2`, `Lag_3`, `Lag_12`)
* Rolling averages (`3` & `6` months)

## 🤖 Model

**Linear Regression**

Evaluation metrics:

* MAE
* RMSE
* R² Score

## 🌐 Streamlit

The trained model is saved using **Pickle** and deployed through Streamlit.

```bash
streamlit run app.py
```
## 📊 Results

### Model Result

![Model Result](./tractor%20sales/img1.png)

### Streamlit Application

![Streamlit App](./tractor%20sales/img2.png)


## 🛠️ Tech Stack

`Python` • `NumPy` • `Pandas` • `Matplotlib` • `Seaborn` • `Scikit-learn` • `Pickle` • `Streamlit`

## 📁 Project Structure

```text
Tractor-Sales/
├── Tractor-Sales.csv
├── app.py
├── models_apply.ipynb
├── tractor_sales_model.pkl
├── tractor_sales_columns.pkl
├── requirements.txt
├── img1.png
├── img2.png
└── README.md
```

## 👨‍💻 Author

**Vinay Sharma**
B.Tech CSE (AI & ML)
