n = int(input())
p = map(int,input().split())
for i in range(1,n+1):
    for j in p:
        li = list(range(0,i+1))
        if j in li:
            try:
                li.remove(j)
            except ValueError:
                pass
        print(min(li))