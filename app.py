from sqlite_commands import prepare_relational_database
from sqlite_commands import add_user
from sqlite_commands import is_username_unique
# to avoid revealing password in terminal
import getpass
#to encode password before saving in database
import bcrypt


def get_nonempty_input(fieldname, is_password=False):
    prompt = f'Ange ditt {fieldname}: '
    while True:
        if is_password:
            user_input = getpass.getpass(prompt)
        else:
            user_input = input(prompt)
        if user_input.strip():  # Check if the input is not empty after stripping whitespace
            return user_input
        else:
            print(f'{fieldname} får inte vara tom.')






if(__name__ == "__main__"):
    prepare_relational_database()
    while True:
        menu = input("""Välj ett alternative:
                     1. Bli medlem 
                     2. Logga in 
                     3. Stäng Appen! \n """)

        if (menu == '1'):
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
            
        elif (menu == '2'):
            pass
        elif (menu == '3'):
            break
        else:
            print("Ingen gilgit inmatning! Försök igen!") 