

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, data):
        self.root = None
        self.data = data
        

    def build(self):
        """
           1. Left most element in preorder traversal is root of a tree
           2. Left most element in inorder traversal is left most leaf of a tree
        """
        pass





def main():
    data = map(int, input().split(','))
    # inorder -> D B E A F C
    # preorder -> A B D E C F
    tree = BinaryTree(data)



if __name__ == "__main__":
    main()
