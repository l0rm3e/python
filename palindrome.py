word = input("Enter string: ")

n_word = word.lower()

reverse =n_word[::-1]

if n_word == reverse:
    print(word + " is a palindrome")

else:
    print(word + " is not a palindrome")


