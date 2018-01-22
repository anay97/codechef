n=int(input())
p1=0
p2=0
current_lead=0
lead_diff=0
for i in range(n):
    x=input().split(" ")
    p1+=(int(x[0]))
    p2+=(int(x[1]))
    lead=abs(p1-p2)
    if lead>lead_diff:
        lead_diff=lead
        if p1>p2:
            current_lead=1
        else:
            current_lead=2
print(str(current_lead)+' '+str(lead_diff))