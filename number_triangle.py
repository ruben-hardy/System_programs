n = 10
for i in range(n+1):
    print((n-i) * " ", end="")
    k = 1
    for j in range(i):
        print(str(k), end=" ")
        k = k + 1
    print()
#Reverse order
n = 10
for i in range(n):
    print(i * " ", end="")
    k = 10-i
    for j in range(n-i):
        print(str(k), end=" ")
        k = k - 1
    print()