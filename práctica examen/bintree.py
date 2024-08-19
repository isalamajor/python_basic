
from slist_only_head import SList

class BinaryNode:

    def __init__(self, elem: object, node_left: 'BinaryNode' = None, node_right: 'BinaryNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right

    def __eq__(self, other: 'BinaryNode') -> bool:
        """checks if two nodes (subtrees) are equal o not"""
        return other is not None and self.elem == other.elem and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.elem)


class BinaryTree:
    def __init__(self) -> None:
        """creates an empty binary tree
        I only has an attribute: _root"""
        self._root = None

    def __eq__(self, other: 'BinaryTree') -> bool:
        """checks if two binary trees are equal o not"""
        return other is not None and self._root == other._root

    def size(self) -> int:
        """Returns the number of nodes"""
        return self._size(self._root)

    def _size(self, node: BinaryNode) -> int:
        """return the size of the subtree from node"""
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def height(self) -> int:
        """Returns the height of the tree"""
        return self._height(self._root)

    def _height(self, node: BinaryNode) -> int:
        """return the height of node"""
        if node is None:
            return -1
        else:
            return 1 + max(self._height(node.left), self._height(node.right))

    def preorder(self) -> None:
        """prints the preorder (root, left, right) traversal of the tree"""
        # self.draw()
        print('Preorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._preorder(self._root)
        print()

    def _preorder(self, node: BinaryNode) -> None:
        """prints the preorder (root, left, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            print(node.elem, end=' ')  # end=' ' avoid new line
            self._preorder(node.left)
            self._preorder(node.right)

    def preorder_list(self) -> list:
        """returns a list with the preorder traversal"""
        # self.draw()
        result = []
        self._preorder_list(self._root, result)
        return result

    def _preorder_list(self, node: BinaryNode, pre_list: list) -> None:
        """populates pre_list with the preorder traversal of the subtree node"""
        if node is not None:
            pre_list.append(node.elem)
            self._preorder_list(node.left, pre_list)
            self._preorder_list(node.right, pre_list)

    def postorder(self) -> None:
        """prints the postorder (left, right, root)  traversal of the tree"""
        # self.draw()
        print('Postorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._postorder(self._root)
        print()

    def _postorder(self, node: BinaryNode) -> None:
        """prints the postorder (left, right, root) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.elem, end=' ')  # end=' ' avoid new line

    def postorder_list(self) -> list:
        """returns a list with the postorder traversal of the tree"""
        # self.draw()
        result = []
        self._postorder_list(self._root, result)
        return result

    def _postorder_list(self, node: BinaryNode, post_list: list) -> None:
        """populates post_list with the postorder traversal of the subtree node"""
        if node is not None:
            self._postorder_list(node.left, post_list)
            self._postorder_list(node.right, post_list)
            post_list.append(node.elem)

    def inorder(self) -> None:
        """prints the inorder (left, root, right)  traversal of the tree"""
        # self.draw()
        print('Inorder traversal: ', end=' ')  # end=' ' avoid the newline
        self._inorder(self._root)
        print()

    def _inorder(self, node: BinaryNode) -> None:
        """prints the inorder (left, root, right) traversal of the subtree
        than hangs from node"""
        if node is not None:
            self._inorder(node.left)
            print(node.elem, end=' ')  # end=' ' avoid new line
            self._inorder(node.right)

    def inorder_list(self) -> list:
        """returns a list with the inorder traversal of the tree"""
        # self.draw()
        result = []
        self._inorder_list(self._root, result)
        return result

    def _inorder_list(self, node: BinaryNode, in_list: list) -> None:
        """populates in_list with the inorder traversal of the subtree node"""
        if node is not None:
            self._postorder_list(node.left, in_list)
            in_list.append(node.elem)
            self._postorder_list(node.right, in_list)

    def level_order(self) -> None:
        """prints the level order of the tree. O(n)"""
        if self._root is None:
            print('tree is empty')
        else:
            print("Level order: ", end= ' ')  # avoid the new line

            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.addLast(self._root)
            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.removeFirst() # O(1)
                print(current.elem, end=' ')
                if current.left is not None:
                    list_nodes.addLast(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.addLast(current.right)  # O(1)

            print()

    def level_order_list(self) -> list:
        """prints the level order of the tree. O(n)"""
        result = []
        if self._root is not None:
            # we can use SList with tail and head
            list_nodes = SList()
            list_nodes.addLast(self._root)
            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.removeFirst() # O(1)
                result.append(current.elem)
                if current.left is not None:
                    list_nodes.addLast(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.addLast(current.right)  # O(1)

        return result

    def depth(self, node):
        """ returns the depth of the node; this is the length from
        the root to the node"""
        depth_level = None

        if self._root is None:
            print('Error: the tree is empty')
        else:
            # we can use SList with tail and head
            depth_level = 0

            list_nodes = SList()
            list_nodes.addLast(self._root)

            while len(list_nodes) > 0:  # loop will be executed the size of tree: n
                current = list_nodes.removeFirst() # O(1)
                if current == node:
                    return depth_level
                if current.left is not None:
                    list_nodes.addLast(current.left)  # O(1)
                if current.right is not None:
                    list_nodes.addLast(current.right)  # O(1)
                depth_level += 1

        print('Not found ', node.elem)
        return None

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: BinaryNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def _isBinarySearchTree(self, node):
        if node is None:
            return True

        if node.left is None and node.right is None:
            return True

        if node.left is None and node.right is not None:
            if node.elem < node.right.elem:
                return self._isBinarySearchTree(node.right)

        if node.left is not None and node.right is None:
            if node.elem > node.left.elem:
                return self._isBinarySearchTree(node.left)
        else:
            if node.left.elem < node.elem < node.right.elem:
                return self._isBinarySearchTree(node.left) and self._isBinarySearchTree(node.right)

        return False

    def isBinarySearchTree(self):
        if self._size == 0:
            return True
        node = self._root
        return self._isBinarySearchTree(node)

    def _closest(self, a, node):
        if self._size == 0:
            return
        if node.elem == a:
            return node
        if node.elem > a:
            if node.left is None:
                return node
            if abs(node.elem - a) >= abs(node.left.elem - a):
                child = self._closest(a, node.left)
            else:
                child = node
            return child

        if node.elem < a:
            if node.right is None:
                return node
            if abs(node.elem - a) >= abs(node.right.elem - a):
                child = self._closest(a, node.right)
            else:
                child = node
            return child

    def closest(self, a):
        return self._closest(a, self._root).elem

    def _isSameStructure(self, node1, node2):

        # Cuando ya no hay más nodos que comparar
        if node1 is None and node2 is None:
            return True

        # Cojo los 2 nodos y comparo si tienen los mismos hijos:
        if node1.left is not None and node1.right is not None:
            if node2.left is None or node2.right is None:
                return False
        if node1.left is not None and node1.right is None:
            if node2.left is None or node2.right is not None:
                return False
        if node1.left is None and node1.right is not None:
            if node2.left is not None or node2.right is None:
                return False
        if node1.left is None and node1.right is None:
            if node2.left is not None or node2.right is not None:
                return False
            return True

        return self._isSameStructure(node1.left, node2.left) and self._isSameStructure(node1.right, node2.right)

    def isSameStructure(self, node2):
        if self._size != node2._size:
            return False
        return self._isSameStructure(self._root, node2._root)

    def _mirror(self, nodeA, nodeB):
        if nodeA is None:
            return
        self._mirror(nodeA)
        self._mirror(nodeB)
        aux = nodeA.elem
        nodeA.elem = nodeB.elem
        nodeB.elem = aux


    def mirror(self):
        if self._size() <= 1:
            return
        return self._mirror(self._root)

a = 20
if a == 20:
    tree = BinaryTree()

    newNode = BinaryNode(2)
    left = BinaryNode(3, newNode, None)

    right = BinaryNode(9)

    right.left = BinaryNode(8)
    right.right = BinaryNode(20)
    rrNode = right.right
    rrNode.right = BinaryNode(3)

    root = BinaryNode(5, left, right)

    tree._root = root
    tree.draw()


    #print("BST?:", tree.isBinarySearchTree()) OKAY!!
    #print(tree.closest(24   )) OKAY!!
    #print(tree.isSameStructure(tree2)) OKAY!!