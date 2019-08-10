
lst = map(int, input().split())
sl = list(sorted(dict.fromkeys(list(lst)), reverse=True))
print(sl[1])

