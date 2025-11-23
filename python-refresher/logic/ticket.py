#-------------------------------Simple ticket price calculator----------------------


age  = int(input('Enter your age:\n'))
discount = input('Are you a student (yes/no)').lower()



if age <=10:
    print('Free ticket for the child')
elif age<=20:
    if discount == "yes":
        print('Pay only $10')    
    else:
        print('Pay $100')
elif age >=25:
    print('Pay $500')
else:
    print('Invalid age')                