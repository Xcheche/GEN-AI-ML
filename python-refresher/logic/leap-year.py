# -----------------------Leap year----------------------


year =int(input('Enter year:'))


if year %4 ==0:
    if year %100 ==0:
        if year %400 ==0:
            print(year,'Is a leap')
        else:
            print(year,'Is not leap')     
    else:
        print(year,'Is a leap')     

else:
    print(year,'Is not leap')           