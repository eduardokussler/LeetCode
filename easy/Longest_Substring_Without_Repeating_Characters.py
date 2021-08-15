class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      lastIndexTested = 0
      longestSubStr = ""
      index = 0
      bestScore = 0
      while(index < len(s)):
        nextOcurrance = s.find(s[index], index+1)
        if(nextOcurrance == -1):
          nextOcurrance = len(s)
        currentScore = nextOcurrance - index
        longestSubStr = s[index:nextOcurrance+1]
        longestSet = set(longestSubStr)
        if(len(longestSubStr) != len(longestSet)):
          subStrIndex = 0
          while(subStrIndex < nextOcurrance):
            longestSubStr = s[index:nextOcurrance+1-subStrIndex]
            longestSet = set(longestSubStr)
            subStrIndex += 1
            if(len(longestSubStr) == len(longestSet)):
              currentScore = len(longestSubStr)
              break 
        if(currentScore > bestScore):
          bestScore = currentScore
        index += 1
      return bestScore

sol = Solution()
#print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("pwwkew"))