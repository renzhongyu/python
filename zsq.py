#!/usr/bin/python
from __future__ import print_function
def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("</______\>")
    return wrapper

@bread
def sandwich(food="--ham--"):
    print(food)

sandwich()
