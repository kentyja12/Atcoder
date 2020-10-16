s = list(input())
t = list(input())
ans = []
for i in range(len(t)):
    cnt = 0
    try:
        if t[i] == s[i]:
            for j in range(1,len(t)):
                if t[j] != s[j]: 
                    cnt += 1
                    
            ans.append(cnt)
    except IndexError:
        break
            

print(min(ans))
