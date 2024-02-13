from helper_functions import get_nonempty_input
from sqlite_commands import add_user
from sqlite_commands import is_username_unique
from sqlite_commands import user_exists
from constants import login_log_file

from datetime import datetime

#to encode password before saving in database
import bcrypt

import csv

from mongodb_commands import create_post

def login_menu():
    while True:
        username = get_nonempty_input("användarnamn")
        password = get_nonempty_input("lösenord",is_password=True)
        if user_exists(username,password):
            with open(login_log_file,'a') as f:    
                writer = csv.writer(f)
                dt=datetime.now()
                writer.writerow([username,dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second])
            print(f'Inloggad som {username}: ')
            while True:
                usermenu = input("""Välj ett alternative:
                            1. Posta Meddelande 
                            2. Söka Meddelende 
                            3. Uppdatera mitt konto
                            4. Logga ut \n """)
                if usermenu == '1':
                    create_post_menu(username)
                elif usermenu == '2':
                    pass
                elif usermenu == '3':
                    pass
                elif usermenu == '4':
                    return
                else:
                    print('Ogiltig Val!')
        else:
            print("Autentisering misslyckades! Försök igen!")

def create_account_menu():
    firstname = get_nonempty_input("förnamn")
    lastname = get_nonempty_input("efternamn")
    while True:
        username = get_nonempty_input("användarnamn: ")
        if not is_username_unique(username):
            print("Användarnamnet är redan upptaget. Välj en annan.")
        else:
            break
    password = get_nonempty_input("lösenord",is_password=True)
    address = input("Ange ditt adress: ")
    telephone = input("Ange ditt telefonnummer: ")

    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    add_user(firstname,lastname,username,password_hash,address,telephone)


def create_post_menu(username):
    post_dic = {}
    post_dic['username'] = username
    post_dic['title'] = get_nonempty_input("rubrik")
    post_dic['message'] = get_nonempty_input("meddelande")
    image = input("Ange din bild: ")
    video = input("Ange din video: ")
    if image:
        post_dic['image'] = image
    if video:
        post_dic['video'] = video
    links = []
    while True:
        print('Skriv \'avsluta\' eller tryck bara på enter för att slutföra tillägget!')
        link = input("Ange din länk: ")
        if link == 'avsluta' or not link:
            #post
            if links:
                post_dic['links'] = links
            create_post(post_dic)
            break
        else:
            links.append(link)
