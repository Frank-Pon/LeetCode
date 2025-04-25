class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''

        def expand(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        s = "cbbd"
        for i in range(len(s)):
            ans = max(ans, expand(s, i, i), expand(s, i, i+1), key=len)
            # max比對字串要使用len的key

        return ans


print(Solution().longestPalindrome('cbbd'))
