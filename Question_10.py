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

def odd_level(root, level=1):
    if not root:
        return

    if level % 2 == 1:
        print(root.value, end=" ")

    odd_level(root.left, level + 1)
    odd_level(root.right, level + 1)


root = build_binary_tree()

if root is not None:
    print("Nodes at odd levels in the binary tree:")
    odd_level(root)
else:
    print("Tree is empty.")
