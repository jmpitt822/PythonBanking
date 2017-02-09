def chooseAction():
    print("What would you like to do? [1. Check Balance, 2. Withdraw, 3. Deposit, 4. Delete Account, 5. Cancel]")
    choice = input()
    if choice == "1":
        checkBalance()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        deposit()
    elif choice == "4":
        deleteAccount()
    elif choice == "5":
        cancel()
    elif choice == "/exit":
        exit()
    else:
        print("Invalid input")

def checkBalance():
    balance = userList[name]
    print("Your balance is $" + str(balance))

def withdraw():
    while True:
        try:
            withdrawAmt = float(input("How much would you like to withdraw?\n"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            prevBal = userList[name]
            if withdrawAmt >= 0 and prevBal >= withdrawAmt:
                userList[name] = prevBal - withdrawAmt
            else:
                print("Error: Insufficient Funds")
            break

def deposit():
    while True:
        try:
            depositAmt = float(input("How much would you like to deposit?\n"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            prevBal = userList[name]
            if depositAmt >= 0:
                userList[name] = prevBal + depositAmt
            else:
                print("Error: Cannon deposit a negative number.")
            break

def deleteAccount():
    delChoice = input("Are you sure you want to delete your account? [y/n]\n")
    if delChoice == "y":
        del(userList[name])
        login()

def cancel():
    login()

def login():
    global name
    name = input("Hello! Please enter your name to log in.\n")
    if name in userList:
        print("Welcome back,", name)
    else:
        while True:
            try:
                newBal = float(input("Thank you for creating an account. How much would you like to deposit?\n"))
            except ValueError:
                print("Please enter a valid number.")
                continue
            else:
                userList[name] = newBal
                break


userList = {"Jeremy": 100.00, "John": 117.00, "Linda": 58.00}



login()
while True:
    chooseAction()
