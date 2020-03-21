# **pyUnit-Prime** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 质数处理和寻找质数的模块
[![](https://img.shields.io/badge/Python-3.7-green.svg)](https://pypi.org/project/pyunit-prime/)


## 安装
    pip install pyunit-prime
    
## 命令行运行:打开控制台
    prime -h # 获取帮助
    
    命令行：
        判断是否是质数: prime -P 13
        寻找一个超大质数：长度: prime -L 100
        寻找一个超大质数：bit位度: prime -B 100
        返回区间内的质数: prime -R 100,500
    
    
### 判断是否是质数
```python
from pyunit_prime import is_prime

if __name__ == '__main__':
    for i in range(10_0000):
        if is_prime(i):
            print(i)
```

### 寻找一个超大质数
```python
from pyunit_prime import get_large_prime_length,get_large_prime_bit_size

if __name__ == '__main__':
    print(get_large_prime_length(150)) # 返回长度位150长度的质数
    print(get_large_prime_bit_size(150)) # 返回长度位150 bit位的质数
```

### 返回区间内的质数
```python
from pyunit_prime import prime_range

if __name__ == '__main__':
    print(prime_range(100, 10000))  # 返回100到10000区间的质数
```


***
[1]: https://blog.jtyoui.com
