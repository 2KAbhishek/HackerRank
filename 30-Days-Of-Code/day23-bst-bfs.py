import sys
import collections

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        if not root:
            return None

        queue = collections.deque()
        queue.append(root)

        while queue:
            current = queue.popleft()
            print(current.data, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

