class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def get_comb(start, temp, target):
            if target == 0:
                ans.append(temp[:])
                return
            
            for idx in range(start, len(candidates)):
                curr = candidates[idx]
                temp_target = target-curr
                
                if temp_target >= 0:
                    get_comb(idx, temp+[curr], temp_target)
            
        
        get_comb(0, [], target)
        
        return ans
        