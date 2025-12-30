from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return max(left, right) + 1


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is None:
        return 0
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if ((p.val < root.val) and (q.val < root.val)):
        return left
    elif((p.val > root.val) and (q.val > root.val)):
        return right
    else:
        return root

