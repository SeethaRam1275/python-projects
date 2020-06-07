x = int(input("Enter a number upto which u want composites!\n"))
z = []
for x in range(2, x) :
    for y in range(2, x) :
        if x % y == 0 :
            z.append(x)
            break
print(z)
input()
