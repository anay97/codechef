t=int(input())
ans=[]
for i in range(t):
    x=input().split(" ")
    a=int(x[0])
    b=int(x[1])
    ans.append(a%b)
for answer in ans:
    print(answer)