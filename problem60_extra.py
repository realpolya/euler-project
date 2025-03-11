def find_candidates(member_1, member_2, sets_1, sets_2, pairs, four_subsets, limit, candidates=None):

    if candidates is None:
        candidates = []

    #base case
    if limit == 0:
        return candidates

    # leave only those sets that contain the same numbers in both sets (excluding the one with member 1 and 2)
    overlap = [s1 for s1 in sets_1 if any(s1 & s2 for s2 in sets_2)]
    overlap = [s for s in overlap if not (member_1 in s and member_2 in s)]

    if len(overlap) == 0:
        return candidates

    new_candidates = [num for s in overlap for num in s if num != member_1]
    new_candidates = [num for num in new_candidates if num in four_subsets]
    
    for candidate in new_candidates[:]:

        sets_3 = [s for s in pairs if candidate in s]
        next_candidates = find_candidates(member_1, candidate, overlap, sets_3, pairs, four_subsets, limit - 1, new_candidates)
        
        if not next_candidates:
            new_candidates.remove(candidate)

    return new_candidates




    


