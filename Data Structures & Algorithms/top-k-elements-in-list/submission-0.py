class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        for i in nums:
            s[i]=s.get(i,0)+1
        o=[[] for _ in range(len(nums)+1)]
        for j,m in s.items():
            o[m].append(j)
        res=[]
        for i in range(len(o)-1,0,-1):
            for n in o[i]:
                res.append(n)
            if len(res)==k:
                return res
        
