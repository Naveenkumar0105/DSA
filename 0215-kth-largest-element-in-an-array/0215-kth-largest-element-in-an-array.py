class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapify(nums)

        for j in range(k-1):
            heappop(nums)
        
        return -heappop(nums)


