class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        b={}
        for i in s:
            b[i]=b.get(i,0)+1
        for j in t:
            a[j]=a.get(j,0)+1
        if a==b:
            return True
        return False