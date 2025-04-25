def expand(s):
    ans = ""  # 設定一個裝結果的變數
# 每個字母都嘗試當中心（奇數長度回文）
    for i in range(len(s)):
        # 設定左右指標都從 i 開始
        l = i
        r = i

        # 向左右擴展，只要還對稱就繼續
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            # print(f'i={i},原:{l, r},return:{l+1, r},結果:{s[l+1:r]}')
            # print(f'========================')
        # 跳出時已經多擴展了一格，回退
        tmp = s[l+1:r]

        l2 = i
        r2 = i+1
        while l2 >= 0 and r2 < len(s) and s[l2] == s[r2]:
            l2 -= 1
            r2 += 1
            # print(f'i={i},原:{l2, r2},return:{l2+1, r2},結果:{s[l2+1:r2]}')
        tmp2 = s[l2+1:r2]

        # 如果找到更長的回文，就更新答案
        if len(tmp) > len(ans):
            ans = tmp
        if len(tmp2) > len(ans):
            ans = tmp2
    return ans


print(expand("cbbd"))
