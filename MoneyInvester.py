money, InterestRate = input('How Much To Invest And What Is The Interest Rate : ').split()
money = float(money)
InterestRate = float(InterestRate) * .01
for i in range(10):
    money = money + (money * InterestRate)
print("Investment After 10 Years {:.2f}".format(money))
