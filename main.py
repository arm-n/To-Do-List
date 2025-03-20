from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- ADD TASK ------------------------------- #
def add_task():
    task = task_input.get()
    if not task:
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    listbox.insert(END, task)
    task_input.delete(0, END)
    save_tasks()


# ---------------------------- DELETE TASK ------------------------------- #
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")


# ---------------------------- SAVE TASKS ------------------------------- #
def save_tasks():
    tasks = listbox.get(0, END)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# ---------------------------- LOAD TASKS ------------------------------- #
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                listbox.insert(END, task)
    except (FileNotFoundError, json.JSONDecodeError):
        pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("To-Do List")
window.config(padx=20, pady=20)

# Task Input
frame = Frame(window)
frame.pack(pady=10)

task_input = Entry(frame, width=40)
task_input.pack(side=LEFT, padx=10)

add_button = Button(frame, text="Add Task", command=add_task)
add_button.pack(side=RIGHT)

# Task List
listbox = Listbox(window, width=50, height=10)
listbox.pack(pady=10)

# Delete Button
delete_button = Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

# Load tasks on startup
load_tasks()

window.mainloop()
