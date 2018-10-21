import accountsDb
import getpass

def main():
    #toy main program
    has_select = 0
    while (not(has_select)):
        select = input("1:Login 2: Create an account\n")
        if (select == "1"):
            user_login()
            has_select = 1
        elif (select == "2"):
            create_account()
            has_select = 1
                
def user_login():
    login = 0
    while (not(login)):
        user = input("Username: ")
        #hides input in command line
        pw = getpass.getpass("Password: ")      
        #check username and password in the database
        name = accountsDb.login(user, pw)
        if (name is not None):
            print("Welcome ", name)
            login = 1
        else:
            print("username or password was entered wrong. Try again.\n")

def create_account():
    account_type = input("1: Agency Account 2: TEQ Staff Account 3: Admin\n")
    if (account_type == "1"):
        acc = "Agency"
    elif (account_type == "2"):
        acc = "TEQ Staff"
    else:
        acc = "Admin"
    username = input("Enter a username: ")
    name = input("Enter a name: ")
    pw = getpass.getpass("Enter a password: ")
    accountsDb.insert_user(username, name, pw, acc)
    main()