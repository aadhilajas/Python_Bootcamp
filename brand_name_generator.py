# Task
# Create a greeting for your program.
# Ask the user for the city that they grew up in and store it in a variable.
# Ask the user for the name of a pet and store it in a variable.
# Combine the name of their city and pet and show them their band name.

# Greetings
print("Welcome t the Brand Name Generator.")
# User inputs
city = str(input("What's the name of the city you grew up in?\n"))
pets_name = str(input("What's your pet's name?\n"))
# Brand name generator
brand_name = city+" "+pets_name
print("Your brand name could be ", brand_name)