n = int(input("Enter number"))
m = 1
for i in range(1, n+1):
    for j in range(1, m+1):
        if i == j:
            e = "\n"
        else:
            e = ""
        print(j, end=e)
    m += 2
