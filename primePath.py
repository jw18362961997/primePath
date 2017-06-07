
# 返回的是以该点出发的所有simple path
def find_onePaths(graph, start, path):
    paths = []
    if  start not in graph: 
        paths.append(path)
        return paths
    path = path + [start]
    '''路径数组'''
   
    # 如果有邻接点
    if len(graph[start]):
        for node in graph[start]:
            # 点不在路径中（避免回路），则路径中加入该点，还要对该点邻接点进行遍历
            if node not in path:
                #print('不在')
                newpaths = find_onePaths(graph, node, path)
                for newpath in newpaths:
                    paths.append(newpath)
            # 点在路径中，且是起点，则将该点加入，且立即返回，不能再往下走，避免回路
            elif node in path and node==path[0]:
                #print("在，且是起点")
                newpath = path + [node]
                #print(path)
                paths.append(newpath)
            # 点在路径中，不是起点，加入会有回路，则不继续往下遍历，将已有路径返回
            else:
                if path not in paths:
                    paths.append(path)

    # 没有邻接点，防止路走到了没有出度的点
    else:
        paths.append(path)        
    return paths



# 这个返回的是依次以所有点出发的simple path ，
# 但是有的点的simples path可能是其他点simple path的子路径，所以还需要去杂
def find_allPaths(graph):
    paths=[]
    for node in graph:
        paths0 = find_onePaths(graph, node, [])
        for path0 in paths0:
            paths.append(path0)
    return paths

def purify(paths):
    # i=0
    newPaths=paths[:]
 
    for path1 in paths:
        # i+=1
        for path2 in paths:
            contain = comparePath(path1, path2)
            if contain==True:
                newPaths.remove(path1)
                break
    return newPaths


def comparePath(list1, list2):
    path1=""
    path2=""
    for node in list1:
        path1 += str(node) + "->"
    for node in list2:
        path2 += str(node) + "->"
    if path1 in path2 and path1!=path2:
        return True
    else:
        return False

def readGraphFromFile(filePath):
    file = open(filePath)
    graph = {}
    n=0
    while 1:
        line = file.readline()
        if not line:
            break
        else:
            if line.startswith("["):
                line = line.strip()[1:-1]
                array = line.split(", ")
                array1 = []
                for node in array:
                    array1.append(int(node))
                graph[n] = array1
                n = n+1
        pass # do something
    return graph

def doBatchTest():
    basePath = "C:\\Users\\Gin\\Desktop\\功能自动化测试框架\\代码题\\测试用例\\"
    filePaths = []
    for i in range(16):
        filePath = basePath + "case"+ str(i) +".txt"
        filePaths.append(filePath)
        #filePath = "C:\\Users\\Gin\\Desktop\\功能自动化测试框架\\代码题\\测试用例\\case11.txt"
        #C:\Users\Gin\Desktop\功能自动化测试框架\代码题\测试用例\case1.txt
        print(filePath)
        doTest(filePath, i)

def doOneTest():
    file_path =  input("请输入需要读取测测试用例文件路径：")  
    
    index = input("请输入保存文件编号：")
    print ("编号为：" , index)
    doTest(file_path, int(index) )

def doTest(filePath, i):
    #print ("测试用例文件路径为: ", filePath  )
    graph = readGraphFromFile(filePath)
    print("graph:", graph)
    paths = find_allPaths(graph)
    #print(paths0)
    paths = purify(paths)
    paths = sorted(paths, key = lambda a:(len(a),a) )
    outFilePath = "answer"+ str(i) +".txt"
    outFile= open(outFilePath, 'w+') 
    outFile.write(str(len(paths)) + "\n")
    for path in paths:
        outFile.write(str(path) + "\n")
    outFile.close()
    
    print("共", len(paths), "条primePath")     
    return outFilePath


graph1 = {'0':['1','2'], '1':['3'], '2':['3'], '3':['0'] }
graph2 = {'0':['1','2'], '1':['2'], '2':['3','4'], '3':['6'], '4':['5','6'], '5':['4'], '6':[] }
graphA = {'1':['2','3'],'2':['9'],'3':['4','5'],'4':['9'],'5':['6'],'6':['7','9'],'7':['8'],'8':['6'],'9':[]}
graphB = {'1':['2','3','4'],'2':['5'],'3':['10'],'4':['9','10'],'5':['6'],'6':['7','10'],'7':['8'],'8':['6'],'9':['10'],'10':[]}



if __name__ == '__main__':
    #doBatchTest()
    #doOneTest()
    #print("结束！")

    paths = find_allPaths(graphB)
    paths = purify(paths)
    print(len(paths))
    print(paths)