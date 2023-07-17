list=list(map(int,input().split()))
a=[1,2,3,4,5,6,7,8,9]
dic={}

for i in a:
   count=0;
   for j in list:
      if(j%i==0):
         count+=1
   dic[i]=count
        
print(dic)
   
