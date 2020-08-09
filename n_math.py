import math
import time
import timeit

def sigmoid(z):
    return 1/(1+math.exp(-z))


def sigmoid_derivative(z):
    sigmoid_z = sigmoid(z)
    return sigmoid_z*(1-sigmoid_z)


def dot(a, b):
    return sum(((el1 * el2) for el1, el2 in zip(a, b)))

def norm_dot(a, b):
    sum = 0
    for id in range(len(a)):
        sum += a[id] * b[id]
    return sum


def bench_dot(sample_count, vector_length, dot_func):
    a, b = list(), list()
    for i in range(vector_length):
        a.append(i)
        b.append(i)

    start = time.time_ns()

    for i in range(sample_count):
        dot_func(a, b)

    print("time: ", time.time_ns() - start)




# bench_dot(5, 100000000, dot)
# bench_dot(5, 100000000, norm_dot)
