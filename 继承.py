"""
@project = '面试题'
@file_name = '继承'
@author = 'Baiyila'
@time = '2023/4/27 14:41'
@product_name = PyCharm
@mail = baiyila2022@163.com
code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""


class Animal:
  def make_sound(self):
    print("The animal makes a sound.")


class Cat(Animal):
  def make_sound(self):
    print("Meow")
    super().make_sound()  # 调用父类的方法


cat = Cat()
cat.make_sound()  # 输出: Meow
# 输出: The animal makes a sound.
