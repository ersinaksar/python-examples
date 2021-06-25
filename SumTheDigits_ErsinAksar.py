sayi = int(input("Enter a integer between 0 and  1000 "))
if(sayi<=0 or sayi>=1000):
    print("Wrong input")
else:
    a = sayi // 100
    b = (sayi-100*a) //10
    c = sayi%10

    d = a+b+c

    print(d)
