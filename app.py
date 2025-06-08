# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import time
import math

app = Flask(__name__)

def rShift(s1, d):
    rs = s1[0:len(s1) - d]
    rss = s1[len(s1) - d:]
    return rss + rs

def lShift(s1, d):
    ls = s1[0:d]
    lss = s1[d:]
    return lss + ls

def reverse(seq, start, stop):
    seq = list(seq)
    size = stop + start
    for i in range(start, (size + 1) // 2):
        j = size - i
        seq[i], seq[j] = seq[j], seq[i]
    return ''.join(seq)

def ibn_omar_hash(i):
    ti = time.time()
    i = ''.join([bin(ord(c)).replace('0b', '') for c in i])
    A = '1100010001111001001110110001010001100101001011000101100110010011101100010111111001010010'
    B = '11001000111110010011101100100100011001010001110010011101100011001011001010010'
    C = '11000101101110010011111100011011111001010001110010100001100100101011001010010'
    D = '1100100001111001001110110010001001100100111011001000101110010011111100100011011001010010'
    E = '1100011001111001001110110001110011100101001011001000001110010011101100011010111001010010'
    F = '1100100001011001001110110001100011100100111011000110100110010011101100010101011001010010'
    G = '110001010111100100111011000101110110010011101100011000011001010010'
    H = '110001101101100100111011000111000110010100001100011101011001010010'
    b = i + A + i + B + i + C + i + D + i + E + i + F + i + G + i + H + i
    block = b + b + '1'

    bSize = len(block)
    if bSize < 2048:
        padL = ''.ljust(2048 - bSize, '0')
        blocks = block + padL
    elif bSize > 2048:
        pv = ((bSize // 2048) + 1) * 2048 - bSize
        padG = ''.ljust(pv, '0')
        blocks = block + padG
    else:
        blocks = block

    blocksR = rShift(blocks, 604)
    andR = int(blocks) & int(blocksR)
    xoR = int(blocks) ^ int(blocksR)
    bR = andR | xoR
    bR = rShift(str(bR), 604)
    bR = int(bR)
    bR = '{0:b}'.format(bR)

    blocksL = lShift(blocks, 309)
    andL = int(blocks) & int(blocksL)
    xoL = int(blocks) ^ int(blocksL)
    bL = andL | xoL
    bL = lShift(str(bL), 309)
    bL = int(bL)
    bL = '{0:b}'.format(bL)

    bLDec = sum([int(d) for d in bL])
    bRDec = sum([int(d) for d in bR])
    iLen = len(i)
    Yl = abs(math.log(int(bL, 2) or 1, iLen or 2))
    Yr = abs(math.log(int(bR, 2) or 1, iLen or 2))
    primes = [101, 103, 107, 109, 113, 127, 131]

    for e in primes:
        bLDec = (int(math.ceil(e * Yr / iLen)) * bLDec) + int(math.ceil(e * Yr / iLen))
        bRDec = (int(math.ceil(e * Yl / iLen)) * bRDec) + int(math.ceil(e * Yl / iLen))

    Y = int(math.floor(Yl * Yr)) or 1
    bDec = (bRDec + bLDec) / Y
    bDec = lShift(str(bDec), Y)
    bBin = bin(int(bDec)).replace('0b', '')

    if len(bBin) > 1024:
        bBin = bBin.ljust(((len(bBin) // 1024) + 1) * 1024, '0')

    bBin = reverse(bBin, -306, -604)
    bBin = lShift(bBin, 1024)
    bBin = reverse(bBin, -910, -295)
    finalBlock = bBin[:1024]
    return hex(int(finalBlock, 2))

@app.route('/hash', methods=['POST'])
def hash_input():
    try:
        user_input = request.json.get('text', '')
        if not user_input:
            return jsonify({'error': 'No input provided'}), 400
        result = ibn_omar_hash(user_input)
        with open("log.txt", "a") as f:
            f.write("Input: %s\nOutput: %s\n\n" % (user_input, result))
        return jsonify({'hash': result})
    except Exception as e:
        print('Hashing Error:', str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return 'Ibn Omar Hash Algorithm API (Python 2.7)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
