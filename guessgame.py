from random import randint

b = True
b1 = 0 ; b2 = 0
gu = []

while b:
    a = input("Enter a number between 1 t0 100 \n(or) Enter q to Quit ") #55
    if a == 'q':
        b = False
        break
    a = int(a) 
    c =  randint(1,100)   #50
    print(f"My number is {c}")
    if a < 1 or a > 100 :     
        print('out of bounds')
    elif a == c :
        print (f'your guess is correct : {a} and you gussed it in {len(gu)}')
        b = False
        break
    d = c+10    #60   
    e = c-10    #40
    while b1 == 0 :
        if a > c and a <= d :   # 55 > 50  and 55  <= 60 
            print('warm')
        if a < c and a >= e :  # 55 < 50 and 55 >= 40
            print('warm')
        if a > d:
            print('cold')
        if a < e :
            print('cold')
        b1 += 1
        break
    while b1 == 1 and b2 == 1  :
        
        if a > c and a <= d :
            print('warmer')
            break
        if a < c and a >= e :
            print('warmer')
            break
        if a > 60:
            print('colder')
            break
        if a < e :
            print('colder')
            break
    b2 = 1
    gu.append(a)
    continue