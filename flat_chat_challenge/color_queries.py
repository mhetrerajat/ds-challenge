CONST_BLACK = "B"
CONST_WHITE = "W"

def getInput():
    nmqList = map(int, raw_input().split(" "))
    grid = []
    xydList = []
    for mItem in range(nmqList[0]):
        mList = map(int, raw_input().split(" "))
        grid.append(mList)

    for item in range(nmqList[2]):
        itemList = map(int, raw_input().split(" "))
        xydList.append(itemList)

    return (nmqList, grid, xydList)

# neighbours of cell such that absolute distance <= d
def neighboursOfCell(x,y,d,nmqList,grid,checkedList):
    # (x-1, y) (x+1,y) (x,y-1) (x, y+1)
    neighbours = []
    try :
        grid[x-2][y-1]
        neighbours.append([x-1,y])
    except:
        pass

    try :
        grid[x-1][y-2]
        neighbours.append([x,y-1])
    except:
        pass

    try :
        grid[x][y-1]
        neighbours.append([x+1,y])
    except:
        pass

    try :
        grid[x-1][y]
        neighbours.append([x,y+1])
    except:
        pass

    blackCell = []
    if(len(checkedList) == 1):
        blackCell = checkedList[0]
    else:
        for item in neighbours:
            if item in checkedList:
                blackCell = item

    #print blackCell
    #cprint neighbours

    result = []
    for item in neighbours:
        #print ' '.join([str(blackCell[0]), str(blackCell[1]), str(item[0]), str(item[1])])
        if(abs(grid[blackCell[0]-1][blackCell[1]-1] - grid[item[0]-1][item[1]-1]) <= d):
            result.append(item)

    return result



def colorCell(x,y,d, coloredGrid ,checkedList):
    neighbours = neighboursOfCell(x,y,d,nmqList, grid, checkedList)
    if len(neighbours) != 0:
        #print "neighbours ->"
        #print ' '.join([str([x,y]) , " -> ", str(neighbours)])
        for neighbourItem in neighbours:
            if neighbourItem not in checkedList:
                #print neighbourItem
                coloredGrid[neighbourItem[0]-1][neighbourItem[1]-1] = CONST_BLACK
                checkedList.append([neighbourItem[0],neighbourItem[1]])
                colorCell(neighbourItem[0],neighbourItem[1], grid[neighbourItem[0]-1][neighbourItem[1]-1], coloredGrid, checkedList)


if __name__ == "__main__":
    #nmqList = [4, 4, 3]
    #grid = [[0, 0, 1, 0], [1, 2, 1, 0], [0, 0, 1, 0], [1, 0, 1, 0]]
    #xydList = [[4, 4, 0], [4, 3, 1], [2, 2, 2]]
    #xydList = [[4, 4, 0]]
    try:
        nmqList, grid, xydList = getInput()


        for xydItem in xydList:
            x,y,d = xydItem[0],xydItem[1],xydItem[2]
            m = nmqList[1]
            n = nmqList[0]
            checkedList = []
            #print x,y,d
            coloredGrid = [[0]*m]*n
            #print coloredGrid
            coloredGrid[x-1][y-1] = CONST_BLACK
            checkedList.append([x,y])
            #print grid
            colorCell(x,y,d,coloredGrid, checkedList)
            frequency = 0
            for i in coloredGrid:
                for j in i:
                    if j is CONST_BLACK:
                        frequency+=1
            print frequency
    except:
        pass
