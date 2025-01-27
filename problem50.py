'''
Consecutive Prime Sum

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13.
This is the longest sum of consecutive primes that adds to a 
prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds 
to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most 
consecutive primes?

'''

from extras.utils import is_prime


def consecutive_prime_sum(limit=100):
    
    primes = [] # in reversed order

    max_sum = 0 # answer
    # current_sum = 2
    current_additives = [2]

    max_cons_primes = 0 # max so far

    # add primes to the list
    for n in range(limit, 1, -1):

        # if prime, add to primes
        if is_prime(n):

            primes.append(n)
    
    # print(primes)

    for i, prime in enumerate(primes):

        # current = prime
        starting_point = 0
        leftover = primes[i+1:]
        # print("leftover are ", leftover)

        for _ in range(len(primes[i+1:])):

            current = prime # reset the prime every round
            counter = 0
            remaining = primes[i+1+starting_point:]
            # print("remaining for this round for this prime", prime, "are" ,remaining)
            starting_point += 1

            for prime_two in leftover[starting_point:]:

                current -= prime_two

                if current < 0:
                    break
                elif current == 0 and counter > max_cons_primes:
                    max_cons_primes = counter
                    max_sum = prime
                    
                counter += 1

    return max_sum

print(consecutive_prime_sum())
# print(consecutive_prime_sum(1000000))

# # add to current sum
#         current_sum += n

#         # if sum is not prime, break the sequence ?
#         if not is_prime(current_sum):
#             print("current sum is not prime", current_sum)
#             current_additives.clear()
#             current_sum = 0
#             continue
        
#         consecutive_primes += 1
#         current_additives.append(n)
#         print("for current sum", current_sum, "current additives are ", current_additives)

#         # if current_sum surpasses max_sum, reassign
#         if consecutive_primes > max_cons_primes:
#             max_cons_primes = consecutive_primes
#             max_sum = current_sum

# for i, prime in enumerate(primes):

#         remaining = primes[i+1:]
#         # chain that starts with prime
#         current_sum = prime
#         chain_length = 1

#         for prime_two in primes:

#             current_sum += prime_two
#             if is_prime(current_sum) and :