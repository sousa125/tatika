# -*- coding: utf-8 -*-
import os
from flask_cors import CORS, cross_origin
from flask import Flask, request
import pandas as pd
import json
import yfinance as yf

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route("/", methods=['GET'])
def index():
    return 'Seja bem vindo ao TATIKA!!!'

@app.route('/up-csv/<acao>/<abertura>', methods=['GET'])
@cross_origin()
def get_history(acao, abertura):
    if acao.tail(3)!= '.SA':
        acao = acao+'.SA'
    symbol = yf.Ticker(acao)
    df = symbol.history("3mo")# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    df.drop(df.tail(1).index,inplace=True) 
    df['up'] = (df['High'] - df['Open'])*100/df['Open']
    df['down'] = (df['Open'] - df['Low'])*100/df['Open']
    ABERTURA = float(abertura)
    
    ordem_v = ('{"ordem": "venda",')+('"75%": "R${}",'.format((ABERTURA*(1 + df.describe()['up']['25%']/100)).round(2)))+('"50%": "R${}",'.format((ABERTURA*(1 + df.describe()['up']['50%']/100)).round(2)))+('"25%": "R${}"'.format((ABERTURA*(1 + df.describe()['up']['75%']/100)).round(2)))+"}"
    ordem_c = ('{"ordem": "compra",')+('"75%": "R${}",'.format((ABERTURA*(1 - df.describe()['down']['25%']/100)).round(2)))+('"50%": "R${}",'.format((ABERTURA*(1 - df.describe()['down']['50%']/100)).round(2)))+('"25%": "R${}"'.format((ABERTURA*(1 - df.describe()['down']['75%']/100)).round(2)))+"}"
    compra = df.describe()['down'].to_json() 
    venda = df.describe()['up'].to_json()
    json = '['+ordem_c+','+compra+','+ordem_v+','+venda+']'
    
    return json
def main():
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)
if __name__ == "__main__":
    main() 

