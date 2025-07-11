#week3作业

#词典；每个词后方存储的是其词频，词频仅为示例，不会用到，也可自行修改
Dict = {"经常":0.1,
        "经":0.05,
        "有":0.1,
        "常":0.001,
        "有意见":0.1,
        "歧":0.001,
        "意见":0.2,
        "分歧":0.2,
        "见":0.05,
        "意":0.05,
        "见分歧":0.05,
        "分":0.1}

#待切分文本
sentence = "经常有意见分歧"

#实现全切分函数，输出根据字典能够切分出的所有的切分方式
def all_cut(sentence, Dict):
    """
    使用动态规划算法，根据给定词表，对文本进行全切分
    """
    n = len(sentence)
    """
    构建n + 1个数组，每个数组内部存储多个切分方案(list)，
    每个方案又是一个列表, 用来存储词（例如：['经常', '有意见', '分歧']），最后一个表示边界情况，切分方案为空
    """
    dp = [[] for _ in range(n + 1)]
    dp[n] = [[]] # 最后一个必须显示赋值为空列表
    for i in range(n - 1, -1, -1): # (n - 1) >= i >= 0
        for j in range(i + 1, n + 1): # (i + 1) >= j >= n
            word = sentence[i:j] # 最大切分范围: 从i到n-1(最后字符)的位置
            if word in Dict:
                # 状态转移：获取已有的切分方案(dp[n]是空方案)
                # 将当前词与后续所有切分方案组合
                for prev in dp[j]:
                    dp[i].append([word] + prev) # 当前状态追加已有的状态
    return dp[0]

for result in all_cut(sentence, Dict):
    print(result, end=None)

#目标输出;顺序不重要
target = [
    ['经常', '有意见', '分歧'],
    ['经常', '有意见', '分', '歧'],
    ['经常', '有', '意见', '分歧'],
    ['经常', '有', '意见', '分', '歧'],
    ['经常', '有', '意', '见分歧'],
    ['经常', '有', '意', '见', '分歧'],
    ['经常', '有', '意', '见', '分', '歧'],
    ['经', '常', '有意见', '分歧'],
    ['经', '常', '有意见', '分', '歧'],
    ['经', '常', '有', '意见', '分歧'],
    ['经', '常', '有', '意见', '分', '歧'],
    ['经', '常', '有', '意', '见分歧'],
    ['经', '常', '有', '意', '见', '分歧'],
    ['经', '常', '有', '意', '见', '分', '歧']
]

