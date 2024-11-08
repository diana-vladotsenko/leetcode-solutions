x = 1000021
s = str(x)
n = len(s)
print(n)
for i in range(0, int(n / 2)):
    last = n - i - 1
    if s[i] != s[last]:
        return False

return True