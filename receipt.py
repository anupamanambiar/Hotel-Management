import yagmail
from fpdf import FPDF

def receipt():
    name=input("Enter full name: ")
    name=name.split(' ')

    f=open('Customer.txt', 'r')
    z=f.read()
    f.close()

    z=z.split('\n')
    z.pop()

    lines='-------------------------------------------------'



    for i in z:
        d=i.split(' ')
        

        if name[0]==d[0] or name[1]==d[1]: 
            print('Name found')

            firstname=d[0]
            lastname=d[1]
            phnumber=d[2]
            email=d[3]
            LOS=d[4]
            rtype=d[5]
            cost=d[6]
            checkin=d[7]+' '+d[8]

            svp=''

            svp+= 'Name:- \t\t\t'+firstname+' '+ lastname+'\n'
            svp+= 'Phoneno.:-\t\t'+phnumber+'\n'
            svp+='email-id:-\t\t'+email+'\n'
            svp+='Length of stay:-\t'+LOS+'\n'


            if rtype==1:
                rtype='Deluxe'       
            if rtype==2:
                rtype='Multi-Deluxe'        
            if rtype==1:
                rtype='Joint'       
            if rtype==1:
                rtype='Regular'
            
            svp+='Room Type:-\t\t'+rtype+ '\n'

            svp+='Checkin:-\t\t'+ checkin +'\n'

            svp+=lines +'\n'
            svp+=lines+'\n'

            svp+= "Total Amount:-\t\t" + cost

            print(svp)

            f=open('Receipt.txt', 'w')
            f.write(svp)
            f.close()
    

    yag=yagmail.SMTP('nanupama15@gmail.com', "@94u2meA@")
    yag.send(to=email,subject='Hotel stay receipt', contents='Attached below is the receipt for your stay', attachments='Receipt.pdf')


    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', size=12)

    f=open('Receipt.txt','r')
    
    for i in f:
        pdf.cell(10,10,txt=i,ln=1,align='L')

    pdf.output('Receipt.pdf')



