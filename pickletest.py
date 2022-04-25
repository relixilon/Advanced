from cgi import test
import pandas as pd
import warnings
import numpy as np
warnings.filterwarnings('ignore')
import joblib
model=joblib.load('testfile.pkl')

f=open('FeedingDashboarddata.csv','r')

testarray=np.array([[4.18200000e+03,7.77102273e+00,1.00000000e+03,4.07864734e+01,
 2.61083333e+01,240, 1.04027778e+00, 4.85555556e+00, 5.01388889e+00,
 1.42857143e+01, 3.00000000e+00, 0.00000000e+00, 3.24603175e+02,
 4.25444444e+02, 5.79624584e+00, 0.00000000e+00, 4.72222222e+01]])

frame=pd.read_csv(f)
print(frame['referral'].sum())
print(len(frame))
def processsingle(array):
	columns=['encounterId','end_tidal_co2','feed_vol','feed_vol_adm','fio2','fio2_ratio','insp_time','oxygen_flow_rate','peep','pip','resp_rate','sip','tidal_vol','tidal_vol_actual','tidal_vol_kg','tidal_vol_spon','bmi']
	array=np.array(array)
	data=pd.DataFrame(array,columns=columns)
	data=data.drop(['sip','encounterId'],axis=1)
	data=data.dropna(axis=0, thresh=7)
	print(len(data))
	if len(data)<1:
		predictions="Not enough Data"
	else:
		predictions=int(model.predict(data))
		print("Entered data: ",data)
	return predictions

print(testarray)
def processfile(CSV):
	CSV=pd.read_csv(CSV)
	topredict=CSV
	print("RECIEVED FILE:\n ",CSV)
	sip=topredict['sip']
	print("TOTAL: ",CSV['referral'].sum())
	topredict=topredict.dropna(axis=0, thresh=7)
	topredict=topredict.drop(['sip','referral'],axis=1)
	id=topredict['encounterId']
	topredict=topredict.drop(['encounterId'],axis=1)
	test=topredict
	print("TEST:\n",test)
	for feature in test.columns[test.isnull().any(axis=0)]:
		test[feature].fillna(test[feature].mean(),inplace=True)
	predictions=model.predict(test)
	topredict['referral']=predictions
	topredict.insert(10,'sip',sip)
	topredict.insert(0,'encounterId',id)
	CSV['referral']="Insufficient Data"
	new=pd.concat([topredict,CSV])
	new=new.drop_duplicates(subset='encounterId',keep='first')
	new=new.sort_values('encounterId')
	print("RETURNED FILE:\n ",new)
	new=new.to_csv('referraldata.csv',index=False)
	return new

# data=processfile(f)



print(processsingle(f))