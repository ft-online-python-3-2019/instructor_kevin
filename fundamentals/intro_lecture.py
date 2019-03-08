# print("Hello World")
# print("Goodnight")
# Declaring variables
# x = 4
# print(x)
# Data types (Python)
# Integer (Whole number)
# Float (Number with decimals)
# Strings
# my_str = "Hello World"
# Boolean
my_bool = True
# JAVASCRIPT VERSION
# if (my_bool == true){
#     console.log("bool is true")
# }
# Python version
# if my_bool==True:
#     print(my_bool)
# print("Out of the conditional code block")
# For loops
# JS
# for (var i=0; i<11; i++){
#     console.log(i);
# }
# Python
# for i in range(0,11):
#     print(i)
# print("Inside of the loop")

# Arrays (called lists in Python)
# x = [1,2,3,"hello"]
# Python: 2 ways to iterate through an array
# Note: To get the length of an array, we need to use len() function
# for i in range(0, len(x)):
#     print(x[i])
# Other way
# Note: This does not allow you to control the index of the array your loop is on
# for item in x:
#     print(item)

# Function
def my_function(x,y):
    if x >5:
        print(x)
        print(y)
        return "Hello"
    else:
        return "Other value"
my_function(10,100)
# result = my_function(10,100)
# print(result)

# dictionaries (key value pairs)
# note: dot notation does not work on dictionaries, dictionaries and objects are separate in python
my_dictionary = {
    "name": "Kobe",
    "rings": 5,
    "goat": True
}
print(my_dictionary["name"])
players = [
    {
        "name": "Kobe",
        "rings": 5,
        "goat": True
    },
    {
        "name": "Lebron",
        "rings": 3,
        "goat": False
    }
]
for player in players:
    print(player['name'])
