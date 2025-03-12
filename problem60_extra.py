def find_candidates(member_1, member_2, sets_1, sets_2, dict, limit, candidates=None):

    # print("dealing with set_1", sets_1, "and set_2", sets_2)

    if candidates is None:
        candidates = []

    #base case
    if limit == 0:
        return candidates
    
    current_members = {member_1, member_2}

    print("sets 1 is ", sets_1, "sets 2 is ", sets_2)

    # leave only those sets that contain the same numbers in both sets (excluding the one with member 1 and 2)
    overlap = [num for num in sets_1 if num in sets_2 and num not in current_members]
    # overlap = [s for s in overlap if not (member_1 in s and member_2 in s)]

    if len(overlap) == 0:
        # print("the overlap is 0")
        return []

    new_candidates = [num for s in overlap for num in s if num != member_1]

    # print("new candidates now are ", new_candidates, "limit is ", limit)
    
    for candidate in new_candidates[:]:

        sets_3 = dict[candidate]
        next_candidates = find_candidates(member_1, candidate, overlap, sets_3, dict, limit - 1, new_candidates)
        
        if not next_candidates:
            new_candidates.remove(candidate)

    return new_candidates




    


