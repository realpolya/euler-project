'''
Prime Pair Sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and 
concatenating them in any order the result will always be prime. For example, taking 7 and 109, 
both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for 
a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

'''

from extras.utils import is_prime

# find the lowest sum of the five primes for which any two primes concatenate to produce another prime
def is_concat_prime(num_1, num_2):

    # try concatenating combinations within that set
    concat_1 = int(str(num_1) + str(num_2))
    concat_2 = int(str(num_2) + str(num_1))

    if not is_prime(concat_1) or not is_prime(concat_2):
        return False
    
    return True


def prime_pair_sets(quantity=4):

    lowest_sum = 0
    start = 3
    limit = 499
    primes = [2]
    answer_list = []
    

    pairs = []
    quadruples = []

    # while loop
    while lowest_sum == 0:

        for i in range(start, limit, +2):
            if is_prime(i):
                primes.append(i)
        
        print("primes length is ", len(primes))
        index = 0

        # work in pairs?
        for prime in primes:

            primes_cut = primes[index+1:]
            index += 1

            for prime_2 in primes_cut:

                if prime == prime_2:
                    continue

                new_pair = set()
                new_pair.update([prime, prime_2])

                if new_pair not in pairs:

                    # if a combination is not prime, discard that pair
                    if not is_concat_prime(prime, prime_2):
                        continue

                    pairs.append(new_pair)
        
        print("number of pairs: ", len(pairs))

        first_member_quantity = quantity - 1
        four_subsets = set()

        for pair in pairs:

            # candidate number - is it found in 4 pairs? if not skip, if yes, go through each sets of 4
            # TODO: do not repeat members
            member_1 = list(pair)[0]
            member_2 = list(pair)[1]

            if member_1 in four_subsets and member_2 in four_subsets:
                continue
            
            member_1_count = sum(1 for s in pairs if member_1 in s)
            member_2_count = sum(1 for s in pairs if member_2 in s)

            if member_1_count < first_member_quantity and member_2_count < first_member_quantity:
                continue
            elif member_1_count > first_member_quantity and member_2_count > first_member_quantity:
                four_subsets.add(member_1)
                four_subsets.add(member_2)
                # print("these members are in more than 4 subsets", member_1, member_2)
            elif member_1_count > first_member_quantity:
                four_subsets.add(member_1)
                # print("this member is in more than 4 subsets", member_1)
            elif member_1_count > first_member_quantity:
                four_subsets.add(member_2)
                # print("this member is in more than 4 subsets", member_2)
            
        print("len of four subsets", len(four_subsets))

        if lowest_sum == 0:
            start = limit
            limit += 500

        
        # lowest_sum = 2
    
    print(quadruples)

    return lowest_sum

print(prime_pair_sets(5))






        # index = 0

        # for pair in pairs:

        #     pairs_cut = pairs[index+1:]
        #     index += 1

        #     for pair_2 in pairs:

        #         pair_list = list(pair)
        #         pair_2_list = list(pair_2)

        #         quadruple = set()
        #         quadruple.update(pair)
        #         quadruple.update(pair_2)

        #         # print(pair_list[0], pair_2_list[0])

        #         if quadruple not in quadruples:

        #             # if a second pair is not working with first, find another larger pair
        #             if (
        #                 not is_concat_prime(pair_list[0], pair_2_list[0]) 
        #                 or not is_concat_prime(pair_list[1], pair_2_list[0])
        #                 or not is_concat_prime(pair_list[0], pair_2_list[1])
        #                 or not is_concat_prime(pair_list[1], pair_2_list[1])
        #             ):
        #                 continue

        #             # print(pair, pair_2)

        #             if quantity == 4:
        #                 answer_list.extend(pair)
        #                 answer_list.extend(pair_2)
        #                 print(answer_list)

        #                 for num in answer_list:
        #                     lowest_sum += num
                        
        #                 break
                        
        #             quadruples.append(quadruple)
            
        #     if lowest_sum > 0:
        #         break
        
        # print("quadruples are ", quadruples)
        
        # if quantity == 5:

        #     for prime in primes:
        #         for quadruple in quadruples:
        #             not_this_match = False

        #             # checking every member of quadruple
        #             for member in quadruple:
        #                 if not is_concat_prime(prime, member):
        #                     not_this_match = True
        #                     break

        #             if not not_this_match:
        #                 answer_list = [*quadruple, prime]
        #                 for n in answer_list:
        #                     lowest_sum += n
        
        # print("answer list is ", answer_list)