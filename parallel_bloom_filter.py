import time
from bitarray import bitarray
import array
from joblib import Parallel, delayed
import math
import numpy as np

def h0(string):
    j = 0
    for i in string:
        j = j + ord(i)
    j = j * 2668478416865146565
    return j % n

def h1(string):
    j = 0
    for i in string:
        j = j + hash(i)
    j = j * 266847841684515+6468546985484
    return j % n

def h2(string):
    j = 1
    for i in string:
        j = j * ord(i)
    j = j * 2668478651
    return j % n

def h3(string):
    j = 1
    for i in string:
        j = j ** 3
    j = j * 266847856
    return j % n

def h4(string):
    j = 0
    for i in string:
        j = j + ord(i)
        j = j * 1651651
    j = int(j / 52)
    return j % n

def h5(string):
    array_local = []

    for i in string:
        array_local.append(ord(i))

    matrix_local = np.vander(array_local, n)
    k = 0
    for j in range(0, len(matrix_local)):
        for i in range(0, len(matrix_local[0])):
            k = k + (matrix_local[j][i]) % 20
    return k % n

def h6(string):
    j = 0
    for i in string:
        j = j + hash(i)
        j = j - 2531859
    j = int(j / 69)
    return j % n

def h7(string):
    j = 0
    for i in string:
        j = j + ord(i)
        j = j - 6464
    j = int(j / 20)
    return j % n


def is_the_string_present(string_to_find,array_of_bits):
    if array_of_bits[h0(string_to_find)] == 0:
        pass
    if array_of_bits[h1(string_to_find)] == 0:
        pass
    if array_of_bits[h2(string_to_find)] == 0:
        pass

    if array_of_bits[h3(string_to_find)] == 0:
        pass

    if array_of_bits[h4(string_to_find)] == 0:
        pass

    if array_of_bits[h5(string_to_find)] == 0:
        pass

    if array_of_bits[h6(string_to_find)] == 0:
        pass

    if array_of_bits[h7(string_to_find)] == 0:
        pass

    else:
        print('the string: ' + string_to_find +  ' is in the array')


if __name__ == '__main__':
    global n
    n = 15000
    text_array = [];
    string_to_find = []
    array_of_bits = bitarray(n)
    array_of_bits.setall(0)

    cores = 8

    with open('Tex_to_fill_the_array.txt', 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            text_array.append(line)

    with open('parole in italiano.txt', 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            string_to_find.append(line)


    array_0 = Parallel(n_jobs=cores)(delayed(h0) (string) for string in text_array)
    array_1 = Parallel(n_jobs=cores)(delayed(h1) (string) for string in text_array)
    array_2 = Parallel(n_jobs=cores)(delayed(h2) (string) for string in text_array)
    array_3 = Parallel(n_jobs=cores)(delayed(h3) (string) for string in text_array)
    array_4 = Parallel(n_jobs=cores)(delayed(h4) (string) for string in text_array)
    array_5 = Parallel(n_jobs=cores)(delayed(h5) (string) for string in text_array)
    array_6 = Parallel(n_jobs=cores)(delayed(h6) (string) for string in text_array)
    array_7 = Parallel(n_jobs=cores)(delayed(h7) (string) for string in text_array)

    for i in range(len(array_0)):
        array_of_bits[array_0[i]] = 1
        array_of_bits[array_1[i]] = 1
        array_of_bits[array_2[i]] = 1
        array_of_bits[array_3[i]] = 1
        array_of_bits[array_4[i]] = 1
        array_of_bits[array_5[i]] = 1
        array_of_bits[array_6[i]] = 1
        array_of_bits[array_7[i]] = 1

    start = time.time()
    Parallel(n_jobs=cores)(delayed(is_the_string_present)(string, array_of_bits) for string in string_to_find)
    end = time.time()
    print(end - start)
