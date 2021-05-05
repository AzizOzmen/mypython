# Exercise 14: Remove empty strings from a list of strings
# Given:

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Expected Output:

# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
def remove_empt(str):
    new_list = []
    for i in str: 
        if i:
           new_list.append(i)
    print(new_list)
remove_empt(str_list)