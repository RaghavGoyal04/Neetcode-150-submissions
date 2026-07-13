class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        if not self.nums: return 0.0

        length = len(self.nums)
        if length % 2 == 0: #even 
            return 1.0*(self.nums[length//2 - 1] + self.nums[length//2])/2
        else:
            return 1.0*self.nums[length//2]