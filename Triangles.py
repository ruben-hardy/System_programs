#Right angled triangle
for i in range (1,10):
    print("*" * i)
#Right angled triangle reverse
n = 10
for i in range(10):
    print("*" * n)
    n = n - 1
#equalilateral triangle
n = 10
p = 10
for i in range(1,p+1):
    print(" " * n, end="")
    n = n - 1
    for j in range(p-n):
        m = 1
        print( m * "* ", end="")
    print()
#Reverse equilateral triangle:
r = 10
l = 0
c = 10
for i in range(r):
    print(l * " ", end="")
    l = l + 1
    m = 10
    for j in range(1):
        print(c * "* ", end="")
    print()
    c = c - 1
#different approch to write a triangle:

n = 10
k = 0
for i in range(n):
    print(k * " " + (n-i) * "* ")
    k = k + 1

#standard triangle with single loop
n = 10
k = 10
for i in range(n):
    print(k * " " + i * "* ")
    k = k - 1


