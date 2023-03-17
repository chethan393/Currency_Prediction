import requests
import mysql.connector
import requests
import json
import datetime


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Hemanth1@",
  database="currencies"
)
# API_KEY = "KBC5QDUSDRfZytGSkQCDR3LCh5YwgR7f"

# headers = {
#    "apikey" : "KBC5QDUSDRfZytGSkQCDR3LCh5YwgR7f"
# }
# params ={
# #   "access_key" : "KBC5QDUSDRfZytGSkQCDR3LCh5YwgR7f",
#   "start_date" : "2022-01-01",
#   "end_date"  : "2022-01-30",
#   "base" : "INR",
#   "symbols" : ["AUD", "CAD", "EUR", "JPY", "NZD", "NOK", "GBP", "SEK", "CHF", "USD" ]
# }
# response = requests.get("https://api.exchangeratesapi.io/v1/timeseries?",headers = headers,  data = params).json()
# print(response


# # sql_command = """CREATE TABLE DATA (
# # staff_number INTEGER PRIMARY KEY,
# # fname VARCHAR(20),
# # lname VARCHAR(30),
# # gender CHAR(1),
# # joining DATE);"""

# # data = requests.get("")
mycursor = mydb.cursor()

start_date = datetime.date(2022,1,1)
end_date = datetime.date(2022,1,31)
symbols  = ["AUD", "CAD", "EUR", "JPY", "NZD", "NOK", "GBP", "SEK", "CHF", "USD"]
base = "INR"

headers= {
  "apikey": "KBC5QDUSDRfZytGSkQCDR3LCh5YwgR7f"
}

for symbol in symbols:
    url = f"https://api.apilayer.com/exchangerates_data/timeseries?start_date={start_date}&end_date={end_date}&base={symbol}&symbols=INR"
    response = requests.request("GET", url, headers=headers).json()

    rates = response['rates']
    rates = json.dumps(rates)
    country_name = symbol
    sql_command = "INSERT INTO currencies.currency_data values(%s, %s)"
    val = (symbol, rates)
    mycursor.execute(sql_command,val)
    mydb.commit()
    # status_code = response.status_code
    # result = response.text



    # print(result)