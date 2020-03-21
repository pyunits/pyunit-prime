#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/21 12:49
# @Author: Jtyoui@qq.com
from pyunit_prime import is_prime, get_large_prime_length, prime_range, get_large_prime_bit_size
import time


def rm():
    for i in range(100000):
        if is_prime(i):
            print(i)


def get():
    print(get_large_prime_length(150))
    print(get_large_prime_bit_size(526))


def rsp():
    print(prime_range(10, 100))  # 0.028922319412231445


if __name__ == '__main__':
    start = time.time()
    # rm()
    get()
    # sp()
    # rsp()
    print(time.time() - start)
