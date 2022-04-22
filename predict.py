import joblib
from cgi import test
import pandas as pd
import predict
import warnings
import numpy as np
warnings.filterwarnings('ignore')
model = joblib.load('model.pkl')


def processsingle(array):
    columns = ['encounterId', 'end_tidal_co2', 'feed_vol', 'feed_vol_adm', 'fio2', 'fio2_ratio', 'insp_time', 'oxygen_flow_rate',
               'peep', 'pip', 'resp_rate', 'sip', 'tidal_vol', 'tidal_vol_actual', 'tidal_vol_kg', 'tidal_vol_spon', 'bmi']
    array = np.array(array)
    data = pd.DataFrame(array, columns=columns)
    data = data.drop(['sip', 'encounterId'], axis=1)
    predictions = int(model.predict(data))
    return predictions


def processfile(CSV):
    CSV = pd.read_csv(CSV)
    topredict = CSV
    print("RECIEVED FILE:\n ", CSV)
    sip = topredict['sip']
    topredict = topredict.dropna(axis=0, thresh=7)
    topredict = topredict.drop(['sip', 'referral'], axis=1)
    id = topredict['encounterId']
    topredict = topredict.drop(['encounterId'], axis=1)
    test = topredict
    print("TEST:\n", test)
    for feature in test.columns[test.isnull().any(axis=0)]:
        test[feature].fillna(test[feature].mean(), inplace=True)
    predictions = model.predict(test)
    topredict['referral'] = predictions
    topredict.insert(10, 'sip', sip)
    topredict.insert(0, 'encounterId', id)
    CSV['referral'] = "Insufficient Data"
    new = pd.concat([topredict, CSV])
    new = new.drop_duplicates(subset='encounterId', keep='first')
    new = new.sort_values('encounterId')
    print("RETURNED FILE:\n ", new)
    new = new.to_csv('referraldata.csv', index=False)
    return new

# data=processfile(f)
