# -*- coding: utf-8 -*-

from bintree import BinaryNode
from bintree import BinaryTree


class BinarySearchTree(BinaryTree):

    def search(self, elem: object) -> BinaryNode:
        """Returns the node whose elem is elem"""
        return self._search(self._root, elem)

    def _search(self, node: BinaryNode, elem: object) -> BinaryNode:
        """Recursive function"""
        if node is None or node.elem == elem:
            return node
        elif elem < node.elem:
            return self._search(node.left, elem)
        elif elem > node.elem:
            return self._search(node.right, elem)

    def searchit(self, elem: object) -> BinaryNode:
        """iterative function"""
        node = self._root
        while node:
            if node.elem == elem:
                # we have found it!!! we can return it and leave the function
                return node

            if elem < node.elem:
                node = node.left
            else:
                node = node.right
        return node

    def insert(self, elem: object) -> None:
        self._root = self._insert(self._root, elem)

    def _insert(self, node: BinaryNode, elem: object) -> BinaryNode:
        if node is None:
            return BinaryNode(elem)

        if node.elem == elem:
            print('Error: elem already exist ', elem)
            return node

        if elem < node.elem:
            node.left = self._insert(node.left, elem)
        else:
            # elem>node.elem
            node.right = self._insert(node.right, elem)
        return node

    def insert_iterative(self, elem: object) -> None:
        """iterative version of insert"""
        if self._root is None:
            self._root = BinaryNode(elem)  # if tree is empty, new node will be the root
            return  # we can leave!!!

        node = self._root  # to search the place
        not_exist = True
        while not_exist and node:
            if elem < node.elem:
                node = node.left
                if node.left is None: # this is the place to insert it
                    node.left = BinaryNode(elem)
            elif elem > node.elem:
                node = node.right
                if node.right is None:  # this is the place to insert it
                    node.right = BinaryNode(elem)
            else:  # elem == node.elem
                print('duplicate elements not allowed!!')
                not_exist = False

    def _minimum_node(self, node: BinaryNode) -> BinaryNode:
        """returns the  node with the smallest elem
        in the subtree node.
        This is the node that is furthest to the left"""
        min_node = node
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    def remove(self, elem: object) -> None:
        # update the root with the new subtree after remove elem
        self._root = self._remove(self._root, elem)

    def _remove(self, node: BinaryNode, elem: object) -> BinaryNode:
        """It recursively searches the node. When the node is
        found, the node has to be removed"""
        if node is None:
            print(elem, ' not found')
            return node

        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:
            # node.elem == elem, node is the node to remove!!!
            if node.left is None and node.right is None:
                # Case 1: node is a leave
                return None

            # Case 2: node only has a child, so the function has to return it
            if node.left is None:
                # It only has the right child
                return node.right

            elif node.right is None:
                # It only has the left child
                return node.left
            else:
                # Case 3: node.left!=None and node.right!=None
                # we search the smallest node from its right child
                successor = self._minimum_node(node.right)
                # we replace elem with the elem of the successor
                node.elem = successor.elem
                # now, we have to remove successor from the right child
                node.right = self._remove(node.right, successor.elem)

        return node

    def _lwc(self, a, b, node, parent):

        nodeA = self.search(a)
        if nodeA is None:
            return

        nodeB = self.search(b)
        if nodeB is None:
            return


    def lwc(self, a, b):
        if self._size == 0:
            return None
        if a == b:
            return a
        if a > b:  # I want "a" to be the smallest and "b" the greatest number.
            aux = a
            a = b
            b = aux
        return self._lwc(a, b, self._root, None)

    def _check_cousins(self, a, b, node):
        if node is None:
            return False
        if node.left is None or node.right is None:
            return False

        if (node.left.left.elem == a or node.right.right.elem == a)\
            and (node.right.right.elem == b or node.right.left.elem == b):
            return True
        return self._check_cousins(a, b, node.left) and self._check_cousins(a, b, node.right)


    def check_cousins(self, a, b):
        if self.search(a) is None or self.search(b) is None or a == b:
            return False
        if a > b:
            aux = a
            a = b
            b = aux
        return self._check_cousins(a, b, self._root)

    def _is_zig_zag(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return False
        if node.left is not None:
            if node.left.left is None:
                return self._is_zig_zag(node.left)
        if node.right is not None:
            if node.right.right is None:
                return self._is_zig_zag(node.right)
        return False

    def is_zig_zag(self):
        if self.size() <= 2:
            return False
        return self._is_zig_zag(self._root)

    def _is_left_odd_right_even(self, node):
        if node is None:
            return True
        if (node.left is None or node.left.elem % 2 != 0) and (node.right is None or node.right.elem % 2 == 0):
            return self._is_left_odd_right_even(node.left) and self._is_left_odd_right_even(node.right)
        return False

    def is_left_odd_right_even(self):
        if self.size == 1:
            return True
        return self._is_left_odd_right_even(self._root)

    def _update_adding_left_child(self, node, sum = 0):
        if node.left is None:
            return node.elem
        if node.left is not None:
            # Recursion for right subtree:
            sum = self._update_adding_left_child(node.right, sum)

            # Recursion for left subtree:
            node.elem += self._update_adding_left_child(node.left, sum)

        return sum

    def update_adding_left_child(self):
        return self._update_adding_left_child(self._root)

    def _get_non_leaves(self, node, list1):
        if node.left is None and node.right is None:
            return
        if node.right is not None:
            self._get_non_leaves(node.right, list1)
            list1.append(node.elem)
        if node.left is not None:
            self._get_non_leaves(node.left, list1)
            if node.elem not in list1:
                list1.append(node.elem)
        return list1

    def get_non_leaves(self):
        if self.size() <= 1:
            return []
        return self._get_non_leaves(self._root, [])

def array2bst(lst_values: list) -> BinarySearchTree:
    """ gets a sorted list and creates a balanced bst"""
    tree = BinarySearchTree()
    if lst_values and len(lst_values) >= 1:
        # lst_values.sort()
        _array2bst(lst_values, 0, len(lst_values) - 1, tree)
    return tree

def _array2bst(lst_values: list, start: int, end: int, tree: BinarySearchTree) -> None:
    if start <= end:
        middle = (start + end) // 2
        tree.insert(lst_values[middle])
        _array2bst(lst_values, start, middle - 1, tree)
        _array2bst(lst_values, middle + 1, end, tree)

tree1 = BinarySearchTree()

newNode = BinaryNode(20)
left = BinaryNode(3, newNode, BinaryNode(10))
right = BinaryNode(15)

right.left = BinaryNode(7)
right.right = BinaryNode(17)
rrNode = right.right
rrNode.right = BinaryNode(19)
root = BinaryNode(20, right, BinaryNode(30))
tree1._root = root
#tree1.draw()
# print(tree.check_cousins(3, 30)) OKAY!!
# print(tree1.is_zig_zag()) OKAY!!
# print(tree1.is_left_odd_right_even()) OKAY!!
# print(tree1.update_adding_left_child()) NOPE
# tree1.draw()
# print(tree1.get_non_leaves()) OKAY!!
tree2 = array2bst([1,2,3,4,5,6,7,8,9])
tree2.draw()
print("HI")