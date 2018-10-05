

class Node(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def create_tree(data):
    root = Node(data[0], None, None)
    root.left = Node(data[1], None, None)
    root.right = Node(data[2], None, None)
    root.left.left = Node(data[3], None, None)
    root.left.right = Node(data[4], None, None)

    return root

def print_inorder(root):
    s = list() # stack
    
    current = root

    while True:
       pass 
 

def main():
    data = [5, 4, 3, 2, 1]
    tree = create_tree(data)
    print_inorder(tree)


if __name__ == "__main__":
    main()
