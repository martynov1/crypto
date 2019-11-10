import numpy as np 
import random

def encrypt(text, key):
    k_size = len(key)
    t_size = len(text)
    dif = t_size % k_size

    if dif != 0:
        for i in range(k_size-dif):
            text.append(chr(random.randrange(ord('а'), ord('я'), 1)))
    t_size = len(text)

    for i in range(0, t_size, k_size):
        string = [text[i+j] for j in range(k_size)]
        for j in range(k_size):
            text[i+j] = string[key[j]]
    return text

def decrypt(code, new_key):
    k_size = len(new_key)
    c_size = len(code)
    for i in range(0, c_size, k_size):
        string =[code[i+j] for j in range(k_size)]
        for j in range(k_size):
            code[i+j] = string[new_key[j]]
    return code

if __name__ == "__main__":
    text = input('Введите текст для шифрования: ')
    print('Строка для шифрования: ', text)
    text = list(text)
    key = [4,3,0,1,2]
    new_key = [2,3,4,1,0]
    result_encrypt = encrypt(text, key)
    se = ''
    for i in result_encrypt:
        se+=i
    print('Шифрованная строка: ', se)

    result_decrypt = decrypt(result_encrypt, new_key)
    sd = ''
    for i in result_decrypt:
        sd+=i
    print('Дешифрованная строка', sd)