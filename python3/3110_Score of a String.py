class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for x in range(0,len(s)-1):
            result += abs(ord(s[x])-ord(s[x+1]))
        return result