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

def sum_left_leaves(root):
    if not root:
        return 0

    left_sum = 0

    if root.left and not root.left.left and not root.left.right:
        left_sum += root.left.value

    left_sum += sum_left_leaves(root.left)
    left_sum += sum_left_leaves(root.right)

    return left_sum


root = build_binary_tree()

if root is not None:
    left_leaves_sum = sum_left_leaves(root)
    print("Sum of left leaves:", left_leaves_sum)
else:
    print("Tree is empty.")