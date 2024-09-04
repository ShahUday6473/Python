# Appointment Booking System

## Description
This project is an Appointment Booking System developed using the Tkinter library in Python. The system allows users to set working hours, book appointments, view free slots, cancel appointments, search for specific appointments, and display all booked appointments. The system utilizes a linked list data structure to manage and navigate through appointment slots efficiently.

## Features
- **Set Working Hours**: Define the start and end times, and the duration for appointment slots. Once set, the working hours cannot be changed.
- **Book Appointments**: Book appointments by entering the name of the client, which gets stored in the first available slot.
- **View Free Slots**: Display all available (unbooked) appointment slots.
- **Cancel Appointments**: Cancel a booked appointment by specifying the client's name.
- **Search Appointments**: Search for an appointment by the client's name.
- **Display All Appointments**: Show all booked appointments with client names and appointment times.

## Data Structures Used
- **Linked List**: Used to manage the list of appointment slots. Each node in the linked list represents an individual appointment slot with a start time, booking status, and client name. The linked list allows efficient traversal and management of appointment slots, making it easy to find, book, and cancel appointments.

## Knowledge About Data Structures
The linked list data structure was chosen for its efficiency in handling dynamic data where the number of appointments can vary. It provides:
- **Efficient Insertion/Deletion**: Adding or removing appointment slots is straightforward as it involves updating pointers in the nodes.
- **Flexible Size**: The size of the list can grow or shrink as needed without a predefined limit.

## Usage
1. **Set Working Time**: Enter the start hour, end hour, and duration for the appointment slots, then click "Set Working Time" to initialize the slots.
2. **Book Appointment**: Click "Book Appointment" to book a slot by entering the client's name for the first available slot.
3. **Show Free Slots**: Click "Show Free Slots" to display all currently available (unbooked) slots.
4. **Cancel Appointment**: Click "Cancel Appointment" and enter the client's name to cancel a booked appointment.
5. **Search Appointment**: Click "Search Appointment" and enter the client's name to find their appointment.
6. **Show All Appointments**: Click "Show All Appointments" to display a list of all booked appointments.
7. **Exit**: Click "Exit" to close the application.

## Requirements
- Python 3.x
- Tkinter library (usually included with Python)

## Installation
To run this application, ensure you have Python installed on your system. The Tkinter library should be included by default. Save the provided code to a `.py` file and execute it with Python.

## Acknowledgments
- The Tkinter library for GUI development.
- Python's built-in libraries for managing data and handling exceptions.
