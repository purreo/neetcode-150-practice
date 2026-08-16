class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        win = {}
        l = 0
        ans = 0
        maxF = 0
        for r, ch in enumerate(s):
            win[ch] = win.get(ch, 0) + 1
            maxF = max(maxF, win[ch])
            while (r - l + 1) - maxF > k:      # shrink while INVALID
                win[s[l]] -= 1
                if win[s[l]] == 0: del win[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans