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

def count_subtrees_with_sum(root, x):
    if not root:
        return 0

    count = 0

    if sum_subtree(root, x):
        count += 1

    count += count_subtrees_with_sum(root.left, x)
    count += count_subtrees_with_sum(root.right, x)

    return count

def sum_subtree(root, x):
    if not root:
        return 0

    left_sum = sum_subtree(root.left, x)
    right_sum = sum_subtree(root.right, x)

    current_sum = root.value + left_sum + right_sum

    return current_sum == x

root = build_binary_tree()

if root is not None:
    target_sum = int(input("Enter the target sum (x): "))
    count = count_subtrees_with_sum(root, target_sum)
    print(f"Number of subtrees with sum {target_sum}: {count}")
else:
    print("Tree is empty.")