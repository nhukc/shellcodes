from pwn import *
from binascii import *
string = "/home/orw/flag"

#Use to create shellcode to push string to stack
#Pushing values in order will create a proper string
#Use 4 bytes_to_word for 32 bit, 8 for 64 bit
def pack_str(string, byte_to_word):
    zero = len(string) % byte_to_word
    if(zero == 0):
        zero = byte_to_word;
    h = a2b_qp(string)
    h += b'\x00'*zero
    for i in range(len(h)-byte_to_word, -1, -byte_to_word):
        word = h[i:i+byte_to_word:]
        word = word[::-1]
        print("%x" % unpack(word, word_size=byte_to_word*8,endianness="big"))

pack_str(string,4)
