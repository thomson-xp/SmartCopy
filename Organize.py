import os
import shutil
import time
import sys
import calendar

extCnt = {}

def fcount(path):
   
    for f in os.listdir(path):
        path1 = os.path.join(path, f)
        if os.path.isfile(path1):
            
            f_path, f_extension = os.path.splitext(path1)

            if f_extension in extCnt:
                extCnt[f_extension].append(f_path)
            else:
                extCnt[f_extension] = [f_path]

def check_exist(path, f_name):
    x = 0

    for lis in os.listdir(path):
        path1 = os.path.join(path, lis)
        if os.path.isdir(path1):
            rt, name = os.path.split(path1)
            if name == f_name:
                x = 1

    return x

def sortfiles():
    
    for key in extCnt:
        
        if len(extCnt[key])> n :# count to max limit of similar files in a folder
            
            #changing to Directory(named by extension)
            os.chdir(path)
            n_folder= key[1:]
            
            chk = check_exist(path, n_folder)
            if chk == 0: os.mkdir(n_folder)
            
            path2 = os.path.join(path, n_folder)

            #change to directory(named by date)
            os.chdir(path2)
            l_time = time.localtime(time.time())
            n_folder = '(' + `l_time.tm_mon` + '-' + `l_time.tm_mday` + '-' + `l_time.tm_year` + ')'
            
            chk = check_exist(path2, n_folder)
            if chk == 0: os.mkdir(n_folder)
     

                
            for i in range(0, len(extCnt[key])):
                f_path = os.path.join(path2,extCnt[key][i] + key)
                try:
                    shutil.move(f_path, os.path.join(path2, n_folder))
     
                except:
                    pass

#main Funtion
path = sys.argv[1]
n = 3
n = int(n)
fcount(path)
sortfiles()
