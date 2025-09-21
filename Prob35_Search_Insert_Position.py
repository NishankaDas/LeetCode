class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        u = len(nums)
        mid = 0
        x = target
        while low <= high:

            mid = (high + low) // 2

            # If x is greater, ignore left half
            if nums[mid] < x:
                low = mid + 1

            # If x is smaller, ignore right half
            elif nums[mid] > x:
                high = mid - 1

            # means x is present at mid
            else:
                return mid

            # If we reach here, then the element was not present
        if x > nums[mid]:
            return mid+1
        if x < nums[0]:
            return 0
        if x> nums[u-2] and x< nums[u-1]:
            return mid
        if x< nums[mid]:
            if mid-1 == 0:
                return mid
            elif nums[mid-1] < x:
                return mid 
            return mid-1

        
            
