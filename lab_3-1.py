# Author: IBN AMDG (3/7/2022)

def r_max(nested_num_lst): 
    total = 0
    for element in nested_num_lst:
            if type(element) == list:
                total = max(element) 
    return total

print(r_max([1, 2, [3, 4, 5], 6]))
