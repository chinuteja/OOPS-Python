from project import chatbook
user = chatbook()
#print(user.__name) # This will raise an AttributeError
print(user._chatbook__name)  # Accessing the private attribute
user.set_name("new_hidden_name") ## Using setter method to modify the private attribute
print(user.get_name())


# print(user.user_id)  # Accessing the user_id attribute

user2 = chatbook()
user3 = chatbook()

print("User IDs assigned to each user:")
print(user.user_id) 
print(user2.user_id)
print(user3.user_id)

print("Unique IDs assigned to each user:")

print(user.id) 
print(user2.id)
print(user3.id)


print("Current User ID from static method:", user.get_id())
user.set_id(10)
print("Updated User ID from static method:", user.get_id())

