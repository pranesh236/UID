import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")  # ✅ Fixed typo

def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        tasks.pop(index)  # ✅ Fixed list removal issue
        update_task_list()  # ✅ Refresh UI after removal
    else:
        messagebox.showwarning("Warning", "Please select a task to remove")

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Input field for tasks
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Buttons for adding and removing tasks
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Listbox to display tasks
task_list = tk.Listbox(app, width=40, height=10)
task_list.pack(pady=10)

# Run the application
app.mainloop()
