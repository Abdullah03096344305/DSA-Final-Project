from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx
import matplotlib.pyplot as plt
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import csv

class CarShowroomGraph:
    def __init__(self):
        self.graph = nx.Graph()
        self.branches = {}  # New attribute to store the branches and their connections

    def add_branch(self, branch_name):
        if branch_name not in self.branches:
            self.branches[branch_name] = []
            self.graph.add_node(branch_name)
        else:
            print(f"Branch '{branch_name}' already exists.")

    def add_connection(self, branch1, branch2):
        if branch1 in self.branches and branch2 in self.branches:
            self.branches[branch1].append(branch2)
            self.branches[branch2].append(branch1)
            self.graph.add_edge(branch1, branch2)
        else:
            print("Invalid branch names. Both branches should exist.")

    def remove_branch(self, branch_name):
        if branch_name in self.branches:
            del self.branches[branch_name]
            self.graph.remove_node(branch_name)
        else:
            print(f"Branch '{branch_name}' not found.")
    def write_to_csv(self, filename='car_showroom.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Branch', 'Connected To'])
            for branch, connections in self.branches.items():
                writer.writerow([branch] + connections)

    def read_from_csv(self, filename='car_showroom.csv'):
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    branch = row[0]
                    connections = row[1:]
                    self.add_branch(branch)
                    for connection in connections:
                        if connection not in self.branches:
                            self.add_branch(connection)
                        self.add_connection(branch, connection)
        except FileNotFoundError:
            print("CSV file not found. Starting with an empty graph.")

    def get_graph_image(self):
        plt.clf()  
        pos = nx.spring_layout(self.graph)
        fig, ax = plt.subplots()
        nx.draw(self.graph, pos, with_labels=True, node_color='pink', edge_color='red', font_color='black', ax=ax)
        canvas = FigureCanvas(fig)
        canvas.draw()
        image = QImage(canvas.buffer_rgba(), canvas.get_width_height()[0], canvas.get_width_height()[1], QImage.Format_RGBA8888)
        return QPixmap.fromImage(image)   

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('GraphsCRUDUI.ui', self)
        self.car_showroom = CarShowroomGraph()
        self.car_showroom.read_from_csv() 
        self.addButton_3.clicked.connect(self.add_new_branch)
        self.deleteButton_3.clicked.connect(self.delete_branch) 
        self.display_graph()

    def add_new_branch(self):
        main_showroom = 'Main Showroom'
        new_branch = self.branchLineEdit_3.text()

        self.car_showroom.add_branch(new_branch)
        self.car_showroom.add_connection(main_showroom, new_branch)

        self.car_showroom.write_to_csv() 
        self.display_graph()

    def delete_branch(self):
        branch_to_delete = self.branchLineEdit_3.text()

        self.car_showroom.remove_branch(branch_to_delete)

        self.car_showroom.write_to_csv() 
        self.display_graph()

    

    def display_graph(self):
     graph_image = self.car_showroom.get_graph_image()
     scene = QGraphicsScene()
     scene.addItem(QGraphicsPixmapItem(graph_image))
     self.graphView.setScene(scene)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
