# Write a Python function that takes a number as a parameter and check the number is prime or not

def check_prime(num):
    if sum([num%i==0 for i in range(2,num)])==0:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')

check_prime(52)