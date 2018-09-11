from sklearn.externals import joblib
import os
from sklearn.feature_extraction.text import  CountVectorizer

import time

cv_vocab = joblib.load('D:\My Python Projects\Main Project\Python\Scikit MLT\Vocabs.txt')
vect = CountVectorizer(vocabulary=cv_vocab)
t1 = time.time()
# load the model from disk
filename = 'D:\My Python Projects\Main Project\Python\Scikit MLT\\finalized_model.sav'
loaded_model = joblib.load(filename)

X_test = ['sacred games']
X_test_dtm = vect.transform(X_test)
test_array= X_test_dtm.toarray()
result = loaded_model.predict(test_array)
dirval = int(result[0])
print dirval
# print type(dirval)
print '\nSuccess: Fitted'
print result
dirdicindx = joblib.load('D:\My Python Projects\Main Project\Python\Scikit MLT\index.txt')
print dirdicindx[dirval]
t2=time.time()
print t2-t1
# time.sleep(700)