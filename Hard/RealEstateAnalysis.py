from collections import defaultdict


class Solution:
    def calculate_mean_std_manual(self, data : list):
        # Calculate the mean
        mean_value = sum(data) / len(data)

        # Calculate the standard deviation
        mean = sum(data) / len(data)
        std_deviation = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5

        return mean_value, std_deviation

    def getValue(self, reqArea, area : list, price : list):
        my_data = defaultdict(list)
        n = len(area)
        for i in range(n):
            my_data[area[i]].append(price[i])
        outs = [False] * n
        for i in range(n):
            my_data[area[i]].remove(price[i])
            compList = my_data[area[i]]
            if compList:
                mean_value, std_deviation = self.calculate_mean_std_manual(compList)
                if abs(price[i] - mean_value) > 3 * std_deviation:
                    outs[i] = True
            my_data[area[i]].append(price[i])
        new_area, new_price = [], []
        for i in range(n):
            if not outs[i]:
                new_area.append(area[i])
                new_price.append(price[i])
        new_n = len(new_area)
        new_data = defaultdict(list)
        for i in range(new_n):
            new_data[new_area[i]].append(new_price[i])
        new_v_v_data = dict()
        for k in new_data.keys():
            new_v_v_data[k] = sum(new_data[k])/len(new_data[k])
        new_area_sorted = sorted(list(new_v_v_data.keys()))
        ans = 0
        index1, index2 = 0, 0
        if not new_area_sorted:
            ans = 1000
        elif len(new_area_sorted) == 1:
            ans = new_v_v_data[new_area_sorted[0]]
        elif reqArea in new_area_sorted:
            ans = new_v_v_data[reqArea]
        elif new_area_sorted[0] > reqArea:
            index1, index2 = 0, 1
        elif new_area_sorted[-1] < reqArea:
            index1, index2 = len(new_area_sorted) - 2, len(new_area_sorted) - 1
        else:
            while new_area_sorted[index2] < reqArea:
                index1 = index2
                index2 += 1
        if index1 != index2:
            ans = new_v_v_data[new_area_sorted[index1]] + ((reqArea - new_area_sorted[index1])*(new_v_v_data[new_area_sorted[index2]] - new_v_v_data[new_area_sorted[index1]])) / (new_area_sorted[index2] - new_area_sorted[index1])
        if ans < 1000:
            ans = 1000
        elif ans > 1000000:
            ans = 1000000
        else:
            ans = round(ans)
        return ans

solu = Solution()
solu.getValue(2800, [1200, 1300, 1200, 1300, 1200, 2000], [12000, 24000, 14000, 22000, 13000, 30000])

# Your number
my_number = 3.7

# Round it to the nearest integer
rounded_number = round(my_number)

print(rounded_number)  # This will print 4
