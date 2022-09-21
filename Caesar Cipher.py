#One of the oldest substitution ciphers algorithm one of the simplest and most widely known encryption techniques
#each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet
#for example.: with a right shift of 3, A would be replaced by D

def encrypt(w,k):  #w- the value we input, k- the key we will be shifting with
    k=k%26
    cipher=''
    for i in range(0,len(w)):
        letter=ord(w[i])
        if letter+k>90:     #90 is the value of letter Z in ASCII
            cipher+=chr(letter+k-26)
        else:
            cipher+=chr(letter+k) #we modify the ASCII value of letter by adding our key value thus shofting the value
    return cipher

def decrypt(w,k):
    k=k%26
    decryption=''
    for i in range(0,len(w)):
        letter=ord(w[i])
        if letter-k<65:
            decryption=decryption+chr(letter-k+26)
        else:
            decryption+=chr(letter-k)
    return decryption


print('Encrypt word: Ant with key 4')
print('Encrypted:',encrypt('ANT',4))

print('\nDecrypt word ERX with key 4')
print('Decrypted:',decrypt('ERX',4))


