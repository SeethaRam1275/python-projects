x = int(input("Enter a number upto which u want even numbers!\n"))
z = []
for x in range(1, x) :
    for y in range(1, x) :
         if x/y == 2  or x/y == 0 :
            z.append(x)
print(z)
input()
