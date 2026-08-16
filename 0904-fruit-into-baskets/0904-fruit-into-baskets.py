class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # only 2 baskets
        # basket can hold only 1 fruit type
        # pick 1 fruit from every tree 
        # return max num of fruits that can fit into 2 baskets

        # find longest substring with only 2 chars

        win = Counter()
        l = 0
        ans = 0
        for r,ch in enumerate(fruits):
            win[ch] = win.get(ch,0) + 1
            while len(win) > 2:
                win[fruits[l]] -= 1
                if win[fruits[l]] == 0: del win[fruits[l]]
                l += 1
            ans = max(ans,r-l+1)
        return ans