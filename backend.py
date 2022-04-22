import pandas as pd
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import numpy as np
import predict

app = Flask(__name__)
#app.config['PROPAGATE_EXCEPTIONS'] = False
CORS(app)
api = Api(app)# Require a parser to parse our POST request.
parser = reqparse.RequestParser()
parser.add_argument('encounterId')
parser.add_argument('end_tidal_co2')
parser.add_argument('feed_vol')
parser.add_argument('feed_vol_adm')
parser.add_argument('fio2')
parser.add_argument('fio2_ratio')
parser.add_argument('insp_time')
parser.add_argument('oxygen_flow_rate')
parser.add_argument('peep')
parser.add_argument('pip')
parser.add_argument('resp_rate')
parser.add_argument('sip')
parser.add_argument('tidal_vol')
parser.add_argument('tidal_vol_actual')
parser.add_argument('tidal_vol_kg')
parser.add_argument('tidal_vol_spon')
parser.add_argument('bmi')

class Predict(Resource):
  def post(self):
    args = parser.parse_args()
    for i in args:
      if args[i] == '':
        args[i] = 0
    data = (
      np.array(
        [[
          float(args["encounterId"]),
          float(args["end_tidal_co2"]),
          float(args["feed_vol"]),
          float(args["feed_vol_adm"]),
          float(args["fio2"]),
          float(args["fio2_ratio"]),
          float(args["insp_time"]),
          float(args["oxygen_flow_rate"]),
          float(args["peep"]),
          float(args["pip"]),
          float(args["resp_rate"]),
          float(args["sip"]),
          float(args["tidal_vol"]),
          float(args["tidal_vol_actual"]),
          float(args["tidal_vol_kg"]),
          float(args["tidal_vol_spon"]),
          float(args["bmi"]),
        ]]
      )
    )
    print(predict.processsingle(data))
    return predict.processsingle(data)

api.add_resource(Predict, "/predict")

if __name__ == "__main__":
  app.run(debug=True)