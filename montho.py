def monthp():
    a=input("Enter month number:- ")

    f=open("Customer.txt",'r')
    z=f.read()
    f.close()

    z=z.split('\n')
    z.pop()
    amount=0

    for i in z:
        d=i.split(' ')

        amountp=d[6]
        day=d[7]

        final= day+'/'+ amountp

        s=final.split('/')

        
        if s[1]==a:
            amount+=int(s[3])
        
    print('Total sales is',amount)

monthp()