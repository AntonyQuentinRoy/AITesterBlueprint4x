#Set Keyword usage in Python

my_set = {1, 2, 3, 4, 5,5,1}
print(my_set)  # Output: {1, 2, 3, 4, 5}
print(type(my_set))  # Output: <class 'set'>
print(len(my_set))  # Output: 5

my_list = [1, 2, 3, 4, 5, 5, 1]
my_set_from_list = set(my_list)
print(my_set_from_list)  # Output: {1, 2, 3, 4, 5}
print(type(my_set_from_list))  # Output: <class 'set'>

#set removes duplicates from the list and creates a set with unique elements.

#set uses curly braces {} to define a set, and it automatically removes duplicate elements.
#list uses square brackets [] to define a list, and it allows duplicate elements.
#collections uses parentheses () to define a tuple, and it allows duplicate elements.
#tuples uses parentheses () to define a tuple, and it allows duplicate elements.

sq = {x**2 for x in range(5)}
print(sq)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}