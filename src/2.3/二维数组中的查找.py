# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
# 整数，判断数组中是否含有该整数。

# matrix = [
#   [1, 3, 5, 7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
#正常遍历
def searchMatrix(self,matrix,target):
    findmark = False
    if matrix == None:
        return findmark
    else:
        i =  0
        j = len(matrix[0])-1
        while i<len(matrix) and j >= 0:
            if matrix[i][j]> target:
                j -= 1
            elif matrix[i][j]<target:
                i += 1
            else:
                findmark = True
                break
        if findmark == True:
            return True
        else:
            return False

# 行二分
def binarysearch(self, list, target):
    low = 0
    high = len(list) - 1
    findmark = False
    while low <= high:
        mid = (low + high) // 2
        if target > list[mid]:
            low = mid + 1
        elif target < list[mid]:
            high = mid - 1
        else:
            findmark = True
            break
    return findmark

def searchMatrix(self, matrix, target):
    findmark = False
    if matrix == None:
        return findmark
    else:
        for row in matrix:
            findmark = self.binarysearch(row, target)
            if findmark:
                break
        return findmark


