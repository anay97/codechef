t=int(input())
ip=[]
for i in range(t):
	ip.append(input())

for i in ip:
	i=int(i)
	i=str(i)
	j=int(i[::-1])
	print(str(j))