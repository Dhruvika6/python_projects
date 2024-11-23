import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task entry
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.pack(pady=5)

# Task listbox
task_listbox = tk.Listbox(root, width=45, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Delete task button
delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task)
delete_button.pack(pady=5)

# Clear tasks button
clear_button = tk.Button(root, text="Clear All", width=10, command=clear_tasks)
clear_button.pack(pady=5)

# Run the main loop
root.mainloop()
