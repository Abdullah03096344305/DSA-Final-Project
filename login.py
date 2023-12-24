from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QApplication, QLineEdit
from PyQt5.uic import loadUi
from PyQt5.QtGui import QBrush, QColor
import csv
import traceback
from sorting import Sorting
from subprocess import call
from deletepy import delete_data_from_csv
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.stack = []

    def setupUi(self):  
        loadUi(r'Welcomepage2.ui', self)
        self.pushButton_5.clicked.connect(self.signin)
        self.pushButton_6.clicked.connect(self.signup)

    def signin(self):
        second_page = loadUi(r'up.ui')
        second_page.pushButton.clicked.connect(self.signincode)
        second_page.pushButton_2.clicked.connect(self.exitsignin)
        self.setCentralWidget(second_page)
    def open_User_Menu(self):
        call(["python","UserMenuVer1.PY"])    
    def signincode(self):
        username = self.centralWidget().lineEdit_6.text()
        password = self.centralWidget().lineEdit_5.text()

        with open('user_data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Username'] == username and row['Password'] == password:
                    
                    role = row['Role']
                    print("Login successful.")
                    if role.lower() == 'customer':
                         print("I am a customer.")
                         self.open_User_Menu()

                    elif role.lower() == 'seller':
                         print("I am a customer.")
                         self.manager()
                        
                    else:
                        print("Unknown role.")
                    return
            QMessageBox.warning(self, 'Invalid Username or Password', 'Please enter a valid username or password')
            print("User not found.")
    def signup(self):
        second_page = loadUi(r'signUp.ui')
        second_page.signupbutton.clicked.connect(self.signupcode)
        second_page.pushButton_2.clicked.connect(self.exitcode)
        self.setCentralWidget(second_page)        
    def exitsignin(self):
         self.signup()
    def exitcode(self):
        self.signin()

    def signupcode(self):
        second_page = loadUi(r'signUp.ui')
        username = self.centralWidget().lineEdit_6.text()
        if not username.isalpha():
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid username (English alphabet characters only).')
            return

        plaintext_password = self.centralWidget().lineEdit_5.text()
        if not plaintext_password.isdigit():
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid password (numeric characters only).')
            return

        role = self.centralWidget().lineEdit_4.text()
        if role.lower() not in ["seller", "customer"]:
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid role ("seller" or "customer").')
            return

        with open('user_data.csv', 'a', newline='') as csvfile:
            fieldnames = ['Username', 'Password', 'Role']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Check if the CSV file is empty and write header if needed
            if csvfile.tell() == 0:
                writer.writeheader()

            # Write user information without hashing the password
            writer.writerow({'Username': username, 'Password': plaintext_password, 'Role': role})

        print(f"User '{username}' signed up successfully.")
        self.setCentralWidget(second_page)
    def manager(self):
        third_page = loadUi(r'manager1.ui')
        try:
         self.DataTable = third_page.tableWidget
         self.load_DataFromFile('student.csv')
        except Exception as e:
            print(f"An error occurred: {e}")
        third_page.pushButton.clicked.connect(self.on_pushButton_click)
        third_page.pushButton_3.clicked.connect(self.on_pushButton3_click)
        third_page.pushButton_5.clicked.connect(self.on_pushButton5_click)
        third_page.pushButton_2.clicked.connect(self.on_pushButton2_click)
        third_page.pushButton_4.clicked.connect(self.on_pushButton4_click)  
        third_page.pushButton_7.clicked.connect(self.graph_click)
        third_page.pushButton_8.clicked.connect(self.complain_click)
        third_page.pushButton_6.clicked.connect(self.order_click)
          

        self.setCentralWidget(third_page)
 #################################################################################################################
   # add code /////////////////////////////////////////////////////////////////////////////////
    def order_click(self):
         
         fourth_page= loadUi(r'orders.ui') 
         
         try:
          self.DataTable = fourth_page.tableWidget
          self.load_DataFromFile('CartData.csv')
          print("h")
         except Exception as e:
            print(f"An error occurred: {e}") 
         

         fourth_page.pushButton.clicked.connect(self.add)
         fourth_page.pushButton_3.clicked.connect(self.delete)
         fourth_page.pushButton_5.clicked.connect(self.view)
         fourth_page.pushButton_2.clicked.connect(self.edit)
         fourth_page.pushButton_4.clicked.connect(self.search)
         fourth_page.pushButton_7.clicked.connect(self.graph)
         fourth_page.pushButton_8.clicked.connect(self.complain)
         self.setCentralWidget(fourth_page)  



    def on_pushButton_click(self):
        
         fourth_page= loadUi(r'add2.ui')  
         try:
          fourth_page.widget_6.findChild(QPushButton,"pushButton_8").clicked.disconnect()
         except TypeError:
            pass
         fourth_page.widget_6.findChild(QPushButton, "pushButton_8").clicked.connect(self.on_pushButton_7_click)

         fourth_page.pushButton.clicked.connect(self.add)
         fourth_page.pushButton_3.clicked.connect(self.delete)
         fourth_page.pushButton_5.clicked.connect(self.view)
         fourth_page.pushButton_2.clicked.connect(self.edit)
         fourth_page.pushButton_4.clicked.connect(self.search)
         fourth_page.pushButton_7.clicked.connect(self.graph)
         fourth_page.pushButton_8.clicked.connect(self.complain) 
         fourth_page.pushButton_6.clicked.connect(self.order) 
         self.setCentralWidget(fourth_page)  
    def on_pushButton_7_click(self):
       
        name = self.centralWidget().widget_6.findChild(QLineEdit, "lineEdit_13").text()

        if not name.isalpha():
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid name (English alphabet characters only).')
            return
        price = self.centralWidget().widget_6.findChild(QLineEdit, "lineEdit_17").text()
       

        # Validate that only numbers are entered for the year
        if not price.isdigit():
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid price (numeric characters only).')
            return
        city = self.centralWidget().widget_6.findChild(QLineEdit, "lineEdit_15").text()
        if not city.isalpha():
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid city name (English alphabet characters only).')
            return
        model = self.centralWidget().widget_6.findChild(QLineEdit, "lineEdit_12").text()
        if not model.isdigit():
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid price (numeric characters only).')
            return
        cc = self.centralWidget().widget_6.findChild(QLineEdit, "lineEdit_14").text()
        if not price.isdigit():
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid cc (numeric characters only).')
            return
        mode =self.centralWidget().widget_6.findChild(QLineEdit, "lineEdit_16").text()
        if mode.lower() not in ["automatic", "manual"]:
         QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid mode ("Automatic" or "Manual").')
         return
        data_tuple = (name, price, city, model, cc, mode)
        self.stack.append(data_tuple)
        print("Data to save:", self.stack)  # Debug: Print the data before saving
        self.save_data_to_csv()
        self.show_save_message()
    def show_save_message(self):
        QMessageBox.information(self, 'Data Saved', 'Data has been saved successfully!', QMessageBox.Ok)    

    def save_data_to_csv(self):
    # Specify the CSV file path
     
     self.csv_filename = 'adddata.csv'
   
     with open(self.csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Iterate over each tuple in self.stack and write it as a new row
        for data_tuple in self.stack:
            writer.writerow(data_tuple)

    # Clear the stack after saving data
     self.stack = []    
#/////////////////////////////////////////////////////////////
    def on_pushButton3_click(self):
        fourth_page = loadUi('deletecar1.ui')
        
        file_path='a.csv'  
        try:
          self.DataTable = fourth_page.tableWidget
          self.load_DataFromFile('a.csv')
        except Exception as e:
         print(f"An error occurred: {e}")
        
        #name = second_page.findChild(QtWidgets.QLineEdit, "lineEdit_10")
        def delete_handler():
        
         self.delete_click( file_path)
         fourth_page.delete_2.clicked.disconnect()
   
        fourth_page.delete_2.clicked.connect(delete_handler)
        fourth_page.pushButton.clicked.connect(self.add)
        fourth_page.pushButton_3.clicked.connect(self.delete)
        fourth_page.pushButton_5.clicked.connect(self.view)
        fourth_page.pushButton_2.clicked.connect(self.edit)
        fourth_page.pushButton_4.clicked.connect(self.search)
        fourth_page.pushButton_7.clicked.connect(self.graph)
        fourth_page.pushButton_8.clicked.connect(self.complain)
        fourth_page.pushButton_6.clicked.connect(self.order)
        self.setCentralWidget(fourth_page)
    def delete_click(self,  file_path):
     name= self.centralWidget().lineEdit_10.text()
     print(f"Name to delete: {name}")
     try:
       
        updated_data = delete_data_from_csv(file_path, name)
        self.DataTable.setRowCount(len(updated_data))
        for i, row in enumerate(updated_data):
            for j, value in enumerate(row):
                self.DataTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        QMessageBox.information(self, 'Data Deleted', 'Data has been deleted successfully!', QMessageBox.Ok)
     except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()      
#/////////////////////////////////////////////////////
    def on_pushButton5_click(self):
     fourth_page = loadUi('viewui1.ui')

     self.setCentralWidget(fourth_page)

     try:
        self.DataTable = fourth_page.tableWidget
        self.load_DataFromFile('student.csv')

        # Fix here: use findChild to locate the pushButtonofsingle directly under the second_page
        push_button = fourth_page.findChild(QPushButton, "pushButtonofsingle")
        if push_button is not None:
            push_button.clicked.connect(
                lambda: self.trigger_sorting(
                    fourth_page.comboBox.currentText(),  # Pass current index as integer
                    
                    fourth_page.comboBox_2.currentText(),
                    fourth_page.comboBox_3.currentText()
                   
                )
                
            )
        else:
            print("Error: 'pushButtonofsingle' not found.")

        self.sorting_instance = Sorting()
        

     except Exception as e:
        print(f"An error occurred: {e}")
     fourth_page.pushButton.clicked.connect(self.add)
     fourth_page.pushButton_3.clicked.connect(self.delete)
     fourth_page.pushButton_5.clicked.connect(self.view)
     fourth_page.pushButton_2.clicked.connect(self.edit)
     fourth_page.pushButton_4.clicked.connect(self.search) 
     fourth_page.pushButton_7.clicked.connect(self.graph)
     fourth_page.pushButton_8.clicked.connect(self.complain) 
     fourth_page.pushButton_6.clicked.connect(self.order)  

     self.setCentralWidget(fourth_page)
    def convert_columns_to_int(self, data):
        
        for row in data[1:]:
            for i in [1,3, 4]:
                
                row[i] = float(row[i].replace(',', ''))

        return data
    def trigger_sorting(self, sorting_algorithm,column_to_sort,ascending):
      print(column_to_sort)
      
      try:   
        file_path = r'student.csv'
        filename = r'student.csv'

        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
          
          datais = list(csv.reader(file))        
        datais = self.convert_columns_to_int(datais)       
        if len(datais) > 0:
         header = datais[0]
    # Rest of your code that uses 'header'
        else:
         print("The list is empty. Cannot access index 0.")

                
        indextosort=header.index(column_to_sort)
        

       
        data=self.sorting_instance.callingfunction(sorting_algorithm,datais, indextosort,ascending)
        
        with open(r'sorteddata.csv', 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
        self.load_DataFromFile('sorteddata.csv')
        print("Data sorted and saved to 'student.csv'")
        return
      except Exception as e:
            print(f"An error occurred: {e}") 
            traceback.print_exc() 

#////////////////////////////////////////////////////////////////////
    def add(self):
       self.on_pushButton_click()
    def delete(self):
     self.on_pushButton3_click()
    def view(self):
     self.on_pushButton5_click()
    def edit(self):
     self.on_pushButton2_click()
    def search(self):
     self.on_pushButton4_click()
    def graph(self):
       self.graph_click()
    def complain(self):
       self.complain_click() 
    def order(self):
       self.order_click()      

    def on_pushButton2_click(self):
       fourth_page = loadUi('edit1.ui') 
       try:
          
          self.DataTable = fourth_page.findChild(QTableWidget, "tableWidget")
          self.load_DataFromFile('a.csv')
       except Exception as e:
         print(f"An error occurred: {e}")

       fourth_page.search_Button.clicked.connect(self.search_input)
       fourth_page.delete_Button.clicked.connect(self.update_data)
       fourth_page.pushButton.clicked.connect(self.add)
       fourth_page.pushButton_3.clicked.connect(self.delete)
       fourth_page.pushButton_5.clicked.connect(self.view)
       fourth_page.pushButton_2.clicked.connect(self.edit)
       fourth_page.pushButton_4.clicked.connect(self.search)
       fourth_page.pushButton_7.clicked.connect(self.graph)
       fourth_page.pushButton_8.clicked.connect(self.complain)
       fourth_page.pushButton_6.clicked.connect(self.order)
       self.setCentralWidget(fourth_page)
    def search_input(self):
        pname = self.centralWidget().name_text.text()
        with open('student.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['name'] == pname:
                    QMessageBox.information(self, 'Name Found', f'The name {pname} is found!', QMessageBox.Ok)
                    self.centralWidget().price_text.setText(row['price'])
                    self.centralWidget().city_text.setText(row['city'])
                    self.centralWidget().model_text.setText(row['model'])
                    self.centralWidget().cc_text.setText(row['cc'])
                    self.centralWidget().mode_text.setText(row['mode'])
                    return
        QMessageBox.warning(self, 'Name Not Found', f'The name {pname} is not found!', QMessageBox.Ok)
    def update_data(self):
        Pr_name = self.centralWidget().name_text.text()
        Pr_price =self.centralWidget().price_text.text()
        Pr_city = self.centralWidget().city_text.text()
        Pr_model = self.centralWidget().model_text.text()
        Pr_cc = self.centralWidget().cc_text.text()
        Pr_mode = self.centralWidget().mode_text.text()
        data = np.genfromtxt('student.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')
        index_to_update = np.where(data['name'] == Pr_name)[0]
        if index_to_update.size > 0:
            data['price'][index_to_update] = Pr_price
            data['city'][index_to_update] = Pr_city
            data['model'][index_to_update] = Pr_model
            data['cc'][index_to_update] = Pr_cc
            data['mode'][index_to_update] = Pr_mode
            np.savetxt('student.csv', data, delimiter=',', fmt='%s', header=','.join(data.dtype.names),
                       comments='')
            QMessageBox.information(self, 'Update Successful', f'The record for {Pr_name} has been updated!',
                                    QMessageBox.Ok)
            self.centralWidget().name_text.clear()
            self.centralWidget().price_text.clear()
            self.centralWidget().city_text.clear()
            self.centralWidget().model_text.clear()
            self.centralWidget().cc_text.clear()
            self.centralWidget().mode_text.clear()
            self.load_DataFromFile('student.csv')
        else:
            QMessageBox.warning(self, 'Name Not Found', f'The name {Pr_name} is not found!', QMessageBox.Ok)   
 #//////////////////////////////////////////////////////////////////////////////////////
    def on_pushButton4_click(self):
        fourth_page = loadUi('searchui1.ui')
        try:
            self.DataTable = fourth_page.findChild(QTableWidget, "tableWidget")
            self.load_DataFromFile('a.csv')
        except Exception as e:
            print(f"An error occurred: {e}")

        fourth_page.search.clicked.connect(self.searchdata)
       # search_button = fourth_page.widget_5.findChild(QPushButton, "pushButton_4")
       # if search_button is not None:
        # search_button.clicked.connect(self.searchdata)
        #else:
         #print("Could not find the search button.")
        fourth_page.pushButton.clicked.connect(self.add)
        fourth_page.pushButton_3.clicked.connect(self.delete)
        fourth_page.pushButton_5.clicked.connect(self.view)
        fourth_page.pushButton_2.clicked.connect(self.edit)
        fourth_page.pushButton_4.clicked.connect(self.search)
        fourth_page.pushButton_7.clicked.connect(self.graph)
        fourth_page.pushButton_8.clicked.connect(self.complain)
        fourth_page.pushButton_6.clicked.connect(self.order)
        self.setCentralWidget(fourth_page)
    def load_DataFromFile(self, file_path):
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row_number, row in enumerate(csv_reader):
                self.DataTable.setRowCount(self.DataTable.rowCount() + 1)
                for column_number, value in enumerate(row):
                    item = QTableWidgetItem(value)
                    self.DataTable.setItem(row_number, column_number, item)

    def searchdata(self):
        print("a")
        pname = self.centralWidget().lineEdit_2.text()

        try:
            # Reset previous highlights
            self.reset_highlight()
            
            name_hashtable = self.load_csv_into_hashtable('a.csv')
            self.check_name_in_hashtable(pname, name_hashtable)
        except Exception as e:
            print(f"An error occurred: {e}")

    def reset_highlight(self):
        for row in range(self.DataTable.rowCount()):
            for col in range(self.DataTable.columnCount()):
                self.DataTable.item(row, col).setBackground(QBrush(QColor(255, 255, 255)))  # Reset background color

    def load_csv_into_hashtable(self, file_path):
        hashtable = {}
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                name = row[0].strip()
                hashtable[name] = True

        return hashtable

    def check_name_in_hashtable(self, name, hashtable):
        for row in range(self.DataTable.rowCount()):
            item = self.DataTable.item(row, 0)  # Assuming the name is in the first column
            if item and item.text().strip() == name:
                # Highlight the row by changing the background color to #1b9aaa
                for col in range(self.DataTable.columnCount()):
                    self.DataTable.item(row, col).setBackground(QBrush(QColor('#1b9aaa')))
               
                return

        message = f"The name '{name}' does not exist in the CSV file."
        QMessageBox.warning(self, 'Name Not Found', message)

                                             
    def load_DataFromFile(self,filename):
        with open(filename, 'r', encoding='iso-8859-1') as fileInput:
            
            tableRows = 0
            self.data = list(csv.reader(fileInput))
            self.DataTable.setRowCount(len(self.data))
            
            
            for row in self.data:
                
                self.DataTable.setItem(tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
                self.DataTable.setItem(tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
                self.DataTable.setItem(tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
                self.DataTable.setItem(tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
                self.DataTable.setItem(tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))
                self.DataTable.setItem(tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
                
                tableRows += 1   
    def load_Data(self):
        tableRows = 0
        self.DataTable.setRowCount(len(self.data))
        for row in self.data:
            self.DataTable.setItem(tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
            self.DataTable.setItem(tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
            self.DataTable.setItem(tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
            self.DataTable.setItem(tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
            self.DataTable.setItem(tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))
            
            self.DataTable.setItem(tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
            tableRows += 1
#################################################################################################
    def graph_click(self):
       call(["python","GraphsCRUDPY.py"])
    def complain_click(self):
       call(["python","complainmanager.py"])    
                                          

if __name__ == '__main__':
    app = QApplication([])  # Create a new QApplication instance
    window = MainWindow()
    window.show()
    app.exec_()
