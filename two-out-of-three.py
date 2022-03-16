def twoOutOfThree(nums1, nums2, nums3):
    nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
    return list((nums1 & nums2) | (nums1 & nums3) | (nums2 & nums3))
# Runtime: 72 ms, faster than 90.48% of Python3 online submissions for Two Out of Three.
# Memory Usage: 13.9 MB, less than 52.09% of Python3 online submissions for Two Out of Three.


nums1 = [1, 1, 3, 2]
nums2 = [2, 3]
nums3 = [3]
print(twoOutOfThree(nums1, nums2, nums3))
