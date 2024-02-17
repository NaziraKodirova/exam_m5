def generate_primes(N):
    number = 2
    while N > 0:
        for i in range(2, number):
            if number % i == 0:
                break
        else: 
            yield number
            N -= 1
        number += 1

N =5
for prime in generate_primes(N):
    print(prime)
