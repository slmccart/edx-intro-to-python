# Ask user for their name, remove whitespace, and capitalize
name = input("What's your name? ").strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")