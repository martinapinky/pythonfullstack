# ####################### PRINT UNIQUE VALUES
# L = [{"V": "S001"}, {"V": "S001"}]

# unique_values = set([val for dictionary in L for val in dictionary.values()])
# print(unique_values)



# ### sum for a specific value
# student_list = {}
# sum(d['id'] for d in student_list)

# ####################key exists or not ####

# my_dict = {}
# keys_to_check = []

# [key in my_dict for key in keys_to_check]



####################PRINT UNIQUE VALUES
L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]


unique_values = set(val for dictionary in L for val in dictionary.values())
print(unique_values)




student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]


print(sum((d['id'] for d in student)))


my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}


########## Key exists or not ############
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}


keys_to_check =['name', 'age']


key_exists= all(key in my_dict for key in keys_to_check )
print(key_exists)


############ nested dictionaries

students = {
    '101': {"name": "Alice", "age": 22, "courses": ["Maths", "Physics"]},
    '102': {"name": "Alice", "age": 22, "courses": ["Maths", "Physics"]},
    '103': {"name": "Alice", "age": 22, "courses": ["Maths", "Physics"]},
}

########Access the value for nested dictionaries
print(students["101"]["name"])
