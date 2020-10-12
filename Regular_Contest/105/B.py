def remove_v(i,li):
    while i in li:
        try:
            li.remove(i)
        except ValueError:
            pass

n = int(input())
p = list(map(int,input().split()))
p.sort(reverse=True)
if max(p) == min(p):
    print(max(p))
    exit()
for i in range(10000):
    tmp = p[0]
    p[0] = p[0]-p[-1]
    remove_v(tmp,p)
    p.sort(reverse=True)
    if p[0] == p[-1]:
        print(max(p))
        exit()