import numpy as np

class Sorter():
    def __init__(self,arr):
        self.arr = arr
    def insertionSort(self,reverse=False):
        '''
        This algorithm take a vector as input and conducts insertion Sorting algorithm
        Input:
        arr: the input array
        reverse: the order of sorting, True for descend while False for ascend. 
        Output:
        newArr: the sorted array
        '''
        arr = self.arr
        if reverse == True:
            sign = -1
        else:
            sign = 1
        newArr = np.array([],dtype='int')
        for i in arr:
            if newArr.shape[0] == 0:
                newArr = np.append(newArr,i)
            else:
                arrLen = newArr.shape[0]
                for ind,j in enumerate(newArr):
                    if sign * (j - i) < 0:
                        if ind == arrLen -1:
                            newArr = np.append(newArr,i)
                        continue
                    else:
                        newArr = np.insert(newArr,ind,i)
                        break
        return newArr
