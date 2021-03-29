from idlelib.tree import TreeNode
from typing import List


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        index = 0
        flag = False
        result = []

        def pre_order(node):
            if node is None:
                return
            nonlocal index
            if node.val != voyage[index]:
                nonlocal flag
                flag = True
            index += 1
            if node.right is not None and node.left is not None and node.right.val == voyage[index]:
                nonlocal result
                result.append(node.val)
                pre_order(node.right)
                pre_order(node.left)
            else:
                pre_order(node.left)
                pre_order(node.right)

        pre_order(root)
        if flag:
            return [-1]
        else:
            return result
