from cgi import test
import pandas as pd
import warnings
import numpy as np
warnings.filterwarnings('ignore')
import joblib
model=joblib.load('testfile.pkl')

f=open('FeedingDashboarddata.csv','r')

frame=pd.read_csv(f)
frame=frame.drop(['encounterId','referral'],axis=1)

print("NaN's: \n",frame.isna().sum())

print("Totals: \n",frame.count())

print(frame.isnull().sum()/len(frame)*100)

print(len(frame))

frame=frame.dropna(axis=0,thresh=7)

print(frame.isnull().sum()/len(frame)*100)

print("Totals: \n",frame.count())

print(len(frame))

