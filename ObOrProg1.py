class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = Dog("Lala", 9)

print(a.name)
print(a.age)

print(f"{a.name} is {a.age}")


import backtrader as bt
import pandas as pd

print(bt.__version__)


