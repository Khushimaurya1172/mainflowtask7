class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def zigzag_level_order(root):
    if not root:
        return []
    result, level, left_to_right = [], [root], True
    while level:
        values = [node.val for node in level][::1 if left_to_right else -1]
        result.append(values)
        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
        left_to_right = not left_to_right
    return result

# Manually build a tree from user input (example structure)
def build_tree():
    val = input("Enter root value (or empty to stop): ")
    if not val:
        return None
    node = TreeNode(int(val))
    print(f"Enter left child of {val}:")
    node.left = build_tree()
    print(f"Enter right child of {val}:")
    node.right = build_tree()
    return node

print("Build the binary tree:")
root = build_tree()
print("Zigzag Traversal:", zigzag_level_order(root))
