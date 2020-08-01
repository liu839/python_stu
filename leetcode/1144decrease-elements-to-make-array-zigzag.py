class Solution:
    def movesToMakeZigzag(self, nums) -> int:
        size = len(nums)

        def up(index, pre):
            if index == size: return 0
            return down(index + 1, nums[index]) + max(0, pre - nums[index] + 1)

        def down(index, pre):
            if index == size: return 0
            return up(index + 1, min(pre - 1, nums[index])) + max(0, nums[index] - pre + 1)

        # 从先升序或先降序中选择操作数小的作为结果
        return min(up(1, nums[0]), down(1, nums[0]))

