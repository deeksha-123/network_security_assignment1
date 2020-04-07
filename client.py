import binascii
import socket
import struct
import sys
import sympy as sy
from random import randint
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes


def random_no():
    return randint(100, 1000)



def prime_generate():
    q=sy.randprime(1000, 65431)
    return q


q=prime_generate()
a=random_no()  
x1=random_no()
x2=random_no()
x3=random_no()
y1 = pow(a,x1) % q 
y2=pow(a,x2) % q  
y3=pow(a,x3) % q   
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 65429)
sock.connect(server_address)

values = (a,q,y1,y2,y3)
packer = struct.Struct('I I I I I')
packed_data = packer.pack(*values)

print('values =', values)
try:
    sock.sendall(packed_data)
    unpacker = struct.Struct('I I I')
    data = sock.recv(unpacker.size)
    if not data:
        print("No data")
    unpacked_data = unpacker.unpack(data)
    m1=int(unpacked_data[0])
    m2=int(unpacked_data[1])
    m3=int(unpacked_data[2])
    k1=pow(m1,x1) % q
    k2=pow(m2,x2) % q
    k3=pow(m3,x3) % q

    print('unpacked:', unpacked_data)
    # key='{0:064b}'.format(k1)+'{0:064b}'.format(k2)+'{0:064b}'.format(k3)
    print(k1)
    print(k2)
    print(k3)
    k1=str(k1)
    k2=str(k2)
    k3=str(k3)
    for i in range(0,8-len(k1)):
        k1=k1+'0'
    for i in range(0,8-len(k2)):
        k2=k2+'0'
    for i in range(0,8-len(k3)):
        k3=k3+'0'
    key=k1+k2+k3    
    print(k1)
    print(k2)
    print(k3)
    print(key)
    key=str(key)
    key=bytes(key,'utf-8')
    
    key = DES3.adjust_key_parity(key)
    cipher = DES3.new(key, DES3.MODE_CFB)
    # plaintext = b'We are no longer the knights who say ni!'
    
    cipher = DES3.new(key, DES3.MODE_CFB)
    with open('ans.txt', 'wb') as f:
        print ('file opened')
        while True:
            print('receiving data...')
            data = sock.recv(4096)
            cipher = DES3.new(key, DES3.MODE_CFB)
            data=cipher.decrypt(data)
            print(str(data))
            if not data:
                break
            # write data to a file
            f.write(data)
    f.close()

        

finally:
    sock.close()