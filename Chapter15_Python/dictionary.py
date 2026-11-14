my_dictionary = {"name": "John", "age": 30, "city": "New York"}
print(my_dictionary["name"])  # Output: John
print(my_dictionary.get("age"))  # Output: 30
print(my_dictionary.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(my_dictionary.values())  # Output: dict_values(['John', 30, 'New York'])


my_dict_compare = {"name": "John", "age": 30, "city": "New York"}
my_dict_compare2 = {"age": 30, "name": "John", "city": "New York"}

print(my_dict_compare == my_dict_compare2)  # Output: True