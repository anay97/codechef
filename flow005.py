def calculate(n,s,ls):
	while True:
		if n==0:
			return s
		greatest=0
		for i in range(len(ls)):
			if ls[i]<=n and ls[i]>greatest:
				greatest=ls[i]
		n=n-greatest
		s=s+1

def init():
	return [1,2,5,10,50,100]

t=int(input())
ip=[]
for i in range(t):
	ip.append(int(input()))
ls=[]
ls=init()
for i in ip:
	ans=calculate(i,0,ls)
	print(ans)
