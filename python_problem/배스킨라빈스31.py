num = 0

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