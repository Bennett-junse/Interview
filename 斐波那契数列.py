"""
@project = '面试题'
@file_name = '斐波那契数列'
@author = 'Baiyila'
@time = '2023/4/27 14:53'
@product_name = PyCharm
@mail = baiyila2022@163.com
code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
# 斐波那契数列
# 使用递归方式：
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


# 输出前10个斐波那契数列数字
for i in range(10):
  print(fibonacci(i))
"""
# 使用循环方式：
def fibonacci(n):
  if n <= 1:
    return n
  else:
    a, b = 0, 1
    for i in range(n - 1):
      a, b = b, a + b
    return b


# 输出前10个斐波那契数列数字
for i in range(10):
  print(fibonacci(i))
"""
