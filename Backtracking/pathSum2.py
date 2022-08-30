# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self ,root , target , path ):
        if not root.left and not root.right and root.val == target:
            self.ans.append(path)
        path.append(root.val)
        if root.left:
            self.solve(root.left , target-root.val , path[:] )
        if root.right:
            self.solve(root.right , target-root.val , path[:] )
        
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        
        self.ans =[]
        path = []
        self.solve(root , targetSum , path)
        
        return self.ans 
    