import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import pandas as pd
class Car:
    def __init__(self, car_name, vin, numberPlate, model, price, engine):
        self.car_name = car_name
        self.vin = vin
        self.numberPlate = numberPlate
        self.model = model
        self.price = price
        self.engine = engine
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.load_DataFromFile('CartData.csv')
        self.DataTable.setColumnWidth(0, 50)
        self.DataTable.setColumnWidth(1, 150)
        self.DataTable.setColumnWidth(2, 150)
        self.DataTable.setColumnWidth(3, 150)
        self.DataTable.setColumnWidth(4, 150)
        self.DataTable.setColumnWidth(5, 150)
        self.RemoveFromCartbtn.clicked.connect(self.Remove_From_Cart)
        self.cart_list = LinkedList()  # Linked list to manage the cart
        total_price = self.calculate_total_price()
        self.lineEdit.setText(str(total_price))

    def setupUi(self):
        loadUi(r'OrderSummaryUI1.ui', self)

    def load_DataFromFile(self, filename):
        try:
            with open(filename, 'r', encoding='iso-8859-1') as fileInput:
                self.data = list(csv.reader(fileInput))
                self.DataTable.setRowCount(len(self.data))

                for row_index, row in enumerate(self.data):
                    for col_index, value in enumerate(row):
                        item = QtWidgets.QTableWidgetItem(value)
                        self.DataTable.setItem(row_index, col_index, item)
        except Exception as e:
            print(f"An error occurred: {e}")

    def closeEvent(self, event):
        self.save_TableDataToFile()
        event.accept()

    def Remove_From_Cart(self):
        selected_items = self.DataTable.selectedItems()

        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "No Car Selected", "Please select a car to Remove from the cart.")
            return

        row = self.DataTable.currentRow()
        car_name = self.DataTable.item(row, 0).text()
        car_vin = self.DataTable.item(row, 1).text()

        # Remove the selected car from the cart
        current = self.cart_list.head
        prev = None
        while current:
            if current.data.car_name == car_name and current.data.vin == car_vin:
                if prev:
                    prev.next = current.next
                else:
                    self.cart_list.head = current.next
                break
            prev = current
            current = current.next

        # Remove the selected row from the DataTable
        self.DataTable.removeRow(row)
        total_price = self.calculate_total_price()
        self.lineEdit.setText(str(total_price))  

    def save_TableDataToFile(self):
        try:
            with open('CartData.csv', 'w', newline='', encoding='iso-8859-1') as cartFile:
                cart_writer = csv.writer(cartFile)
                for row in range(self.DataTable.rowCount()):
                    cart_data = [
                        self.DataTable.item(row, 0).text(),
                        self.DataTable.item(row, 1).text(),
                        self.DataTable.item(row, 2).text(),
                        self.DataTable.item(row, 3).text(),
                        self.DataTable.item(row, 4).text(),
                        self.DataTable.item(row, 5).text(),
                    ]
                    cart_writer.writerow(cart_data)

        except Exception as e:
            print(f"An error occurred while updating the CSV file: {e}")
    def calculate_total_price(self):
        total_price = 0
        current = self.cart_list.head
        while current:
            # Assuming that the price is in the 2nd column (index 1)
            total_price += float(current.data[1])
            current = current.next
        return total_price    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
