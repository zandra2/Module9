'''
I am creating a bank statement that keeps track of transactions
  and only user with correct name and password can access the statement.
The program will ask the user to input his/her name and password.
It will requires the user to input the information correctly otherwise, he/she can't view the bank statements.
The programs will allow the user to input his/her name and password 4x before it ends the program.
The banking records will appears and saved in a text file.

The program includes the following criteria:

    function that takes at least two user arguments from the command line (not the input function)
    Contain at least one if/else statement
    Perform a calculation on a list
    Use at least one dictionary
    Have one try/except statement
    Write either output or a graph to a file
    Must include docstrings telling us how to run your script
    Each function must be documented with comments telling us what the purpose of the function is, and what it's inputs and outputs are
    Either create a class to contain the related functions OR output a simple graph
    Upload your final python script or jupyter notebook to Github, turn in the link on Canvas

'''

#!usr/bin/env python3
import sys
from Banking import Banking

#asking user to enter all the names to view the statements from the command line
if (len(sys.argv) < 6):
    print("Please list all 5 user names on the command line. ie Nathan, Reid, Jadenn, Elsa, Melina.")
#all user bank statements
else:
    name1 = sys.argv[1]
    name2 = sys.argv[2]
    name3 = sys.argv[3]
    name4 = sys.argv[4]
    name5 = sys.argv[5]

    person1 = Banking(name = name1, initial_bal = 7035)
    person1.current_bal()
    person1.deposit(500)
    person1.deposit(1250)
    person1.deposit(25)
    person1.withdraw(200)
    person1.withdraw(40)
    person1.withdraw(335)
    person1.withdraw(2065)

    print()

    person2 = Banking(name = name2, initial_bal = 5520)
    person2.current_bal()
    person2.deposit(1250)
    person2.deposit(523)
    person2.deposit(1122)
    person2.deposit(64)
    person2.withdraw(2000)

    print()

    person3 = Banking(name = name3, initial_bal = 4630)
    person3.current_bal()
    person3.deposit(519)
    person3.deposit(298)
    person3.deposit(460)
    person3.withdraw(255)

    print()

    person4 = Banking(name = name4, initial_bal = 1530)
    person4.current_bal()
    person4.deposit(470)
    person4.deposit(298)
    person4.deposit(460)
    person4.deposit(450)
    person4.withdraw(250)
    person4.withdraw(200)

    print()

    person5 = Banking(name = name5, initial_bal = 2655)
    person5.current_bal()
    person5.deposit(545)
    person5.deposit(450)
    person5.deposit(460)
    person5.withdraw(390)
    person5.withdraw(250)

#banking statement for Nathan
def nathan(name1):
    name1 = "Nathan"
    person1 = Banking(name=name1, initial_bal=7035)
    person1.current_bal()
    person1.deposit(500)
    person1.deposit(1250)
    person1.deposit(25)
    person1.withdraw(200)
    person1.withdraw(40)
    person1.withdraw(335)
    person1.withdraw(2065)
    return name1

#banking statement for Reid
def reid(name2):
    name2 = "Reid"
    person2 = Banking(name=name2, initial_bal=5520)
    person2.current_bal()
    person2.deposit(1250)
    person2.deposit(523)
    person2.deposit(1122)
    person2.deposit(64)
    person2.withdraw(2000)
    return name2

#banking statement for Jadenn
def jadenn(name3):
    name3 = "Jadenn"
    person3 = Banking(name=name3, initial_bal=4630)
    person3.current_bal()
    person3.deposit(519)
    person3.deposit(298)
    person3.deposit(460)
    person3.withdraw(255)
    return name3

#banking statement for Elsa
def elsa(name4):
    name4 = "Elsa"
    person4 = Banking(name=name4, initial_bal=1530)
    person4.current_bal()
    person4.deposit(470)
    person4.deposit(298)
    person4.deposit(460)
    person4.deposit(450)
    person4.withdraw(250)
    person4.withdraw(200)
    return name4

#banking statement for Melina
def melina(name5):
    name5 = "Melina"
    person5 = Banking(name=name5, initial_bal=2655)
    person5.current_bal()
    person5.deposit(545)
    person5.deposit(450)
    person5.deposit(460)
    person5.withdraw(390)
    person5.withdraw(250)
    return name5

#assigning value to variable to call it later
user_nathan = nathan
user_reid = reid
user_jadenn = jadenn
user_elsa = elsa
user_melina = melina
banking_info = Banking

#creating a dictionary with user's name and password
acct_info = {"Nathan":"Minecraft", "Reid":"Trombone", "Jadenn":"Lego", "Elsa":"Bike", "Melina":"School"}

#requesting user input
user_name = input("\nWhat is your name? ")

#verifing account information and allowing user to enter name and password 4x max.

#verifing user's name
counter = 0
while (user_name not in acct_info.keys()) and (counter < 3):
    user_name = (input("There is nobody by that name. Please enter a different name: "))
    counter += 1

#vertifing user's password
counter1 = 0
passw_count = []
if (user_name in acct_info.keys()):
    pswd = input("What's your password? ")
    if pswd in acct_info.values():
        print("\nWelcome, {}! Thank you for signing in. Here is your statement\n".format(user_name))
    if pswd == "Minecraft":
        with open("acct_for_nathan.txt", "w") as file:
            file.write(nathan(banking_info))
    elif pswd == "Trombone":
        with open("acct_for_reid.txt", "w") as file:
            file.write(reid(banking_info))
    elif pswd == "Lego":
        with open("acct_for_jadenn.txt", "w") as file:
            file.write(jadenn(banking_info))
    elif pswd == "Bike":
        with open("acct_for_elsa.txt", "w") as file:
            file.write(elsa(banking_info))
    elif pswd == "School":
        with open("acct_for_melina.txt", "w") as file:
            file.write(melina(banking_info))
    while pswd not in acct_info.values() and (counter1 <3):
        pswd = input("Please enter a correct password: ")
        counter1 +=1
        if pswd in acct_info.values():
            print("Thank you, {}. Here is your statement\n".format(user_name))
        try:
            if pswd == "Minecraft":
                with open("acct_for_nathan1.txt", "w") as file:
                    file.write(user_nathan(banking_info))
            elif pswd == "Trombone":
                with open("acct_for_reid1.txt", "w") as file:
                    file.write(user_reid(banking_info))
            elif pswd == "Lego":
                with open("acct_for_jadenn1.txt", "w") as file:
                    file.write(user_jadenn(banking_info))
            elif pswd == "Bike":
                with open("acct_for_elsa1.txt", "w") as file:
                    file.write(user_elsa(banking_info))
            elif pswd == "School":
                with open("acct_for_melina1.txt", "w") as file:
                    file.write(user_melina(banking_info))
            else:
                print("Sorry you forgot your password.")
        except SystemError:
            print("You entered too many passwords")

