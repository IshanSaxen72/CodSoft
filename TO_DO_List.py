from tkinter import *

# Function to add task to the listbox
def add_task():
    task = task_add_dis.get()  # Get the task from the entry box
    if task != "":  # If the entry box is not empty
        listbox_tasks.insert(END, task)  # Add task to the listbox
        task_add_dis.delete(0, END)  # Clear the entry box

# Function to remove the selected task
def remove_task():
    selected_task_index = listbox_tasks.curselection()  # Get index of the selected task
    if selected_task_index:  # If any task is selected
        listbox_tasks.delete(selected_task_index)  # Remove selected task

# Function to mark the selected task as completed
def complete_task():
    selected_task_index = listbox_tasks.curselection()  # Get index of the selected task
    if selected_task_index:  # If any task is selected
        task = listbox_tasks.get(selected_task_index)  # Get the selected task
        listbox_tasks.delete(selected_task_index)  # Remove the original task
        listbox_tasks.insert(selected_task_index, task + " - DONE")  # Append 'DONE' to the task

# Main window
root = Tk()
root.geometry('500x500')
root.configure(bg='light grey')

# Heading
Label(root, text='TO-DO LIST', font=('Arial', 16), borderwidth=3, relief='ridge', bg='grey', fg='white').place(x=180, y=12)

# Task entry box
task_add_dis = Entry(root, font=('Arial', 16), borderwidth=3, relief='ridge', width=25)
task_add_dis.place(x=30, y=70)

# Add task button
Button(root, text='Add Task', borderwidth=3, relief='ridge', width=10, bg='grey', fg='white', activebackground='grey', command=add_task).place(x=350, y=70)

# Listbox to display tasks
listbox_tasks = Listbox(root, font=('Arial', 12), borderwidth=3, relief='ridge', width=56, height=15)
listbox_tasks.place(x=30, y=120)

# Remove task button
Button(root, text='Remove Task', borderwidth=3, relief='ridge', width=25, bg='red', fg='black', font=('Arial', 12), activebackground='red', command=remove_task).place(x=30, y=430)

# Complete task button
Button(root, text='Complete Task', borderwidth=3, relief='ridge', width=16, bg='light green', fg='black', activebackground='light green', font=('Arial', 12), command=complete_task).place(x=275, y=430)

root.mainloop()
