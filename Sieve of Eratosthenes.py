#Sieve of Eratosthenes
#The sieve of Eratosthenes is an ancient algorithm used for finding all prime numbers up to any given limit.
#Algorithm is very simple in its working after describing our sgement [1,...,n] we find all multiples of 2 (as it is both smallest even and prime number)
#and mark them as composite (in our algorithm they will be given boolean value of false) then find another number which was not marked as composite and repeat our process
#eventually we are left only with proper prime numbers in our segment



#First variation of algorithm
#our algorithm will consist of 2 functions
#function which checks if number is prime via Sieve of Eratosthenes
#and auxiliary function which uses our prime checker in order to return list of prime numbers in sgement

def prime_check_eratosthenes(n):
    array=[]
    if n<2:
        return False
    if n==1:
        return False
    for i in range(0,n+1):
        array.append(i)
        array[i]=True
    i=2

    while i<=(n**0.5):
        for j in range(i,n+1,i):
            array[j]=False
        i+=1
    return array[n]

print('Sieve of Eratosthenes 1 variation of algorithm')

print('\nIs 11 prime:',prime_check_eratosthenes(11))
print('Is 34 prime:',prime_check_eratosthenes(34))
print('Is 67 prime:',prime_check_eratosthenes(67))
print('Is 97 prime:',prime_check_eratosthenes(97))
print('Is 99 prime:',prime_check_eratosthenes(99))

#auxiliary function

def sieve_iter(n): #iterative solution
    listaliczb=[]
    for i in range(0,n+1):
        if prime_check_eratosthenes(i)==True:
            listaliczb.append(i)
    return listaliczb

print('\nPrime numbers up to 100')
print(sieve_iter(100))

