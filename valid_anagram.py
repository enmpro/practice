class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            print(s[i])
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
           
            
        for c in countS:
            print(countS[c], countT[c])
            if countS[c] != countT.get(c, 0):
                return False
        return True


obj = Solution()

obj.isAnagram("anagram", "nagaram")