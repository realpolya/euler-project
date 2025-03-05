'''
XOR Decryption

Each character on a computer is assigned a unique code and the preferred standard is 
ASCII (American Standard Code for Information Interchange). For example, uppercase 
A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. The advantage with 
the XOR function is that using the same encryption key on the cipher text, restores 
the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, 
and the key is made up of random bytes. The user would keep the encrypted message 
and the encryption key in different locations, and without both "halves", it is 
impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method 
is to use a password as a key. If the password is shorter than the message, which 
is likely, the key is repeated cyclically throughout the message. The balance for 
this method is using a sufficiently long password key for security, but short 
enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower 
case characters. Using 0059_cipher.txt
(right click and 'Save Link/Target As...'), a file containing the encrypted 
ASCII codes, and the knowledge that the plain text must contain common English words, 
decrypt the message and find the sum of the ASCII values in the original text.
'''

import string
import time
import enchant
import nltk
from nltk.corpus import words
from extras.xor59 import CIPHER

# print(enchant.list_dicts())
nltk.download("words")


def decrypt(encrypted, key):

    decrypted = int(encrypted) ^ int(key) # XOR operation
    return decrypted


def xor_decryption():

    # find the sum of ASCII values in the original text
    ascii_sum = 0

    cipher_list = CIPHER.split(",")
    # print(cipher_list)

    # introduce spell-checking
    dict = enchant.Dict("en_US-wo_accents")
    # aspell_dict = enchant.DictWithPWL("en_US", "/Users/polinastepanova/.aspell.en.pws")
    # print(dict.check("wonderful"))

    english_words = set(words.words())
    # print(english_words)
    # print("l" in english_words)

    # space is ascii 32, letters 65-122
    upper_range = range(65, 91)
    lower_range = range(97, 123)
    correct_keys = []

    # loop through possible keys ascii lowercase 97 through 122
    for a in range(97, 123):

        for b in range(97, 123):

            for c in range(97, 123):

                # establish the key sequence
                keys = [a, b, c]
                i = 0
                word_list = []
                other_words = []
                decrypted = ""
                not_key = False

                # apply the sequence over and over again
                for char in cipher_list:
                    
                    # print("i is", i)
                    decrypted_char = decrypt(char, keys[i])

                    if i == 2:
                        i = 0
                    else:
                        i += 1

                    # analyze the char
                    if decrypted_char in upper_range or decrypted_char in lower_range: # adding letters to the word
                        # print("a letter now", chr(decrypted_char))
                        decrypted += chr(decrypted_char)
                        # print(decrypted)
                    # signals break in a word
                    elif len(decrypted) != 0:
                        # print("decrypted char is not a letter, break in letter", chr(decrypted_char))

                        # if single letter - only I and a are allowed
                        if len(decrypted) == 1 and decrypted_char in [65, 97, 73]: # single-letter word, a, A, I 
                            # print("appending ", decrypted)
                            word_list.append(decrypted)
                            decrypted = ""
                        elif decrypted in english_words and len(decrypted) > 1:
                            # print("i is", i, "key is", keys[i], "appending", decrypted)
                            word_list.append(decrypted)
                            decrypted = ""
                        else:
                            other_words.append(decrypted)
                            decrypted = ""
                            # not_key = True
                            # break # this key combo is not the answer
                    # else:
                    #     print("empty", chr(decrypted_char))

                # if not_key:
                #     continue
                # print("this is done")
                if len(word_list) > len(other_words):
                    # print("possible keys ", keys, "word list is ", word_list)
                    correct_keys = [a, b, c]
                    # print(correct_keys)

    final_text = ""

    i = 0
    print(correct_keys)
    # print("this later part is kicking in")
    for char in cipher_list:

        decrypted_char = decrypt(char, correct_keys[i])
        ascii_sum += decrypted_char

        if i == 2:
            i = 0
        else:
            i += 1

        final_text += chr(decrypted_char)
    
    # print(final_text)

    return ascii_sum
        


    # once it starts returning actual english words


# print(CIPHER)
print(xor_decryption())