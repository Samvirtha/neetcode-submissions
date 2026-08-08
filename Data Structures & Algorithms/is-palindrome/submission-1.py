class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=[]
        for i in s.lower():
            if i.isalnum():
                c.append(i)
        g="".join(c)
        return g==g[::-1]