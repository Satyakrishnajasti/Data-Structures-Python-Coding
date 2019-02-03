n=(int)(input("Enter the Item\t"))
temp=0
a=[10,23,15,8,4,3,25,30,34,2,19]
for i in range(0,10):
    if a[i]==n:
        temp=i+1
        break
    else:
        temp=0
if temp!=0:
    print("Item found\t",temp)
else:
    print("Item not found")
