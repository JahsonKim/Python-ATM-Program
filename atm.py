from datetime import date
import sys
users = [{
    "username": "trial",
    "pin": '0000',
    "balance": {'Ksh': 140, 'usd': 0}
}, {
    "username": "trial1",
    "pin": '7875',
    "balance": {'Ksh': 0, 'usd': 0}
}, {
    "username": "trial2",
    "pin": '0987',
    "balance": {'Ksh': 569, 'usd': 5}
}]
today = str(date.today())
# print("Today date is: "+str(today))
# enter user name and pin
hasFailedLogin = True
print("\n\n==============================================\n\nWelcome dear Customer.\nPlease login with your details below")

while hasFailedLogin:
    print('Enter your username')
    username = input()
    print('Enter your PIN')
    pin = input()
    # print(username +"  "+pin )
    loggedInUser = {}
    isLoggedIn = False

    # check if user exists
    for user in users:
        # print(user)
        if username == user['username'] and pin == user['pin']:
            isLoggedIn = True
            loggedInUser = user
            break


    if isLoggedIn:
        print("Welcome "+loggedInUser['username'])
        hasFailedLogin = False

        goBack=True
        while goBack:
            print("-------------------------------")
            print("KARIBU MEMBER\n")
            print("Menu\n")
            print("Please select one choice\n")
            print("1. Withdraw\n2. Deposit\n3. Check Balance \n4. Exit")
            choice=input()
            if choice=="1":
                print ('Withrawal in \n1. Ksh \n2. USD')
                withrawalType=input()
                print("Enter amount to withrawal")
                withdrawalAmount=input()
                if withrawalType=="1" and int(withdrawalAmount)<=loggedInUser['balance']['Ksh']:
                    print('You have withdrawn Ksh.'+withdrawalAmount+"\n")
                    loggedInUser['balance']['Ksh']=loggedInUser['balance']['Ksh']-int(withdrawalAmount)
                    print("Print receipt 1. Yes 2. No")
                    printReceipt=input()
                    if printReceipt=="1":
                        print("\nReceipt\n ----------------\n\nAmount: Ksh."+withdrawalAmount+"\n\nDate:"+today+"\n\n")

                    else: 
                        print("Thank you")
                elif withrawalType=="2" and int(withdrawalAmount)<=loggedInUser['balance']['usd']:
                    print('You have withdrawn $.'+withdrawalAmount+"\n")

                    loggedInUser['balance']['usd']=loggedInUser['balance']['usd']-int(withdrawalAmount)

                    print("Print receipt 1. Yes 2. No")
                    printReceipt=input()
                    if printReceipt=="1":
                        print("\nReceipt\n ----------------\n\nAmount: $."+withdrawalAmount+"\\nnDate:"+today+"\n\n")

                    else: 
                        print("Thank you")

                else: 
                    print("you have insufficient balance in your account")

            

            elif choice=="2":
            
                print("Deposit in \n1. Ksh \n2. USD")
                depositIn=input()
                print("Enter amount to Deposit")
                depositAmount=input()
                if depositIn=="1":
                    loggedInUser['balance']['Ksh']=loggedInUser['balance']['Ksh']+int(depositAmount)
                elif depositIn=="2":
                    loggedInUser['balance']['usd']=loggedInUser['balance']['usd']+int(depositAmount)
                else:
                    print("inavlid choice")


            elif choice=="3":
                print('Check Balance in')
                print("1. Ksh \n2. USD")
                balIn=input()
                if balIn=="1":
                    print("Your account balance is :Ksh "+str(loggedInUser['balance']['Ksh']))
                elif balIn=="2":
                    print("Your account balance is :$ "+str(loggedInUser['balance']['usd']))
                else: 
                    print("Invalid option")

            elif choice=="4":
                print("------------------------------\n")
                print("THANK YOU FOR USING OUR SERVICES\n")
                print("-------------------------------\n")
                goBack=False
                hasFailedLogin = True
                sys.exit()

            else:
                print("Invalid choice")
            
        
    else:
        print("Invalid login details")
        hasFailedLogin = True
