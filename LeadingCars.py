from PyQt5 import QtCore, QtGui, QtWidgets, uic
import csv
from datetime import datetime
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog

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

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('LeadingCarsUI.ui', self)
        self.DataTable.setColumnWidth(0, 50)
        self.DataTable.setColumnWidth(1, 150)
        self.DataTable.setColumnWidth(2, 150)
        self.DataTable.setColumnWidth(3, 150)
        self.DataTable.setColumnWidth(4, 150)
        self.DataTable.setColumnWidth(5, 150)
        self.load_DataFromFile('student.csv')
        self.cart_list = LinkedList()  # Linked list to manage the cart
        self.AddtoCartbtn.clicked.connect(self.add_to_cart)
       
       
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

    def update_cart_ui(self):
        try:
            # Open the file in append mode to add the new cart data
            with open('CartData.csv', 'a', newline='', encoding='iso-8859-1') as cartFile:
                cart_writer = csv.writer(cartFile)

                # Write the header if the file is empty
                if cartFile.tell() == 0:
                    header = ["Car Name", "VIN", "Number Plate", "Model", "Price", "Engine"]
                    cart_writer.writerow(header)

                # Iterate over the cart list and write each car's data
                current = self.cart_list.head
                while current:
                    car_data = [
                        current.data.car_name,
                        current.data.vin,
                        current.data.numberPlate,
                        current.data.model,
                        current.data.price,
                        current.data.engine
                    ]
                    cart_writer.writerow(car_data)
                    current = current.next

        except Exception as e:
            print(f"An error occurred while updating the cart UI: {e}")
    def load_Data(self):
        tableRows = 0
        self.DataTable.setRowCount(len(self.data))
        for row in self.data:
            self.DataTable.setItem(tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
            self.DataTable.setItem(tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
            self.DataTable.setItem(tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
            self.DataTable.setItem(tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
            self.DataTable.setItem(tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))
            if int(row[5].split(":")[0]) >= int(24):
                row[5] = row[5][0:len(row[5]) - 1]
            self.DataTable.setItem(tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
            tableRows += 1
    def add_to_cart(self):
        
        selected_items = self.DataTable.selectedItems()
    
        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "No Car Selected", "Please select a car to add to the cart.")
            return
    
        row = self.DataTable.currentRow()
        car_name = self.DataTable.item(row, 0).text()
        car_vin = self.DataTable.item(row, 1).text()
        car_numberPlate = self.DataTable.item(row, 2).text()
        car_model = self.DataTable.item(row, 3).text()
        car_price = self.DataTable.item(row, 4).text()
        car_engine = self.DataTable.item(row, 5).text()
    
        # Check if the car is already in the cart
        current = self.cart_list.head
        while current:
            if current.data.car_name == car_name and current.data.vin == car_vin:
                QtWidgets.QMessageBox.warning(self, "Car Already in Cart", "The selected car is already in the cart.")
                return
            current = current.next
    
        # Create a Car object and add it to the linked list (cart)
        new_car = Car(car_name, car_vin, car_numberPlate, car_model, car_price, car_engine)
        self.cart_list.append(new_car)
    
        try:
            with open('CartData.csv', 'a', newline='', encoding='iso-8859-1') as cartFile:
                cart_writer = csv.writer(cartFile)
                cart_data = [
                    car_name,
                    car_vin,
                    car_numberPlate,
                    car_model,
                    car_price,
                    car_engine
                ]
                cart_writer.writerow(cart_data)
    
        except Exception as e:
            print(f"An error occurred while updating the cart UI: {e}")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
