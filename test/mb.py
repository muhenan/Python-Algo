# - 数据清洗系统包含多种算子（如分词、去重、归一化）。为了防止数据格式被破坏，某些算子不能紧挨着执行。
# - 题目描述： 给定一个包含 n 种清洗算子名称的列表 operators，以及一个整数 m 代表流水线必须包含的步骤数。同时给定一个字典 exclusions，记录了每个算子后面不能直接紧跟哪些算子（例如 {"clean": ["clean", "tokenize"]} 表示如果在流水线中使用了 "clean"，那么它的下一个步骤不能是 "clean" 或 "tokenize"）。
# - 请找出并返回所有长度为 m 的合法流水线执行序列。同一个算子可以在序列中重复使用。
#
# pipeline_test_cases = [
#     {
#         "operators": ["clean", "tokenize", "normalize"],
#         "m": 3,
#         "exclusions": {"clean": ["clean"], "tokenize": ["clean", "tokenize"]},
#         # 解释：clean 后不能接 clean。# tokenize 后不能接 clean/tokenize (只能接 normalize)。"expected_length": 13 # 建议测试时验证返回的列表长度和具体规则
#     },
#
#     # 互相排斥：没有任何合法的后续步骤
#     {
#         "operators": ["A", "B"],
#         "m": 2,
#         "exclusions": {"A": ["A", "B"], "B": ["A", "B"]},
#         "expected_length": 0
#     }，
#
# ]

'''
deep copy

ans.append(current_ans[:])
ans.append(list(current_ans))
ans.append(current_ans.copy())
ans.append([x for x in current_ans])
'''

def dfs(operators, m, exclusions, current_ans, ans):
    if len(current_ans) == m:
        ans.append(current_ans[:])
        return
    for operator in operators:
        if len(current_ans) == 0 or operator not in exclusions.get(current_ans[-1], []):
            current_ans.append(operator)
            dfs(operators, m, exclusions, current_ans, ans)
            current_ans.pop()

if __name__ == "__main__":
    test_cases = [
        {
            "operators": ["A", "B"],
            "m": 2,
            "exclusions": {"A": ["A", "B"], "B": ["A", "B"]},
            "expected_length": 0,
        },
        {
            "operators": ["clean", "tokenize", "normalize"],
            "m": 3,
            "exclusions": {"clean": ["clean"], "tokenize": ["clean", "tokenize"]},
            "expected_length": 13,
        },
    ]

    for i, case in enumerate(test_cases, 1):
        ans = []
        dfs(case["operators"], case["m"], case["exclusions"], [], ans)
        print(f"case {i}: {ans}")
        print(f"case {i} length: {len(ans)}")
        assert len(ans) == case["expected_length"]