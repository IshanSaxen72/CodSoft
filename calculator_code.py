from tkinter import *

# Function to handle button clicks and display input
def button_click(value):
    current = cal_dis.get()  # Get current value in display
    cal_dis.delete(0, END)  # Clear the display
    cal_dis.insert(END, current + value)  # Append new value

# Function to clear the display (for "C" and "CE" buttons)
def clear_display():
    cal_dis.delete(0, END)  # Clear everything in the display

# Function to delete the last character (for "DEL" button)
def delete_last():
    current = cal_dis.get()
    if current:  # Check if the display is not empty
        cal_dis.delete(len(current)-1, END)  # Remove the last character

# Function to change the sign of the current number (for "+/-" button)
def change_sign():
    current = cal_dis.get()
    if current:
        if current[0] == "-":  # If it's negative, make it positive
            cal_dis.delete(0)  # Remove the negative sign
        else:
            cal_dis.insert(0, "-")  # Insert a negative sign at the beginning

# Function to evaluate the expression
def calculate():
    try:
        result = eval(cal_dis.get())  # Evaluate the expression
        cal_dis.delete(0, END)  # Clear the display
        cal_dis.insert(END, str(result))  # Show the result
    except:
        cal_dis.delete(0, END)
        cal_dis.insert(END, "Error")  # Show error for invalid expressions

# Main window setup
root = Tk()
root.geometry("320x408")
root.title("Codsoft Calculator")
root.configure(bg='grey')

# Configure row and column weights for resizing
root.grid_rowconfigure(0, weight=1)  # Row 0 for the display
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)  # Rows 1 to 5 for buttons

for j in range(4):  # Columns 0 to 3 for buttons
    root.grid_columnconfigure(j, weight=1)


# Display of calculator
cal_dis = Entry(root, width=12, font=('Arial', 35), borderwidth=2, relief='ridge', justify='right', bg='grey', fg='white')
cal_dis.grid(row=0, column=0, columnspan=4, sticky='nsew')

# Creating buttons with functionality
Button(root, text='CE', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=clear_display).grid(row=1, column=0, padx=2, pady=3, sticky='nsew')
Button(root, text='C', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=clear_display).grid(row=1, column=1, padx=2, pady=3, sticky='nsew')
Button(root, text='DEL', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=delete_last).grid(row=1, column=2, padx=2, pady=3, sticky='nsew')
Button(root, text='/', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('/')).grid(row=1, column=3, padx=2, pady=3, sticky='nsew')

Button(root, text='7', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('7')).grid(row=2, column=0, padx=2, pady=1, sticky='nsew')
Button(root, text='8', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('8')).grid(row=2, column=1, padx=2, pady=1, sticky='nsew')
Button(root, text='9', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('9')).grid(row=2, column=2, padx=2, pady=1, sticky='nsew')
Button(root, text='X', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('*')).grid(row=2, column=3, padx=2, pady=1, sticky='nsew')

Button(root, text='4', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('4')).grid(row=3, column=0, padx=2, pady=1, sticky='nsew')
Button(root, text='5', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('5')).grid(row=3, column=1, padx=2, pady=1, sticky='nsew')
Button(root, text='6', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('6')).grid(row=3, column=2, padx=2, pady=1, sticky='nsew')
Button(root, text='-', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('-')).grid(row=3, column=3, padx=2, pady=1, sticky='nsew')

Button(root, text='1', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('1')).grid(row=4, column=0, padx=2, pady=1, sticky='nsew')
Button(root, text='2', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('2')).grid(row=4, column=1, padx=2, pady=1, sticky='nsew')
Button(root, text='3', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('3')).grid(row=4, column=2, padx=2, pady=1, sticky='nsew')
Button(root, text='+', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('+')).grid(row=4, column=3, padx=2, pady=1, sticky='nsew')

Button(root, text='+/-', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=change_sign).grid(row=5, column=0, padx=2, pady=1, sticky='nsew')
Button(root, text='0', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('0')).grid(row=5, column=1, padx=2, pady=1, sticky='nsew')
Button(root, text='.', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=lambda: button_click('.')).grid(row=5, column=2, padx=2, pady=1, sticky='nsew')
Button(root, text='=', height=3, borderwidth=3, relief='ridge', bg='grey', fg='white', font=('Arial', 11), activebackground='grey', command=calculate).grid(row=5, column=3, padx=2, pady=1, sticky='nsew')

root.mainloop()
