'''
va_One=int(input("Give a Number--"))
if(va_One%2 == 1):
    print("Weird")

elif(va_One % 2 == 0 and 2<= va_One <= 5):
    print("Not Weird")

elif(va_One%2 == 0 and 6<= va_One <=20 ):
    print("Weird")

elif(va_One%2 == 0 and va_One >=20):
    print("Not Weird")

'''


n=int(input())
if(n%2 == 1):
    print("Weird")

elif(n % 2 == 0 and 2<= n <= 5):
    print("Not Weird")

elif(n%2 == 0 and 6<= n <=20 ):
    print("Weird")

elif(n%2 == 0 and n >=20):
    print("Not Weird")