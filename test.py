a,b = input().split()
a = int(a)
b = int(b)
starti = 0
startj = 0
lostlist = [([0]*b) for i in range(a)]
doorlist = []
resultlist =[]
maindlist = ['x' for i in range(a * b)]
for i in range(a):
    row = str(input())
    for j in range(b):
        lostlist[i][j]=row[j]
        if(row[j]=='2'):
            starti = i
            startj = j
        if not(row[j].isdigit()):
            dict = {'name':row[j],'i':i,'j':j,'isopen':0}
            doorlist.append(dict)

def BFS(x,y):
    result = 0
    visitlist = [0 for i in range(a * b)]
    bfslist = []
    maindlist[x*b+y] = int(0)
    visitlist[x*b+y] = 1
    point = {'point':lostlist[x][y],'x':x,'y':y}
    bfslist.append(point)
    while(bfslist):
        x = bfslist[0]['x']
        y = bfslist[0]['y']
        del bfslist[0]
        upx = x-1
        if(x!=0):
            if(visitlist[upx*b+y]==0):
                if(lostlist[upx][y]!='0'):
                    point = {'point': lostlist[upx][y], 'x': upx, 'y': y}
                    visitlist[upx * b + y] = 1
                    if not(lostlist[upx][y].isdigit()):
                        if(lostlist[upx][y].isupper()):
                            start2key = findkey(starti,startj,lostlist[upx][y].lower())
                            for id in doorlist:
                                if(id['name']==lostlist[upx][y].lower()):
                                    keyx = id['i']
                                    keyy = id['j']
                            key2door = findkey(keyx,keyy,lostlist[upx][y])
                            for doorid in doorlist:
                                if (doorid['name'] == lostlist[upx][y]):
                                    doorid.update({'isopen':1})
                            maindlist[upx * b + y] = start2key+key2door
                            print(doorlist)

                    else:
                        maindlist[upx * b + y] = maindlist[x*b+y]+1
                    if (lostlist[upx][y] == '3'):
                        result = maindlist[upx * b + y]
                    else:
                        bfslist.append(point)

        if(x!=(a-1)):
            downx = x + 1
            if (visitlist[downx * b + y] == 0):
                if (lostlist[downx][y] != '0'):
                    point = {'point': lostlist[downx][y], 'x': downx, 'y': y}
                    visitlist[downx * b + y] = 1
                    if not(lostlist[downx][y].isdigit()):
                        if(lostlist[downx][y].isupper()):
                            start2key = findkey(starti,startj,lostlist[downx][y].lower())
                            for id in doorlist:
                                if(id['name']==lostlist[downx][y].lower()):
                                    keyx = id['i']
                                    keyy = id['j']
                            key2door = findkey(keyx,keyy,lostlist[downx][y])
                            for doorid in doorlist:
                                if (doorid['name'] == lostlist[downx][y]):
                                    doorid.update({'isopen':1})
                            maindlist[downx * b + y] = start2key+key2door
                    else:
                        maindlist[downx * b + y] = maindlist[x * b + y] + 1
                    if (lostlist[downx][y] == '3'):
                        result = maindlist[downx * b + y]
                    else:
                        bfslist.append(point)
        if(y!=0):
            lefty = y - 1
            if (visitlist[x * b + lefty] == 0):
                if (lostlist[x][lefty] != '0'):
                    point = {'point': lostlist[x][lefty], 'x': x, 'y': lefty}
                    visitlist[x * b + lefty] = 1
                    if not(lostlist[x][lefty].isdigit()):
                        if(lostlist[x][lefty].isupper()):
                            start2key = findkey(starti,startj,lostlist[x][lefty].lower())
                            for id in doorlist:
                                if(id['name']==lostlist[x][lefty].lower()):
                                    keyx = id['i']
                                    keyy = id['j']
                            key2door = findkey(keyx,keyy,lostlist[x][lefty])
                            for doorid in doorlist:
                                if (doorid['name'] == lostlist[x][lefty]):
                                    doorid.update({'isopen':1})
                            maindlist[x * b + lefty] = start2key+key2door
                    else:
                        maindlist[x * b + lefty] = maindlist[x * b + y] + 1
                    if (lostlist[x][lefty] == '3'):
                        result = maindlist[x * b + lefty]
                    else:
                        bfslist.append(point)
        if(y!=b-1):
            righty = y + 1
            if (visitlist[x * b + righty] == 0):
                if (lostlist[x][righty] != '0'):
                    point = {'point': lostlist[x][righty], 'x': x, 'y': righty}
                    visitlist[x * b + righty] = 1
                    if not(lostlist[x][righty].isdigit()):
                        if(lostlist[x][righty].isupper()):
                            start2key = findkey(starti,startj,lostlist[x][righty].lower())
                            for id in doorlist:
                                if(id['name']==lostlist[x][righty].lower()):
                                    keyx = id['i']
                                    keyy = id['j']
                            key2door = findkey(keyx,keyy,lostlist[x][righty])
                            for doorid in doorlist:
                                if (doorid['name'] == lostlist[x][righty]):
                                    doorid.update({'isopen':1})
                            maindlist[x * b + righty] = start2key+key2door
                    else:
                        maindlist[x * b + righty] = maindlist[x * b + y] + 1
                    if(lostlist[x][righty] == '3'):
                        result = maindlist[x * b + righty]
                    else:
                        bfslist.append(point)
    return result


def findkey(x,y,key):
    result = 0
    visitlist = [0 for i in range(a * b)]
    bfslist = []
    dlist = ['x' for i in range(a * b)]
    dlist[x * b + y] = int(0)
    visitlist[y * a + x] = 1
    point = {'point': lostlist[x][y], 'x': x, 'y': y}
    bfslist.append(point)
    while (bfslist):
        x = bfslist[0]['x']
        y = bfslist[0]['y']
        del bfslist[0]
        upx = x - 1
        if (x != 0):
            if (visitlist[upx * b + y] == 0):
                if (lostlist[upx][y] != '0'):
                    point = {'point': lostlist[upx][y], 'x': upx, 'y': y}
                    bfslist.append(point)
                    visitlist[upx * b + y] = 1
                    if not(lostlist[upx][y].isdigit()):
                        if(lostlist[upx][y].isupper()):
                            for doorid in doorlist:
                                if(doorid['name']==lostlist[upx][y]):
                                    isopen = doorid['isopen']
                            if(isopen==0):
                                start2key = findkey(starti,startj,lostlist[upx][y].lower())
                                for id in doorlist:
                                    if(id['name']==lostlist[upx][y].lower()):
                                        keyx = id['i']
                                        keyy = id['j']
                                key2door = findkey(keyx,keyy,lostlist[upx][y])
                                dlist[upx * b + y] = start2key+key2door
                            else:
                                dlist[upx * b + y] = dlist[x * b + y] + 1
                    else:
                        dlist[upx * b + y] = dlist[x*b+y]+1
                    if (lostlist[upx][y] == key):
                        result = dlist[upx * b + y]
                        break
        if (x != (a - 1)):
            downx = x + 1
            if (visitlist[downx * b + y] == 0):
                if (lostlist[downx][y] != '0'):
                    point = {'point': lostlist[downx][y], 'x': downx, 'y': y}
                    bfslist.append(point)
                    visitlist[downx * b + y] = 1
                    if not(lostlist[downx][y].isdigit()):
                        if(lostlist[downx][y].isupper()):
                            for doorid in doorlist:
                                if(doorid['name']==lostlist[downx][y]):
                                    isopen = doorid['isopen']
                            if(isopen==0):
                                start2key = findkey(starti,startj,lostlist[downx][y].lower())
                                for id in doorlist:
                                    if(id['name']==lostlist[downx][y].lower()):
                                        keyx = id['i']
                                        keyy = id['j']
                                key2door = findkey(keyx,keyy,lostlist[downx][y])
                                dlist[downx * b + y] = start2key+key2door
                            else:
                                dlist[downx * b + y] = dlist[x * b + y] + 1
                    else:
                        dlist[downx * b + y] = dlist[x * b + y] + 1
                    if (lostlist[downx][y] == key):
                        result = dlist[downx * b + y]
                        break
        if (y != 0):
            lefty = y - 1
            if (visitlist[x * b + lefty] == 0):
                if (lostlist[x][lefty] != '0'):
                    point = {'point': lostlist[x][lefty], 'x': x, 'y': lefty}
                    bfslist.append(point)
                    visitlist[x * b + lefty] = 1
                    if not(lostlist[x][lefty].isdigit()):
                        if(lostlist[x][lefty].isupper()):
                            for doorid in doorlist:
                                if(doorid['name']==lostlist[x][lefty]):
                                    isopen = doorid['isopen']
                            if(isopen==0):
                                start2key = findkey(starti,startj,lostlist[x][lefty].lower())
                                for id in doorlist:
                                    if(id['name']==lostlist[x][lefty].lower()):
                                        keyx = id['i']
                                        keyy = id['j']
                                key2door = findkey(keyx,keyy,lostlist[x][lefty])
                                dlist[x * b + lefty] = start2key+key2door
                            else:
                                dlist[x * b + lefty] = dlist[x * b + y] + 1
                    else:
                        dlist[x * b + lefty] = dlist[x * b + y] + 1
                    if (lostlist[x][lefty] == key):
                        result = dlist[x * b + lefty]
                        break
        if (y != b - 1):
            righty = y + 1
            if (visitlist[x * b + righty] == 0):
                if (lostlist[x][righty] != '0'):
                    point = {'point': lostlist[x][righty], 'x': x, 'y': righty}
                    bfslist.append(point)
                    visitlist[x * b + righty] = 1
                    if not(lostlist[x][righty].isdigit()):
                        if(lostlist[x][righty].isupper()):
                            for doorid in doorlist:
                                if(doorid['name']==lostlist[x][righty]):
                                    isopen = doorid['isopen']
                            if(isopen==0):
                                start2key = findkey(starti,startj,lostlist[x][righty].lower())
                                for id in doorlist:
                                    if(id['name']==lostlist[x][righty].lower()):
                                        keyx = id['i']
                                        keyy = id['j']
                                key2door = findkey(keyx,keyy,lostlist[x][righty])
                                dlist[x * b + righty] = start2key+key2door
                            else:
                                dlist[x * b + righty] = dlist[x * b + y] + 1
                    else:
                        dlist[x * b + righty] = dlist[x * b + y] + 1
                    if (lostlist[x][righty] == key):
                        result = dlist[x * b + righty]
                        break

    return result



dis = BFS(starti,startj)
m = 0
for i in range(a):
    for j in range(b):
        print(maindlist[m],end=' ')
        m+=1
    print('\n')

print(dis)
