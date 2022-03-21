# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again."
# }
# # Retrieving items from the dictionary 
# print(programming_dictionary["Bug"])
# #  adding new items to the dictionary
# programming_dictionary["Loop"] = "The action of doing the something again and again"

# # Creating an empty dictionary
# # empty_dictionary = {}

# # Wipe an existing dictionary 
# # programming_dictionary = {}

# # Edit an item in dictionary 
# programming_dictionary["Bug"] = "A mug inside your computer."

# # print(programming_dictionary)

# # Loop through Dictionary 
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


# Nesting list in a dictionary 
from typing import List


travel_log = {
    "France" : ["Paris","Lion","Lille"],
    "Germany" : ["Berlin","Hamburg","Studgart"]
}

#Nesting dictionary in a dictinary
travel_log2 = {
    "France": {"cities_visited":["Paris","Lion","Lille"],"total_visits":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","Studgart"],"total_visits":5},
}

# Nesting Dictionary in a List
travel_log3 = [
    {"country":"France",
    "cities_visited":["Paris","Lion","Lille"],
    "total_visits":12
    },
    {"country":"Germany",
    "cities_visited":["Berlin","Hamburg","Studgart"],
    "total_visits":5
    },
]
# print(travel_log["France"]) # --> ['Paris', 'Lion', 'Lille']

# print(travel_log2["France"]["total_visits"]) # --> 12

# print (travel_log3[0]["total_visits"]) # --> 12