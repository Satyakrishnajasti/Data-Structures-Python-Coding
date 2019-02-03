a=[1,5,2,7,8,0,3]
for i in range (1,6):
    temp=a[i]
    j=i-1
    while j>=0 and a[j]>=temp:
        a[j+1]=a[j]
        j=j-1
        a[j+1]=temp
for k in a:
    print(k)
