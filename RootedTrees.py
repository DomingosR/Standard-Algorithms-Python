# Import section
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

def constructTree(nums):
    if not nums or not nums[0]:
        return None
    
    root = TreeNode(nums[0])
    i, n = 1, len(nums)
    nodeQueue = deque()
    nodeQueue.appendleft(root)

    while i < n:
        currentNode = nodeQueue.pop()
        if nums[i]:
            currentNode.left = TreeNode(nums[i])
            nodeQueue.appendleft(currentNode.left)
        i += 1
        if nums[i]:
            currentNode.right = TreeNode(nums[i])
            nodeQueue.appendleft(currentNode.right)
        i += 1
    
    return root

def printTree(root):
    if not root:
        return []
    
    treeList = [root.val]
    nodeQueue = deque([root])
    leafCount = 0

    while nodeQueue:
        currentNode = nodeQueue.pop()
        leftNode, rightNode = currentNode.left, currentNode.right

        treeList.append(leftNode.val if leftNode else None)
        treeList.append(rightNode.val if rightNode else None)

        leafCount += 0 if leftNode or rightNode else 1

        if leftNode:
            nodeQueue.appendleft(leftNode)

        if rightNode:
            nodeQueue.appendleft(rightNode)

    return treeList[: (-2)*leafCount]

def inOrderTraversal(root):
    inOrder = []

    def processNode(node):
        if node:
            if node.left:
                processNode(node.left)
            inOrder.append(node.val)
            if node.right:
                processNode(node.right)
    
    processNode(root)
    return inOrder

def preOrderTraversal(root):
    preOrder = []

    def processNode(node):
        if node:
            preOrder.append(node.val)
            if node.left:
                processNode(node.left)
            if node.right:
                processNode(node.right)
    
    processNode(root)
    return preOrder

def postOrderTraversal(root):
    postOrder = []

    def processNode(node):
        if node:
            if node.left:
                processNode(node.left)
            if node.right:
                processNode(node.right)
            postOrder.append(node.val)

    processNode(root)
    return postOrder

def deleteVal(root, key):
    canDelete = isBST(root)

    if not canDelete:
        print("Error: given tree is not a BST.")
        return 
    
    def processNode(node, target):
        if not node:
            return None

        if target == node.val:
            if not node.left:
                return node.right
            
            if not node.right:
                return node.left
            
            auxNode = node.right
            while auxNode.left:
                auxNode = auxNode.left
                
            node.val = auxNode.val
            node.right = processNode(node.right, node.val)
                
        elif target < node.val:
            node.left = processNode(node.left, target)
            
        else:
            node.right = processNode(node.right, target)
        
        return node
    
    return processNode(root, key)

def isBST(root):
    def processNode(node):
        if not (node.left or node.right):
            return (True, node.val, node.val)

        minBelow, maxBelow = node.val, node.val

        if node.left:
            isBSTLeft, minLeft, maxLeft = processNode(node.left)
            if (not isBSTLeft) or maxLeft >= node.val:
                return (False, None, None)
            else:
                minBelow = minLeft
        
        if node.right:
            isBSTRight, minRight, maxRight = processNode(node.right)
            if (not isBSTRight) or minRight <= node.val:
                return (False, None, None)
            else:
                maxBelow = maxRight

        return (True, minBelow, maxBelow)
    
    return processNode(root)[0]

# Test Code
treeValues = [4, 2, 6, 1, 3, 5, 7]
root = constructTree(treeValues)
print(printTree(root))
print(inOrderTraversal(root))
print(preOrderTraversal(root))
print(postOrderTraversal(root))
print(isBST(root))
root = deleteVal(root, 2)
print(printTree(root))

treeValues2 = [1, 2, 3]
root2 = constructTree(treeValues2)
print(printTree(root2))
print(isBST(root2))
root2 = deleteVal(root2, 2)

