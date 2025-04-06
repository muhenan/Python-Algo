"""
贪心！
"""
def isSubSequence(longerStr : str, shorterStr : str) -> bool:
    def nextChar(c : str):
        if c == 'z':
            return 'a'
        return chr(ord(c) + 1)
    n_long, n_short = len(longerStr), len(shorterStr)
    if n_long < n_short:
        return False
    i_l, i_s = 0, 0
    while i_l < n_long and i_s < n_short:
        if longerStr[i_l] == shorterStr[i_s] or nextChar(longerStr[i_l]) == shorterStr[i_s]:
            i_l += 1
            i_s += 1
        else:
            i_l += 1
    return i_s == n_short

print(isSubSequence("xasd", "be"))
print(isSubSequence("sdfasd", "ege"))
print(isSubSequence("xasd", "we"))