#!/usr/bin/env python
# coding: utf-8
# monolith.py 
# Licensed under the Apache 2.0 license

def donut():
    return 5

def coffee():
    return 5.5

def beer():
    return 8

def shoes():
    return 85

def google_swag():
    return 180

def calcprice(items):
    total = 0
    for item in items:
        total += item()
    return total

print(calcprice([beer,google_swag, coffee]))
