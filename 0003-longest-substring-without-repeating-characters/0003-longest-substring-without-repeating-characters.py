class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length of longest substring w/o repeating characters
        # set 
        l = 0
        win = {}
        ans = 0
        for r, ch in enumerate(s):
            win[ch] = win.get(ch, 0) + 1
            while win[ch] > 1:
                win[s[l]] -= 1
                if win[s[l]] == 0: del win[s[l]]
                l += 1
            ans = max(ans,r-l+1)
        return ans
