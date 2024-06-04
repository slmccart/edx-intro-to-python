import re

name = input("What's your name? ").strip()

matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last, first = matches.groups()
    # Alternatively last = matches.group(1) and first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")
