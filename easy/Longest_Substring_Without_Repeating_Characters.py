class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      lastIndexTested = 0
      longestSubStr = ""
      index = 0
      bestScore = 0
      while(index < len(s)):
        nextOcurrance = s.find(s[index], index+1)
        if(nextOcurrance == -1):
          nextOcurrance = len(s) - 1 
        currentScore = nextOcurrance - index
        longestSubStr = s[index:nextOcurrance]
        longestSet = set(longestSubStr)
        if(len(longestSubStr) != len(longestSet)):
          index += 1
        else:
          if(currentScore > bestScore):
            bestScore = currentScore
        return bestScore

sol = Solution()
#print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("pwwkew"))