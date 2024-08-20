import tkinter as tk  # Import the tkinter library for GUI creation
import math  # Import the math library for mathematical operations

# Function to handle button click and append the clicked value to the entry widget
def button_click(value):
    current = entry.get()  # Get the current text from the entry widget
    entry.delete(0, tk.END)  # Clear the entry widget
    entry.insert(tk.END, current + str(value))  # Insert the new value (button click) into the entry widget

# Function to clear the entire entry widget (reset the input)
def clear_entry():
    entry.delete(0, tk.END)  # Clear all text from the entry widget

# Function to remove the last character (backspace functionality)
def backspace():
    current = entry.get()  # Get the current text from the entry widget
    entry.delete(0, tk.END)  # Clear the entry widget
    entry.insert(tk.END, current[:-1])  # Insert the text back into the entry, excluding the last character

# Function to evaluate the mathematical expression entered by the user
def evaluate():
    try:
        expression = entry.get()  # Get the expression entered by the user
        result = eval(expression)  # Evaluate the expression using eval()
        entry.delete(0, tk.END)  # Clear the entry widget
        entry.insert(tk.END, str(result))  # Display the result of the evaluation in the entry widget
    except Exception as e:
        entry.delete(0, tk.END)  # Clear the entry widget in case of an error
        entry.insert(tk.END, "Error")  # Display "Error" if evaluation fails

# Function to apply square root operation to the current value in the entry widget
def apply_sqrt():
    current = entry.get()  # Get the current value from the entry widget
    entry.delete(0, tk.END)  # Clear the entry widget
    entry.insert(tk.END, str(math.sqrt(float(current))))  # Calculate and display the square root

# Function to apply sine operation (in degrees) to the current value in the entry widget
def apply_sin():
    current = entry.get()  # Get the current value from the entry widget
    entry.delete(0, tk.END)  # Clear the entry widget
    entry.insert(tk.END, str(math.sin(math.radians(float(current)))))  # Calculate and display the sine of the value

# Function to apply cosine operation (in degrees) to the current value in the entry widget
def apply_cos():
    current = entry.get()  # Get the current value from the entry widget
    entry.delete(0, tk.END)  # Clear the entry widget
    entry.insert(tk.END, str(math.cos(math.radians(float(current)))))  # Calculate and display the cosine of the value

# Function to apply tangent operation (in degrees) to the current value in the entry widget
def apply_tan():
    current = entry.get()  # Get the current value from the entry widget
    entry.delete(0, tk.END)  # Clear the entry widget
    entry.insert(tk.END, str(math.tan(math.radians(float(current)))))  # Calculate and display the tangent of the value

# Main window configuration
root = tk.Tk()  # Create the main application window
root.title("Scientific Calculator")  # Set the title of the window
root.geometry("400x600")  # Set the size of the window (width x height)
root.config(bg="#2c3e50")  # Set the background color of the window

# Entry widget for displaying and entering the expression
entry = tk.Entry(root, width=20, font=('Arial', 20), justify=tk.RIGHT, bd=10)
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10, ipady=20)  # Place the entry widget at the top

# Parameters for button styling (common to all buttons)
button_params = {
    'font': ('Arial', 14),  # Set the font and size for button text
    'padx': 20,  # Set horizontal padding
    'pady': 20,  # Set vertical padding
    'bg': "#3498db",  # Set background color of buttons
    'fg': "#ecf0f1"  # Set text color of buttons
}

# List of buttons to be displayed (each value represents a button)
buttons = [
    '7', '8', '9', '/',   # Row 1 buttons
    '4', '5', '6', '*',   # Row 2 buttons
    '1', '2', '3', '-',   # Row 3 buttons
    '0', '.', '=', '+',   # Row 4 buttons
    '(', ')', 'C', '⌫',   # Row 5 buttons (C for clear, ⌫ for backspace)
    'sin', 'cos', 'tan', 'sqrt'  # Row 6 buttons (scientific functions)
]

# Placement of buttons on the grid
row_val = 1  # Start placing buttons from row 1
col_val = 0  # Start placing buttons from column 0

# Loop through the buttons list to create and place buttons on the grid
for button in buttons:
    tk.Button(
        root, text=button,  # Set the text of the button
        command=lambda b=button: button_click(b) if b not in {'=', 'sin', 'cos', 'tan', 'sqrt', 'C', '⌫'} 
        else evaluate() if b == '=' else apply_sqrt() if b == 'sqrt' 
        else apply_sin() if b == 'sin' else apply_cos() if b == 'cos' 
        else apply_tan() if b == 'tan' else clear_entry() if b == 'C' 
        else backspace(),  # Assign the appropriate function to each button
        **button_params  # Apply the common styling parameters to the button
    ).grid(row=row_val, column=col_val, sticky="nsew")  # Place the button in the grid
    col_val += 1  # Move to the next column
    if col_val > 3:  # If the column index exceeds 3, move to the next row
        col_val = 0
        row_val += 1

# Configure the grid to be responsive (make buttons resize with window)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)  # Make each row expand equally
    root.grid_columnconfigure(i, weight=1)  # Make each column expand equally

# Start the Tkinter event loop (start the application)
root.mainloop()
