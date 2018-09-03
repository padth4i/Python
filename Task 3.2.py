def insertionsort(l):
     for i in range(1, n):
 
        temp = l[i]
        j = i-1
        while j >=0 and temp < l[j] :
                l[j+1] = l[j]
                j = j-1
        l[j+1] = temp
        
l = [1, 3, 6, 13, 2]
n=len(l) 
insertionsort(l)
print ("Sorted array is:")
for i in range(n):
    print (l[i])
