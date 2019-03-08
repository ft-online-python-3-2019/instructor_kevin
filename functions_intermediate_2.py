# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Original version
# x_inner_list = x[1]
# x_inner_list[0] = 15
# refactored
x[1][0] = 15


# Change the last_name of the first student from 'Jordan' to 'Bryant'
# first_student = students[0]
# first_student['last_name'] = "Bryant"
# Refactored
students[0]['last_name'] = "Bryant"

# In the sports_directory, change 'Messi' to 'Andres'
# soccer_players = sports_directory['soccer']
# soccer_players[0] = "Andres"
# Refactored
sports_directory['soccer'][0] = "Andres"

# Change the value 20 in z to 30
z[0]['y'] = 30

# print(x)
# print(students)
# print(sports_directory)
# print(z)


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(students_list):
    for student in students_list:
        # print(student)
        print(f"first_name - { student['first_name'] }, last_name - { student['last_name'] }")
    
    for i in range(0, len(students_list)):
        print(f"first_name - { students[i]['last_name'] }, last_name - { students[i]['last_name'] }")
# iterateDictionary(students)
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel



students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])
    
    # for i in range(0, len(some_list)):
    #     print(some_list[i][key_name])

# iterateDictionary2('first_name', students)

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# def printInfo(some_dict):
#     for key in some_dict:
#         # print(key)
#         # print(some_dict[key])
#         list_at_value = some_dict[key]
#         my_str = f"{ len(list_at_value) } {key.upper()}"
#         print(my_str)
#         for item in list_at_value:
#             print(item)
# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


sports=[
	{"name": "Soccer", "rules": "no hands"},
	{"name": "Basketball", "teams": 30},
	{"name": "Curling", "rules": "no idea"},
]
for sport in sports:
	print(sport["rules"])
