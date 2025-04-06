from typing import List


class RelativeRankAssigner:
    """
    LeetCode 506: Relative Ranks
    
    Problem Description:
    Given an array of scores of athletes in a competition, return an array of their relative ranks
    as strings. The ranks are assigned based on scores in descending order where:
    - The athlete with the highest score gets "Gold Medal"
    - The second highest gets "Silver Medal"
    - The third highest gets "Bronze Medal"
    - All others get their placement as a string (e.g., "4", "5", etc.)
    
    Examples:
    - Input: score = [5,4,3,2,1]
      Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
    - Input: score = [10,3,8,9,4]
      Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
    
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n) for the auxiliary arrays
    """
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # 定义前三名的奖牌名称
        titles = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        # 创建分数到索引的映射字典
        score_map = {}
        for i in range(len(score)):
            score_map[score[i]] = i
            
        # 对分数进行排序（降序）
        sorted_scores = sorted(score, reverse=True)
        
        # 初始化结果数组
        ans = [""] * len(score)
        
        # 为每个分数分配名次
        for i in range(len(sorted_scores)):
            idx = score_map[sorted_scores[i]]
            if i < 3:
                ans[idx] = titles[i]  # 前三名获得奖牌
            else:
                ans[idx] = str(i + 1)  # 其他名次
        
        return ans