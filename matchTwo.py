# Udemy Assignment
# Create a regular expression that matches any two words that start with any character and is followed by
# two o's. Then use Python re module to match boo and loo in the sentence
# "The ghost that says boo haunts the loo." Save the result in a variable and print it.

import re

s = "The ghost that says boo haunts the loo."

result = re.findall(".oo", s)

print(result)