a=[4,2,7,1,9,0]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
for i in a:
    print(i)

