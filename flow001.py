n=int(input())
sums=[]
for i in range(n):
    x=input().split(" ")
    sums.append(int(x[0])+int(x[1]))
for sum in sums:
    print(sum)