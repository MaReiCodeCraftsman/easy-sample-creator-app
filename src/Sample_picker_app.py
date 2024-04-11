import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import pandas as pd

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.configure(bg="dark slate gray")

        self.role = tk.StringVar()

        role_label = tk.Label(root, text="Enter User Role:", bg="dark slate gray", fg="light blue")
        role_label.pack()

        self.role_entry = tk.Entry(root, width=50, bg="light blue", fg="dark slate gray")
        self.role_entry.pack()

        login_button = tk.Button(root, text="Login", command=self.login, bg="light blue", fg="dark slate gray")
        login_button.pack()

    def login(self):
        role = self.role_entry.get()
        if role not in ("poweruser", "defaultuser"):
            messagebox.showerror("Error", "Invalid user role. Please enter 'poweruser' or 'defaultuser'.")
            return
        self.root.destroy()
        MainWindow(role)

class MainWindow:
    def __init__(self, role):
        self.role = role
        self.root = tk.Tk()
        self.root.title("Sample Picker")
        self.root.geometry("600x400")  # Larger window size
        self.root.configure(bg="dark slate gray")

        self.counter = 3 if role == "defaultuser" else None

        file_label = tk.Label(self.root, text="Excel File Path:", bg="dark slate gray", fg="light blue")
        file_label.pack()

        self.file_entry = tk.Entry(self.root, width=50, bg="light blue", fg="dark slate gray")
        self.file_entry.pack(pady=(0, 10))  # Add padding between widgets

        browse_button = tk.Button(self.root, text="Open folder", command=self.browse_file, bg="light blue", fg="dark slate gray", width=20)  # Set width for button
        browse_button.pack(pady=(0, 10))  # Add padding between widgets

        self.run_button = tk.Button(self.root, text="Create sample data", command=self.run_script, bg="light blue", fg="dark slate gray", width=20)  # Set width for button
        self.run_button.pack(pady=(0, 10))  # Add padding between widgets

        if role == "defaultuser":
            self.counter_label = tk.Label(self.root, text=f"Remaining runs: {self.counter}", bg="dark slate gray", fg="light blue")
            self.counter_label.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(tk.END, file_path)

    def run_script(self):
        if self.counter is not None:
            if self.counter <= 0:
                messagebox.showerror("Error", "No more runs allowed.")
                return
            else:
                self.counter -= 1
                self.counter_label.config(text=f"Remaining runs: {self.counter}")
        file_path = self.file_entry.get()
        if not file_path:
            messagebox.showerror("Error", "Please select an Excel file.")
            return

        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load Excel file: {e}")
            return

        names_df = df[['Supplier Name']]
        sample_df = names_df.sample(frac=0.1)

        date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        sample_file_name = f'DEMO DATA_Suppliers_{date_time}.xlsx'

        with pd.ExcelWriter(sample_file_name, engine='openpyxl') as writer:
            sample_df.to_excel(writer, sheet_name='10_perc_sample', index=False, header=['Supplier Name'])

        random_values = names_df.sample(n=10)
        with pd.ExcelWriter(sample_file_name, mode='a', engine='openpyxl') as writer:
            random_values.to_excel(writer, sheet_name='10_absolute_sample', index=False)
        
        messagebox.showinfo("Success", f"Sample created successfully: {sample_file_name}")

# Create the login window
root = tk.Tk()
login_window = LoginWindow(root)
root.mainloop()
