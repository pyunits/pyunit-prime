#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/21 13:04
# @Author: Jtyoui@qq.com


def rabin_miller(n, k=10):
    """米勒-拉宾素性检验是一种素数判定法则

    米勒-拉宾素性检验是一种素数判定法则，利用随机化算法判断一个数是合数还是可能是素数。
    卡内基梅隆大学的计算机系教授Gary Lee Miller首先提出了基于广义黎曼猜想的确定性算法，
    由于广义黎曼猜想并没有被证明，其后由以色列耶路撒冷希伯来大学的Michael O. Rabin教授作出修改，
    提出了不依赖于该假设的随机化算法。

    :param n: 质数
    :param k: 检验的次数
    :return: 是质数返回True，不是返回False
    """
    pass


def get_large_prime(number=500, k=10):
    """获取一个超大的质数


    :param number: 位数，默认是500位的质数
    :param k: 检验的次数
    :return: 返回一个超大质数
    """
    pass


def prime_range(start, end, k=10):
    """区间获取质数:埃拉托斯特尼质数筛法

    :param start: 开始值
    :param end: 结束值
    :param k: 检验的次数
    :return: 列表的质数
    """
    pass
