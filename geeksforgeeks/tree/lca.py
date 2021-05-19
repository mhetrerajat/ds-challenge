class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_path(root, path, key):
    if root is None:
        return False

    path.append(root.data)

    if root.data == key:
        return True

    if (root.left is not None and find_path(root.left, path, key)) or (root.right is not None and find_path(root.right, path, key)):
        return True

    path.pop()
    return False

def lca(n1, n2, root):
    n1_path, n2_path= [], []
    
    is_n1_path_exists = find_path(root, n1_path, n1)
    is_n2_path_exists = find_path(root, n2_path, n2)

    if not is_n1_path_exists or not is_n2_path_exists:
        return -1

    i = 0
    while i < len(n1_path) and i < len(n2_path):
        if n1_path[i] != n2_path[i]:
            break
        i += 1

    return n1_path[i-1]

    

def main(root):
    T = [
        ((10, 14), 12),
        ((14, 8), 8),
        ((10, 22), 20)
    ]
    for (n1, n2), answer in T:
        assert lca(n1, n2, root) == answer


if __name__ == "__main__":
    # Generate tree
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    main(root)
