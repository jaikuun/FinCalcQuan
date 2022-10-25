import math
import os
question = 0
q = 0
e = 2.7183
def car():
    p = float(input("Input Principal: "))
    n = float(input("Input N: "))
    r = float(input("Input Rate: "))
    r = r*0.01
    t = float(input("Input Time: "))
    s1t = r/n
    top = p*s1t 
    ppp = s1t+1
    expo = -n*t
    pp = ppp**expo
    bottom = 1-pp
    final = top/bottom
    total1 = final*n*t
    total = total1 - p
    return (final, total)
def simp():
    p = float(input("Input Principal: "))
    r = float(input("Input Rate: "))
    r = r*0.01
    t = float(input("Input Time: "))
    interest = p*r*t
    return interest
def comp():
    p = float(input("Input Principal: "))
    r = float(input("Input Rate: "))
    r = r*0.01
    t = float(input("Input Time: "))
    n = float(input("Input N: "))
    step1 = r/n
    step2 = step1 + 1
    step3 = n*t
    step4 = step2**step3
    final = step4*p
    return final
def pres():
    a = float(input("Input Accumulation: "))
    r = float(input("Input Rate: "))
    r = r*0.01
    t = float(input("Input Time: "))
    n = float(input("Input N: "))
    s1 = 1 +(r/n)
    s2 = n*t
    s3 = s1**s2
    final = a/s3
    return final
def yie():
    r = float(input("Input Rate: "))
    r = r*0.01
    n = float(input("Input N: "))
    s1 = 1+(r/n)
    s2 = s1**n
    s3 = s2 - 1
    s4 = s3 * 100
    final = s4 
    return final
def cont():
    p = float(input("Input Principal: "))
    r = float(input("Input Rate: "))
    r = r*0.01
    t = float(input("Input Time: "))
    s1 = r*t
    s2 = e**s1
    final = s2 * p
    return final
def house():
    #under development
    p = float(input("Input Principal: "))
    n = 12
    r = float(input("Input Rate: "))
    r = r*0.01
    t = float(input("Input Time: "))
    super = float(input("Input Points: "))
    super = super*0.01
    points = super*p
    s1t = r/n
    top = p*s1t 
    ppp = s1t+1
    expo = -n*t
    pp = ppp**expo
    bottom = 1-pp
    final = top/bottom
    total1 = final*n*t
    total = total1 - p
    
    
    return (final, total, points)


def start():
    print("1. simple interest")
    print("2. compound interest")
    print("3. present value")
    print("4. find yield")
    print("5. continuasly compunded")
    print("6. car")
    question = int(input(": "))
    if question == 1:
        q = simp()
        clear()
        print (q)
        start()
    elif question == 2:
        q = comp()
        clear()
        print (q)
        start()
    elif question == 3:
        q = pres()
        clear()
        print (q)
        start()
    elif question == 4:
        q = yie()
        clear()
        print (q)
        start()
    elif question == 5:
        q = cont()
        clear()
        print (q)
        start()
    elif question == 6:
        q = car()
        clear()
        print(f"monthly payment is {q[0]} \ntotal interest is {q[1]}")
        start()
    elif question == 7:
        q = house()
        clear()
        print(f"monthly payment is {q[0]} \ntotal interest is {q[1]} \npoints are {q[2]}")
        start()
    elif question == 0:
        quit()
def clear():
    os.system("cls")
    pass

clear()
start()






