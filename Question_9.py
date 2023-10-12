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

def max_level_sum(root):
    if not root:
        return None

    max_sum = root.value
    level = 1
    result_level = 1

    queue = [root]
    
    while queue:
        level_sum = sum(node.value for node in queue)
        
        if level_sum > max_sum:
            max_sum = level_sum
            result_level = level
        
        level += 1
        temp = []
        for node in queue:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        queue = temp

    return max_sum, result_level


root = build_binary_tree()

if root is not None:
    max_sum = max_level_sum(root)
    print("Maximum level sum in the binary tree:", max_sum)
else:
    print("Tree is empty.")
