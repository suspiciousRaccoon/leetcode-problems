
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x // 2 if x > 1 else x

        while left <= right:
            mid = (left + right) // 2
            power = mid * mid

            if power == x:
                return mid
            elif power < x:
                left = mid + 1
            elif power > x:
                right = mid - 1

        return right


class NormalSolution:
    def mySqrt(self, x: int) -> int:
        if x in [1, 0]:
            return x
        number = 1
        while number*number <= x:
            number += 1
        return number


class OwnSolution:  # yeah...
    def mySqrt(self, x: int) -> int:
        last_root = x
        for i in range(1, x+1):
            power = i*i
            if power > x:
                return last_root
            else:
                last_root = i
        return last_root
