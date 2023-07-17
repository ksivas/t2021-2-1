lst=list(map(int, input().split(',')))
a=[1,2,3,4,5,6,7,8,9]
dit={}

for i in a:
   count=0;
   for j in lst:
      if(j%i==0):
         count+=1
   dit[i]=count
        
print(dit)
   
