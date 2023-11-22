#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    a, b = 0, 1
    for _ in range(length):
        fib_list.append(a)
        a, b = b, a + b
    print(fib_list)


print_fibonacci(5)
