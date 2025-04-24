class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        d = {}
        max_len = 0
        n = len(s)

        if n == 1:
            return 1
        while r < n:
            if s[r] in d:
                l = max(l, d[s[r]]+1)
            max_len = max(max_len, r-l+1)
            d[s[r]] = r
            r += 1
        return max_len


print(Solution().lengthOfLongestSubstring('pwwkew'))
