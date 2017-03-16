# Basic Method: two loop
def twosum(arr,S):
    sums=[]
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]+arr[j]==S):
                sums.append([arr[i],arr[j]])
    return sums
print twosum([3,5,4,-2,-4,8,11],7)

# Time complexity of above algorithm is O(n^2)

#Using Hash Map
def twoSum(arr,S):
    sums=[]
    hashTable={}
    for i in range(0,len(arr)):
        p= S-arr[i]
        if p in hashTable:
            sums.append([arr[i],p])
        hashTable[arr[i]]=arr[i]
    return sums
print twoSum([3,5,4,-2,-4,8,11],7)

# Time complexity of above algorithm is O(n)

# When input array is sorted i.e in ascending order. using Binary search


# Time complexity O(n log n) runtime, O(1) space

# Two pointer : two sum.



#Time complexity O(n) runtime, O(1) space