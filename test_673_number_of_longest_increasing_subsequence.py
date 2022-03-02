from code_673_number_of_longest_increasing_subsequence import Solution

def test_example_1():
    s = Solution()
    nums = [1,3,5,4,7]
    output = 2
    assert s.findNumberOfLIS(nums) == output

def test_example_2():
    s = Solution()
    nums = [2,2,2,2,2]
    output = 5
    assert s.findNumberOfLIS(nums) == output