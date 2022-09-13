import hashlib
import time

from bitarray import bitarray
import array
from hash_functions import *


def bool_hash_functions(string, array_of_bits,n):
    i = h0(string,n)
    array_of_bits[i] = 1
    i = h1(string,n)
    array_of_bits[i] = 1
    i = h2(string,n)
    array_of_bits[i] = 1
    i = h3(string,n)
    array_of_bits[i] = 1
    i = h4(string,n)
    array_of_bits[i] = 1
    i = h5(string,n)
    array_of_bits[i] = 1
    i = h6(string,n)
    array_of_bits[i] = 1
    i = h7(string,n)
    array_of_bits[i] = 1


def is_the_string_present(string_to_find,n,array_of_bits):
    if array_of_bits[h0(string_to_find, n)] == 0:
        pass
    if array_of_bits[h1(string_to_find, n)] == 0:
        pass
    if array_of_bits[h2(string_to_find, n)] == 0:
        pass

    if array_of_bits[h3(string_to_find, n)] == 0:
        pass

    if array_of_bits[h4(string_to_find, n)] == 0:
        pass

    if array_of_bits[h5(string_to_find, n)] == 0:
        pass

    if array_of_bits[h6(string_to_find, n)] == 0:
        pass

    if array_of_bits[h7(string_to_find, n)] == 0:
        pass

    else:
        print('the string: ' + string_to_find +  ' is in the array')


if __name__ == '__main__':
    n = 15000
    text_array =[];
    string_to_find = []
    array_of_bits = bitarray(n)
    array_of_bits.setall(0)

    with open('Tex_to_fill_the_array.txt', 'r') as file:
        for line in file:
            line = line.replace('\n','')
            text_array.append(line)



    with open('parole in italiano.txt', 'r') as file:
        for line in file:
            line = line.replace('\n','')
            string_to_find.append(line)


    start = time.time()
    for string in text_array:
        bool_hash_functions(string,array_of_bits,n)

    for s in string_to_find:
        is_the_string_present(s,n,array_of_bits)

    finish = time.time()

    print(finish - start)

