
# AutoPulse Showroom


**Welcome** to our car models management system! This application aims to provide users with a seamless experience in exploring, selecting, and managing their favorite car models. Whether you're a customer looking to browse through the latest car models or a manager overseeing the inventory, we've got you covered.



# Instructions

## 1. Sign Up / Sign In

### Sign Up:
1. Open the application and click on the "Sign Up" option.
2. Fill in the required information, including your name, email, and password.
3. Click "Sign Up" to create a new account.

### Sign In:
1. If you already have an account, click on the "Sign In" option.
2. Enter your registered email and password.
3. Click "Sign In" to access your account.

## 2. Explore Cars

1. After signing in, navigate to the "View Cars" section.
2. Browse through the list of leading car models.
3. Click on a specific model to view the car and you can also add to cart it.

## 3. Add Cars to Cart

1. While viewing a car model, locate the "Add to Cart" button.
2. Click on "Add to Cart" to include the selected car model in your shopping cart.
3. You can continue exploring and adding more cars to your cart.

## 4. Provide Feedback and Complaints

1. In the user menu, find and click on the "Complaints" section.
2. Use this section to submit feedback, report issues, or make suggestions.
3. Provide detailed information and submit your feedback.

### Delete Items from Cart:
1. Navigate to your shopping cart.
2. Identify the item you want to remove.
3. Click on the "Delete" or "Remove" option to eliminate the item from your cart.

---

# Manager Console Instructions

## Buttons Overview

### 1. Add Vehicle

- **Description:**
  - Use this button to add a new vehicle to the inventory.

- **Instructions:**
  1. Click on the "Add Vehicle" button.
  2. Fill in the required details for the new vehicle (e.g., name, price, cc).
  3. Click "ADD" to add the vehicle to the inventory.

### 2. Edit Vehicle

- **Description:**
  - This button allows you to edit the details of an existing vehicle in the inventory.

- **Instructions:**
  1. Click on the "name" from the list.
  2. Select the vehicle you want to edit from the list.
  3. Modify the necessary details in the text boxes.
  4. Click "EDIT" button to update the vehicle information.

### 3. Delete

- **Description:**
  - Use this button to remove a vehicle from the inventory.

- **Instructions:**
  1. Click on the "Delete" button.
  2. Choose the vehicle you want to remove.
  3. Confirm the deletion when prompted.

### 4. Search

- **Description:**
  - Enables you to search for a specific vehicle in the inventory.

- **Instructions:**
  1. Click on the "Search" button.
  2. Enter the name of the vehicle.
  3. If it is present in the fields it showed up.
  4. View the search results.

### 5. Complain

- **Description:**
  - Access the complaints section to review user feedback and respond accordingly.

- **Instructions:**
  1. Click on the "Complain" button.
  2. Review user complaints and feedback.
  3. Click on "Resolve" button to remove the complain from the list.
  

### 6. View

- **Description:**
  - View details or statistics related to the inventory or other relevant information.

- **Instructions:**
  1. Click on the "View" button.
  2. View all the cars data here "inventory".

### 7. Franchises

- **Description:**
  - Navigate to the franchises management section.

- **Instructions:**
  1. Click on the "Franchises" button.
  2. Add or Delete and view information related to franchises in the form of "Graphs".

### 8. Order Summary

- **Description:**
  - Access a summary of recent orders.

- **Instructions:**
  1. Click on the "Order Summary" button.
  2. Review and analyze recent orders.

# Packages, Libraries and Paths
We are using PyQt5 for GUI, Matplotlib for plotting, NetworkX for network analysis, and some other standard libraries such as csv, numpy, and sys.

Before you begin, ensure you have met the following requirements:

- Python 3.6 or above
- PyQt5
- Matplotlib
- NetworkX
- NumPy

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries.

```bash
pip install PyQt5 matplotlib networkx numpy

Ensure that your file paths are correctly specified in the code. Here are some key paths to check:

CSV Files: 
Verify the paths for reading and writing CSV files.

UI Files: 
If you're using .ui files created with Qt Designer, ensure the paths are correct when using loadUi.
