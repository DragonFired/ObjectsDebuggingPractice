__author__ = 'arana'

import string

decodingDictionary = {'a':'c', 'b':'d', 'c':'e', 'd':'f', 'e':'g', 'f':'h', 'g':'i', 'h':'j', 'i':'k', 'j':'l', 'k':'m', 'l':'n', 'm':'o', 'n':'p', 'o':'q', 'p':'r', 'q':'s', 'r':'t', 's':'u', 't':'v', 'u':'w', 'v':'x', 'w':'y', 'x':'z', 'y':'a', 'z':'b'}
inputMessage = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


decodedMessage = ""
for char in inputMessage:
    if char in 'abcdefghijklmnopqrstuvwxyz':
    # if char in decodingDictionary.keys():
        decodedMessage += decodingDictionary[char]
    else:
        decodedMessage += char

print(decodedMessage)

# chars = "abcdefghijklmnopqrstuvwxyz"
# for char in chars:
#     print("\'%s\':\'%s\', " % (char, chars[(chars.index(char) + 2)%26]))