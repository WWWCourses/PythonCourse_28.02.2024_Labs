import re

# TASK: Write a Python program to validate usernames using Regular Expressions. The program should check if a given username meets specific criteria and print an appropriate message indicating whether the username is valid or not.

# Criteria for a Valid Username:
# Username Length: 3 to 15 characters inclusive.
# Allowed Characters: only alphanumeric characters, dashes (-), and underscores (_).
# Starting Character: must start with a letter (either uppercase or lowercase).
# Ending Character: must not end with an underscore or dash



user_names = [
    "User123",		# yes
    "Valid-User_123",	# yes
    "u1234567890123",	# yes
    "u____a",		# yes
    "us",			# no
    "user_name_with_long_length", # no
    "1username", # no
    "_username", # no
    "username-", # no
    "username_", # no
    "User@name-", # no
]