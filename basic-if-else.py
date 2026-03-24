name= input('what is your name: ')
if name=='Rachit':
    password = input('what is your password: ')
    print('Hello Rachit')
    if password=='rachit':
        print('Access granted')
    else:
        print('Access denied')
elif name == 'Sakshi' :
    print ('Hi Sakshi, You dont have access')

    print('Incorrect user login')