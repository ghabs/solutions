# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.sum = sum
        self.answers = []
        def recurse_solve(node, ancestors, total):
            """
            :type node: TreeNode
            :type ancestors: List
            :type total: int
            :rtype: List
            """
            if node is None:
                return False
            ancestors.append(node.val)
            total += node.val
            if (node.left is None) and (node.right is None) and total == self.sum:
                self.answers.append(ancestors)
                return True
            recurse_solve(node.left, ancestors[:], total)
            recurse_solve(node.right, ancestors[:], total)

        recurse_solve(root, [], 0)
        return self.answers
