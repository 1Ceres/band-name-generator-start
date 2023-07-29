#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

print("Welcome to band name generator!\n")
city = input("What city do you grew up?\n")
pet = input("What is your pet's name?\n")
print("One of option for your band name is:\n")
print(pet + " of " + city)
