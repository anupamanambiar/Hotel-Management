from login import logino
from otp import forgotpwd
from register import register
from formatt import formatoba
import os
from admin import custo
from receipt import receipt


def indexo():
    print('********************MAIN PAGE*********************')
    print('1.Admin\n2.Registration\n3.Forgotten Password\n4.Receipt')
    formatoba()
    ch=int(input("Enter choice from above: "))
    formatoba()

    if ch==1:
        x=logino()
        if x==1:
            print("Access granted")
            input("Press enter to continue...")
            os.system('cls')
            custo()
            formatoba()
            os.system('cls')
            
        else:
            print("Wrong password")
            input("Press enter to retry....")
            os.system('cls')
            formatoba()
            indexo()
            

    if ch==2:
        register()
        formatoba()
        input("Press enter to continue...")
        os.system('cls')
        indexo()

    if ch==3:
        forgotpwd()
        formatoba()
        input("Press enter to continue... ")
        os.system('cls')
        indexo()
    
    if ch==4:
        x=logino()
        if x==1:
            print('********************RECEIPT PAGE*********************\n\n')
            os.system('cls')
            receipt()
            formatoba()
            os.system('cls')
        else:
            print("Wrong password")
            input("Press enter to retry....")
            os.system('cls')
            formatoba()
            indexo()




indexo()