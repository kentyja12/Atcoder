def check(n):
    ans = 0
    for i in range(1,n+1):
        if not ('7' in list(str(i)) or "7" in list(str(oct(i)))):
            ans += 1
    print(ans)

n = int(input())
check(n)