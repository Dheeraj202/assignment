# Name:- Dheeraj Sharma  
# SID:- 21107025
class BSTNode:
    def __init__(self,data=None):
        self.data=data
        self.rightChild=None
        self.leftChild=None
def insertNode(rootNode,value):
    if rootNode.data==None:
        rootNode.data=value
    else:
        if rootNode.data>=value:
            if rootNode.leftChild is None:
                rootNode.leftChild=BSTNode(value)
            else:
                rootNode=insertNode(rootNode.leftchild,value)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild=BSTNode(value)
            else:
                rootNode=insertNode(rootNode.rightChild,value)
    return rootNode
def minValueNode(rootNode):
    currentNode=rootNode
    while currentNode.leftChild is not None:
        currentNode=currentNode.leftChild
    return currentNode
def deleteNode(rootNode,value):
    if rootNode is None:
        return rootNode
    if rootNode.data>value:
        rootNode.leftChild=deleteNode(rootNode.leftChild,value)
    if rootNode.data<value:
        rootNode.rightChild=deleteNode(rootNode.rightChild,value)
    else:
        if rootNode.leftChild is None:
            temp=rootNode.rightChild
            rootnode=None
            return temp
        if rootNode.rightChild is None:
            temp=rootNode.leftChild
            rootNode=None
            return temp
        temp= minValueNode(rootNode.rightNode)
        rootNode.data=temp.data
        rootNode=deleteNode(rootNode.rightNode,temp.data)

    return rootNode
def arrayDelete(arr,value):
    arr1=[]
    for i in arr:
        if i == value:
            continue
        arr1.append(i)
    return arr1
arr=[]
a=int(input("Enter the no of elements"))
for i in range(0,a):
    arr.append(int(input()))
bstNode=BSTNode()
for i in arr:
    bstNode=insertNode(bstNode,i)
delValue=int(input("Enter the value to be deleted: "))
arr=arrayDelete(arr,delValue)
bstNode=deleteNode(bstNode,delValue)
 #Space Complexity of deleting via Binary Search TREE:- O(log N)
 # Space Complexity of Delteing via array:- O(N)
 # So deleting values via using Binary search Tree is better than via Arrays with respect to space complexity







        
