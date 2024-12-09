'''
Maximum Path Sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3 
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
<p class="note"><b>NOTE:</b> As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, <a href="problem=67">Problem 67</a>, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)

'''

pyramid = '''3 
7 4
2 4 6
8 5 9 3
'''

long_pyramid = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

def pyramid_to_list(str=pyramid):
    pyra_dict = {}
    lines = str.splitlines()
    key = 0

    for line in lines:
        nums = line.split()
        nums = [int(num) for num in nums]
        pyra_dict[key] = nums
        key += 1
    
    return pyra_dict

def max_in_row(dict):
    max_value_path = True
    prev_i = 0
    max_values = []

    # loop through dict
    for i in dict:
        
        # find a maximum value in each list
        max_value = max(dict[i])
        print("max value is ", max_value)

        # note the index of the max value
        max_i = dict[i].index(max(dict[i]))
        print("max i is ", max_i)

        # if it is NOT equal to prev_i or prev_i + 1
        if max_i != prev_i and max_i != (prev_i + 1):
            max_value_path = False
            break
    
    return max_value_path


# always pick the larger of the two at the bottom
def max_sum(dict):

    if max_in_row(dict):
        print("Found a super path")
    else:
        print("no super path")

    # create a max_sum variable
    top_sum = 0
    prev_i = 0

    # create a for loop for the keys of the dict
    for i in dict:
        # print('currently at ', dict[i])
        # start at the top 0[0]
        if i == 0:
            top_sum += dict[i][0]
        else:
            # pick the larger of the following two options (either 1[0] or 1[1] - which is larger)
            if dict[i][prev_i] >= dict[i][prev_i + 1]:
                # print("adding ", dict[i][prev_i])
                top_sum += dict[i][prev_i]
            elif dict[i][prev_i] < dict[i][prev_i + 1]:
                # print("adding ", dict[i][prev_i + 1])
                top_sum += dict[i][prev_i + 1]
                prev_i += 1

    bottom_sum = 0
    for i in range(len(dict.keys()) - 1, 0, -1):
        
        if i == len(dict.keys()) - 1:
            max_value = max(dict[i])
            max_i = dict[i].index(max(dict[i]))
            prev_i = max_i
            bottom_sum += max_value
            print("max value is ", max_value)
        else:
            print("prev i is ", prev_i)
            # edge cases
            if prev_i == 0:
                bottom_sum += dict[i][prev_i]
                print("adding ", dict[i][prev_i])
            elif prev_i == i:
                bottom_sum += dict[i][prev_i]
                print("adding ", dict[i][prev_i])
                prev_i -= 1

            elif dict[i][prev_i] >= dict[i][prev_i - 1]:
                print("adding ", dict[i][prev_i])
                bottom_sum += dict[i][prev_i]
            elif dict[i][prev_i] < dict[i][prev_i - 1]:
                # print("adding ", dict[i][prev_i + 1])
                bottom_sum += dict[i][prev_i - 1]
                prev_i -= 1

    print("bottom sum is ", bottom_sum)

    # return the max top_sum
    return top_sum









def start_bottom(dict):

    # create a copy of dictionary
    new_dict =  dict.copy()
    print("new dict is ", new_dict)

    for i in range(len(new_dict.keys()) - 2, -1, -1): # start at row second to last
        print("current row is ", new_dict[i])
        
        # interior loop for every row
        for index, num in enumerate(new_dict[i]):

            # compare the options below
            if new_dict[i+1][index] >= new_dict[i+1][index+1]:

                new_dict[i][index] += new_dict[i+1][index]
            
            elif new_dict[i+1][index] < new_dict[i+1][index+1]:

                new_dict[i][index] += new_dict[i+1][index+1]
        
        print("row after transformation ", new_dict[i])
        
    return new_dict[0][0]





        

# print(max_sum(pyramid_to_list()))
# print(max_sum(pyramid_to_list(long_pyramid)))
print(start_bottom(pyramid_to_list()))
print(start_bottom(pyramid_to_list(long_pyramid)))