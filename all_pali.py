class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_list = []

        def expand(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r]  # 回傳一段回文

        for i in range(len(s)):
            tmp = expand(s, i, i)
            tmp2 = expand(s, i, i+1)

            if len(tmp) > 1:
                ans_list.append(tmp)
            if len(tmp2) > 1:
                ans_list.append(tmp2)
            # 如果回文不是單字元就放進列表
        return ans_list


print(Solution().longestPalindrome('abacdedcxyzyxpopoo'))
# ['aba', 'cdedc', 'xyzyx', 'pop', 'opo', 'oo']
# 將所有回文段輸出
