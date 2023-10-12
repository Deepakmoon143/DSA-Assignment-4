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

def pre_order(root):
    if root:
        print(root.value, end=" ")
        pre_order(root.left)
        pre_order(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.value, end=" ")


root = build_binary_tree()

print("\nPreorder Traversal:")
pre_order(root)

print("\nInorder Traversal:")
inorder(root)

print("\nPostorder Traversal:")
post_order(root)
