import math
from typing import Union

def check_is_numeric(*value) -> bool:
    if all(isinstance(v, (int, float)) for v in value):
        return True
    return False

class SciPy():
    PI = math.pi
    e = math.e
    # 1
    def addition(self, *nums: Union[int, float]) -> Union[int, float, None]:
        """Performs addition over entered numbers."""
        if all(check_is_numeric(n) for n in nums):
            return sum(nums)
        return None
    # 2
    def subtraction(self, *nums: Union[int, float]) -> Union[int, float, None]:
        """Performs subtraction over entered numbers. Order of numbers inputed will effect the result."""
        res = nums[0]
        if all(check_is_numeric(n) for n in nums):
            for n in nums[1:]:
                res -= n
            return res
        return None
    # 3
    def multiplication(self, *nums: Union[int, float]) -> Union[int, float, None]:
        """Performs multiplication over entered numbers."""
        res = 1
        if all(check_is_numeric(n) for n in nums):
            for n in nums:
                res *= n
            return res
        return None
    # 4
    def divison(self, *nums: Union[int, float]) -> Union[int, float, None]:
        """Performs division over entered numbers. Order of numbers inputed will effect the result."""
        try:
            res = nums[0]
            if all(check_is_numeric(n) for n in nums):
                for num in nums[1:]:
                    if (num == 0):
                        raise ZeroDivisionError("Can't divide by zero.")
                    res /= num
                return res
            return None
        except ZeroDivisionError as e:
            print(f"Error: {e}")
    # 5
    def square_root(self, radicand: Union[int, float]) -> Union[float, None]:
        """Gives the square root of a number."""
        try:
            if radicand < 0:
                raise ValueError("The radicand in a square root can't be negative.")
            if (check_is_numeric(radicand)):
                res = math.sqrt(radicand)
                return res
            return None
        except ValueError as e:
            print(f"Error: {e}")
    # 6
    def n_root(self, radicand: Union[int, float], index: int) -> Union[int, float, None]:
        """Gives the n-th root of a number."""
        try:
            if radicand < 0 and index % 2 == 0:
                raise ValueError("The result of negative radicand of even index of a root gives imaginery number.")
            if (index == 0):
                raise ZeroDivisionError("Index can't be zero.")
            if (check_is_numeric(radicand, index)):
                res = radicand ** (1/index)
                return res
            return None
        except (ZeroDivisionError, ValueError) as e:
            print(f"Error: {e}")
    # 7
    def exponent(self, x: Union[int, float]) -> Union[int, float, None]:
        """Gives the result of exponentiating e^(x)."""
        if (check_is_numeric(x)):
            res = self.e ** x
            return res
        return None
    # 8
    def power(self, base: Union[int, float], n: Union[int, float]) -> Union[int, float, None]:
        """Gives the result of rasing base to the n-th power."""
        if (check_is_numeric(base, n)):
            res = base ** n
            return res
        return None
    # 9
    def factorial(self, base: int) -> Union[int, None]:
        """Calculates the result of a facorial."""
        if (check_is_numeric(base) and base >= 0):
            res = math.factorial(base)
            return res
        return None
    # 10
    def log(self, x: Union[int, float], base: int) -> Union[float, None]:
        """Calculates the natural log(x) function."""
        try:
            if x <= 0:
                raise ValueError("Math domain error: log(x) is undefined for x <= 0")
            if (check_is_numeric(x, base)):
                res = math.log(x, base)
                return res
            return None
        except ValueError as e:
            print(f"Error: {e}")
    # 11
    def log10(self, x: Union[int, float]) -> Union[float, None]:
        """Calculates the log base 10, log10(x) function."""
        try:
            if x <= 0:
                raise ValueError("Math domain error: log(x) is undefined for x <= 0")
            if (check_is_numeric(x)):
                res = math.log10(x)
                return res
            return None
        except ValueError as e:
            print(f"Error: {e}")
    # 12
    def hypotenuse(self, a: Union[int, float], b: Union[int, float]) -> Union[float, None]:
        """Calculates the length of a hypotenuse."""
        if (check_is_numeric(a, b)):
            res = math.sqrt(a**2 + b**2)
            return res
        return None
    # 13
    def sin(self, x: Union[int, float]) -> Union[float, None]:
        """Calculates the sin(x) function."""
        if (check_is_numeric(x)):
            res = math.sin(x)
            return res
        return None
    # 14
    def cos(self, x: Union[int, float]) -> Union[float, None]:
        """Calculates the cos(x) function."""
        if (check_is_numeric(x)):
            res = math.cos(x)
            return res
        return None
    # 15
    def tan(self, x: Union[int, float]) -> Union[float, None]:
        """Calculates the tan(x) function."""
        try:
            if x == 90 or x == 270:
                raise ValueError("For tan(x) function the value of 90 will result in undefind.")
            if (check_is_numeric(x)):
                res = math.tan(x)
                return res
            return None
        except ValueError as e:
            print(f"Error: {e}")
    # 16
    def arcsin(self, x: Union[int, float]) -> Union[float, None]:
        """Calculates the arcsin(x) function."""
        try:
            if x == self.PI:
                raise ValueError("For arcsin(x) function the value of π will result in undefind.")
            if (check_is_numeric(x)):
                res = math.asin(x)
                return res
            return None
        except  ValueError as e:
            print(f"Error: {e}")
    # 17
    def arccos(self, x: Union[int, float]) -> Union[float, None]:
        """Calculates the arccos(x) function."""
        try:
            if x == self.PI:
                raise ValueError("For arccos(x) function the value of π will result in undefind.")
            if (check_is_numeric(x)):
                res = math.acos(x)
                return res
            return None
        except ValueError as e:
            print(f"Error: {e}")
    # 18
    def arctan(self, x: Union[int, float]) -> Union[float, None]:
        """Calculates the arctan(x) function."""
        if (check_is_numeric(x)):
            res = math.atan(x)
            return res
        return None
    # 19
    def scientific_notation(self, num: Union[str, int, float]) -> str:
        """Converts number from standard to scientific notation."""
        if (isinstance(num, str)):
            numList = [n for n in str(num) if (not n == ".")]
            numOriginalLength = len(numList)
            numList.insert(1, ".")
            num = float("".join(numList))
            numList = [n for n in str(num) if (not n == ".")]
            numAfterLength = len(numList)
            exponent = numOriginalLength - numAfterLength
            return f"{num} * 10^{exponent}"
        else:
            return None
    # 20
    def percent_of_change(self, original: Union[int, float], new: Union[int, float]) -> Union[float, None]:
        """Calculates the percent of change of two numbers."""
        try:
            if original == 0:
                pass
            if (check_is_numeric(original) and check_is_numeric(new)):
                res = (abs(original - new) / original) * 100
                return res
            return None
        except Exception as e:
            print(f"Error: {e}")

scipy = SciPy()
print(scipy.addition(13,10,100,115))
print(scipy.subtraction(13,-10,-100,115))
print(scipy.multiplication(13,-10,-100,115))
print(scipy.divison(115,5))
print(scipy.square_root(169))
print(scipy.n_root(169, 3))
print(scipy.exponent(3))
print(scipy.power(3,3))
print(scipy.factorial(5))
print(scipy.log(5, 3))
print(scipy.log10(5))
print(scipy.hypotenuse(3,4))
print(scipy.sin(math.pi))
print(scipy.cos(math.pi))
print(scipy.tan(math.pi))
print(scipy.arcsin(1))
print(scipy.arccos(1))
print(scipy.arctan(math.pi))
print(scipy.scientific_notation("294.04341000"))
print(scipy.percent_of_change(64, 30))