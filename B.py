h,w = map(int,input().split()) 
a = [list(input()) for l in range(h)]
cnt = 0
for i in range(h):
    for j in range(w-1):
        if a[i][j] == a[i][j+1] == ".":
            cnt += 1
for i in range(h-1):
    for j in range(w):
        if a[i][j] == a[i+1][j] == ".":
            cnt += 1
print(cnt)