#For establishment of a shared session key KA,B between the client A and the server B, we will use the
Diffie-Hellman key exchange protocol, which is described below:

Global Public Elements
– q: a sufficiently large prime, such that it is intractable to compute the discrete logarithms in
– α: α < q and α a primitive root of q.
## User A Key Generation
– Select private XA such that XA < q
– Calculate public YA such that YA = α
XA mod q
A → B : {YA, q, α}
Here A → B : M denotes party A sends a message M to party B.


## User B Key Generation
– Select private XB such that XB < q
– Calculate public YB such that YB = α
XB mod q
B → A : {YB}


## Generation of secret key by User A
– Compute the shared key with B as KA,B = (YB)
XA mod q


## Generation of secret key by User B
– Compute the shared key with A as KB,A = (YA)
XB mod q = KA,B

for this implementation we will install
pip install pycryptodome
pip install pycryptodomex
pip install cryptodome
pip install crypto

for transfering file --
use inbuilt 3des function
for encryption
use inbuilt 3des encryption function

for handling multiple client--
use multithreading

