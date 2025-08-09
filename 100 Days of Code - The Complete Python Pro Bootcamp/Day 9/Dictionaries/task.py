programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary["Bug"])

programming_dictionary["UEM" ] ="Useless"

print(programming_dictionary)

programming_dictionary["UEM"] = "More Useless"

print(programming_dictionary["UEM"])

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])