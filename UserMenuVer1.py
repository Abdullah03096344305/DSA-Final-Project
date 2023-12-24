from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import csv
import sys
from PyQt5.QtWidgets import *
from collections import deque
from subprocess import call

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.setupUi()

    def setupUi(self):
        loadUi(r'UserMenuUI1.ui', self)   
        #self.viewBrandsbtn.clicked.connect(self.on_pushButtonVIEW_click)
        self.LeadingModelsbtn.clicked.connect(self.on_pushButtonVIEWLeading_click)
        self.OrderSummarybtn.clicked.connect(self.on_pushButtonVIEWOrderSummary_click)
        self.Complainbtn.clicked.connect(self.on_pushButtonVIEWComplain_click)    
        self.Branchesbtn.clicked.connect(self.on_pushButtonVIEWBranch_click)       

    #--------------View all Cars button function    
    def on_pushButtonVIEW_click(self):
        call(["python", "BrandsViewUI.py"])  
    #--------------View Leading Cars button function
    def on_pushButtonVIEWLeading_click(self):
        call(["python", "LeadingCars.py"])   
    #--------------Order Summary Button button function 
    def on_pushButtonVIEWOrderSummary_click(self):
        call(["python", "OrderSummaryPY.py"])  
    #--------------Complain button function 
    def on_pushButtonVIEWComplain_click(self):
        call(["python", "ComplainPY.py"])  
    #--------------Branches button function 
    def on_pushButtonVIEWBranch_click(self):
        call(["python", "GraphsPY.py"])            

            

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())  