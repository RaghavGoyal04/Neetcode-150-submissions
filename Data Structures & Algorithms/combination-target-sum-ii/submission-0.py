class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, cur, total):
            if total >= target or i == len(candidates):
                if total == target:
                    res.append(cur[:])
                return
            #take
            dfs(i+1, cur + [candidates[i]], total + candidates[i])
            #not take
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res