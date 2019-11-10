import random
import numpy as np
import math
import binascii


def convert(text):
    """ Текст -> бинарники """
    tl = list(text)
    t = []
    for i in tl:
        t.append(bin(ord(i))[2:])
    return t


def fkey(text, A, T, C, M):
    """ Вычисляем ключ """
    for i in range(1, len(text)):
        T[i] = (A * T[i - 1] + C) % M
    T_ = []
    for i in T:
        T_.append(bin(i)[2:])
    key = T_
    return key


def proccessing(key, n, t):
    """ Дописываем нули, если не полная длина в бинарниках """
    for i in range(len(key)):
        if len(key[i]) != n:
            key[i] = '0' * (n - len(key[i])) + key[i]
    for i in range(len(t)):
        if len(t[i]) != n:
            t[i] = '0' * (n - len(t[i])) + t[i]
    return key, t


def fsum(t, key, n):
    """ Вычисляем суммы """
    sum = []
    res = ''
    for q in range(len(t)):
        for i, j in zip(key[q], t[q]):
            if i == '0' and j == '0':
                res += '0'
            elif i == '0' and j == '1':
                res += '1'
            elif i == '1' and j == '0':
                res += '1'
            else:
                res += '0'
            if len(res) == n:
                sum.append(res)
                res = ''
    return sum


def fcrypt(sum):
    """ Шифрование """
    crypt_sum = sum
    crypt = [0] * len(crypt_sum)
    for i in range(len(crypt)):
        crypt[i] = '0b' + crypt_sum[i]
        crypt[i] = chr(int(crypt_sum[i], 2))
    cr = ''
    for i in crypt:
        cr += i
    return crypt, crypt_sum, cr


def fdecrypt(decrypt_sum):
    """ Расшифрование """
    decrypt = [0]*len(decrypt_sum)
    for i in range(len(decrypt_sum)):
        decrypt[i] = '0b' + decrypt_sum[i]
        decrypt[i] = chr(int(decrypt[i], 2))
    dcr = ''
    for i in decrypt:
        dcr+=i
    return decrypt, dcr


def main():
    '''Начальные параметры'''
    text = input('Введите сообщение для шифровки (на английском!): ')
    b = 6
    A = 5
    C = 3
    T = [0] * len(text)
    T[0] = 4
    M = 2 ** b
    n = 7

    print('Сообщение для шифрования : ', text)
    t = convert(text)
    key = fkey(text, A, T, C, M)
    proccessing(key, n, t)
    print('Сообщение в двоичном коде: ', t)
    print('Ключ в двоичном коде: ', key)
    sum = fsum(t, key, n)
    print('Сумма для шифрования: ', sum)
    crypt, crypt_sum, cr = fcrypt(sum)
    print('Зашифрованное сообщение: ', cr)
    decrypt = []
    decrypt_sum = fsum(crypt_sum, key, n)
    decrypt, dcr = fdecrypt(decrypt_sum)
    print('Дешифрованное сообщение: ', dcr)


if __name__=='__main__':
    main()