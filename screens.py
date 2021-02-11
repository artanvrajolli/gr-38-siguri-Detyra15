#!/usr/bin/python

import tkinter as tk
import events as event
import jwt
import constants
from tkinter import messagebox


def create_menu(root, canvas):
    Login_with_password = tk.Button(text='Login with password',
                                    width=20, command=lambda : \
                                    event.login_event_handler(root,
                                    canvas))
    canvas.create_window(600, 200, window=Login_with_password)
    Login_with_token = tk.Button(text='Login with token', width=20,
                                 command=lambda : \
                                 event.Token_event_handler(root,
                                 canvas))
    canvas.create_window(600, 250, window=Login_with_token)
    Register_button = tk.Button(text='Register', width=20,
                                command=lambda : \
                                event.register_event_handler(root,
                                canvas))
    canvas.create_window(600, 300, window=Register_button)
    return [Login_with_password, Login_with_token, Register_button]


def clear_elements(array):
    for x in array:
        x.destroy()


def login_screen(root, canvas, menu):

    # labels

    usernameLabel = tk.Label(text='Username:')
    passwordLabel = tk.Label(text='Password:')

    # Field Entry

    Username = tk.Entry(root, width=30)
    Password = tk.Entry(root, show='*', width=30)
    LoginBTN = tk.Button(text='Login', width=10, command=lambda : \
                         event.login_event(
            root,
            canvas,
            Username.get(),
            Password.get(),
            [usernameLabel, passwordLabel, Username, Password,
             LoginBTN],
            menu,
            ))
    root.bind('<Return>', lambda event=None: LoginBTN.invoke())

    # define placeholder

    Username.insert(0, 'Username')
    Password.insert(0, 'Password')

    # UI

    canvas.create_window(100, 200, window=usernameLabel)
    canvas.create_window(100, 250, window=passwordLabel)
    canvas.create_window(250, 200, window=Username)
    canvas.create_window(250, 250, window=Password)
    canvas.create_window(300, 300, window=LoginBTN)
    return [usernameLabel, passwordLabel, Username, Password, LoginBTN]


def register_screen(root, canvas, menu):

    # labels

    usernameLabel = tk.Label(text='Username:')
    passwordLabel = tk.Label(text='Password:')

    # Field Entry

    Username = tk.Entry(root, width=30)
    Password = tk.Entry(root, show='*', width=30)
    RegisterBTN = tk.Button(text='Register', width=10, command=lambda : \
                            event.register_event(
            root,
            canvas,
            Username.get(),
            Password.get(),
            [usernameLabel, passwordLabel, Username, Password,
             RegisterBTN],
            menu,
            ))
    root.bind('<Return>', lambda event=None: RegisterBTN.invoke())

    # define placeholder

    Username.insert(0, 'Username')
    Password.insert(0, 'Password')

    # UI

    canvas.create_window(100, 200, window=usernameLabel)
    canvas.create_window(100, 250, window=passwordLabel)
    canvas.create_window(250, 200, window=Username)
    canvas.create_window(250, 250, window=Password)
    canvas.create_window(300, 300, window=RegisterBTN)
    return [usernameLabel, passwordLabel, Username, Password,
            RegisterBTN]


def token_screen(root, canvas, menu):

    # labels


    tokenLabel = tk.Label(text='Token:')

    # Field Entry


    Token = tk.Text(root, height=5, width=30)
    TokenBTN = tk.Button(text='Login', width=10, command=lambda : \
                         event.token_event(root, canvas, Token.get('1.0'
                         , 'end-1c'), [tokenLabel, Token, TokenBTN],
                         menu))
    root.bind('<Return>', lambda event=None: TokenBTN.invoke())

    # UI


    canvas.create_window(100, 200, window=tokenLabel)
    canvas.create_window(250, 235, window=Token)
    canvas.create_window(330, 300, window=TokenBTN)
    return [tokenLabel, Token, TokenBTN]


def online_screen(
    root,
    canvas,
    username,
    menu,
    ):
    clear_elements(menu)
    Token = jwt.encode({'Username': username}, constants.TOKEN_CODE,
                       algorithm=constants.ALGORITHM)

    # labels


    usernameLabel = tk.Label(text='Username:')
    usernameLabelValue = tk.Label(text=username)
    tokenLabel = tk.Label(text='Token:')
    tokenLabelValue = tk.Label(text=Token, wraplength=200)

    # Field Entry


    clipboardBTN = tk.Button(text='Copy token', width=10,
                             command=lambda : \
                             event.copy_to_clipboard(root, Token))
    LogoutBTN = tk.Button(text='Logout', width=10, command=lambda : \
                          event.logout_event(root, canvas, [
            usernameLabel,
            tokenLabel,
            tokenLabelValue,
            clipboardBTN,
            LogoutBTN,
            usernameLabelValue,
            ]))

    # UI


    canvas.create_window(260, 200, window=usernameLabel)
    canvas.create_window(400, 200, window=usernameLabelValue)
    canvas.create_window(250, 225, window=tokenLabel)
    canvas.create_window(400, 250, window=tokenLabelValue)
    canvas.create_window(370, 300, window=clipboardBTN)
    canvas.create_window(460, 300, window=LogoutBTN)
    return [
        usernameLabel,
        usernameLabelValue,
        tokenLabel,
        tokenLabelValue,
        clipboardBTN,
        LogoutBTN,
        ]


def show_info(message):
    messagebox.showerror('Error', message)
    return False