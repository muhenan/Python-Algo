class Solution:
    def zh_int(self, num):
        dict_zh = {
            1: "一",
            2: "二",
            3: "三",
            4: "四",
            5: "五",
            6: "六",
            7: "七",
            8: "八",
            9: "九",
        }
        ans = ""
        index = 0
        while num > 0:
            current = num % 10
            if current == 0:
                if index == 0:
                    num = num // 10
                    index += 1
                    continue
                if len(ans) != 0 and ans[0] != "零":
                    ans = "零" + ans
            if current > 0:
                if index == 0:
                    ans = dict_zh[current] + ans
                elif index == 1:
                    ans = dict_zh[current] + "十" + ans
                elif index == 2:
                    ans = dict_zh[current] + "百" + ans
                elif index == 3:
                    ans = dict_zh[current] + "千" + ans
                elif index == 4:
                    ans = dict_zh[current] + "万" + ans
            num = num // 10
            index += 1
        return ans + "元整"

solu = Solution()
print(solu.zh_int(22))
print(solu.zh_int(1234))
print(solu.zh_int(7))


print(solu.zh_int(105))
print(solu.zh_int(2004))
print(solu.zh_int(10409))