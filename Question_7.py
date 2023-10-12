class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_perfect_binary_tree(level):
    if level == 0:
        return None
    value = int(input(f"Enter an integer for level {level}: "))
    root = Tree(value)
    root.left = build_perfect_binary_tree(level - 1)
    root.right = build_perfect_binary_tree(level - 1)
    return root

def sum_all_nodes(root):
    if not root:
        return 0
    return root.value + sum_all_nodes(root.left) + sum_all_nodes(root.right)


level = int(input("Enter the level of the perfect binary tree: "))
root = build_perfect_binary_tree(level)

if root is not None:
    total_sum = sum_all_nodes(root)
    print("Sum of all nodes in the perfect binary tree:", total_sum)
else:
    print("Tree is empty.")