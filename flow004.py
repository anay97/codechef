def get_sum(str):
	sum=int(str[0])+int(str[len(str)-1])
	print(sum)

t=int(input())
ls=[]
for i in range(t):
	ls.append(input())
for str in ls:
	get_sum(str)
