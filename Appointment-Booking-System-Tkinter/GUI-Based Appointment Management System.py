import tkinter as tk
from tkinter import messagebox, simpledialog

# Class representing a single appointment slot
class Appointment:
    def __init__(self, hour, minute):
        self.start_time = f"{hour:02}:{minute:02}"  # Format time as hh:mm
        self.name = ""  # Initialize with no name
        self.booked = False  # Slot is initially not booked
        self.next = None  # Pointer to the next appointment

# Main application class
class AppointmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Booking System")  # Set window title
        self.head = None  # Head of the linked list for appointments
        self.working_hours_set = False  # Flag to check if working hours are set
        self.create_widgets()  # Create GUI widgets

    def create_widgets(self):
        # Frame for placing widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Entry for start hour
        tk.Label(self.frame, text="Start Hour (hh):").grid(row=0, column=0, padx=5, pady=5)
        self.start_hour_entry = tk.Entry(self.frame)
        self.start_hour_entry.grid(row=0, column=1, padx=5, pady=5)

        # Entry for end hour
        tk.Label(self.frame, text="End Hour (hh):").grid(row=1, column=0, padx=5, pady=5)
        self.end_hour_entry = tk.Entry(self.frame)
        self.end_hour_entry.grid(row=1, column=1, padx=5, pady=5)

        # Entry for duration
        tk.Label(self.frame, text="Duration (min):").grid(row=2, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(self.frame)
        self.duration_entry.grid(row=2, column=1, padx=5, pady=5)

        # Button to set working time and create appointments
        self.set_time_button = tk.Button(self.frame, text="Set Working Time", command=self.set_working_time)
        self.set_time_button.grid(row=3, columnspan=2, pady=10)

        # Menu Buttons
        tk.Button(self.frame, text="Book Appointment", command=self.book_appointment).grid(row=4, column=0, pady=5)
        tk.Button(self.frame, text="Show Free Slots", command=self.free_slots).grid(row=4, column=1, pady=5)
        tk.Button(self.frame, text="Cancel Appointment", command=self.cancel_appointment).grid(row=5, column=0, pady=5)
        tk.Button(self.frame, text="Search Appointment", command=self.search_appointment).grid(row=5, column=1, pady=5)
        tk.Button(self.frame, text="Show All Appointments", command=self.display_appointments).grid(row=6, columnspan=2, pady=10)
        tk.Button(self.frame, text="Exit", command=self.root.quit).grid(row=7, columnspan=2, pady=10)

    def set_working_time(self):
        # Set working hours and create appointments
        if self.working_hours_set:
            messagebox.showinfo("Info", "Working hours are already set.")
            return

        try:
            start_hour = int(self.start_hour_entry.get())
            end_hour = int(self.end_hour_entry.get())
            duration = int(self.duration_entry.get())
            self.head = self.create_appointments(start_hour, end_hour, duration)
            self.working_hours_set = True  # Set the flag to true after setting working hours
            self.set_time_button.config(state=tk.DISABLED)  # Disable the button after setting time
            messagebox.showinfo("Success", "Working time set and appointments created.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

    def create_appointments(self, start_hour, end_hour, duration):
        # Create appointment slots based on start hour, end hour, and duration
        head = None
        current_hour = start_hour
        current_minute = 0

        while current_hour < end_hour or (current_hour == end_hour and current_minute < 60):
            # Create a new appointment slot
            new_appointment = Appointment(current_hour, current_minute)
            if head is None:
                head = new_appointment
            else:
                temp = head
                while temp.next:
                    temp = temp.next
                temp.next = new_appointment

            # Update time for the next slot
            current_minute += duration
            if current_minute >= 60:
                current_hour += 1
                current_minute %= 60

            # Stop adding slots if the next slot would start at or after end time
            if current_hour == end_hour and current_minute >= 0:
                break

        return head

    def find_available_slot(self):
        # Find the first available (unbooked) slot
        temp = self.head
        while temp:
            if not temp.booked:
                return temp
            temp = temp.next
        return None

    def book_appointment(self):
        # Book an appointment in the first available slot
        if not self.working_hours_set:
            messagebox.showwarning("Warning", "Working hours not set. Please set working hours first.")
            return

        slot = self.find_available_slot()
        if slot:
            name = simpledialog.askstring("Book Appointment", f"Enter name for slot {slot.start_time}:")
            if name:
                slot.name = name
                slot.booked = True
                messagebox.showinfo("Success", f"Appointment booked for {slot.start_time}.")
            else:
                messagebox.showwarning("Warning", "No name entered.")
        else:
            messagebox.showwarning("No Slots", "No available slots.")

    def free_slots(self):
        # Display all free (unbooked) slots
        if not self.working_hours_set:
            messagebox.showwarning("Warning", "Working hours not set. Please set working hours first.")
            return

        free_slots = []
        temp = self.head
        while temp:
            if not temp.booked:
                free_slots.append(temp.start_time)
            temp = temp.next

        if free_slots:
            slots = "\n".join(free_slots)
            messagebox.showinfo("Free Slots", f"Free Slots:\n{slots}")
        else:
            messagebox.showinfo("No Slots", "No free slots available.")

    def display_appointments(self):
        # Display all booked appointments
        if not self.working_hours_set:
            messagebox.showwarning("Warning", "Working hours not set. Please set working hours first.")
            return

        appointments = []
        temp = self.head
        while temp:
            if temp.booked:
                appointments.append(f"Name: {temp.name}\nAppointment Time: {temp.start_time}")
            temp = temp.next

        if appointments:
            appointments_str = "\n\n".join(appointments)
            messagebox.showinfo("Appointments", appointments_str)
        else:
            messagebox.showinfo("No Appointments", "No appointments available.")

    def search_appointment(self):
        # Search for an appointment by name
        if not self.working_hours_set:
            messagebox.showwarning("Warning", "Working hours not set. Please set working hours first.")
            return

        name = simpledialog.askstring("Search Appointment", "Enter name:")
        if name:
            temp = self.head
            while temp:
                if temp.name == name:
                    messagebox.showinfo("Appointment Found", f"Name: {temp.name}\nAppointment Time: {temp.start_time}")
                    return
                temp = temp.next
            messagebox.showinfo("No Appointment", f"No appointment found for {name}.")
        else:
            messagebox.showwarning("No Name", "No name entered.")

    def cancel_appointment(self):
        # Cancel an appointment by name
        if not self.working_hours_set:
            messagebox.showwarning("Warning", "Working hours not set. Please set working hours first.")
            return

        name = simpledialog.askstring("Cancel Appointment", "Enter the name of the client whose appointment you want to cancel:")
        if name:
            temp = self.head
            while temp:
                if temp.name == name and temp.booked:
                    temp.booked = False
                    temp.name = ""
                    messagebox.showinfo("Cancelled", f"Appointment for {name} has been canceled.")
                    return
                temp = temp.next
            messagebox.showinfo("No Appointment", f"No appointment found for {name}.")
        else:
            messagebox.showwarning("No Name", "No name entered.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentApp(root)
    root.mainloop()
