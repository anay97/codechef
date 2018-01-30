def convert_to_int(ls):
	ls2=[]
	for i in ls:
		ls2.append(int(i))
	return ls2

t=int(input())
for i in range(t):
	x=input().split(' ')
	x=convert_to_int(x)
	small=min(x)
	large=max(x)
	for val in x:
		if val!=small and val!=large:
			print(val)