a=[1,2,2,3,4,5,5,6]
v=[]
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                if a[i] in v:
                    break
                else:
                    v.append(a[i])
print("duplicate elements are:",v)
              
              
