import random as rd
import sys

def cipher(inp, keys, f):
    for key in keys:
        L, R = split(inp)
        Ln = xor(L, f(key, R))
        inp = R+Ln
    return Ln+R

def split(inp):
    assert len(inp)%2==0
    return inp[:int(len(inp)/2)], inp[int(len(inp)/2):]

def fsum(a, b):
	return a+b

def xor(a, b):
    output=""
    for i in range(len(a)):
        inter=int(a[i])+int(b[i])
        if inter==2: inter=0
        output = output+str(inter)
    return output

def keyGen(l,n):
    o=[]
    for i in range(n):
        k=""
        for i in range(l):
            k = k + str(rd.randint(0,1))
        o.append(k)
    return o

def binToHex(binary):
	res="0x"
	hexList = [hex(int(binary[i:i+8], 2))[2:] for i in range(0, len(binary),8)]
	for hexa in hexList:
		if len(hexa)==1: hexa ="0"+hexa
		res = res + hexa
	return res


if __name__ == "__main__":
	plainText = "Hello MIREA! Hi-tech education!"
	plainInts = [bin(ord(letter))[2:] for letter in plainText]
	plainBin=""
	for integer in plainInts:
		while len(integer)!=8:
			integer = "0"+integer
		plainBin = plainBin+integer
	# генерация ключей
	keyList = keyGen(int(len(plainBin)/2), 8)
	# кодирование
	C = cipher(plainBin, keyList, fsum)
	keyList.reverse()
	# декодирование
	result = cipher(C, keyList, fsum)
	resultToChar = [chr(int(result[i:i+8], 2)) for i in range(0, len(result),8)]
	resultText=""
	for letter in resultToChar:
		resultText = resultText+letter
	print("Plain text:         {}".format(plainText))
	print('Plain text to hexa: {}'.format(binToHex(plainBin)))
	print("Cipher:             {}".format(binToHex(C)))
	print("Result as hexa:     {}".format(binToHex(result)))
	print("Result to text:     {}".format(resultText))









