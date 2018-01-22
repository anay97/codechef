import math

def greatest_int_func(num,power):
    denom=math.pow(5,power)
    return int(num/denom)
def get_count(x):
    count = 0
    i=1
    while True:
        y =int(greatest_int_func(x,i))
        if y!=0:
            count=count + y
            i=i+1
        else:
            break
    print(count)
t=int(input())
l=[]
for i in range(t):
    l.append(int(input()))
for list_item in l:
    get_count(list_item)