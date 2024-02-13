from sqlite_commands import prepare_relational_database
from helper_functions import prepare_log_files
from menu_functions import login_menu, create_account_menu


def main():
    prepare_relational_database()
    prepare_log_files()
    while True:
        menu = input("""Välj ett alternative:
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
            print("Ingen gilgit inmatning! Försök igen!") 


if __name__ == "__main__":
    main()