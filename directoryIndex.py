import os,sys
import json
# dirIndex = {}
dir ={}
def indexer(root):
    dir[root] = {}
    try :
        for path in os.listdir(root):
            curr_path = os.path.join(root, path)
            if os.path.isfile(curr_path):

                name, ext = os.path.splitext(curr_path)

                if ext in dir[root]:
                        dir[root][ext] += 1
                else:
                        dir[root][ext] = 1

            elif os.path.isdir(curr_path):
                  temp = indexer(curr_path)
                  for v in temp[curr_path]:
                    # print curr_path, v, temp[curr_path][v]
                    if v in dir[root]:
                        # print root, v
                        dir[root][v] += temp[curr_path][v]
                    else:
                        dir[root][v] = temp[curr_path][v]

    except:
            pass# print temp[v]


    return dir
indexer('E:\\')
with open ('index.txt', 'w') as f:
    print 'Completed!. Contents written to index.txt'
    json.dump(dir,f,ensure_ascii=False)
# with open ('index.txt', 'r') as ipf:
#     data = ipf.read()
#     js = json.loads(data)

