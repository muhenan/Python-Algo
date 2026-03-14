# array A: original list
# array B: diff array

# 差分数组
# 差分数组是一种用于高效处理区间操作的数据结构
# 它通过记录数组中相邻元素之间的差值来简化对区间操作的计算
# 差分数组在处理多次区间修改和查询时非常高效


# 差分数组的应用场景
# 1. 区间修改
# 2. 区间查询
# 3. 多次区间修改和查询

class DifferenceArray:
    """
    差分数组工具类
    
    差分数组的核心操作：
    1. 构建：B[i] = A[i] - A[i-1]
    2. 区间增加：在区间[l,r]上增加val
       - B[l] += val
       - B[r+1] -= val
    3. 还原：A[i] = B[0] + B[1] + ... + B[i]
    """
    def __init__(self, nums):
        """
        初始化差分数组
        Time: O(n), Space: O(n)
        """
        self.diff = [0] * (len(nums) + 1)  # 多开一个空间便于处理右边界
        # 构建差分数组
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i-1]
    
    def add_range(self, left: int, right: int, val: int) -> None:
        """
        区间增加操作：将区间[left, right]内的所有元素加上val
        Time: O(1)
        """
        self.diff[left] += val
        self.diff[right + 1] -= val
    
    def reconstruct(self) -> list:
        """
        还原原始数组
        Time: O(n), Space: O(n)
        """
        result = [0] * (len(self.diff) - 1)
        result[0] = self.diff[0]
        for i in range(1, len(result)):
            result[i] = result[i-1] + self.diff[i]
        return result


# 使用示例
def example_usage():
    # 示例1：基本操作
    nums = [1, 2, 3, 4, 5]
    diff_array = DifferenceArray(nums)
    print("原始数组:", nums)
    
    # 在区间[1,3]上加2
    diff_array.add_range(1, 3, 2)
    result = diff_array.reconstruct()
    print("区间[1,3]加2后:", result)  # [1,4,5,6,5]
    
    # 在区间[2,4]上减1
    diff_array.add_range(2, 4, -1)
    result = diff_array.reconstruct()
    print("区间[2,4]减1后:", result)  # [1,4,4,5,4]

    # 示例2：航班预订统计
    def corpFlightBookings(bookings: list, n: int) -> list:
        """
        LeetCode 1109: Corporate Flight Bookings
        给定航班预订表bookings和航班数n，返回每个航班的预订人数
        bookings[i] = [firsti, lasti, seatsi]表示在航班firsti到lasti上预订seatsi个座位
        """
        diff = DifferenceArray([0] * n)
        for first, last, seats in bookings:
            diff.add_range(first-1, last-1, seats)  # 注意转换为0-based索引
        return diff.reconstruct()
    
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    print("\n航班预订示例:")
    print("预订表:", bookings)
    print("各航班预订数:", corpFlightBookings(bookings, n))

    # 示例3：区间加法
    def getModifiedArray(length: int, updates: list) -> list:
        """
        LeetCode 370: Range Addition
        给定长度为length的数组（初始值全0）和更新操作updates
        updates[i] = [startIdx, endIdx, inc]表示将区间[startIdx,endIdx]内的元素都加上inc
        返回最终数组
        """
        diff = DifferenceArray([0] * length)
        for start, end, inc in updates:
            diff.add_range(start, end, inc)
        return diff.reconstruct()
    
    length = 5
    updates = [[1,3,2],[2,4,3],[0,2,-2]]
    print("\n区间加法示例:")
    print("更新操作:", updates)
    print("最终数组:", getModifiedArray(length, updates))


if __name__ == "__main__":
    example_usage()
