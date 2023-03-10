class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset1 = set()
        hashset2 = set()
        
        tuple1 = tuple(s)
        tuple2 = tuple(t)
        
        if len(tuple1) != len(tuple2):
            return False
        
        
        
        for char in s:
            hashset1.add(char)
        for char in t:
            hashset2.add(char)
        if hashset1 == hashset2:
            return True
        else:
            return False