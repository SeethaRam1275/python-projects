x = input("enter a number upto which u want primes!\n")
x = int(x)
z = []
for x in range(2,x) :
    for y in range(2,x) :
        if x % y == 0 :
            break
    else :
        z.append(x)
print(z)
input("")






   
