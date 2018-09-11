import pandas as pd
import time
from sklearn.externals import joblib
# import pickle
t1=time.time()
# path = 'D:\My Python Projects\Main Project\Python\Scikit MLT\dir.tsv'
path = 'D:\My Python Projects\Symptoms Checker\olla.tsv'

print path


dirData = pd.read_table(path, header=None, names=['Label', 'Group'])
print(dirData)

X_train = dirData.Label
y_train = dirData.Group
X_test = ['Abort']

from sklearn.feature_extraction.text import  CountVectorizer
vect = CountVectorizer()
X_train_dtm = vect.fit_transform(X_train)
print '\nSuccess: Document Term Matrix Created'
dump = pd.DataFrame(X_train_dtm.toarray(), columns= vect.get_feature_names())
nofeats = X_train_dtm.shape
# cutoff = float(nofeats[0])
cutoff = float(1.0/nofeats[0])
print "cutoff",cutoff
feat_list = vect.get_feature_names()
ref_feats = []
for col in feat_list:
    # print dump[col].mean(), col
    if dump[col].mean() > cutoff:    #0006
        ref_feats.append(col)
# print len(feat_list)
# print len(ref_feats)
#
# with open ('Vocabs.txt', 'w') as vocfile:
#     print 'ol'
#     json.dump(feat_list,vocfile,ensure_ascii=False)

joblib.dump(ref_feats,'Vocabs.txt')

vect = CountVectorizer(vocabulary=ref_feats)
X_train_dtm = vect.fit_transform(X_train)
X_test_dtm = vect.transform(X_test)
#
# dumpFile = pd.DataFrame(X_train_dtm.toarray(), columns= vect.get_feature_names())
# dumpFile.to_csv('E:\Project\Python\Scikit MLT\Dump.csv')
# print("\nDump Complete!")
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.externals import joblib

test_array= X_test_dtm.toarray()
# print od
MLmodel = OneVsRestClassifier(SGDClassifier(alpha=0.0001)).fit(X_train_dtm, y_train)
# save the model to disk
filename = 'finalized_model.sav'
joblib.dump(MLmodel, filename)

result = MLmodel.predict(test_array)
dirval = result[0]
print '\nSuccess: Fitted'
# print type(MLmodel)
t2 = time.time()
print t2-t1
print result

# dirdicindx = joblib.load('index.txt')
# print dirdicindx[dirval]