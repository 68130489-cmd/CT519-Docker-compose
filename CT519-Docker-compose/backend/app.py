from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI()

# สร้างข้อมูลจำลองสำหรับ train model
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

class InputData(BaseModel):
    value: float

@app.get("/")
def home():
    return {"message": "ML Backend API is running"}

@app.post("/predict")
def predict(data: InputData):
    input_value = np.array([[data.value]])
    prediction = model.predict(input_value)

    return {
        "input": data.value,
        "prediction": round(float(prediction[0]), 2)
    }
