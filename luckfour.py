def count4(s):
	count=0
	for i in range(len(s)):
		if s[i]=='4':
			count=count+1
	print(count)

t=int(input())
ls=[]
for i in range(t):
	ls.append(input())
for ip in ls:
	count4(ip)
