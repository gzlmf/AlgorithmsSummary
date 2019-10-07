class Searcher():
    def binarySearchR(self,arr, start, end, keyword):
        '''
        This is binary search algorithm(recursive version)
        Input:
        arr: sorted array
        start: the start position of searching range
        end: the end position of searching range
        keyword: the target word
        Output:
        pos: the position of target value
        '''
        medium = int((start + end)/2)
        if arr[medium] == keyword:
            return medium
        if arr[medium] < keyword:
            return self.binarySearch(arr,medium+1,end,keyword)
        elif arr[medium] > keyword:
            return self.binarySearch(arr,start, medium, keyword)
    
    def binarySearch(self,arr,start,end,keyword):
        '''
        This is binary search algorithm
        Input:
        arr: sorted array
        start: the start position of searching range
        end: the end position of searching range
        keyword: the target word
        Output:
        pos: the position of target value
        利用循环或者递归来二等分数组，从而降低查找的次数，但是传入的数组必须是有序的。时间复杂度是O(log2(n))
        '''
        while(start < end):
            medium = int((start + end)/2)
            if arr[medium] == keyword:
                return medium
            if arr[medium] < keyword:
                start = medium + 1
            elif arr[medium] > keyword:
                end = medium 
        print('no found')
    
    def interpolationSearch(self,arr, start, end, keyword):
        '''
        This algorithm is interpolation search.
        Input:
        arr: sorted array
        start: the start position of searching range
        end: the end position of searching range
        keyword: the target word
        Output:
        pos: the position of target value
        插值查找是二分查找的改良版，主要改进在于它初始化medium的值，让这个值离目标更近一些。他的时间复杂度是O(log2(log2(n)))
        '''
        while(start < end):
            medium = int(start + ((keyword - arr[start]) / (arr[end] - arr[start])) * (end - start))
            if arr[medium] == keyword:
                return medium
            if arr[medium] < keyword:
                start = medium + 1
            elif arr[medium] > keyword:
                end = medium
