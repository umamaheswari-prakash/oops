arr=input("Enter a array :")
x=len(arr)
count=0
n=[]
list=[]
for i in (0,x):
    for j in (0,i):  
      n.append(arr[j]+arr[j+1])
      list.append(arr[j],arr[j+1])
length=len(n)   
for i in (0,length):
    for num in (0,i):
        if n[num]==n[num+1]:
           print("sum",n[num])
           count=count+1   
print("pair!",count)
   