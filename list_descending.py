
## WAP to sort the element of given list??  

#! Descending Order

l=[12,23,34,45,56,67,78,999,654,456,897,234,432,457,758]
n=len(l)
for passes in range(n-1):
    for i in range(n-1-passes):
        if l[i] < l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)
