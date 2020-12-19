def dif(li,point):
    ans=0
    for s in range(h*w):
        ans += li[s]-point
    return ans

h,w =map(int,input().split())

li = []
for i in range(h):
    li_tmp = [int(k) for k in input().split()]
    li += li_tmp
li.sort()
point = li[0]

print(dif(li,point))