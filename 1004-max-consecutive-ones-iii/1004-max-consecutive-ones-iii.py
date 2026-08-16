class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        numZeros = 0
        l = 0
        ans = 0
        maxF = 0

        for r,ch in enumerate(nums):
            if ch == 0: numZeros += 1
            while numZeros > k:
                if nums[l] == 0:
                    numZeros -= 1
                l += 1
            ans = max(r-l+1,ans)
        return ans