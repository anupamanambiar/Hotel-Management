def forgotpwd():

    username=input("Enter username: ")

    f=open('C:\\Users\\nanup\\Desktop\\python1\\Hotel management\\admin.txt','r')
    z=f.read()
    f.close()

    z=z.split('\n')
    z.pop()

    for i in z:
        d=i.split(' ')


        if username==d[4]:
            print('Username found\nYour OTP has been sent to your registered email.')

            from random import randint
            c=''
            finalOTP=''
            for i in range(6):
                x=randint(0,9)
                c+=str(x)
                finalOTP+=' '+str(x)


            import yagmail

            yag=yagmail.SMTP('nanupama15@gmail.com', '@94u2meA@')
            yag.send(to=d[3],subject='OTP',contents='Your OTP is'+ finalOTP)

            a=input('Enter otp: ')

            if a==c:
                print('Your password is',d[5])


