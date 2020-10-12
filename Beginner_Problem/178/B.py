a,b,c,d = map(int,input().split())
if a>=0 and b>=0 and c>=0 and d>=0:
    print(b*d)
    exit()
if a<=0 and b<=0 and c<=0 and d<=0:
    print(a*c)
    exit()
if a<=0 and c<=0 and b>=0 and d>=0:
    print(b*d)
    exit()
if c<=0 and d<=0 and a>=0 and b>=0:
    print(a*d)
    exit()
if a<=0 and b<=0 and c>=0 and d>=0:
    print(b*c)
    exit()