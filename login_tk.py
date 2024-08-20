from tkinter import *

global window
window=Tk()
window.title("hello")
window.geometry("500x500")

def starting_window():
    Label(text = 'bruv', bg = 'grey' , font = ('calibri',27) , width = '4' ,height = '1').pack()
    Label(text = '').pack()
    Button(text = 'Login', height = '2', width = '5',command = login).pack()
    Label(text = '').pack()
    Button(text = 'register',height = '5', width = '15',command = register).pack()
    Label(text = '').pack()
    Button(text = 'guest',height = '5', width = '25',command = guest).pack()
    window.mainloop()
    return(username)

def login():

    global login_window
    global username_entry
    global password_entry
    global username
    global password

    login_window = Toplevel(window)
    login_window.title('login')
    login_window.geometry('500x310')

    username = StringVar()
    password = StringVar()
    Label(login_window ,text = 'login bruv',  font = ('calibri',27) ).pack()
    Label(login_window,text = '').pack()
    Label(login_window , text = 'Username').pack()
    username_entry = Entry(login_window ,textvariable = username)
    username_entry.pack()
    Label(login_window,text = '').pack()
    Label(login_window ,text = 'Password').pack()
    password_entry =  Entry(login_window ,textvariable = password)
    password_entry.pack()
    Label(login_window,text = '').pack()
    Button(login_window ,text = 'Login', font = ('calibri',14) , width = '4' ,height = '1', command = login_enter).pack()

def register():

    global reg_window
    global reg_username_entry
    global reg_password_entry
    global reg_username
    global reg_password
    reg_window = Toplevel(window)
    reg_window.title('register')
    reg_window.geometry('500x310')

    reg_username = StringVar()
    reg_password = StringVar()
    Label(reg_window ,text = 'register bruv',  font = ('calibri',27) ).pack()
    Label(reg_window,text = '').pack()
    Label(reg_window , text = 'Username').pack()
    reg_username_entry = Entry(reg_window ,textvariable = reg_username)
    reg_username_entry.pack()
    Label(reg_window,text = '').pack()
    Label(reg_window ,text = 'Password').pack()
    reg_password_entry =  Entry(reg_window ,textvariable = reg_password)
    reg_password_entry.pack()
    Label(reg_window,text = '').pack()
    Button(reg_window ,text = 'Register', font = ('calibri',14) , width = '6' ,height = '1', command = reg_enter).pack()

def guest():
    global username

    Label(window,text = '').pack()
    Label(window,text = 'as u selected guest u can just play game').pack()
    Label(window,text = '').pack()
    username = 0
    Button(text = 'play game',height = '5', width = '25',command = play_game).pack()

def login_enter():
    global username

    username_entered = username.get()
    password_entered = password.get()

    print(username_entered, password_entered)

    username = username_entered

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    # i have to do database check and stuff and then only allow game to run if login and passowrd is correct
    account = 1 #this means nothing now but later it will mean if account passowrd and user name is real (and i relised that 1 = true and 0 = false in python
    if account == True:
        Label(login_window, text = 'username and password correct well done bro',font = ('calibri',14) ).pack()
        Button(login_window ,text = 'press to play the game', font = ('calibri',14) , width = '17' ,height = '1', command = play_game).pack()

    else:
        Label(login_window,fg = 'red' ,text = 'username and password incorrect',font = ('calibri',14) ).pack()

def reg_enter():
    global username

    reg_username_entered = reg_username.get()
    reg_password_entered = reg_password.get()

    print(reg_username_entered, reg_password_entered)

    username = reg_username_entered

    reg_username_entry.delete(0,END)
    reg_password_entry.delete(0,END)
    # i have to do database check and stuff and then only allow game to run if login and passowrd is correct
    account = 1 # this is very similar to login but the data checks and stuff thta will be done is different
    if account == True:
            Label(reg_window,text = 'username is unique and u can play the game',font = ('calibri',14) ).pack()
            Button(reg_window ,text = 'press to play the game', font = ('calibri',14) , width = '17' ,height = '1', command = play_game).pack()
    else:
        Label(reg_window,fg = 'red', text = 'invalid',font = ('calibri',14) ).pack()

def play_game():
    window.destroy()
    #print(username)
    #username1 = username
    #return username1

#starting_window()
hi = starting_window()   # if this file is being imported this line can't be here
print(hi)
