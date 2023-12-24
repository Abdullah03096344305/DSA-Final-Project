from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import csv
import sys
from PyQt5.QtWidgets import *
from collections import deque
from subprocess import call

def open_py_file():
    call(["python", "leads.py"])

open_py_file()    