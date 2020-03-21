# **pyUnit-Prime** [![](https://gitee.com/tyoui/logo/raw/master/logo/photolog.png)][1]

## 质数处理和寻找质数的模块
[![](https://img.shields.io/badge/Python-3.7-green.svg)](https://pypi.org/project/pyunit-prime/)


## 安装
    pip install pyunit-prime
    
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
from pyunit_prime import get_large_prime

if __name__ == '__main__':
    print(get_large_prime(150)) # 返回长度位150位的质数
```

### 返回区间类的质数
```python
from pyunit_prime import prime_range

if __name__ == '__main__':
    print(prime_range(100, 10000))  # 返回100到10000区间的质数
```


***
[1]: https://blog.jtyoui.com
