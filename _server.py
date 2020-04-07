import binascii
import socket
import struct
import sys
import sympy as sy
# from threading import Thread 
# from socketserver import ThreadingMixIn
from random import randint
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server_address = ('localhost', 65429)
sock.bind(server_address)
sock.listen(5)
unpacker = struct.Struct('I I I I I')
while (True):
    print('\nwaiting for a connection')
    connection, client_address = sock.accept()
    # newthread = ClientThread(ip,port) 
    # newthread.start() 
    # threads.append(newthread)
    i=1
    while (i==1):   
        try:
            data = connection.recv(unpacker.size)
            # print('received {!r}'.format(binascii.hexlify(data)))
            
            unpacked_data = unpacker.unpack(data)
            print('unpacked:', unpacked_data)
            q= int(unpacked_data[1])
            a= int(unpacked_data[0])
            m1=int(unpacked_data[2])
            m2=int(unpacked_data[3])
            m3=int(unpacked_data[4])
            
            x1=randint(100, 1000)
            x2=randint(100, 1000)
            x3=randint(100, 1000)
            y1=pow(a,x1) % q 
            y2=pow(a,x2) % q 
            y3=pow(a,x3) % q 
            k1=pow(m1,x1)%q
            k2=pow(m2,x2)%q
            k3=pow(m3,x3)%q
            value=(y1,y2,y3)
            packer = struct.Struct('I I I')
            packed_data = packer.pack(*value)
            print('values =',value)
            print(k1)
            print(k2)
            print(k3)
            key='{0:064b}'.format(k1)+'{0:064b}'.format(k2)+'{0:064b}'.format(k3)
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
            key=str(key)
            key=bytes(key,'utf-8')
            key = DES3.adjust_key_parity(key)
            cipher = DES3.new(key, DES3.MODE_CFB)
            connection.sendall(packed_data)
            filename='temp.txt'
            f = open(filename,'rb')
            l = f.read(4096)
            while (l):
                msg = cipher.iv + cipher.encrypt(l)
                connection.send(msg)
                l = f.read(4096)
            f.close()
        finally:
            connection.close()
            i=0
# for t in threads: 
#     t.join()             