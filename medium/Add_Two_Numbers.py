# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      if(l1 == None):
        return l2
      if(l2 == None):
        return l1
      numberl1 = self.reverse(l1)
      numberl2 = self.reverse(l2)
      result = numberl1 + numberl2
      return self.buildList(result)
      
    def reverse(self, number: ListNode):
      result = 0
      shift = 1
      while number != None:
        result += number.val * shift
        shift *= 10
        number = number.next
      return result
    
    def buildList(self, num: int):
      numStr = str(num)
      numList = []
      numList[:0] = numStr
      returnList = ListNode(int(numList[len(numList)-1]), None)
      temp = returnList
      
      index = len(numList) - 2
      while(index >= 0):
        temp.next = ListNode(int(numList[index]), None)
        index -= 1
        temp = temp.next
        
      return returnList