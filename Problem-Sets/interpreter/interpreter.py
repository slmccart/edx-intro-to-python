equation = input("Expression: ").strip()

x, y, z = equation.split(" ")
x = int(x)
z = int(z)

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z

print(f"{result:.1f}")
