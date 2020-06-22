#Write a Python program to find Kth Smallest Element in a BST

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kth_smallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            break
        root = root.right
    return root.val

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(13)
root.right.right = TreeNode(17)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(4)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(9)
root.right.left.left = TreeNode(11)
root.right.left.right = TreeNode(14)
root.right.right.left = TreeNode(16)
root.right.right.right = TreeNode(18)

print(kth_smallest(root, 1))
print(kth_smallest(root, 2))
print(kth_smallest(root, 3))
print(kth_smallest(root, 4))
print(kth_smallest(root, 5))
print(kth_smallest(root, 6))
print(kth_smallest(root, 7))
print(kth_smallest(root, 8))
print(kth_smallest(root, 9))
print(kth_smallest(root, 10))
print(kth_smallest(root, 11))
print(kth_smallest(root, 12))
print(kth_smallest(root, 13))
print(kth_smallest(root, 14))
print(kth_smallest(root, 15))
