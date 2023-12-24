import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QTextEdit
from PyQt5.QtCore import Qt
import csv

class ComplaintQueue:
    def __init__(self):
        self.queue = []

    def add_complaint(self, complaint):
        self.queue.append(complaint)
        print(f"Complaint '{complaint}' added to the queue.")

    def process_complaint(self):
        if not self.is_empty():
            processed_complaint = self.queue.pop(0)
            print(f"Processing complaint: '{processed_complaint}'")
            return processed_complaint
        else:
            print("No complaints in the queue.")

    def is_empty(self):
        return len(self.queue) == 0

    def view_queue(self):
        print("Current complaints in the queue:")
        for complaint in self.queue:
            print(f"- {complaint}")

class ComplaintWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("COMPLAINTS FROM CUSTOMERS")
        self.setGeometry(100, 100, 500, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        title_label = QLabel("Customer Complaints", self)
        title_label.setStyleSheet("background-color: #35424a; color: white; font-size: 24px; font-weight: bold; padding: 10px; border-top-left-radius: 5px; border-top-right-radius: 5px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Create a ComplaintQueue instance
        self.complaint_queue = ComplaintQueue()

        # Load complaint data from CSV file into the queue
        self.load_complaint_data_from_csv("ComplainsData.csv")

        # Create complaint boxes dynamically
        self.complaint_widgets = []
        for _ in range(len(self.complaint_queue.queue)):
            complaint_widget = QWidget(self)
            complaint_widget.setStyleSheet("background-color: #e1e5ea; border: 1px solid #35424a; border-radius: 5px; margin: 5px;")

            text_edit = QTextEdit(self)
            text_edit.setStyleSheet("background-color: #ffffff; border: 1px solid #35424a; border-radius: 5px;")
            text_edit.setPlainText(self.complaint_queue.process_complaint())

            button = QPushButton("Resolve", self)
            button.setStyleSheet("background-color: #1B9AAA; color: white; border: none; border-radius: 3px; padding: 6px 12px; margin-top: 8px; font-size: 14px;")
            button.clicked.connect(self.resolve_complaint)

            complaint_layout = QVBoxLayout(complaint_widget)
            complaint_layout.addWidget(text_edit)
            complaint_layout.addWidget(button)

            layout.addWidget(complaint_widget)
            self.complaint_widgets.append(complaint_widget)

        return_button = QPushButton("Return", self)
        return_button.setStyleSheet("background-color: #1B9AAA; color: white; border: none; border-radius: 3px; padding: 6px 12px; margin-top: 8px; border-bottom-left-radius: 5px; border-bottom-right-radius: 5px; font-size: 14px;")
        return_button.clicked.connect(self.return_to_main)

        layout.addWidget(return_button)

    def load_complaint_data_from_csv(self, csv_file):
        with open(csv_file, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                self.complaint_queue.add_complaint(row[0])

    def resolve_complaint(self):
        # Remove the complaint from the UI
        widget = self.sender().parentWidget()
        widget.setParent(None)
        self.complaint_widgets.remove(widget)

        # Update the CSV file with the modified complaint data
        self.save_complaint_data_to_csv("ComplainsData.csv")

    def save_complaint_data_to_csv(self, csv_file):
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for complaint in self.complaint_queue.queue:
                writer.writerow([complaint])

    def return_to_main(self):
        print("a")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ComplaintWindow()
    window.show()
    sys.exit(app.exec_())
