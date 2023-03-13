def solution(S):
    seen = {0: -1}
    res = cur = 0
    for i in range(len(S)):
        cur ^= 2**(ord(S[i]) - ord('a'))
        if cur in seen:
            res = max(res, i - seen.get(cur))
        else:
            seen[cur] = i
    return res


dic = {}
dic[23] = 45

print(dic)

print(dic[23])

# print(dic.get(23))

key = 45
if key in dic:
    print(dic[key])