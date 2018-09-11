import os
import sys
import hashlib
from win32com.shell import shell,shellcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *




class Mode(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('ADAPT')
        self.setWindowIcon(QIcon('logo.png'))
        self.setGeometry(100, 100, 640, 280)
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)

        self.tree = QTreeWidget()
        self.headerItem = QTreeWidgetItem()



        self.dup_b = QPushButton('Delete')
        self.dup_b.setCheckable(True)
        self.dup_b.clicked.connect(self.handleButton)
        layout.addWidget(self.tree, 0)

        layout.addWidget(self.dup_b, 0)


    def print_text(self,result):
        if result != '\n':
            for subresult in result:

                child = QTreeWidgetItem(self.tree)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, subresult)
                child.setCheckState(0, Qt.Unchecked)
        else:
            child = QTreeWidgetItem(self.tree)
            child.setText(0,'\n')

    def handleButton(self):
        select = []
        iterator = QTreeWidgetItemIterator(self.tree, QTreeWidgetItemIterator.Checked)
        while iterator.value():
             item = iterator.value()
             if item.text(0) not in select:
                 select.append(item.text(0))
             iterator += 1
        if select:
            for p in range(0,len(select)):
                if os.path.isfile(select[p]):
                    #shutil.remove(select[p])
                    shell.SHFileOperation((0, shellcon.FO_DELETE, select[p], None, shellcon.FOF_NOCONFIRMATION | shellcon.FOF_NOERRORUI))
                    # menu.print_text("Deleted")
        if not select:
            pass
             #sys.exit(appx.exec_())


def initial():
    dups = {}
    folders = [sys.argv[1]]
    # for i in range(0, 1):
    #     folders.append('D:\\xxx')
    for i in folders:
        # Iterate the folders given
        if os.path.exists(i):
            # Find the duplicated files and append them to the dups
            joinDicts(dups, findDup(i))
        else:
            print('%s is not a valid path, please verify' % i)
    printResults(dups)


# Reading out files to Hash
def hashfile(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


# Checking for Duplicates
def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        #str = ('Scanning %s...' % dirName)
        #thread.start_new_thread(menu.print_text,('\n'+str,))#menu.print_text('\n' + str)
        #print str
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups


# Merging/Appending Dict.
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]

# Result Printing Method.
def printResults(dict1):
    #appx = QApplication(sys.argv)
    #menu = Mode()

    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        #print('Duplicates Found:')
        #print('\nThe following files are identical. The name could differ, but the content is identical')
        #print('\n___________________')
        for result in results:
            #for subresult in result:
                #print('\n\t%s' % subresult)
            menu.print_text(result)
            menu.print_text('\n')
            #print '1'

    else:
        print('\nNo duplicate files found.')

    # menu.show()
    # sys.exit(appx.exec_())



appx = QApplication(sys.argv)
menu = Mode()
run = initial()
menu.show()
sys.exit(appx.exec_())

