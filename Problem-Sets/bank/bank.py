prompt = input("Greeting: ").strip().lower()

if prompt.startswith("hello"):
    print("$0")
elif prompt.startswith("h"):
    print("$20")
else:
    print("$100")
