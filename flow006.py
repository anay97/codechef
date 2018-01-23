def sum_of_nos(n):
    sum=0
    while n!=0:
        digit=n%10
        sum=sum + digit
        n=int(n/10)
    return sum

t=int(input())
ans=[]
for i in range(t):
    ans.append(sum_of_nos(int(input())))
for answer in ans:
    print(answer)