import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        j = 0
        k = 0
        for i in range(0, len(nums1)+len(nums2)):
            if j >= len(nums1):
                nums3.append(nums2[k])
                k += 1
            elif k >= len(nums2):
                nums3.append(nums1[j])
                j += 1
            elif nums1[j] < nums2[k]:
                nums3.append(nums1[j])
                j += 1
            else:
                nums3.append(nums2[k])
                k += 1
        
        size = len(nums3)
        median = 0
        if(size % 2 == 0):
            num1 = math.floor((size+1)/2)-1
            num2 = math.ceil((size+1)/2)-1
            median = nums3[num1] + nums3[num2]
            median = median / 2
        else:
            median = nums3[int(size/2)]
        return median