# -*- coding: utf-8 -*-
import os 
from flask import Flask, request
#from flask_cors import CORS
import pandas as pd


app = Flask(__name__)
#cors = CORS(app, resource={r"/*":{"origins": "*"}})


@app.route("/", methods=['GET'])
def index():
    return 'Hello from Flask!'
@app.route("/a", methods=['GET'])
def a():
    return 'aaaaaaaaaaaaaa'

# @app.route('/up-csv', methods=['POST'])
# def upload_csv():
    
#     data = StringIO(request.data)
#     df = pd.read_csv(data, sep=",", decimal=',')
#     df['UP'] = (df['MÁXIMO'] - df['ABERTURA'])*100/df['ABERTURA']
#     df['DOWN'] = (df['ABERTURA'] - df['MÍNIMO'])*100/df['ABERTURA']
#     ABERTURA = 7.20
#     print("VENDA")
#     print("75%: {}".format((ABERTURA*(1 + df.describe()['UP']['25%']/100)).round(2)))
#     print("50%: {}".format((ABERTURA*(1 + df.describe()['UP']['50%']/100)).round(2)))
#     print("25%: {}".format((ABERTURA*(1 + df.describe()['UP']['75%']/100)).round(2)))

#     print("COMPRA")
#     print("75%: {}".format((ABERTURA*(1 - df.describe()['DOWN']['25%']/100)).round(2)))
#     print("50%: {}".format((ABERTURA*(1 - df.describe()['DOWN']['50%']/100)).round(2)))
#     print("25%: {}".format((ABERTURA*(1 - df.describe()['DOWN']['75%']/100)).round(2)))
#     return "OK"




def main():
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)
if __name__ == "__main__":
    main() 

