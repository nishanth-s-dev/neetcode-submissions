# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_one = find_path(root, p)
        path_two = find_path(root, q)
        path_two_set = set(path_two)
        for node in path_one:
            if node in path_two_set:
                return node
        return TreeNode()
        

def find_path(root, target):
    if root is None:
        return []
    if root.val == target.val:
        return [ root ]

    left_path = find_path(root.left, target)
    if left_path:
        return left_path + [ root ]
    
    right_path = find_path(root.right, target)
    if right_path:
        return right_path + [ root ]
    
    return []
