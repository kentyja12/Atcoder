p = list(map(int,input().split()))
p.sort(reverse=True)
if max(p) > sum(p)-max(p):
    print("No")
elif max(p) == sum(p)-max(p):
    print("Yes")
else:
    cnt = p[0]
    del p[0]
    for i in range(2,0,-1):
        cnt += p[i]
        del p[i]
        if cnt == sum(p):
            print("Yes")
            exit()
    print("No")
