import math

class Sorter():
    
    #插入排序
    def insertionSort(self,arr,descend=False):
        '''
        This algorithm take a vector as input and conducts insertion Sorting algorithm
        Input:
        arr: the input array
        descend: the order of sorting, True for descend while False for ascend, default is ascend.
        Output:
        arr: the sorted array
        简单说，插入排序就是从前往后一个元素一个元素地和前面已经排序好的数组比较。因为当前元素之前的数字都是排序好的，所以只有找到对的位置，
        就可以直接插入进去，故而为插入排序。最换情况下为数组全部倒序，时间复杂度是n平方，最好是已经排序好，时间复杂度为n。
        '''
        if descend == True:
            sign = -1
        else:
            sign = 1
        for i in range(len(arr)):
            for j in range(i-1,-1,-1):
                if sign * (arr[j] - arr[j+1]) > 0:
                    tmp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = tmp
        return arr
    
    #希尔排序
    def shellSort(self,arr,gap=None,descend=False):
        '''
        This algorithm is an improve version of insertionSort
        Input:
        arr: input array
        gap: the step size to split array
        descend: the order of sorting. True for descend while False for ascend, default is ascend.
        Output:
        arr: sorted array
        这是个加强版的插入排序。主要就是通过分组来加速排序过程。插入排序中，后面的元素每次循环中只能向前移动一个元素。在希尔排序中，通过gap给数组分组，
        最后一个元素可以移动到当前分组最前面的位置。至于时间复杂度，最坏情况下是n平方，最好情况下是n，平均是n的1.3次方。时间复杂度取决于增量序列
        （本例是通过减半来获得序列）。
        '''
        arrLen = len(arr)
        if gap is None:
            gap = math.floor(arrLen/2)
        if descend == True:
            sign = -1
        else:
            sign = 1
        while(gap!=0):
            for i in range(gap,arrLen):
                for j in range(i-gap,-1,-gap):
                    if sign * (arr[j+gap] - arr[j]) < 0:
                        tmp = arr[j]
                        arr[j] = arr[j+gap]
                        arr[j+gap] = tmp
            gap = math.floor(gap/2)
        return arr
    
    #选择排序
    def selectSort(self,arr,descend=False):
        '''
        This algorithm is selection sort.
        Input:
        arr: input array
        descend: the order of sorting. True for descend while False for ascend, default is ascend.
        Output:
        arr: sorted array
        这个算法就是通过当前数字和这个数字之后的数进行比较找到他们当中最小的数（而且比当前数字要小），然后进行交换。最坏、最好、平均时间复杂度都是n的平方
        '''
        if descend == True:
            sign = -1
        else:
            sign = 1
        for i in range(len(arr)):
            target = i
            for j in range(i,len(arr)):
                if sign * (arr[target] - arr[j]) > 0:
                    target = j
            tmp = arr[target]
            arr[target] = arr[i]
            arr[i] = tmp
        return arr
    
    #堆排序
    def _adjustHeap(self, arr, curP, sign):
        lChild = 2 * curP + 1
        rChild = 2 * curP + 2
        largest = curP
        if lChild < arrLen and sign* (arr[lChild] - arr[largest]) > 0:
            largest = lChild
        if rChild < arrLen and sign * (arr[rChild] - arr[largest]) > 0:
            largest = rChild
        if largest != curP:
            tmp = arr[largest]
            arr[largest] = arr[curP]
            arr[curP] = tmp
            self._adjustHeap(arr,largest,sign)
            
    def _buildHeap(self,arr,sign):
        layer = int(math.log2(len(arr)+1))
        sRange = int(math.pow(2,layer) - 1)
        for i in range(sRange,-1,-1):
            self._adjustHeap(arr,i,sign)
    
    def heapSort(self, arr, descend=False):
        '''
        This algorithm is Heap sorting algorithm
        Input:
        arr: input array
        descend: the order of sorting, True for descend while False for ascend, default is ascend.
        堆排序最重要的就是要保持最大（最小）堆的性质，通过二叉树的性质找到子结点。这样就可以减少遍历的次数。整体步骤是：1.构建最大（最小）堆机构，2.将第一个和最后一个交换，3.此时最后一个为已排序
        4.剩下未排序的数字除了第一个外都是满足堆性质的，所以将第一个与其子节点比较并与最大者交换，直到他就是最大者。5.以此类推解决所有数字。
        '''
        if descend == True:
            sign = -1
        else:
            sign = 1
        global arrLen
        arrLen = len(arr)
        self._buildHeap(arr,sign)
        for i in range(arrLen-1,0,-1):
            tmp = arr[0]
            arr[0] = arr[i]
            arr[i] = tmp
            arrLen -= 1
            self._adjustHeap(arr,0,sign)
        return arr
    
    #冒泡排序
    def bubbleSort(self, arr, descend=False):
        if descend == True:
            sign = -1
        else:
            sign = 1
        arrLen = len(arr)
        for i in range(0,arrLen-1):
            for j in range(0,arrLen-i-1):
                if sign * (arr[j] - arr[j+1]) > 0:
                    tmp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = tmp
        return arr
    
    #快速排序
    def quickSort(self,arr,start,end,descend=False):
        '''
        This is quick sort algorithm
        Input:
        arr: the input array
        start: the start position
        end: the end position
        descend: the order of sorting, True for descend while False for ascend, default is ascend.
        Output:
        arr: the sorted array
        快速排序利用分治的方法，先找到一个基准，然后设立一前一后两个指针。过程中，两个指针向对方靠近并将大于基准数字的数放在右边，小于的数放在左边。
        最后当两个指针重合时，这个位置就是基准数的位置。最坏情况下是n的平方，其他都是nlog2(n)。
        '''
        i = start
        j = end
        if descend == True:
            sign = -1
        else:
            sign = 1
        if i >= j:
            return None
        base = arr[start]
        while(i!=j):
            while(sign * (arr[j]-base)>0 and i < j):
                j -= 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            while(sign * (arr[i]-base)<=0 and i < j):
                i += 1
            if i < j:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
        arr[i] = base
        self.quickSort(arr,start,i-1,descend)
        self.quickSort(arr,i+1,end,descend)
        return arr
    
    #归并排序
    def mergeSort(self, arr,start,end,descend=False):
        '''
        This algorithm is merge sort algorithm
        Input:
        arr: the input array
        start: the start position of slide
        end: the end position of slide
        descend: the order of sorting, True for descend while False for ascend, default is ascend.
        Output:
        arr: the sorted array
        归并排序是分治法的极致，先将数组分割到最小单元（一组一个数字）然后两两合并成一个有序组（1到2），然后一直合并（2到4，4到8。。。）。 
        主要利用递归来进行。时间复杂度是nlog2(n)
        '''
        if descend == True:
            sign = -1
        else:
            sign = 1
        if start == end:
            return [arr[start]]
        medium = int((start+end)/2)
        part1 = self.mergeSort(arr,start, medium , descend)
        part2 = self.mergeSort(arr, medium + 1, end ,descend)
        merge = []
        j = 0
        for i in part1:
            while(j < len(part2) and sign * (part2[j] - i) < 0):
                merge.append(part2[j])
                j += 1
            merge.append(i)
        while(j<len(part2)):
            merge.append(part2[j])
            j += 1
        return merge