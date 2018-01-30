def print_list(ls):
	s=''
	for i in ls:
		s=s+str(int(i))+' '
	print(s)

def get_hcf(ls):
	smallest=min(ls)
	hcf=1
	for i in range(1,smallest+1):
		f=0
		for num in ls:
			if num%i!=0:
				f=1
				break
		if f==0:
			hcf=i
	ls2=[]
	for i in ls:
		x=float(float(i)/float(hcf))
		ls2.append(int(x))
	return ls2


t=int(input())
ans=[]
for i in range(t):
	x=input().split(' ')
	n=int(x[0])
	ingredients=[]
	for i in range(1,n+1):
		ingredients.append(int(x[i]))
	ans.append(get_hcf(ingredients))
for a in ans:
	print_list(a)