s = input().split(" ");
n = int(s[0])
m = int(s[1])
a = int(s[2])
b = int(s[3])
print(min((n%m) * b, (m - (n%m))*a))