import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import csv

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('ComplainUI.ui', self)  
        self.Confirmbtn.clicked.connect(self.Confirm_btn_click_event)     

    def Confirm_btn_click_event(self):
        self.AddComplainsToFileAndQueue()

    def AddComplainsToFileAndQueue(self):
        element = self.ComplainBox.toPlainText().strip()  # Remove leading and trailing whitespace
        if not element:
            QMessageBox.warning(self, 'Empty Complaint', 'Please fill out the complaint form.')
            return
        
        q.enqueue(element)
        q.display() 
        with open('ComplainsData.csv', 'a+', encoding="utf-8", newline="") as fileInput:
            writer = csv.writer(fileInput)
            writer.writerow([element])         

q = Queue()
q.display()
print(q.size())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
