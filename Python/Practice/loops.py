n = int(input("Enter number"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    for k in range(1, i):
        i -= 1
        print(i, end="")
    print("")


