# reverse array

a=[1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(a)//2):
    temp=a[i]
    a[i]=a[-i-1]
    a[-i-1]=temp

print(a)
