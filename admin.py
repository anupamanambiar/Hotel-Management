from datetime import *

def custo():
    print('********************CUSTOMER DETAILS*********************\n\n')
    first_name= input("Enter first name: ")
    last_name= input("Enter last name: ")
    Ph_no=input("Enter phone number: ")
    email_id=input('Enter email-id: ')
    LOS=int(input("Enter length of stay: "))
    print('1.Deluxe\n2.Multi Deluxe\n3.Joint\n4.Regular')
    typ=int(input("Enter type of room needed: "))

    x=datetime.now()
    dat=x.strftime('%d/%m/%Y')
    tim=x.strftime('%H:%M:%S')


    space=' '



    if typ==1: 
        amount=5000*LOS

    if typ==2:
        amount=10000*LOS

    if typ==3:
        amount=3000*LOS

    if typ==4:
        amount=1000*LOS


    final= first_name+space+last_name+space+Ph_no+space+email_id+space+str(LOS)+space+str(typ)+space+str(amount)
    final= final+space+dat+space+tim



    f=open('Customer.txt','a')
    f.write(final+'\n')
    f.close()