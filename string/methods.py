data = "My Name Is 5 @" 

#case-sensitive, can take multiple chars
print("Starts with ", data.startswith("in"))
print("Ends with ", data.endswith("ia"))

print("Checks for both alphabet and numbers: ", data.isalnum()) #true if either 1 satisfies, returns false for special symbols and whitespace
print("Checks for only alphabets: ", data.isalpha()) #returns false for numbers and special symbols and whitespace
print("Checks for only numbers: ", data.isdigit()) #returns false for alphabets and special symbols and whitespace

print("Checks for only upper case: ", data.isupper()) #returns true only if all chars are uppercase, false for lower case
print("Checks for only lower case: ", data.islower()) #returns true only if all chars are lowercase, false for upper case 

print("Checks for only spaces: ", data.isspace()) #returns true for \t, \n and spaces only. false for alphabets, numbers and special symbols

print("Checks if every word's first letter is capital: ", data.istitle()) #returns true if every word starts with uppercase letter

print("Checks if the content is printable or not: ", data.isprintable()) #returns false for non-printable characters(escape characters such as \t, \n etc.)

print("Splits the string into a list of words: ", data.split(" ")) #splits the string into a list, can be used for counting words or whitespaces