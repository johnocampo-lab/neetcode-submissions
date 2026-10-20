from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Easy hard fail - O(1) time check
        if len(s) != len(t):
            return False

        # Optimal Hash Map approach - O(N) time, O(K) space
        countS = {}
        countT = {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

        # Alternative: One-liner using Counter - O(N) time, O(K) space
        # return Counter(s) == Counter(t)

        # Alternative: Sorting approach - O(N log N) time, O(N) space
        # return sorted(s) == sorted(t)