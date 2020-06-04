# -*- coding: utf-8 -*-
import os
from flask_cors import CORS, cross_origin
from flask import Flask, request
import pandas as pd
import json


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET'])
def index():
    return 'Seja bem vindo ao TATIKA!!!'

@app.route('/up-csv/<abertura>', methods=['GET'])
@cross_origin()
def upload_csv(abertura):
    


    df = pd.read_csv('AMAR3.csv', decimal=',')
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

