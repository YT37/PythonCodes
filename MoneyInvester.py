money, InterestRate, time = input(
    "How Much To Invest And What Is The Interest Rate And Time : "
).split()

money = float(money)

InterestRate = float(InterestRate) * 0.01

for i in range(int(time)):
    money = money + (money * InterestRate)

print("Investment After {} Years {:.2f}".format(time, money))
