n = int(input())
s = 0
for i in range(n):
    a,b = map(int,input().split())
    s += (b*(b+1)-a*(a-1))/2
print(int(s))