class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        li = []
        for i in range(0, len(nums)):
            j = i + 1
            for k in range(j, len(nums)):

                sum = nums[i] + nums[k]

                if sum == target:

                    li.append(i)
                    li.append(k)
                    # print(li)
                    return li
                # print(j, k)

if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    # target = 9
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    li = solution.twoSum(nums, target)
    print(li)


