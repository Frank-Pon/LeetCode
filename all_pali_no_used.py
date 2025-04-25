class Solution:
    def longestPalindrome(self, s: str) -> str:
        index = set()
        ans_list = []

        def expand(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r  # 會回傳一個(start,end)形式的tuple

        for i in range(len(s)):
            for l, r in [expand(s, i, i), expand(s, i, i+1)]:  # 將本次的tuple放在list裡,用l、r取用
                if r-l > 1:  # 如果這個回文不是單字元,組成回文至少3個字元
                    # any裡只要任一個是true就是true
                    overlap = any(idx in index for idx in range(l, r))
                    # idx in index for idx in range(l, r)的原理跟以下一樣
                    # overlap = False
                    # for idx in range(l,r):                       #index為某字元在此字串裡的位置
                    #     if idx in index:                         #例如:l 在 apple裡的index就是3
                    #         overlap = True                       #pp 則是[1:3] 從第1開始算到第2
                    if not overlap:  # 如果index沒有用過的話
                        ans_list.append(s[l:r])  # 把此段回文放進list
                        index.update(range(l, r))  # 把此段回文在字串裡的index放進index set
        return ans_list


print(Solution().longestPalindrome('abacdedcxyzyxpopoo'))
# ['aba', 'cdedc', 'xyzyx', 'pop', 'oo']
# 將不重複的回文段輸出
