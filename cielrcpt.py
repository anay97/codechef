import math

def calculate(n,s,ls):
	if n==0:
		return s
	greatest=0
	for i in range(12):
		if ls[i]<=n and ls[i]>greatest:
			greatest=ls[i]
	n=n-greatest
	s=s+1
	return calculate(n,s,ls)


t=int(input())
ip=[]
for i in range(t):
	ip.append(int(input()))
ls=[]
for i in range(12):
	ls.append(math.pow(2,i))
for i in ip:
	ans=calculate(i,0,ls)
	print(ans)
