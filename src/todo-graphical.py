import json
import tkinter as tk
from tkinter import messagebox, simpledialog

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)

def add_task(tasks, task_listbox):
    title = simpledialog.askstring("Add Task", "Enter task title:")
    if title:
        tasks.append({"title": title, "completed": False})
        task_listbox.insert(tk.END, f"{title} - Incomplete")
        save_tasks(tasks)

def mark_task_completed(tasks, task_listbox):
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        tasks[index]["completed"] = True
        task_listbox.delete(index)
        task_listbox.insert(index, f"{tasks[index]['title']} - Completed")
        save_tasks(tasks)

def remove_task(tasks, task_listbox):
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task_listbox.delete(index)
        tasks.pop(index)
        save_tasks(tasks)

def create_main_window():
    tasks = load_tasks()
    
    root = tk.Tk()
    root.title("Todo List")

    task_listbox = tk.Listbox(root, width=50, height=15)
    task_listbox.pack()

    for task in tasks:
        status = "Completed" if task["completed"] else "Incomplete"
        task_listbox.insert(tk.END, f"{task['title']} - {status}")

    add_button = tk.Button(root, text="Add Task", command=lambda: add_task(tasks, task_listbox))
    add_button.pack()

    complete_button = tk.Button(root, text="Mark as Completed", command=lambda: mark_task_completed(tasks, task_listbox))
    complete_button.pack()

    remove_button = tk.Button(root, text="Remove Task", command=lambda: remove_task(tasks, task_listbox))
    remove_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
