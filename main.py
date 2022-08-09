import copy
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:  # noqa
        """Best time and space complexity"""
        while m > 0 and n > 0:
            x = nums1[m - 1]
            y = nums2[n - 1]
            if x == y:
                nums1[m + n - 1] = x
                nums1[m + n - 2] = x
                m -= 1
                n -= 1
            elif y > x:
                nums1[m + n - 1] = y
                n -= 1
            else:
                nums1[m + n - 1] = x
                m -= 1
        while n > 0:
            nums1[n - 1] = nums2[n - 1]
            n -= 1

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:  # noqa
        """Best time performance"""
        nums1[m:] = nums2
        nums1.sort()


test_data = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([3, 0, 0], 1, [1, 2], 2, [1, 2, 3]),
]

if __name__ == '__main__':
    for nums1, m, nums2, n, result in copy.deepcopy(test_data):
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == result

    for nums1, m, nums2, n, result in copy.deepcopy(test_data):
        Solution().merge2(nums1, m, nums2, n)
        assert nums1 == result
