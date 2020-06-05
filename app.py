# -*- coding: utf-8 -*-
import os
from flask_cors import CORS, cross_origin
from flask import Flask, request
import pandas as pd
import json


import unirest


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
API_URL = 'apidojo-yahoo-finance-v1.p.rapidapi.com'
API_KEY = 'dda2e60a90mshc1e20a3757953eap1af18bjsn242463ad19df'
response = unirest.post(API_URL,
  headers={
    "X-RapidAPI-Key": API_KEY,
    "Content-Type": "stock/v2/get-historical-data"
  },
  params={
    "period1": "1546448400",
    "period2": "1562086800",
    "symbol": "AMAR3"


  }
)
@app.route("/", methods=['GET'])
def index():
    return 'Seja bem vindo ao TATIKA!!!'

@app.route('/up-csv/<acao>/<abertura>', methods=['GET'])
@cross_origin()
def upload_csv(acao, abertura):
    


    df = pd.read_csv(acao+'.csv', decimal=',')
    df['UP'] = (df['MÁXIMO'] - df['ABERTURA'])*100/df['ABERTURA']
    df['DOWN'] = (df['ABERTURA'] - df['MÍNIMO'])*100/df['ABERTURA']
    ABERTURA = float(abertura)
    
    ordem_v = ('{"ordem": "venda",')+('"75%": "R${}",'.format((ABERTURA*(1 + df.describe()['UP']['25%']/100)).round(2)))+('"50%": "R${}",'.format((ABERTURA*(1 + df.describe()['UP']['50%']/100)).round(2)))+('"25%": "R${}"'.format((ABERTURA*(1 + df.describe()['UP']['75%']/100)).round(2)))+"}"
    ordem_c = ('{"ordem": "compra",')+('"75%": "R${}",'.format((ABERTURA*(1 - df.describe()['DOWN']['25%']/100)).round(2)))+('"50%": "R${}",'.format((ABERTURA*(1 - df.describe()['DOWN']['50%']/100)).round(2)))+('"25%": "R${}"'.format((ABERTURA*(1 - df.describe()['DOWN']['75%']/100)).round(2)))+"}"
    compra = df.describe()['DOWN'].to_json() 
    venda = df.describe()['UP'].to_json()
    json = '['+ordem_c+','+compra+','+ordem_v+','+venda+']'
    
    return json

    




def main():
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)
if __name__ == "__main__":
    main() 

