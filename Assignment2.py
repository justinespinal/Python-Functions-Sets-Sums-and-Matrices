# Discrete Structures (CSCI 220)
# Summer 2023, Session 2
# Assignment 1 - Propositional Logic and Truth Tables
# Justin Espinal
import math

# Acknowledgements:
# I worked with the class
# I used the following sites ... (if applicable)

from itertools import chain, combinations
import random
import numpy as np

# [2] Define functions that compute the following set operations.
# The first five functions are binary and should accept two arguments each,
# while the last function is unary and should accept only one argument.
# You may use built-in functions to your language or implement them yourself.

# set_union(set1, set2) : X ∪ Y
# set_intersection(set1, set2): X ∩ Y
# set_difference(set1, set2): X − Y
# set_symmetric_difference(set1, set2):  X ∆  Y
# set_cartesian_product(set1, set2): X x Y
# set_power_set(set1):  P(X)

def set_union(set1, set2):
    set3 = set()
    for s in set1:
        set3.add(s)
    for s in set2:
        set3.add(s)
    return set3


def set_intersection(set1, set2):
    set3 = set()
    for s in set1:
        if s in set2:
            set3.add(s)
    return set3


def set_difference(set1, set2):
    set3 = set()
    for s in set1:
        if s not in set2:
            set3.add(s)
    return set3


def set_symmetric_difference(set1, set2):
    set3 = set()
    for s in set1:
        if s not in set2:
            set3.add(s)
    for s in set2:
        if s not in set1:
            set3.add(s)
    return set3


def set_power_set(set1):
    s = list(set1)
    return set(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


def set_cartesian_product(set1, set2):
    cp = []
    for s1 in set1:
        for s2 in set2:
            cp.append([s1, s2])
    return cp


def q2():
    X = {"a", "ab", "abc", "abcd"}
    Y = {"a", "bb", "ccc", "dddd"}
    print("X =", X)
    print("Y =", Y)

    print("X U Y = ", set_union(X, Y))

    print("X ∩ Y =", set_intersection(X, Y))

    print("X - Y =", set_difference(X, Y))

    print("Y - X =", set_difference(Y, X))

    print("X ∆ Y = ", set_symmetric_difference(X, Y))

    print("Y ∆ X = ", set_symmetric_difference(Y, X))

    print("X x Y =", set_cartesian_product(X, Y))

    print("P(X) =", str(set_power_set(X)).replace("(", "{").replace(")", "}"))


# geometric_series(a, r, n) = a + ar + ar^2 + … + ar^n
# arithmetic_series(n, a, d) = a + ad + 2ad + … + nad
# counting(n) = 1 + 2 + … + n
# squares(n) = 1^2 + 2^2 + 3^2 + … + n^2
# cubes(n) = 1^3 + 2^3 + 3^3 + … + n^3

# [a] Write functions to compute each sum by looping over the terms
# [b] Write functions to compute each term by using a closed-form formula available in slides or online
# [c] Compare the results (since there may be roundoff error, do not look for equality but rather a difference less than 1)


def geometric_series_loop(a, r, n):
    return sum([a*(r**i) for i in range(n+1)])


def geometric_series_formula(a, r, n):
    return a * (r * (n + 1)) if r == 1 else a * (r ** (n + 1) - 1) / (r - 1)


def compare_sums(name, loop, formula):
    print(name, loop, formula, "Match" if loop == formula else "Mismatch")


def arithmetic_series_loop(a, d, n):
    return sum([a+d*i for i in range(n+1)])


def arithmetic_series_formula(a, d, n):
    return a * (n+1) + d*n*(n+1)/2


def counting_series_formula(n):
    return n*(n+1)/2


def counting_series_loop(n):
    return sum([i for i in range(n+1)])


def squares_series_formula(n):
    return n * (n+1) * 2 * (n+1)/6


def square_series_loop(n):
    return sum([i**2 for i in range(n+1)])


def cube_series_formula(n):
    return (n*(n+1))**2/4


def cube_series_loop(n):
    return sum([i**3 for i in range(n+1)])


def q3():
    compare_sums("Geometric", geometric_series_loop(2, 3, 4), geometric_series_formula(2, 3, 4))
    compare_sums("Arithmetic", arithmetic_series_loop(2, 3, 4), arithmetic_series_loop(2, 3, 4))
    compare_sums("Counting", counting_series_loop(4), counting_series_loop(4))
    compare_sums("Square", square_series_loop(4), square_series_loop(4))
    compare_sums("Cubed", cube_series_loop(4), cube_series_loop(4))


# [4] Consider a pair of matrices

# [a] Write code to generate the two random n x n matrices
# [b] Write code to add the matrices using loops and compare the result to that of numpy.matrix.sum()
# [c] Write code to multiply the matrices using loops and compare the result to that of numpy.multiply()


def random_matrix(size, mn, mx):
    return [[random.randint(mn, mx) for i in range(size)] for j in range(size)]


def add_matrices(matrix1, matrix2):
    size=len(matrix1) #Assume matrix1 and matrix2 are the same size
    return [[matrix1[i][j]+matrix2[i][j] for j in range(size)] for i in range(size)]


def print_matrix(matrix):
    print(np.array(matrix))


def compare_matrices(name, matrix1, matrix2):
    result = True
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] != matrix2[i][j]:
                result = False

    print(name, "Match" if result else "Mismatch")


def multiply_matrices(matrix1, matrix2):
    size = len(matrix1)  # Assume matrix1 and matrix2 are the same size
    return [[sum([matrix1[i][k]*matrix2[k][j] for k in range(size)]) for j in range(size)] for i in range(size)]


def q4():
    n = 4
    mn = 1
    mx = 100
    matrix1= random_matrix(n, mn, mx)
    matrix2 = random_matrix(n, mn, mx)
    print_matrix(matrix1)
    print_matrix(matrix2)

    sum1= add_matrices(matrix1, matrix2)
    sum2 = np.add(matrix1, matrix2)

    prod1 = multiply_matrices(matrix1, matrix2)
    prod2 = np.matmul(matrix1, matrix2)

    compare_matrices("Addition", sum1, sum2)
    compare_matrices("Multiplication", prod1, prod2)


def main():
    q2()
    print("")
    q3()
    print("")
    q4()


if __name__ == "__main__":
    main()
