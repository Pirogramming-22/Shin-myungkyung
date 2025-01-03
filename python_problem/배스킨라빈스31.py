num = 0


while True: 
    #player A
    while True:
        a = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

        try:
            a = int(a)  
        except ValueError:
            print("정수를 입력하세요")
            continue 
        if a != 1 and a != 2 and a != 3:
            print("1, 2, 3 중 하나를 입력하세요")
            continue 
        else:
            break  

    for i in range(a):
        num+=1
        print(f"playerA : {num}")
        if num == 313:
            break

    if num == 31:
        break

    #player B
    while True:
        b = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

        try:
            b = int(b)  
        except ValueError:
            print("정수를 입력하세요")
            continue 
        if b != 1 and b != 2 and b != 3:
            print("1, 2, 3 중 하나를 입력하세요")
            continue 
        else:
            break  

    for i in range(b):
        num+=1
        print(f"playerB : {num}")
        if num == 31:
            break

    if num == 31:
        break