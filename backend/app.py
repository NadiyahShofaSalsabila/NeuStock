from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

# ===============================
# CONFIG
# ===============================
MODEL_PATH = "model/model.h5"
SCALER_PATH = "model/scaler.pkl"
DATA_PATH = "data/price.csv"

N_FUTURE = 30
TIME_STEP = 1

# ===============================
# INIT APP
# ===============================
app = Flask(__name__)
CORS(app)

# ===============================
# LOAD MODEL & SCALER
# ===============================
model = load_model(MODEL_PATH)
scaler_y = joblib.load(SCALER_PATH)

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv(DATA_PATH)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# ===============================
# ROUTES
# ===============================
@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/api/predict")
def predict():
    last_sequence = scaler_y.transform(
        df[['Close']].values[-TIME_STEP:]
    ).reshape(1, TIME_STEP, 1)

    future_scaled = []

    for _ in range(N_FUTURE):
        pred = model.predict(last_sequence, verbose=0)
        future_scaled.append(pred[0, 0])
        last_sequence[0, -1, 0] = pred[0, 0]

    future_prices = scaler_y.inverse_transform(
        np.array(future_scaled).reshape(-1, 1)
    ).flatten()

    future_dates = pd.date_range(
        start=df.index[-1] + pd.Timedelta(days=1),
        periods=N_FUTURE
    )

    return jsonify([
        {"date": str(d.date()), "close": float(v)}
        for d, v in zip(future_dates, future_prices)
    ])

@app.route("/api/actual")
def actual():
    return jsonify([
        {"date": str(d.date()), "close": float(v)}
        for d, v in zip(df.index, df['Close'])
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
