class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Tree(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

root = None
while True:
    user_input = input("Enter a value to insert (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    
    value = int(user_input)
    root = insert(root, value)
print("Inorder Traversal:")
inorder(root)

search_key = int(input("Enter a value to search for in the tree: "))

if search(root, search_key):
    print(f"{search_key} found in the tree.")
else:
    print(f"{search_key} not found in the tree.")
