ip = input().split(" ")
n=int(ip[0])
k=int(ip[1])
t=[]
count=0
for i in range(n):
    x=int(input())
    t.append(x)
    if x%k==0:
        count=count+1
print(count)