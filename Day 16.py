class Solution:
    def calculate(self, s: str) -> int:
        cur = res = 0
        sign = 1
        stack = []
        for char in s:
            if char.isdigit():
                cur = cur * 10 + int(char)
            elif char in ["+", "-"]:
                res += sign * cur
                sign = 1 if char == "+" else -1
                cur = 0
            elif char == "(":
                stack.append(res)
                stack.append(sign)

                sign = 1

                res = 0
            elif char == ")":
                res += sign * cur
                res *= stack.pop()
                res += stack.pop()
                cur = 0
        return res + sign * cur


s = "(1+(4+5+2)-3)+(6+8)"
func = Solution()
print(func.calculate(s))


############################################################################################################################
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False

        def helper(first, second, remaining):
            if len(remaining) < max(len(first), len(second)):
                return False

            if (first[0] == "0" and len(first) != 1) or (
                second[0] == "0" and len(second) != 1
            ):
                return False
            first = int(first)
            second = int(second)
            res = str(first + second)
            len_res = len(res)

            if len(remaining) < len_res:
                return False
            if res == remaining[0:len_res]:
                if len(remaining) == len_res:
                    return True
                first = second
                second = res
                remaining = remaining[len_res:]
                return helper(str(first), str(second), remaining)
            return False

        indx1 = 0
        for indx2 in range(indx1 + 1, len(num)):
            for indx3 in range(indx2 + 1, len(num)):
                first = num[indx1:indx2]
                second = num[indx2:indx3]
                remaining = num[indx3:]
                if helper(first, second, remaining):
                    return True
        return False


s = "199100199"
func = Solution()
print(func.isAdditiveNumber(s))
