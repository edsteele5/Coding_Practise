# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        runner = root
        vals = []
        queue.append(root)
        if root is None:
            return []
        while queue:
            child_queue = deque()
            prev = -1
            while queue:
                curr = queue.popleft()
                if curr.left is not None:
                    child_queue.append(curr.left)
                if curr.right is not None:
                    child_queue.append(curr.right)
                prev = curr
            vals.append(prev.val)
            queue = child_queue


       
        
        

        return vals
        