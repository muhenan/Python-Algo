from collections import defaultdict

def distinctSums(arr):
    n = len(arr)
    last = defaultdict(lambda: -1)
    res = 0
    for i in range(n):
        res += (i - last[arr[i]]) * (n - i)
        last[arr[i]] = i
    return res

"""
算每一个数的贡献
如果这个数是第一次出现，那么它可以贡献所有它存在的子数组
    它存在的所有子数组，就是左边它可以形成的 乘 右边它可以形成的
    例如 [1,2,3,2,6,7,8]
    对于第一个 2，那么左边可以贡献 2，右边 6 （算一个空的），所以也就是 2 乘 6
如果不是第一次出现，那么它可以贡献的就要除去左边的出现过的，但是右边的依旧都可以贡献
    对于第二个 2，右边依旧可以贡献 4 个（算上空的一个），左边只能贡献 2 了，因为再前面的
    第一个 2 已经贡献过了

核心：每个数能够给答案贡献多少
"""

print(distinctSums([1,2,3])) # 10
print(distinctSums([1,2,1,3])) # 18