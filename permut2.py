a=int(input())
while a!=0:
    list1=[int(x) for x in input().split(" ")]
    list2=[0 for i in range(len(list1))]
    for i in range(a):
        list2[list1[i]-1]=i+1
    f=0
    for i in range(a):
        if list1[i]!=list2[i]:
            f=1
            break
    if f==1:
        print("not ambiguous")
    else:
        print("ambiguous")
    a=int(input())