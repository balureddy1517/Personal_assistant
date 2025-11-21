# s=input("enter string:\n")
# o=input("enter order number:\n")

# c={}
# for i in range(len(s)):
#     if s[i] in c:
#         c[s[i]]+=1
#     else:
#         c[s[i]]=1
        

# keys=list(c.keys())
# print(keys)

# ns=""
# r=""
# d=[]

# for i in o:
#     if i in c:
#         count=c[i]
#         ns=ns+i*count

    
        
# for k in keys:
#     if k not in o:
#         count=c[k]
#         r=r+k*count

# print(ns+r)

        

    
l=list(map(int,input().split(',')))

min=l[0]
curr=0
f=0
count=0

while(curr<len(l)):
    min=l[curr]
    print(l,min,curr)
    for i in range(curr+1,len(l)):

        if(l[i]<min):
            min=l[i]
            pos=i
            f=1
            

    if(f==1):
        temp=l[curr]
        l[curr]=min
        l[pos]=temp
        count+=1
        
    f=0
    curr+=1

print(count)
    



        
    
    