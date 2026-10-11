class Solution:
    def climbStairs(self, n: int) -> int:
        var_one = 1
        var_two = 1
        new = 0

        for i in range(0,n-1):
            new = var_one+var_two
            var_two = var_one
            var_one = new
        return var_one
        