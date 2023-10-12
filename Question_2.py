class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_binary_tree():
    print("Enter integers to build a binary tree.")
    print("\nEnter done to stop.")
    
    root = None
    while True:
        user_input = input("\nEnter a value to insert (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        value = int(user_input)
        root = insert(root, value)
    return root

def insert(root, value):
    if root is None:
        return Tree(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def find_height(root):
    if root is None:
        return 0
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    return max(left_height, right_height) + 1


root = build_binary_tree()

if root is not None:
    height = find_height(root)
    print("Height of the tree:", height)
else:
    print("Tree is empty.")

