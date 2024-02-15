from helper_functions import append_to_log, get_nonempty_input
from sqlite_commands import add_user, is_username_unique, user_exists, update_user,create_users_logins_tables, get_user_id
from constants import login_log_file, field_sv_to_column_name
from mongodb_commands import create_post,read_posts, get_message_count

from datetime import datetime

#to encode password before saving in database
import bcrypt

import csv




#to print out posts in a readable way
from pprint import pprint

def main_menu():
    create_users_logins_tables()
    # prepare_log_file()
    while True:
        menu = input("""*****Välkommen till hemsida! Välj ett alternative:*****
                     1. Bli medlem 
                     2. Logga in 
                     3. Stäng Appen! \n """)

        if menu == '1':
            create_account_menu()
        elif menu == '2':
            login_menu()
        elif menu == '3':
            break
        else:
            print("*****Ingen gilgit inmatning! Försök igen!*****") 



def login_menu():
    print('*****Logga in*****')
    while True:
        username = get_nonempty_input("användarnamn")
        password = get_nonempty_input("lösenord",is_password=True)
        if user_exists(username,password):
            append_to_log(username)
            print(f'*****Inloggad som {username}*****')
            while True:
                usermenu = input("""Välj ett alternative:
                            1. Posta Meddelande 
                            2. Söka Meddelende 
                            3. Uppdatera mitt konto
                            4. Få antalet mina meddelanden
                            5. Logga ut \n """)
                if usermenu == '1':
                    create_post_menu(username)
                elif usermenu == '2':
                    find_posts_menu()
                elif usermenu == '3':
                    update_user_menu(username)
                elif usermenu == '4':
                    messagecount = get_message_count(username)
                    print(f'Du har postat {messagecount} meddelande(n)')
                elif usermenu == '5':
                    return
                else:
                    print('*****Ogiltig Val!*****')
        else:
            print("*****Autentisering misslyckades! Försök igen!*****")

def create_account_menu():
    print('*****Skapa ett konto*****')
    firstname = get_nonempty_input("förnamn")
    lastname = get_nonempty_input("efternamn")
    while True:
        username = get_nonempty_input("användarnamn")
        if not is_username_unique(username):
            print("*****Användarnamnet är redan upptaget. Välj en annan.*****")
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


def find_posts_menu():
    print('*****Söka på en titel*****')
    title = input('Sökord: ')
    posts = read_posts(title)
    if posts:
        pprint(posts)
    else:
        print('*****Ingen meddelande hittades!*****')
    

def update_user_menu(username):
    while True:
        print('*****Konto Uppdatering*****')
        field = input("""Skriv namnet på fältet som du vill uppdatera. Välj mellan:
                                   lösenord, förnamn,efternamn, adress, telefonnummer: """)
        if field in ('lösenord', 'förnamn',
                                    'efternamn', 'adress', 'telefonnummer'):
            break
        else:
            print('*****Ogiltig fält!*****')
    if field == 'adress' or field == 'telefonnummer':
        new_value = input(f'Ange ditt nya {field}')
    else:
        new_value = get_nonempty_input('nya '+ field, is_password= (field == 'lösenord'))
    
    if field == 'lösenord':
        new_value = bcrypt.hashpw(new_value.encode('utf-8'), bcrypt.gensalt())

    update_user(username,field_sv_to_column_name[field],new_value)
    print('*****Ditt konto har uppdateras!*****')