#  LIST which contains symbols to delete.
symbol_to_remove = [" ", "\n", ".", ",", "-", ":", ";", "?", "!", '"', "'"]

#  variable for checked string
#  checked_string = ""
#  variable for inverse string
#  inverse_string = ""
#  I tried to declare variables before using its, but PEP8 said that's a wrong way.

#  input of data by user
print("A palindrome is a word, number, phrase that reads the same backwards as forwards")
string_to_check = input("Enter, please, what you want to check: ")

#  according to the task we must put away some symbols.
#  I decided to check every symbol and make a new variable.
checked_string = string_to_check
for symbol in symbol_to_remove:
    checked_string = checked_string.replace(symbol, "")

#  one register for all letters
checked_string = checked_string.lower()

#  make inversion!
inverse_string = checked_string[::-1]

#  let's check if it is a palindrome

if checked_string == inverse_string:
    print(f"Wow! This is a palindrome! {string_to_check}")
else:
    print(f"It seems this is not a palindrome! {string_to_check}")

#  These were used to see how variables changing
#  for educational purposes only
#  print(string_to_check)
#  print(checked_string)
#  print(inverse_string)
