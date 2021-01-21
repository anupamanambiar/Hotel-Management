def register():
    first_name=input("Enter first name: ")
    last_name=input("Enter last name: ")
    ph_no=input("Enter phone number: ")
    username=input("Enter username: ")
    password=input('Enter password: ')
    email_id=input("Enter Email ID: ")
    flag=1

    space=' '

    final= first_name+ space+last_name+space+ph_no+space+email_id+space+username+space+password+'\n'
    
    f=open('C:\\Users\\nanup\\Desktop\\python1\\Hotel management\\admin.txt','r')
    z=f.read()
    f.close()

    z=z.split('\n')
    z.pop()
    

    for i in z:
        d=i.split(' ')
        

        if username==d[4]:
            print('Username already exists')
            print("Try again")
            input('\n\nPress enter to continue\n\n')
            register()
            flag=0







    if flag==1:
        f=open('C:\\Users\\nanup\\Desktop\\python1\\Hotel management\\admin.txt','a')
        f.write(final)
        f.close()

