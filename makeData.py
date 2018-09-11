import os,re
import directoryIndex as di
import mediaFile as extChk
import win32api
from sklearn.externals import joblib
dirIndex = {}
rootIndex = {}
print "Please eject all connected External Storage Device and press Enter"
raw_input()
print "Parsing Directories...\nCreating Database"
fp = open ('dir.tsv', 'w')
count = 0
# fp.write('Label\tGroup\n')
fp.close()
def dirSetMaker(root):
    # fp.write('ollo')
   try:
    if root not in dirIndex:
        global count
        dirIndex[root] = count
        rootIndex[root] = count

        count = count+1
        # count+=1
    for path in os.listdir(root):
        if re.search(r'RECYCLE', path):
            continue
        curr_path = os.path.join(root, path)
        fp = open('dir.tsv', 'a')
        # print path

        if os.path.isfile(curr_path):

            name, ext = os.path.splitext(curr_path)

            if extChk.isMedia(ext):

                if ext in di.dir[root]:
                    if di.dir[root][ext] < 2:
                        # print root, ext, di.dir[root][ext]
                        parentpath, restfname = os.path.split(root)
                        dirIndex[root] = dirIndex[parentpath]

                        # count = dirIndex[root]
                    else:
                        pass
        if re.search(r'\d*_n', path):
                path = 'fb_img.jpg'

        elif re.search(r'DSC_\d\d\d\d',path):
                path = 'NikonD1.jpg'
        elif re.search(r'DSCN\d\d\d\d',path):
                path = 'NikCoolpix.jpg'

        elif re.search(r'SBCS_\d\d\d\d', path):
            path = 'CanonEOS.jpg'

        elif re.search(r'IMG_\d\d\d\d', path):
            path = 'CanonG2.jpg'
        elif re.search(r'Screenshot*', path):
            path = 'ScreenShots'
        elif re.search(r'_SCN\d\d\d\d', path):
            path = 'Cam1.jpg'
            # elif re.search(r'IMG-\d\d\d\d\d\d\d\d-WA\d\d\d\d',path,flags=re.IGNORECASE):
            #     pass
            # elif re.search('\\b\d\d\d.jpg\\b',path,flags=re.IGNORECASE):
            #     path='pic.jpg'
            # elif re.search('\\b\d\d\d\d.jpg\\b',path,flags=re.IGNORECASE):
            #     path='pic1.jpg'
            # elif re.search('\\b\d\d\d\d\d.jpg\\b',path,flags=re.IGNORECASE):
            #     path='pic2.jpg'


        fp.write((path+'\t'+str(dirIndex[root])+'\n').encode('utf8'))

        # fp.close()

        if os.path.isdir(curr_path):
            p1, p2 = os.path.split(curr_path)
            if re.search(r'cache*',p2):
                pass
            elif re.search(r'thumbnail',p2):
                pass
            else:
                curr_path = os.path.join(p1,p2)
                dirSetMaker(curr_path)

   except:
       pass

# drives = win32api.GetLogicalDriveStrings()
# drives = drives.split('\000')[:-1]
# for i in range(1,len(drives)):
#     di.indexer(drives[i])
#     # print di.dir['F:\\']
#     dirSetMaker(drives[i])
dirSetMaker('E:\\')
print "Almost there"
dictDir = dict()
for key in rootIndex:
    dictDir[rootIndex[key]] = key

joblib.dump(dictDir,'index.txt')

# import json
# with open ('virtual.txt', 'w') as fileDict:
#     json.dump(dirIndex,fileDict,ensure_ascii=False)
#
# with open ('real.txt', 'w') as feDi:
#     json.dump(rootIndex,feDi,ensure_ascii=False)
print "Success"