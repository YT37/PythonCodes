def solveEq(equation):
    num1, _, _, _, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2 - num1)


print(solveEq("4 + x = 9"))
