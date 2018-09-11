from win32com.shell import shell, shellcon
from PyQt5.QtWidgets import *
import sys
import re

def selectFolder(src):
    win = QWidget()
    filepath = str(QFileDialog.getExistingDirectory(win, "Select Folder"))
    repath = filepath.replace('/','\\',20)
    copyFile(src,repath)
    #shutil.copy(source, destiny) #both in complete path string

def copyFile(src, dst):
    shell.SHFileOperation(
        (0, shellcon.FO_COPY, src,
         dst, 0, None, None)
    )

    sys.exit(app.exec_())

    #shutil.copy(source,destiny) #bothin complete path string



from sklearn.externals import joblib
import os
from sklearn.feature_extraction.text import  CountVectorizer

import time

cv_vocab = joblib.load('E:\Project\Python\Scikit MLT\Vocabs.txt')
vect = CountVectorizer(vocabulary=cv_vocab)
t1 = time.time()
# load the model from disk
filename = 'E:\Project\Python\Scikit MLT\\finalized_model.sav'
loaded_model = joblib.load(filename)

curfile = sys.argv[1]

p1,p2 = os.path.split(curfile)


if re.search(r'\d*_n', p2):
    p2 = 'fb_img.jpg'
elif re.search(r'DSC_\d\d\d\d', p2):
    p2 = 'NikonD1.jpg'
elif re.search(r'DSCN\d\d\d\d', p2):
    p2 = 'NikCoolpix.jpg'
elif re.search(r'SBCS_\d\d\d\d', p2):
    p2 = 'CanonEOS.jpg'
elif re.search(r'IMG_\d\d\d\d', p2):
    p2 = 'CanonG2.jpg'
elif re.search(r'Screenshot*', p2):
    p2 = 'ScreenShots'
elif re.search(r'_SCN\d\d\d\d', p2):
    p2 = 'Cam1.jpg'

# print p2
X_test = [p2]
X_test_dtm = vect.transform(X_test)
test_array= X_test_dtm.toarray()
result = loaded_model.predict(test_array)
dirval = int(result[0])
# print type(dirval)
# print '\nSuccess: Fitted'
# print result
dirdicindx = joblib.load('E:\Project\Python\Scikit MLT\index.txt')
resLoc = dirdicindx[dirval]
# print resLoc
t2=time.time()
# print t2-t1




app = QApplication(sys.argv)


screen  = QWidget()

#title and window size is set
screen.setWindowTitle("SmartCopy")
screen.setMaximumWidth(400)
screen.setMaximumHeight(300)
screen.setMinimumWidth(400)
screen.setMinimumHeight(300)
screen.resize(400,300)

#setting Grid Layout
layout = QGridLayout()
screen.setLayout(layout)

#drop_down option code
D_down = QComboBox()
D_down.insertItem(1, resLoc)
D_down.insertItem(2, 'Location 2')
layout.addWidget(D_down,2,0)


#Copy button code
C_button = QPushButton('Copy')
layout.addWidget(C_button, 2, 1)
C_button.clicked[bool].connect(lambda : copyFile(curfile,resLoc))

#BrowseButton
B_button = QPushButton('Browse')
layout.addWidget(B_button, 4, 1)
B_button.clicked[bool].connect(lambda : selectFolder(curfile))

#B_button.clicked(app, False)
screen.show()

sys.exit(app.exec_())

