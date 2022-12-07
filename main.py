import pandas as pd
from fastapi import FastAPI
import uvicorn
import pickle
from starlette.middleware.cors import CORSMiddleware

# Create the app
app = FastAPI()
#test

# Load trained Pipeline
#filename = "./models/model.pickle"
filename = "./models/model.pkl"
model = pickle.load(open(filename, 'rb'))

# stuff for cors
origins = [
    "*"
    "http://127.0.0.1:5500/",
    "https://localhost:5500",
    "http://localhost",
    "http://localhost:8080",
    "https://fraud-detect.web.app"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Define Homepage
@app.get('/')
def read_root():
    msg = {
        "message": "Welcome to the Credit Card Fraud Detection System API",
        "API Endpoints":"Below are two API Endpoints that you can use to predict whether a credit card transaction is fraudulent or not.",
        "First Endpoint":"for a JSON response link:https://ccfds.herokuapp.com/predict",
        "Second Endpoint":"for a STRING response link:https://ccfds.herokuapp.com/api",
        # "First Method": "for a JSON response link:http://127.0.0.1:8000/predict",
        # "Second Method": "for a TEXT response link:http://127.0.0.1:8000/api",
    }
    return msg

# Define predict function
# @app.post('/predict')
@app.get('/predict')
def predict(Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount):
    data = pd.DataFrame([[Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13,
                        V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount]])
    data.columns = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14',
                    'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']
    predictions = model.predict(data)
    return str({'prediction': list(predictions)})

@app.get("/api")
async def main(Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount):
    data = pd.DataFrame([[Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13,
                        V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount]])
    data.columns = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14',
                    'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']
    predictions = model.predict(data)
    if predictions == 0:
        return "This is a Legit Transaction"
    else:
        return "This is a Fraud Transaction"

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)