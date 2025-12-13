class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        count = 0
        left = Counter()
        right = Counter(nums)

        for i in nums:
            right[i] -= 1
            count += left[i * 2] * right[i * 2]
            left[i] += 1

        return count % MOD
