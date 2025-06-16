from typing import List


class Soluton:
    def billChange(self, bills: List[int], price):
        ans = float('inf')
        def backtrack(index, current_total, current_bills, price):
            nonlocal ans
            if index == len(bills):
                return
            if current_total == price:
                ans = min(ans, current_bills)
            elif current_total > price:
                return
            else:
                current_total += bills[index]
                current_bills += 1
                for i in range(index, len(bills)):
                    backtrack(i, current_total, current_bills, price)
                # current_bills.
        for i in range(0, len(bills)):
            backtrack(i, 0, 0, price)
        return ans
    #
    def dpBillChange(self, bills: List[int], price):
        return 0





    def billChange_counts(self, bills: List[int], price): # 错了，还需要 debug
        ans = 0
        def backtrack(index, current_total, current_bills, price):
            nonlocal ans
            if index == len(bills):
                return
            if current_total == price:
                ans += 1
            elif current_total > price:
                return
            else:
                current_total += bills[index]
                current_bills += 1
                for i in range(index, len(bills)):
                    backtrack(i, current_total, current_bills, price)
        for i in range(0, len(bills)):
            backtrack(i, 0, 0, price)
        return ans

solu = Soluton()


print(solu.billChange_counts([2,5,10], 21))