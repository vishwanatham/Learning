def intreverse(n):
    s = ""
    for i in range(0, len(str(n))):
        s = s + str(n % 10)
        n = int(n / 10)
    return (s)


# supporting function for sumprimes
def isprime(n):
    count = 0
    if n <= 1:
        return False
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
        if i < n and count == 2:
            return False
    return True


def sumprimes(l):
    sum = 0
    for x in l:
        if isprime(x):
            sum += x
    return sum


import re


def matched(s):
    s = re.sub("[^()]", "", s)  # Replace all non-bracket characters with empty string
    if len(s) > 0:
        r = re.sub("[(][)]", "", s)  # Replace () with empty string as it's a match
        if r == s:
            return False
        else:
            return matched(r)
    else:
        return True


