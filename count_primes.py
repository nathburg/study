# COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
#    count_primes(100) --> 25

# By convention, 0 and 1 are not prime.

def count_primes(num):
    counter = 1
    primelist = [2]
    if abs(num) < 2:
        return 0
    elif abs(num) == 2:
        return 1
    else:
        for x in range(3,abs(num)+1):
            state = 'prime'
            for y in primelist:
                if x % y == 0:
                    state = 'composite'
                    break
            if state == 'prime':
                primelist.append(x)
        return len(primelist)
