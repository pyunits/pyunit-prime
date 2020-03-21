#!/usr/bin/python3.7
# cython: language_level=3
# -*- coding: utf-8 -*-
# @Time  : 2020/3/21 11:55
# @Author: Jtyoui@qq.com
from random import randrange
import math

cpdef rabin_miller(n, k=10):
    cdef s = n - 1
    cdef f = s
    cdef t = 0
    if n <= 4:
        return [False, False, True, True, False][n]
    while s % 2 == 0:
        s //= 2
        t += 1
        for _ in range(k):
            a = randrange(2, f)
            v = pow(a, s, n)
            if v != 1:
                i = 0
                while v != f:
                    if i == t - 1:
                        return False
                    else:
                        i += 1
                        v = (v ** 2) % n
        return True
    return False

cpdef get_large_prime(number=500, k=10):
    cdef size = 10 ** number
    cdef n = 10 ** (number - 1)
    while True:
        num = randrange(n, size)
        if rabin_miller(num, k):
            return num

cpdef prime_range(start, end, k=10):
    cdef sieve = [True] * end
    cdef primes = []
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.sqrt(end)) + 1):
        point = i * 2
        while point < start:
            point += i
        while point < end:
            sieve[point] = False
            point += i

    for i in range(start, end):
        if sieve[i]:
            primes.append(i)
    return primes
