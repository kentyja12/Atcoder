n = int(input())
cnt = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a*b >= n:
            break
        elif a*b < n:
            cnt += 1
print(cnt)