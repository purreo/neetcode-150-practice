class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # fixed size window of size k
        # win = hashmap counts
        win = Counter()
        l = 0
        ans = 0
        for r,ch in enumerate(s):
            win[ch] = win.get(ch,0) + 1
            
            if len(win) > k:
                win[s[l]] -= 1
                if win[s[l]] == 0: del win[s[l]]
                l += 1

            ans = max(r-l+1, ans)
        return ans