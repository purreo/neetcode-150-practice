class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1); win = Counter()
        k = len(s1)
        for r, ch in enumerate(s2):
            win[ch] += 1
            if r >= k:                      
                l = s2[r-k]
                win[l] -= 1
                if win[l] == 0: del win[l]
            if win == need: return True
        return False