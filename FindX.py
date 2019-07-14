def solve_eq(equation):
    num1, add, x, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2 - num1)


print(solve_eq("4 + x = 9"))
