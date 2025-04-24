s="pwwkew"
left = 0 
max_length = 0
seen = set()

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left+=1
        #print(f'{s[right]} 已重複, 移除 {s[left]} , right now = {right} , left now = {left}')
    #只要s[right]還在seen裡面,就重複執行下方程式直至seen裡沒有s[right]
    seen.add(s[right])
    max_length = max(max_length,right-left+1)

print(max_length)


'''
---------------------------------------------
| right |  left  | max_length | seen |  str |
---------------------------------------------
|   0   |    0   |      1     |   p  |   p  |  -> p
---------------------------------------------
|   1   |    0   |      2     |  p w |   w  |  -> pw
---------------------------------------------
|   2   |    1   |      2     |  w w |   w  |  -> pw -> _w -> _ww
---------------------------------------------
|   2   |    2   |      2     |   w  |   w  |  -> ww -> _w 以上兩部因為w都還在重複,所以right直到全部重複消失才繼續往下
---------------------------------------------
|   3   |    2   |      2     |  w k |   k  |  -> wk
---------------------------------------------
|   4   |    2   |      3     |  wke |   e  |  -> wke
---------------------------------------------
|   5   |    3   |      3     |  kew |   w  |  -> wke -> _ke -> _kew
---------------------------------------------

'''