import tkinter as tk
from tkinter import messagebox, simpledialog

# Global variables
password_manager = {}  # To store usernames and passwords

# Function to handle account creation
def create_account():
    username = username_entry.get()
    password = password_entry.get()
    
    if username and password:
        password_manager[username] = password  # Storing the password directly for easy editing
        messagebox.showinfo("Success", "Account created successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username and password:
        if username in password_manager and password_manager[username] == password:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password.")
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")

# Function to view, edit, delete credentials and accounts
def open_password_manager():
    manager_window = tk.Toplevel(window)
    manager_window.title("Password Manager")
    manager_window.geometry("400x350")
    manager_window.configure(bg="#F0F8FF")
    
    credentials_label = tk.Label(manager_window, text="Saved Credentials", font=("Arial", 14), bg="#F0F8FF", fg="#333")
    credentials_label.pack(pady=10)

    # Listbox to display saved usernames
    credentials_listbox = tk.Listbox(manager_window, width=40, height=10)
    credentials_listbox.pack(pady=10)
    
    for username in password_manager:
        credentials_listbox.insert(tk.END, f"Username: {username}, Password: {password_manager[username]}")

    # Function to edit the selected credential
    def edit_credential():
        selected = credentials_listbox.curselection()
        if selected:
            selected_text = credentials_listbox.get(selected)
            username_to_edit = selected_text.split(",")[0].split(": ")[1]
            new_password = simpledialog.askstring("Edit Password", f"Enter new password for {username_to_edit}:")
            
            if new_password:
                password_manager[username_to_edit] = new_password
                credentials_listbox.delete(selected)
                credentials_listbox.insert(selected, f"Username: {username_to_edit}, Password: {new_password}")
                messagebox.showinfo("Success", f"Password for {username_to_edit} updated successfully!")
            else:
                messagebox.showwarning("Input Error", "Password cannot be empty.")
        else:
            messagebox.showwarning("Selection Error", "Please select a credential to edit.")

    # Function to delete the selected credential
    def delete_credential():
        selected = credentials_listbox.curselection()
        if selected:
            selected_text = credentials_listbox.get(selected)
            username_to_delete = selected_text.split(",")[0].split(": ")[1]
            if username_to_delete in password_manager:
                del password_manager[username_to_delete]
                credentials_listbox.delete(selected)
                messagebox.showinfo("Success", f"Deleted {username_to_delete} successfully!")
        else:
            messagebox.showwarning("Selection Error", "Please select a credential to delete.")
    
    

    # Buttons to edit or delete the selected credential
    edit_button = tk.Button(manager_window, text="Edit Selected", font=("Arial", 12), bg="#4CAF50", fg="white", command=edit_credential)
    edit_button.pack(pady=5)

    delete_button = tk.Button(manager_window, text="Delete Credential", font=("Arial", 12), bg="#f44336", fg="white", command=delete_credential)
    delete_button.pack(pady=5)

   
# Function to clear entry fields
def clear_entries():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Initialize the Tkinter window
window = tk.Tk()
window.title("Simple Password Manager")
window.geometry("400x350")
window.configure(bg="#F0F8FF")

# Header label
header_label = tk.Label(window, text="Simple Password Manager", font=("Helvetica", 16, "bold"), bg="#F0F8FF", fg="#333")
header_label.pack(pady=20)

# Frame for user input fields
input_frame = tk.Frame(window, bg="#F0F8FF")
input_frame.pack(pady=10)

# Create and place the widgets for username and password inside the frame
username_label = tk.Label(input_frame, text="Username:", font=("Arial", 12), bg="#F0F8FF", fg="#333")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(input_frame, text="Password:", font=("Arial", 12), bg="#F0F8FF", fg="#333")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(input_frame, font=("Arial", 12), show="*", width=20)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Frame for buttons
button_frame = tk.Frame(window, bg="#F0F8FF")
button_frame.pack(pady=20)

# Buttons for creating an account and logging in
create_account_button = tk.Button(button_frame, text="Create Account", font=("Arial", 12), bg="#4CAF50", fg="white", width=15, command=create_account)
create_account_button.grid(row=0, column=0, padx=10)

login_button = tk.Button(button_frame, text="Login", font=("Arial", 12), bg="#2196F3", fg="white", width=15, command=login)
login_button.grid(row=0, column=1, padx=10)

# Button to open the password manager to view, edit, or delete saved credentials
open_manager_button = tk.Button(window, text="Open Password Manager", font=("Arial", 12), bg="#FF9800", fg="white", command=open_password_manager)
open_manager_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
