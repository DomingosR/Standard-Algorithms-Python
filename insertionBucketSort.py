from collections import defaultdict

def insertionSort(nums):
    n = len(nums)
    
    for i in range(1, n):
        currentVal = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > currentVal:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = currentVal
    
    return nums

def bucketSort(nums, minVal, maxVal, numBuckets):
    buckets = defaultdict(set)
    interval = 1.0 * (maxVal - minVal) / (numBuckets - 2)

    for num in nums:
        bucket = 0 if num < minVal else min((num - minVal) // interval, numBuckets - 2) + 1
        buckets[bucket].add(num)
    
    i = 0
    for k in range(numBuckets):
        for num in buckets[k]:
            j = i - 1
            while j >= 0 and nums[j] > num:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = num
            i += 1
    
    return nums


nums = [0.5983, 0.5716, 0.8429, 0.5168, 0.1358, 0.3945, 0.1997, 0.5497, 0.525, 0.0966, 0.9487, 0.0783, 0.432, 0.0454, 0.0264, 0.1343, 0.6655, 0.212, 0.359, 0.9172, 0.3015, 0.6195, 0.5804, 0.0186, 0.4881, 0.9177, 0.6256, 0.6642, 0.8897, 0.3492, 0.198, 0.7053, 0.8797, 0.8566, 0.3853, 0.0671, 0.2576, 0.7126, 0.1115, 0.7783, 0.2891, 0.1217, 0.9761, 0.2337, 0.1231, 0.5707, 0.5418, 0.3835, 0.8004, 0.4016, 0.2877, 0.2443, 0.9826, 0.4873, 0.1704, 0.7084, 0.3903, 0.7138, 0.8425, 0.8214, 0.9075, 0.7965, 0.4471, 0.0531, 0.8937, 0.9518, 0.4885, 0.7094, 0.2787, 0.4343, 0.9792, 0.5478, 0.4787, 0.5748, 0.5672, 0.035, 0.3285, 0.7906, 0.1709, 0.0641, 0.6461, 0.9439, 0.8217, 0.4832, 0.0901, 0.9532, 0.5211, 0.947, 0.5669, 0.4359, 0.3093, 0.897, 0.6212, 0.8158, 0.0968, 0.9776, 0.2265, 0.9092, 0.3327, 0.0699]
print(insertionSort(nums))
print(bucketSort(nums, 0.1, 0.9, 8))