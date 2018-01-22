def get_factorial(num):
    ans=1
    for i in range(2,num+1):
        ans=ans*i
    print(ans)
t=int(input())
num_list=[]
for i in range(t):
    num_list.append(int(input()))
for num in num_list:
    get_factorial(num)