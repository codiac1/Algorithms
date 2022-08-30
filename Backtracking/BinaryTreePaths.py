# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root , s1):
        if not root.left and not root.right:
            self.ans.append(s1)
            return
        
        s1 = s1 + "->"
        if root.left:
            self.solve(root.left , s1 + str(root.left.val))
        if root.right:
            self.solve(root.right , s1 + str(root.right.val))

            
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:return []
        self.ans = []
        s = str(root.val)
        self.solve(root , s)
        return self.ans