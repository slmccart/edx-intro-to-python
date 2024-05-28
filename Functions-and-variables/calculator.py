# Prompt for input and convert to number
x = float(input("What's x? "))
y = float(input("What's y? "))

#Round to nearest int
z = round(x + y)

#Format answer with comma separators
print(f"{z:,}")