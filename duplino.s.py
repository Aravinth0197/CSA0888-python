a=[1,2,3,4,5,2,5]
v=[]
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                if a[i] in v:
                    break
                else:
                    v.append(a[i])
print(v)
z=[]     
for i in range(len(a)):
    for j in range(len(v)):
            if a[i]!=v[j]:
                if a[i] in z:
                     break
                else:
                   z.append(a[i])
            else:
              break
print(z)
