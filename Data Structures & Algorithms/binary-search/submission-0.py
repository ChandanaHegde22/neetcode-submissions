class Solution:
    def search(self, nums: List[int], key: int) -> int:
        n = len(nums)
        low,high = 0,n-1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]==key:
                return mid
            elif key > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1