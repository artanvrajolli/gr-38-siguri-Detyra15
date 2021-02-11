#!/usr/bin/python
import hashlib
import jwt
import re
import os
import screens as screen
import constants

dirname = os.path.dirname(os.path.realpath(__file__))


def login_event(
    root,
    canvas,
    username,
    password,
    elements,
    menu,
    ):
    Hashpassword = hashlib.sha256(password.encode()).hexdigest()
    file1 = open(dirname + '/Database.txt', 'r')
    while True:
        line = file1.readline()
        if not line:
            file1.close()
            screen.show_info('Wrong Username or Password!')
            break
        txt = line.strip()
        x = re.search('^' + username + "\|\|\|" + Hashpassword, txt)
        if x:
            screen.clear_elements(elements)
            screen.online_screen(root, canvas, username, menu)
            break


def register_event(
    root,
    canvas,
    username,
    password,
    elements,
    menu,
    ):

    # check if user already exist in Database.txt

    file1 = open(dirname + '/Database.txt', 'r')
    while True:
        line = file1.readline()
        if not line:
            file1.close()
            break
        txt = line.strip()
        x = re.search('^' + username + "\|\|\|", txt)
        if x:
            screen.show_info('User already exist!')
            return False

    Hashpassword = hashlib.sha256(password.encode()).hexdigest()
    f = open(dirname + '/Database.txt', 'a+')
    f.write('\n' + username + '|||' + Hashpassword)
    f.close()
    screen.clear_elements(elements)
    screen.online_screen(root, canvas, username, menu)


def register_event_handler(root, canvas):
    canvas.delete('all')
    menu = screen.create_menu(root, canvas)
    screen.register_screen(root, canvas, menu)


def login_event_handler(root, canvas):
    canvas.delete('all')
    menu = screen.create_menu(root, canvas)
    screen.login_screen(root, canvas, menu)


def Token_event_handler(root, canvas):
    canvas.delete('all')
    menu = screen.create_menu(root, canvas)
    screen.token_screen(root, canvas, menu)


def token_event(
    root,
    canvas,
    token,
    elements,
    menu,
    ):
    try:
        TokenDecoded = jwt.decode(token.strip(), constants.TOKEN_CODE,
                                  algorithms=[constants.ALGORITHM])
        screen.clear_elements(elements)
        screen.online_screen(root, canvas, TokenDecoded['Username'],
                             menu)
    except:
        screen.show_info('Wrong Token!')


def copy_to_clipboard(root, text):
    root.clipboard_clear()
    root.clipboard_append(text)


def logout_event(root, canvas, elements):
    screen.clear_elements(elements)
    menu = screen.create_menu(root, canvas)
    screen.login_screen(root, canvas, menu)
