class FenwickTree:
    def __init__(self, nums, maxVal):
        self.maxVal = maxVal
        self.tree = [0] * (maxVal + 2)

        for num in nums:
            self.update(num)

    def update(self, num):
        while num <= self.maxVal:
            self.tree[num + 1] += 1
            num += num & (-num)

    def getCount(self, num):
        sum = 0

        while num > 0:
            sum += self.tree[num + 1]
            num -= num & (-num)
        
        return sum

    def getIntervalCount(self, num1, num2):
        if num1 >= num2:
            return 0
        
        return self.getCount(num2 - 1) - self.getCount(num1 - 1)

class SegmentTree:
    #  Segment tree designed to retrieve minimum of a range
    #  For other purposes, adapt code accordingly
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        self.maxVal = nums[0] + 1

        for i in range(self.n):
            self.tree[i + self.n] = nums[i]
            self.maxVal = max(self.maxVal, nums[i] + 1)

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])

    def updateNode(self, i, newVal):
        self.tree[i + self.n] = newVal
        i += self.n

        while i > 1:
            self.tree[i // 2] = min(self.tree[i], self.tree[i ^ 1])
            i //= 2

    def getMin(self, lowVal, highVal):
        #  The range in question includes lowVal but excludes highVal
        minVal = self.maxVal
        lowVal += self.n
        highVal += self.n

        while lowVal < highVal:
            if lowVal & 1:
                minVal = min(minVal, self.tree[lowVal])
                lowVal += 1
            if highVal & 1:
                highVal -= 1
                minVal = min(minVal, self.tree[highVal])
            
            lowVal //= 2
            highVal //= 2
        
        return minVal

# Test Code
nums = [2, 2, 2, 4, 4, 5, 7]
fenwick = FenwickTree(nums, max(nums))
print(fenwick.getIntervalCount(2, 4))

nums2 = [2, 3, 5, 1, 4, 5, 7, 6]
segment = SegmentTree(nums2)
print(segment.getMin(0, 4))