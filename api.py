from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
API_KEY = "KBC5QDUSDRfZytGSkQCDR3LCh5YwgR7f"


@app.get("/currency/predict")
def get_prediction(base, date):
    pass


@app.get("/currency/exchange")
def exchange_method(base, destination, amount):
    headers = {
         "apikey" : "KBC5QDUSDRfZytGSkQCDR3LCh5YwgR7f"
    }
    data = {
        "from" : base,
        "to" : destination,
        "amount" : amount
    }
    response = requests.get("https://api.apilayer.com/exchangerates_data/convert?",headers= headers, params= data).json()

    print(response['result'])
    
    return response['result']


