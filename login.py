def logino():
    
    print('********************LOGIN PAGE*********************')

    from formatt import formatoba
    a=input("Enter username: ")
    b=input("Enter password: ")

    f=open('C:\\Users\\nanup\\Desktop\\python1\\Hotel management\\admin.txt', 'r')
    z=f.read()
    f.close()

    z=z.split('\n')
    z.pop()
    

    for i in z:
        d=i.split(' ')

      

        if a==d[4] and b==d[5]:
            
            return 1
            break

    else:
        formatoba()
        
        return 0


            
    

        


