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

def BFS(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

def DFS(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


root = build_binary_tree()

print("\nBreadth-First Search (BFS) Traversal:")
print(BFS(root))

print("\nDepth-First Search (DFS) Traversal:")
print(DFS(root))
