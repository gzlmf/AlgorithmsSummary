from Node import *
from queue import Queue

class BinaryTree():
    #初始化二叉查找树
    def __init__(self,arr=None):
        self.arr = arr
        self.tree = None
        self._buildTree()
        
    #获取该节点的深度    
    def _getBalance(self,node):
        if (node==None):
            return 0
        else:
            return node.depth
    
    #更新当前节点深度
    def _updateDepth(self,point):
        if point.parent == None:
            point.depth = max([self._getBalance(point.lChild), self._getBalance(point.rChild)]) + 1
        else:
            point.depth = max([self._getBalance(point.lChild), self._getBalance(point.rChild)]) + 1
        #每次插入数据时只更新自己的深度，然后从下至上检查平衡，同时更新其他结点
    
    #对当前节点进行左旋转
    def _leftRotate(self,point):
        parPoint = point.parent
        rChild = point.rChild
        if rChild.lChild !=None:
            rChild_lChildP = rChild.lChild
        else:
            rChild_lChildP = None
            
        #parent
        if parPoint != None:
            if parPoint.lChild != None and parPoint.lChild == point:
                parPoint.lChild = rChild
            elif parPoint.rChild != None and parPoint.rChild == point:
                parPoint.rChild = rChild
                
        #point
        point.parent = rChild
        point.rChild = rChild_lChildP
        
        self._updateDepth(point)
        
        #lChild
        if parPoint != None:
            rChild.parent = parPoint
        else:
            rChild.parent = None
            self.tree = rChild
            #####
            self.tree.head = True
            point.head=False
            #####
        rChild.lChild = point
        
        self._updateDepth(rChild)
        
        #lChildR
        if rChild_lChildP != None:
            rChild_lChildP.parent = point
    
    #对当前节点进行右旋转
    def _rightRotate(self,point):
        parPoint = point.parent
        lChild = point.lChild
        if lChild.rChild !=None:
            lChild_rChildP = lChild.rChild
        else:
            lChild_rChildP = None
            
        #parent
        if parPoint != None:
            if parPoint.lChild != None and parPoint.lChild == point:
                parPoint.lChild = lChild
            elif parPoint.rChild != None and parPoint.rChild == point:
                parPoint.rChild = lChild
                
        #point
        point.parent = lChild
        point.lChild = lChild_rChildP
        
        self._updateDepth(point)
        
        #lChild
        if parPoint != None:
            lChild.parent = parPoint
        else:
            lChild.parent = None
            self.tree = lChild
            ####
            self.tree.head = True
            point.head=False
            ####
        lChild.rChild = point
        
        self._updateDepth(lChild)
        
        #lChildR
        if lChild_rChildP != None:
            lChild_rChildP.parent = point
        
    #检查当前树是否平衡
    def _checkBalance(self,point):
        while(point!=None):
            self._updateDepth(point)
            l_depth = self._getBalance(point.lChild)
            r_depth = self._getBalance(point.rChild)
            #左
            if (l_depth - r_depth) > 1:
                lpoint = point.lChild
                ll_depth = self._getBalance(lpoint.lChild)
                lr_depth = self._getBalance(lpoint.rChild)
                #左
                if ll_depth > lr_depth:
                    self._rightRotate(point)
                #右
                elif ll_depth < lr_depth:
                    self._leftRotate(lpoint)
                    self._rightRotate(point)
                #深度相等时可以等同于左左
                else:
                    self._rightRotate(point)
                point = point.parent
            #右
            elif (r_depth - l_depth) > 1:
                rpoint = point.rChild
                rl_depth = self._getBalance(rpoint.lChild)
                rr_depth = self._getBalance(rpoint.rChild)
                #右
                if rr_depth > rl_depth:
                    self._leftRotate(point)
                #左
                elif rr_depth < rl_depth:
                    self._rightRotate(rpoint)
                    self._leftRotate(point)
                #当两边深度相等时可以等同于右右
                else:
                    self._leftRotate(point)
                point = point.parent
            else:
                point = point.parent
                continue
        
    #插入节点          
    def insertNode(self,x):
        if self.tree == None:
            self.tree = Node(x)
            #####
            self.tree.head = True
            #####
        else:
            point = self.tree
            flag = True
            while(point != None):
                if point.data < x:
                    if point.rChild == None:
                        point.rChild = Node(x)
                        point.rChild.parent = point
                        point = point.rChild
                        break
                    else:
                        point = point.rChild
                elif point.data > x:
                    if point.lChild == None:
                        point.lChild = Node(x)
                        point.lChild.parent = point
                        point = point.lChild
                        break
                    else:
                        point = point.lChild
                else:
                    print('data exists')
                    flag = False
                    break
            if flag == True:
                self._updateDepth(point)
                self._checkBalance(point.parent)
    
    #创建二叉树
    def _buildTree(self):
        arr = self.arr
        if len(arr) == 0:
            return None
        else:
            for i in arr:
                self.insertNode(i)
    
    #中序遍历
    def sortTree(self):
        stack = []
        arr = []
        point = self.tree
        while point or len(stack) > 0:
            while(point):
                stack.append(point)
                point = point.lChild
            point = stack.pop()
            arr.append(point.data)
            point = point.rChild
        return arr
    
    #查找目标值
    def searchTree(self,target):
        point = self.tree
        flag = False
        while(point):
            if point.data < target:
                point = point.rChild
            elif point.data > target:
                point = point.lChild
            else:
                flag = True
                return point
        if flag == False:
            print('data not exist')
    
    ############
    #TODO
    #可视化
    ############
    #目前完成层次遍历，还需要定位每个数字的位置
    def visualization(self):
        arr = []
        stack = Queue(maxsize=0)
        point = self.tree
        stack.put(point)
        while(stack.qsize() > 0):
            tmp = stack.get()
            arr.append(tmp.data)
            if tmp.lChild!=None:
                stack.put(tmp.lChild)
            if tmp.rChild!=None:
                stack.put(tmp.rChild)
        return arr
    #删除叶子结点的具体操作
    def _leafNode_del(self,point):
        if point.head == True:
#             print(1)
            point = None
            self.tree = None
        else:
#             print(2)
            parPoint = point.parent
            if parPoint.lChild != None and parPoint.lChild == point:
                parPoint.lChild = None
            elif parPoint.rChild != None and parPoint.rChild == point:
                parPoint.rChild = None
            point = None
            self._checkBalance(parPoint)
    #删除单一子树结点的具体操作
    def _rightOrleftEmpty_del(self,point,child):
        if point.head == True:
#             print(3)
            self.tree = child
            child.head = True
            child.parent = None
            point = None
            self._checkBalance(child)
        else:
#             print(4)
            parPoint = point.parent
            if parPoint.lChild != None and parPoint.lChild == point:
                parPoint.lChild = child
            elif parPoint.lChild != None and parPoint.rChild == point:
                parPoint.rChild = child
            child.parent = parPoint
            point = None
            self._checkBalance(child)
    #删除双子树结点的操作
    def _noEmpty_del(self,point):
#         print(point.parent.data)
        rChild = point.rChild
        while(rChild.lChild != None):
            rChild = rChild.lChild
        selected = rChild
        parPoint = selected.parent
        if point.head == True:
            self.tree = selected
            selected.head = True
            selected.lChild = point.lChild
            point.lChild.parent = selected
            selected.parent = point.parent
            if parPoint == point:
#                 print(5)
                point = None
                self._checkBalance(selected)
            else:
#                 print(6)
                if selected.rChild != None:
                    parPoint.lChild = selected.rChild
                    selected.rChild.parent = parPoint
                    selected.rChild = point.rChild
                    point.rChild.parent = selected
                    point = None
                    self._checkBalance(parPoint.lChild)
                else:
                    parPoint.lChild = None
                    selected.rChild = point.rChild
                    point.rChild.parent = selected
                    point = None
                    self._checkBalance(parPoint)
        else:
            if point.parent.lChild != None and point.parent.lChild == point:
                point.parent.lChild = selected
            elif point.parent.lChild != None and point.parent.rChild == point:
                point.parent.rChild = selected
            selected.lChild = point.lChild
            point.lChild.parent = selected
            selected.parent = point.parent
            if parPoint != point:
#                 print(7)
                if selected.rChild != None:
                    parPoint.lChild = selected.rChild
                    selected.rChild.parent = parPoint
                    selected.rChild = point.rChild
                    point.rChild.parent = selected
                    point = None
                    self._checkBalance(parPoint.lChild)
                else:
                    parPoint.lChild = None
                    selected.rChild = point.rChild
                    point.rChild.parent = selected
                    point = None
                    self._checkBalance(parPoint)
            else:
#                 print(8)
                point = None
                self._checkBalance(selected)
            
    #删除结点
    def deleteNode(self,target):
        point = self.searchTree(target)
        if point==None:
            print('not exist')
            print(target)
            return None
        #叶子结点
        if point.lChild==None and point.rChild==None:
#             print('yezi')
            self._leafNode_del(point)
        #左子树空
        elif point.lChild == None and point.rChild != None:
#             print('zuozishu')
            self._rightOrleftEmpty_del(point,point.rChild)
        #右子树空
        elif point.lChild != None and point.rChild == None:
#             print('youzishu')
            self._rightOrleftEmpty_del(point,point.lChild)
        elif point.lChild != None and point.rChild != None:
#             print('both')
            self._noEmpty_del(point)