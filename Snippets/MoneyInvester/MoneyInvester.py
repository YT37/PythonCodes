money, interestRate, time = input(
    "How Much To Invest And What Is The Interest Rate And Time : "
).split()

money = float(money)

interestRate = float(interestRate) * 0.01

for i in range(int(time)):
    money = money + (money * interestRate)

print("Investment After {} Years {:.2f}".format(time, money))
