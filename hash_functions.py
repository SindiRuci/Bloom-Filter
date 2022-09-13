import math
import numpy as np

def h0(string,n):
    j = 0
    for i in string:
        j = j + ord(i)
    j = j * 2668478416865146565
    return j % n

def h1(string,n):
    j = 0
    for i in string:
        j = j + hash(i)
    j = j * 266847841684515+6468546985484
    return j % n

def h2(string,n):
    j = 1
    for i in string:
        j = j * ord(i)
    j = j * 2668478651
    return j % n

def h3(string,n):
    j = 1
    for i in string:
        j = j ** 3
    j = j * 266847856
    return j % n

def h4(string,n):
    j = 0
    for i in string:
        j = j + ord(i)
        j = j * 1651651
    j = int(j / 52)
    return j % n

def h5(string,n):
    arrray_local = [0] * len(string)
    i = 0
    for j in string:
        arrray_local[i] = ord(j)
        i = i + 1
    matrix = np.vander(arrray_local, n)
    sumElements = 0
    for j in range(0, len(matrix)):
        for i in range(0, len(matrix[0])):
            sumElements = sumElements + (matrix[j][i]) % 20
    return sumElements % n

def h6(string,n):
    j = 0
    for i in string:
        j = j + hash(i)
        j = j - 2531859
    j = int(j / 69)
    return j % n

def h7(string,n):
    j = 0
    for i in string:
        j = j + ord(i)
        j = j - 6464
    j = int(j / 20)
    return j % n