n = int(input())
ans = ""
for i in range(n):
    s = input()
    if len(s) < 10: ans = s
    else: 
        ans += s[0]
        ans += str(len(s)-2)
        ans += s[len(s)-1]
    print(ans)
    ans = ""