class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product_without_zeros = 1

        for x in nums:
            if x == 0:
                zero_count += 1
            else:
                product_without_zeros *= x

        result = []
        for x in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                result.append(product_without_zeros if x == 0 else 0)
            else:
                result.append(product_without_zeros // x)

        return result