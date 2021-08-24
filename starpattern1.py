#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 16:04:37 2021

@author: syedabbasaman
"""


n= int(input("Enter number of rows"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end= "")
    print("")

for i in range(n,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print("")
        