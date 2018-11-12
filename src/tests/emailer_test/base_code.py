if __name__ == "__main__":
    import sys
    sys.path.insert(0, "../../emailer")
    from account_creation_emailer import *
    from password_forgetting_emailer import *

    recipient = input("What is your email address?\n")
    
    test = 0
    while (test not in ["1", "2"]):
        test = input("Which emailer are you testing right now? (Enter 1 or 2)"
                 + "\n1) AccountCreationEmailer"
                 + "\n2) PasswordForgettingEmailer\n")
        if (test not in ["1", "2"]):
            print ("Make sure to enter either 1 or 2.")
    
    if (test == "1"):
        emailer = AccountCreationEmailer()
    elif (test == "2"):
        emailer = PasswordForgettingEmailer()

    emailer.send(recipient)
