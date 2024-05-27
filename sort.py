import random

def quickSort(nums):
    n = len(nums)

    if n <= 1:
        return
    
    def partition(i, j):
        if j <= i:
            return
        pivot, current = nums[j], i
        for k in range(i, j):
            if nums[k] <= pivot:
                nums[current], nums[k] = nums[k], nums[current]
                current += 1
        nums[current], nums[j] = nums[j], nums[current]
        partition(i, current-1)
        partition(current+1, j)

    partition(0, n-1)
    return nums

def quickSortRnd(nums):
    n = len(nums)

    if n <= 1:
        return
    
    def partition(i, j):
        if j <= i:
            return
        
        auxIndex = random.randint(i, j)
        nums[auxIndex], nums[j] = nums[j], nums[auxIndex]

        pivot, current = nums[j], i
        for k in range(i, j):
            if nums[k] <= pivot:
                nums[current], nums[k] = nums[k], nums[current]
                current += 1
        nums[current], nums[j] = nums[j], nums[current]
        partition(i, current-1)
        partition(current+1, j)

    partition(0, n-1)
    return nums

def mergeSort(nums):
    def merge(nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        merged = []
        i1, i2 = 0, 0

        while i1 < n1 and i2 < n2:
            if nums1[i1] < nums2[i2]:
                merged.append(nums1[i1])
                i1 += 1
            else:
                merged.append(nums2[i2])
                i2 += 1

        while i1 < n1:
            merged.append(nums1[i1])
            i1 += 1

        while i2 < n2:
            merged.append(nums2[i2])
            i2 += 1

        return merged
    
    def sort(nums):
        n = len(nums)

        if n < 2:
            return nums
        
        nums1, nums2 = nums[:n//2], nums[n//2:]
        return merge(sort(nums1), sort(nums2))
    
    return sort(nums)

def heapSort(nums):
    if len(nums) <= 1:
        return nums
    
    def parent(i):
        return (i - 1) // 2
    
    def processNode(i):
        n = len(nums)
        minIndex = i
        if 2*i+1 < n and nums[2*i+1] < nums[i]:
            minIndex = 2*i+1
        if 2*i+2 < n and nums[2*i+2] < nums[minIndex]:
            minIndex = 2*i+2
        if minIndex > i:
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
            processNode(minIndex)

    def heapify():
        n = len(nums)
        for i in range(parent(n-1), -1, -1):
            processNode(i)
        
    def getMin():
        nums[0], nums[-1] = nums[-1], nums[0]
        minVal = nums.pop()
        processNode(0)
        return minVal

    heapify()
    sorted = []
    while nums:
        sorted.append(getMin())
    
    return sorted

nums1 = [2, 5, 7, 8, 3, 4, 1, 6, 9]
nums2 = [2, 5, 7, 8, 3, 4, 1, 6, 9]
nums3 = [2, 5, 7, 8, 3, 4, 1, 6, 9]
nums4 = [2, 5, 7, 8, 3, 4, 1, 6, 9]

print(quickSort(nums1))
print(mergeSort(nums2))
print(heapSort(nums3))
print(quickSortRnd(nums4))