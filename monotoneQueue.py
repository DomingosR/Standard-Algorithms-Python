def monotoneQueue(nums):
    n = len(nums)
    prevLarger, nextLarger = [-1] * n, [-1] * n
    numStack = []

    for i, num in enumerate(nums):
        while numStack and nums[numStack[-1]] < num:
            nextLarger[numStack.pop()] = num
        if numStack:
            prevLarger[i] = nums[numStack[-1]]
        numStack.append(i)

    return prevLarger, nextLarger

def monotoneQueueInc(nums):
    n = len(nums)
    largeNum = 10 ** 9 + 7
    prevSmaller, nextSmaller = [largeNum] * n, [largeNum] * n
    numStack = []

    for i, num in enumerate(nums):
        while numStack and nums[numStack[-1]] > num:
            nextSmaller[numStack.pop()] = num
        if numStack:
            prevSmaller[i] = nums[numStack[-1]]
        numStack.append(i)

    return prevSmaller, nextSmaller


nums = [2, 7, 9, 1, 4, 3, 8, 5, 0, 6]
print(monotoneQueueInc(nums))
print(monotoneQueue(nums))