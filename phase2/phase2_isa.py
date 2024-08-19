# from binarysearchtree import BinarySearchTree
from bst import BinarySearchTree
from bst import BinaryNode

# Solución de Isa :^)
class AVLTree(BinarySearchTree):

    # Override insert method from base class to keep it as AVL
    def insert(self, elem: object) -> None:
        """inserts a new node, with key and element elem"""
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        """gets a node, searches the place to insert a new node with element e (using super()._insert),  and then,
        the function has to balance the node returned by the function super.()_insert"""
        node = super()._insert(node, elem)
        node = self._rebalance(node)
        return node

    # Override remove method from base class to keep it as AVL
    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """ gets a node, searches the node with element elem in the subtree that hangs down node , and
        then remove this node (using super()._remove). After this, the function has to balance the node returned by the function super()._remove"""
        node = super()._remove(node, elem)
        node = self._rebalance(node)
        return node

    def _rebalance(self, node: BinaryNode) -> BinaryNode:
        """ gets node and balances it"""
        if node is None:  # If we get to the end of the tree, we do nothing else
            return
        # Right rotation:
        if self._height(node.left) - self._height(node.right) > 1:
            if node.left.left is None:  # ZigZag, left-right rotation:
                aux = node.left
                node.left = aux.right
                node.left.left = aux
                aux.right = None
            lost_child = node.left.right
            aux = node
            node = node.left
            node.right = aux
            aux.left = lost_child
        # Left rotation:
        if self._height(node.right) - self._height(node.left) > 1:
            if node.right.right is None:  # ZigZag, right-left rotation:
                aux = node.right
                node.right = aux.left
                node.right.right = aux
                aux.left = None
            lost_child = node.right.left  # If a node is left hanging, we will recue it later
            aux = node
            node = node.right
            node.left = aux
            aux.right = lost_child

        # No rotation needed, children may need it:
        else:
            if node.left is not None:
                node.left = self._rebalance(node.left)
            if node.right is not None:
                node.right = self._rebalance(node.right)
        return node
