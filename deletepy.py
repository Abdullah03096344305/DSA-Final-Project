from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import csv
from PyQt5.QtWidgets import *

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self._delete(root.left, key)
        elif key > root.data:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.data = self._get_min_value_node(root.right).data
            root.right = self._delete(root.right, root.data)

        return root

    def _get_min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

def delete_data_from_csv(file_path, data_to_delete):
    # Read CSV file and build BST
    bst = BinarySearchTree()
    csv_data = []

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row:
                continue

            name = row[0]
            bst.insert(name)
            csv_data.append(row)

    print(f"BST before deletion: {bst}")

    # Delete data from BST
    bst.delete(data_to_delete)

    print(f"BST after deletion: {bst}")

    # Update CSV file with modified data
    updated_data = [row for row in csv_data if row and row[0] != data_to_delete]

    print(f"Updated data: {updated_data}")

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(updated_data)

    return updated_data
