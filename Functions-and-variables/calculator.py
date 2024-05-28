# Prompt for input and convert to number
x = float(input("What's x? "))
y = float(input("What's y? "))

#Round to 2 digits
z = round(x / y, 2)

#Format answer with comma separators
print(f"{z:,}")