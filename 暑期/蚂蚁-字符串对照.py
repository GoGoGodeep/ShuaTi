# https://mp.weixin.qq.com/s/BjYgrBwnCnq32UXeuSaVsg

n = int(input())
s = input()
t = input()

res = ""
for i in range(n):
    if'A' <= s[i] <= 'Z':
        res += t[i].upper()
    elif'a' <= s[i] <= 'z':
        res += t[i].lower()
    elif'0' <= s[i] <= '9':
        res += str(ord(t[i]))
    else:
        res += "_"

print(res)
