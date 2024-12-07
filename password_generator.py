from tkinter import*
import random
import string

root = Tk()
root.geometry('350x250')

root.title('Codsoft password Generator')
root.configure(bg='light blue')


#Logic to generate password
def password_generator():
    
    try:
        length = int(pass_dis.get())
        if length <= 0:
            show.delete(0,END)
            show.insert(0,'Enter a positive Number')
            return
    
    except ValueError:
        show.delete(0,END)
        show.insert(0,"Enter Valid Number")
        return  
    
    
    # Generate a random password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length)) 
    
    
    # Display the generated password in the designated entry field
    show.delete(0,END)
    show.insert(0,password)          

#Disable window resizable option.
root.resizable(False,False)

#Heading Label
heading1 = Label(root , text = 'Password Generator' , font = ('Arial',16),borderwidth=3, relief='ridge')
heading1.place(x=10,y=15)

heading2 = Label(root,text='Enter Password Length :-',font=('Arial',16),borderwidth=3, relief='ridge')
heading2.place(x=10,y=80)

#display to enter password
pass_dis = Entry(root,width=27,font=('Arial',16),borderwidth=3, relief='ridge')
pass_dis.place(x=10,y=120,height=30)

#Generate password button 
Button(root,text='Generate Password',font=('Arial',12),width=35,bg='navy blue',fg='white',activebackground='navy blue',borderwidth=3, relief='ridge',command=password_generator).place(x=10,y=160)


#password display show
Label(root,text='Password :-',font=('Arial',13),borderwidth=3, relief='ridge').place(x=10,y=205)


#display in which password is shown
show = Entry(root,font=('Arial',13),width=25,borderwidth=3, relief='ridge')
show.place(x=108,y=205)


root.mainloop()




