n=int(input())
#L's
for i in range(n):
    for j in range(n):
        if (j==0 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#Square
for i in range(n):
     for j in range(n):
        if (i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
     print()

# Horizontal lines
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#verticle lines
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
