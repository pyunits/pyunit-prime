#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/21 15:23
# @Author: Jtyoui@qq.com
from pyunit_prime.prime import rabin_miller, get_large_prime, prime_range
import argparse
import re

parser = argparse.ArgumentParser(description='质数处理和寻找质数的模块')

parser.add_argument('-P', '--isPrime', help='判断是否是质数')
parser.add_argument('-L', '--large', help='生成一个超大的质数')
parser.add_argument('-R', '--range', help='生成区间内的质数,开始和结束用逗号隔开')

args = parser.parse_args()
if args.isPrime:
    print(rabin_miller(int(args.isPrime)))
elif args.large:
    print(get_large_prime(int(args.large)))
elif args.range:
    start, end = re.split('[，,.。！？!?#$%&*+:;<=>@]', args.range)
    print(prime_range(start=int(start), end=int(end)))

if __name__ == '__main__':
    pass
