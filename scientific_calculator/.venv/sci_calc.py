import math, random, numpy as np
from typing import Union

spinner_1: dict[str, Union[int, float]] = {
    "Eat an apple": 60,
    "Eat a chocolate bar": 21.5,
    "Eat a spinach": 12.5,
    "Eat a garlic": 5.5,
    "Eat a stone": 0.5
}

spinner_2: dict[str, Union[int, float]] = {
    "Not lucky": 90,
    "Pretty lucky": 8,
    "Really lucky": 1.9,
    "Mega lucky": 0.1
}

matrixOne = np.array([[[1/2, 2/2, 3/2]], [[4/2, 5/2, 6/2]], [[7/2, 8/2, 9/2]], [[10/2, 11/2, 12/2]]])
matrixTwo = np.array([[[1/2, 2/2, 3/2]], [[4/2, 5/2, 6/2]], [[7/2, 8/2, 9/2]], [[10/2, 11/2, 12/2]]])
matrixSub = np.array([[[3/2, 2/2, 1/2]], [[6/2, 5/2, 4/2]], [[9/2, 8/2, 7/2]], [[12/2, 11/2, 10/2]]])
matrixScl = np.array([[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]], [[10, 11, 12]], [[13, 14, 15]], [[16, 17, 18]]])
matrix_2 = np.array([[1,2], [3,4]])
matrix_3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
matrix_dot_prod_1 = np.array([[1, 2, 3, 4],
                     [4, 5, 6, 7],
                     [7, 8, 9, 10]])
matrix_dot_prod_2 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9],
                     [10, 11, 12]])

def length_of_matrix(matrix: Union[np.ndarray, list]) -> int:
    elements = []
    def recurse(matrix):
        for ele in matrix:
            if (isinstance(ele, (np.ndarray, list))):
                recurse(ele)
            else:
                elements.append(ele)
    recurse(matrix)
    return len(elements)

def length_of_columns_rows_matrix(matrix: Union[np.ndarray, list]) -> int:
    rows = 0
    cols = 0
    def recurse(matrix: Union[np.ndarray, list], rows: int, cols: int):
        for ele in matrix:
            if (isinstance(ele, (np.ndarray, list))):
                rows += 1
                cols, rows = recurse(ele, rows, cols)
            else:
                cols += 1
        return cols, rows
    cols, rows = recurse(matrix, rows, cols)
    return cols // rows, rows

def check_is_numeric(*value: Union[int, float]) -> bool:
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
        numList = [n for n in str(num) if (not n == ".")]
        numOriginalLength = len(numList)
        numList.insert(1, ".")
        num = float("".join(numList))
        numList = [n for n in str(num) if (not n == ".")]
        numAfterLength = len(numList)
        exponent = numOriginalLength - numAfterLength
        return f"{num} * 10^{exponent}"
    # 20
    def percent_of_change(self, original: Union[int, float], new: Union[int, float]) -> Union[float, None]:
        """Calculates the percent of change of two numbers."""
        try:
            if original == 0:
                return new
            if (check_is_numeric(original, new)):
                res = (abs(original - new) / original) * 100
                return res
            return None
        except Exception as e:
            print(f"Error: {e}")
    # 21
    def permutation(self, n: int, r: int) -> Union[int, None]:
        """Calculates the permutation of r objects taken at the time from the total of n."""
        try:
            if (n < 0 and r < 0):
                raise ValueError("Both n and r values can't be negative.")
            if (check_is_numeric(n, r)):
                res = int((math.factorial(n)) / (math.factorial(n - r)))
                return res
            return None
        except ValueError as e:
            print(f"Error: {e}")
    # 22
    def combination(self, n: int, r: int) -> Union[int, None]:
        """Calculates the combination of r objects taken at the time from the total of n."""
        try:
            if (n < 0 and r < 0):
                raise ValueError("Both n and r values can't be negative.")
            if (check_is_numeric(n, r)):
                res = int((math.factorial(n)) / (math.factorial(n - r) * math.factorial(r)))
                return res
            return None
        except ValueError as e:
            print(f"Error: {e}")
    # 23
    def coin_flip_simulation(self, n: int) -> list[tuple[str, str]]:
        """Simulates the n times of a coin flip. Returns a list of tuples [(n, "outcome"), (n + 1, "outcome"), ...]"""
        if (check_is_numeric(n)):
            outcomes = ["Tails", "Heads"]
            res = []
            for i in range(1, n + 1):
                rand_choice = random.randint(0,1)
                res.append((f"Coin: {i}", outcomes[rand_choice]))
            return res
        return None
    # 24
    def dice_roll_simulation(self, n: int) -> list[tuple[str, int]]:
        """Simulates the n times of a 6-sided dice roll. Returns a list of tuples [(n, x), (n + 1, y), ...]"""
        res = []
        if (check_is_numeric(n)):
            for i in range(1, n + 1):
                outcome = random.randint(1,6)
                res.append((f"Roll: {i}", outcome))
            return res
        return None
    # 25
    def spinner_spin_simulation(self, n: int, **spindata: Union[int, float]) -> list[dict[str, tuple[str, Union[int, float]]]]:
        """Simulates the n times of a circle spinner spin. Returns a list of tuples [(n, "outcome"), (n + 1, "outcome"), ...]"""
        try:
            res = []
            if (isinstance(n, int) and isinstance(spindata, dict)):
                percents = sorted([*spindata.values()])
                valuePairs = sorted([*spindata.items()], key=lambda tup: tup[1])
                percents.reverse()
                valuePairs.reverse()
                percents.insert(0,0)
                if (not sum(percents) == 100):
                    raise ValueError("Percents of each event doesn't add up to a 100.")
                for x in range(1, n + 1):
                    rand = (random.random() * 100)
                    for i in range(0, len(percents) - 1):
                        if (rand > sum(percents[0:i+1])) and rand < sum(percents[0:i+2]):
                            res.append({f"Spin: {x}": valuePairs[i]})
                return res
        except ValueError as e:
            print(f"Error: {e}")
    # 26
    def matrix_addition(self, matrix_1: Union[np.ndarray, list], matrix_2: Union[np.ndarray, list]) -> Union[np.ndarray, list]:
        """Performs addition on two matrices."""
        try:
            if (not length_of_matrix(matrix_1) == length_of_matrix(matrix_2)):
                raise ValueError("Both matrices must have the same number of elements for addition and subtraction.")
            def add(matrix_1: np.ndarray, matrix_2: np.ndarray) -> Union[np.ndarray, list]:
                ind = 0
                elements_1 = []
                elements_2 = []
                sum_of_elements = []
                result = matrix_1.copy()
                def get_elements_from_matrix(matrix, elements):
                    for ele in matrix:
                        if (isinstance(ele, (np.ndarray, list))):
                            get_elements_from_matrix(ele, elements)
                        else:
                            elements.append(float(ele))
                get_elements_from_matrix(matrix_1, elements_1)
                get_elements_from_matrix(matrix_2, elements_2)
                for index in range(0, length_of_matrix(matrix_1)):
                    sum_of_elements.append(elements_1[index] + elements_2[index])
                def add_elements_of_matrices(result, sum, ind):
                    for i, ele in enumerate(result):
                        if isinstance(ele, (np.ndarray, list)):
                            ind = add_elements_of_matrices(ele, sum, ind)
                        else:
                            result[i] = sum[ind]
                            ind += 1
                    return ind
                add_elements_of_matrices(result, sum_of_elements, ind)
                return result
            return add(matrix_1, matrix_2)
        except ValueError as e:
            print(f"Error: {e}")
    # 27
    def matrix_subtraction(self, matrix_1: Union[np.ndarray, list], matrix_2: Union[np.ndarray, list]) -> Union[np.ndarray, list]:
        """Performs subtraction on two matrices."""
        try:
            if (not length_of_matrix(matrix_1) == length_of_matrix(matrix_2)):
                raise ValueError("Both matrices must have the same number of elements for addition and subtraction.")
            def add(matrix_1: np.ndarray, matrix_2: np.ndarray) -> Union[np.ndarray, list]:
                ind = 0
                elements_1 = []
                elements_2 = []
                sum_of_elements = []
                result = matrix_1.copy()
                def get_elements_from_matrix(matrix, elements):
                    for ele in matrix:
                        if (isinstance(ele, (np.ndarray, list))):
                            get_elements_from_matrix(ele, elements)
                        else:
                            elements.append(float(ele))
                get_elements_from_matrix(matrix_1, elements_1)
                get_elements_from_matrix(matrix_2, elements_2)
                for index in range(0, length_of_matrix(matrix_1)):
                    sum_of_elements.append(elements_1[index] - elements_2[index])
                def add_elements_of_matrices(result, sum, ind):
                    for i, ele in enumerate(result):
                        if isinstance(ele, (np.ndarray, list)):
                            ind = add_elements_of_matrices(ele, sum, ind)
                        else:
                            result[i] = sum[ind]
                            ind += 1
                    return ind
                add_elements_of_matrices(result, sum_of_elements, ind)
                return result
            return add(matrix_1, matrix_2)
        except ValueError as e:
            print(f"Error: {e}")
    # 28
    def matrix_scaler_multiplication(self, matrix: Union[np.ndarray, list], scaler: Union[int, float]) -> Union[np.ndarray, list]:
        """Performs scaler multiplication on two matrices."""
        ind = 0
        elements = []
        result = matrix.copy()
        def get_elements_from_matrix(matrix: Union[np.ndarray, list], scaler: Union[int, float]):
            for ele in matrix:
                if (isinstance(ele, (list, np.ndarray))):
                    get_elements_from_matrix(ele, scaler)
                else:
                    elements.append(ele)
        get_elements_from_matrix(matrix, scaler)
        elements_multiplied = [x * scaler for x in elements if x]
        def construct_result_matrix(matrix: Union[np.ndarray, list], ind: int):
            for i, ele in enumerate(matrix):
                if (isinstance(ele, (list, np.ndarray))):
                    ind = construct_result_matrix(ele, ind)
                else:
                    matrix[i] = elements_multiplied[ind]
                    ind += 1
            return ind
        construct_result_matrix(result, ind)
        return result
    # 29
    def matrix_determinant(self, matrix: Union[np.ndarray, list]) -> int:
        """Finds the determinant of a matrix."""
        try:
            def determinant_of_matrix_2(matrix: Union[np.ndarray, list]) -> int:
                a = matrix[0][0] * matrix[1][1]
                b = matrix[0][1] * matrix[1][0]
                determinant = a - b
                return determinant
            def determinant_of_matrix_3(matrix: Union[np.ndarray, list]) -> int:
                a = matrix[0][0]*(matrix[1][1] * matrix[2][2] - matrix[1][2]*matrix[2][1])
                b = matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
                c = matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
                determinant = a - b + c
                return determinant
            def determinant_of_matrix_4(matrix: Union[np.ndarray, list]) -> int:
                result = []
                matrix_without_first_row = np.delete(matrix, 0, axis=0)
                matrix_first_row = np.delete(matrix, [1, 2, 3], axis=0)
                for i in range(0, 4):
                    matrix = np.delete(matrix_without_first_row, i, axis=1)
                    a = matrix[0][0]*(matrix[1][1] * matrix[2][2] - matrix[1][2]*matrix[2][1])
                    b = matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
                    c = matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])
                    determinant = a - b + c
                    result.append(determinant * matrix_first_row[0][i])
                    matrix = matrix_without_first_row
                determinant_4 = result[0] - result[1] + result[2] - result[3]
                return determinant_4
            def check_perfect_sqr_dimensions(matrix: Union[np.ndarray, list]) -> int:
                if (not math.sqrt(length_of_matrix(matrix)) == int(math.sqrt(length_of_matrix(matrix)))):
                    raise ValueError("The matrix must have equal dimensions, same amount of rows as columns.")
                return int(math.sqrt(length_of_matrix(matrix)))
            dimensions = check_perfect_sqr_dimensions(matrix)
            if (dimensions == 2):
                return determinant_of_matrix_2(matrix)
            if (dimensions == 3):
                return determinant_of_matrix_3(matrix)
            if (dimensions == 4):
                return determinant_of_matrix_4(matrix)
        except ValueError as e:
            print(f"Error: {e}")
    # 30
    def matrix_dot_product(self, matrix_1: Union[np.ndarray, list], matrix_2: Union[np.ndarray, list]) -> Union[np.ndarray, list]:
        """Performs dot product on two matrices."""
        try:
            result = []
            subarray = []
            subarray_result = []
            cols_1, rows_1 = length_of_columns_rows_matrix(matrix_1)
            cols_2, rows_2 = length_of_columns_rows_matrix(matrix_2)
            if (not cols_1 == rows_2):
                raise ValueError("Can't calculate a dot product of matrices with unequal length of rows and columns.")
            for k in range(0, rows_1):
                for j in range(0, cols_2):
                    for i in range(0, cols_1):
                        a = matrix_1[k][i] * matrix_2[i][j]
                        subarray.append(a)
                        if (len(subarray) == cols_1):
                            e = sum(subarray)
                            subarray_result.append(e)
                            subarray.clear()
                        if (len(subarray_result) == cols_2):
                            result.append(list(subarray_result))
                            subarray_result.clear()
            return result
        except ValueError as e:
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
print(scipy.permutation(10, 3))
print(scipy.combination(10, 3))
print(scipy.coin_flip_simulation(5))
print(scipy.dice_roll_simulation(5))
print(scipy.spinner_spin_simulation(5, **spinner_1))
print(scipy.matrix_addition(matrixOne, matrixTwo))
print(scipy.matrix_subtraction(matrixSub, matrixTwo))
print(scipy.matrix_scaler_multiplication(matrixScl, 10))
print(scipy.matrix_determinant(matrix_2))
print(scipy.matrix_determinant(matrix_3))
print(scipy.matrix_determinant(matrix_4))
print(scipy.matrix_dot_product(matrix_dot_prod_1, matrix_dot_prod_2))